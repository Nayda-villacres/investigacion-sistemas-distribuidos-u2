"""Real loopback benchmark. See README.md. No synthetic measurements."""
import argparse, asyncio, csv, datetime, json, multiprocessing as mp
import os, platform, random, statistics, time
from pathlib import Path
import aiohttp
from aiohttp import web
import grpc
import psutil
from google.protobuf import descriptor_pb2, descriptor_pool, message_factory

# Embedded schema: syntax="proto3"; package bench;
# message Payload { string text=1; } service Echo { rpc Call(Payload) returns(Payload); }
fd=descriptor_pb2.FileDescriptorProto(name='echo.proto',package='bench',syntax='proto3')
m=fd.message_type.add(name='Payload'); m.field.add(name='text',number=1,type=9,label=1)
pool=descriptor_pool.DescriptorPool(); pool.Add(fd)
Payload=message_factory.GetMessageClass(pool.FindMessageTypeByName('bench.Payload'))

async def serve(protocol, ready):
    if protocol=='REST':
        async def echo(request):
            assert request.version==aiohttp.HttpVersion11
            body=await request.json()
            return web.json_response({'text':body['text']})
        app=web.Application(); app.router.add_post('/echo',echo)
        runner=web.AppRunner(app,access_log=None); await runner.setup()
        site=web.TCPSite(runner,'127.0.0.1',0); await site.start()
        ready.send(site._server.sockets[0].getsockname()[1])
    else:
        async def echo(request,context): return Payload(text=request.text)
        server=grpc.aio.server()
        server.add_generic_rpc_handlers((grpc.method_handlers_generic_handler('bench.Echo',{
            'Call':grpc.unary_unary_rpc_method_handler(echo,request_deserializer=Payload.FromString,
                response_serializer=Payload.SerializeToString)}),))
        port=server.add_insecure_port('127.0.0.1:0'); await server.start(); ready.send(port)
    await asyncio.Event().wait()

def server_main(protocol,ready): asyncio.run(serve(protocol,ready))

async def trial(protocol,c,size,seconds,warmup,pid,port):
    text='x'*size; lat=[]; errors=0; error_types={}; proc=psutil.Process(pid); rss=[]
    session=None; channel=None
    if protocol=='REST':
        session=aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=c),
            timeout=aiohttp.ClientTimeout(total=10))
        async def call():
            async with session.post(f'http://127.0.0.1:{port}/echo',json={'text':text}) as r:
                r.raise_for_status(); body=await r.json(); assert body['text']==text
    else:
        channel=grpc.aio.insecure_channel(f'127.0.0.1:{port}')
        await asyncio.wait_for(channel.channel_ready(),10)
        rpc=channel.unary_unary('/bench.Echo/Call',request_serializer=Payload.SerializeToString,
            response_deserializer=Payload.FromString)
        async def call():
            response=await rpc(Payload(text=text),timeout=10); assert response.text==text
    async def worker(deadline,record):
        nonlocal errors
        while time.perf_counter()<deadline:
            start=time.perf_counter_ns()
            try:
                await call()
                if record: lat.append((time.perf_counter_ns()-start)/1e6)
            except Exception as exc:
                if not record: raise
                errors+=1
                key=type(exc).__name__
                if isinstance(exc,grpc.RpcError): key+=':'+str(exc.code())
                error_types[key]=error_types.get(key,0)+1
    async def sample():
        while True:
            rss.append(proc.memory_info().rss/2**20); await asyncio.sleep(.02)
    try:
        end=time.perf_counter()+warmup
        await asyncio.gather(*(worker(end,False) for _ in range(c)))
        before=proc.cpu_times(); client_before=time.process_time(); start=time.perf_counter()
        sampler=asyncio.create_task(sample()); end=start+seconds
        await asyncio.gather(*(worker(end,True) for _ in range(c)))
        elapsed=time.perf_counter()-start; client_cpu=time.process_time()-client_before
        after=proc.cpu_times(); sampler.cancel()
        await asyncio.gather(sampler,return_exceptions=True)
        cpu=after.user+after.system-before.user-before.system
        ordered=sorted(lat)
        def quantile(q):
            # Linear interpolation, equivalent to numpy default.
            x=(len(ordered)-1)*q; lo=int(x); hi=min(lo+1,len(ordered)-1)
            return ordered[lo]+(ordered[hi]-ordered[lo])*(x-lo)
        if not lat: raise RuntimeError('No successful requests')
        return dict(requests=len(lat),errors=errors,error_types=json.dumps(error_types,sort_keys=True),elapsed_s=elapsed,rps=len(lat)/elapsed,
            mean_ms=statistics.mean(lat),p50_ms=quantile(.5),p95_ms=quantile(.95),p99_ms=quantile(.99),
            server_cpu_s=cpu,server_cpu_pct=100*cpu/elapsed,server_cpu_us_req=cpu*1e6/len(lat),
            server_rss_mean_mib=statistics.mean(rss),server_rss_max_mib=max(rss),rss_samples=len(rss),
            client_cpu_s=client_cpu)
    finally:
        if session: await session.close()
        if channel: await channel.close()

def main():
    p=argparse.ArgumentParser(); p.add_argument('--seconds',type=float,default=3)
    p.add_argument('--warmup',type=float,default=1); p.add_argument('--repeats',type=int,default=5)
    p.add_argument('--concurrency',type=int,nargs='+',default=[1,8,32,64])
    p.add_argument('--sizes',type=int,nargs='+',default=[256,4096]); p.add_argument('--seed',type=int,default=20261113)
    p.add_argument('--output',default='results.csv'); a=p.parse_args()
    if min(a.seconds,a.warmup,a.repeats,*a.concurrency,*a.sizes)<=0: p.error('all values must be positive')
    jobs=[(r,c,s,proto) for r in range(1,a.repeats+1) for c in a.concurrency for s in a.sizes for proto in ['REST','gRPC']]
    random.Random(a.seed).shuffle(jobs)
    with open(a.output,'w',newline='',encoding='utf-8') as f:
        writer=None
        for order,(r,c,s,proto) in enumerate(jobs,1):
            parent,child=mp.Pipe(); process=mp.Process(target=server_main,args=(proto,child)); process.start()
            try:
                if not parent.poll(20): raise RuntimeError('Server startup timeout')
                port=parent.recv()
                result=asyncio.run(trial(proto,c,s,a.seconds,a.warmup,process.pid,port))
                row=dict(timestamp_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),order=order,
                    protocol=proto,concurrency=c,payload_bytes=s,repeat=r,seed=a.seed,warmup_s=a.warmup,
                    target_s=a.seconds,**result,python=platform.python_version(),os=platform.platform(),
                    cpu=platform.processor(),logical_cpus=os.cpu_count(),ram_gib=psutil.virtual_memory().total/2**30,
                    aiohttp=aiohttp.__version__,grpcio=grpc.__version__,psutil=psutil.__version__)
                if writer is None: writer=csv.DictWriter(f,fieldnames=row); writer.writeheader()
                writer.writerow(row); f.flush()
                print(f'{order}/{len(jobs)} {proto} c={c} bytes={s} rps={result["rps"]:.0f} errors={result["errors"]}',flush=True)
            finally:
                process.terminate(); process.join(10); parent.close(); child.close()

if __name__=='__main__': mp.freeze_support(); main()
