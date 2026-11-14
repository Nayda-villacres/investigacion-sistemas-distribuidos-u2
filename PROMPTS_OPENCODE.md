# Bitácora de OpenCode, Codex e integridad académica

Fecha local: 13 de noviembre de 2026 (Ecuador, UTC-5). Las marcas de herramientas y del CSV pueden corresponder al 14 de noviembre en UTC. Investigadora responsable: **Villacres Martinez Nayda Antonela**. Tema exclusivo: apartado 3, REST HTTP/1.1 frente a gRPC HTTP/2 bajo concurrencia.

## Roles y alcance real

Codex ejecutó comandos en el entorno local de Windows, escribió y auditó el benchmark, consultó fuentes bibliográficas, ejecutó las pruebas y elaboró el artículo Quarto. OpenCode 2.2.7 se utilizó realmente mediante terminal, incluyendo una invocación desde CMD, como asistente de revisión metodológica, código y maquetación. No se afirma que OpenCode haya producido por sí solo el proyecto. La autora todavía debe revisar y aceptar código, interpretación y documento. No se firma una declaración en su nombre.

## Consultas principales realmente enviadas

1. **Consulta inicial desde CMD, modelo predeterminado.**

   > Actua como copiloto academico. Propone un benchmark Python reproducible REST HTTP/1.1 aiohttp versus grpc.aio HTTP/2 con protobuf real, servicio echo identico, procesos servidor separados, concurrencias 1 8 32 64, repeticiones y CPU/RSS con psutil. No ejecutes ni crees archivos. Audita sesgos y propone bloques Quarto IEEE con label y fig-cap y bibliografia BibTeX verificable. Responde conciso.

   Resultado real: error de proveedor `401`, `User not found`. No hubo una respuesta académica válida. Se informó a la usuaria y se buscaron modelos disponibles mediante `opencode models`. No se solicitaron ni registraron contraseñas.

2. **Revisión de código, `opencode/big-pickle`, salida JSON.**

   > Revisa sin modificar archivos outputs/benchmark.py. Propone correcciones metodologicas y un bloque Quarto con label y fig-cap, IEEEtran, referencias BibTeX. No inventes resultados ni ejecutes pruebas.

   OpenCode inició una sesión y leyó archivos. La captura de esa sesión contiene eventos de herramientas y una última línea JSON incompleta; no se usa como prueba de una auditoría concluida. Se intentó continuar la sesión con: «Continua sin usar herramientas. Devuelve tu auditoria y bloque Quarto directamente». Esa continuación no produjo texto utilizable en su archivo de captura.

3. **Auditoría autocontenida, `opencode/big-pickle`, con `--auto`.**

   > Sin herramientas ni acceso a archivos: audita este diseno: Python aiohttp JSON HTTP1.1 con pool C versus grpc.aio Protobuf HTTP2 canal compartido, eco texto ASCII 256/4096, C 1/8/32/64, cinco repeticiones, orden aleatorio, servidor proceso separado, 1 s calentamiento 3 s medicion, CPU psutil y RSS 20 ms, perf_counter_ns. Da 5 limitaciones y un bloque Quarto ejecutable con label fig-cap y matplotlib leyendo results.csv. Indica configuracion IEEEtran y un ejemplo BibTeX. No inventes mediciones. Responde directamente sin usar herramientas.

   Respuesta: advirtió confusión entre transporte, códec y conexión, duración breve y carga cerrada. Propuso bloques de lectura de CSV. Su observación sobre `cpu_percent(interval=0.02)` era hipotética: el benchmark realmente usa diferencias de `cpu_times()` y no ese método bloqueante. No se incorporó como un defecto existente.

4. **Consulta independiente con `--standalone`, `opencode/big-pickle`.**

   > Responde directamente sin herramientas. Para un benchmark aiohttp REST JSON contra grpc.aio Protobuf con C 1 8 32 64, cinco repeticiones, 1s calentamiento y 3s medicion, propone 5 limitaciones y bloque Quarto con label fig-cap leyendo results.csv; configura IEEEtran. No inventes resultados.

   Respuesta completa: límites de calentamiento, ventanas breves, rejilla de concurrencia, loopback y confusores. Mostró `documentclass: IEEEtran`, `classoption: [conference]`, etiquetas de figura y lectura real del CSV. Se adaptaron estas ideas al esquema existente, a dos tamaños y a intervalos t explícitamente condicionados. No se adoptó `error: true`, porque los errores de análisis deben detener la compilación. Su estimación sin datos de «decenas–cientos» de llamadas a C=1 no se usó.

5. **Maquetación con `opencode/beam-free`.**

   > Sin herramientas. Da una limitacion de comparar REST aiohttp JSON con grpc.aio Protobuf y un bloque Quarto matplotlib con label y fig-cap. No ejecutes nada.

   Respuesta: bloque con `label` y `fig-cap`, pero incluyó latencias ilustrativas 12.4 y 4.1. **Se descartaron esas cifras**, que nunca se incorporaron al CSV, figura ni análisis. Se corrigió además la afirmación de soporte HTTP/2 opcional en aiohttp y la supuesta necesidad ineludible de stubs generados: aquí se usa HTTP/1.1 en aiohttp y descriptor Protobuf dinámico.

6. **Asistencia de código y BibTeX, `opencode/beam-free`.**

   > Responde sin herramientas ni mediciones ilustrativas: propone un esqueleto Python asyncio para C workers midiendo eco con perf_counter_ns, CPU psutil de servidor separado y RSS, y un ejemplo BibTeX valido con DOI 10.1145/1297027.1297033. Especifica que JSON y Protobuf son confusores y que un descriptor dinamico evita protoc. No afirmes que aiohttp soporta HTTP2.

   Errores detectados: interpretó C como lenguaje C y sugirió subprocessos de un binario inexistente. También asoció incorrectamente el DOI de Georges et al. con *The Google File System*. **Se rechazó ese BibTeX**. La referencia correcta se verificó en DBLP y Crossref: Georges, Buytaert y Eeckhout, OOPSLA 2007, pp. 57–76.

7. **Corrección explícita al asistente.**

   > Correccion: C significa numero de corutinas concurrentes, no lenguaje C. Necesito solo un esqueleto Python con async def worker(call, deadline): medir await call() con perf_counter_ns en bucle; asyncio.gather para 8 workers; CPU por diferencia proc.cpu_times() de psutil. No herramientas ni numeros inventados ni bibliografia.

   OpenCode creó un esqueleto con el bucle y `asyncio.gather`, pese a solicitar respuesta sin herramientas. Se revisó y trasladó al directorio de trabajo para no añadir un noveno archivo al repositorio. Su `psutil.Process()` apuntaba al proceso actual; el benchmark entregado conserva `psutil.Process(pid)` del servidor, usa deadline coherente y añade verificación, calentamiento, errores, cierre de recursos y mediciones por repetición. El esqueleto no se ejecutó como experimento.

## Decisiones y correcciones aplicadas por Codex

- Se mantuvo exclusivamente el tema asignado. No se generaron actividades de otros estudiantes.
- Dos servicios reales con igual semántica de texto; no se simuló una ventaja para ningún protocolo.
- Se separó el proceso servidor y se reutilizaron conexiones/canal. Las diferencias JSON/Protobuf y pool/canal son parte de las pilas y se declaran como confusores.
- Calentamiento por ejecución, cinco repeticiones, orden aleatorio fijo, perf_counter_ns y denominador temporal real con drenaje.
- RSS total del servidor muestreada, CPU por diferencias de contadores y percentiles de llamadas verificadas; no se confundió RSS con memoria incremental.
- La gráfica de Quarto lee `results.csv`; ningún número ilustrativo de IA se usa como dato experimental.
- Se corrigió la ficha de Grigorik por Crossref: *ACM Queue* 11(10), 40–53, DOI 10.1145/2542661.2555617. Se verificaron las cinco referencias con fuentes bibliográficas; no se inventaron autores ni DOI.
- Las recomendaciones del agente fueron sometidas a auditoría técnica por otro agente (Codex). Esto **no equivale a la supervisión humana pendiente**.

## Pruebas e incidente experimental

Se ejecutó una prueba funcional con 0.3 s de medición, 0.2 s de calentamiento, C=1/8, 256 bytes y una repetición: cuatro filas, cero errores. Los primeros intentos de esa prueba fallaron por dependencias todavía en instalación; no se cuentan como ejecuciones válidas.

La primera batería de 80 ejecuciones completó 795882 respuestas válidas y cinco errores. La fila de orden 47 (gRPC, C=8, 256 bytes) registró 1589 respuestas, cinco errores y 415.810696 s. La duración total medida fue 653.4615285 s. No se identificó la causa; no es correcto atribuirla a HTTP/2, al proveedor de IA, al sistema operativo o a suspensión del equipo sin evidencia.

Se decidió repetir **todo el diseño**, añadiendo `error_types` al script antes de la segunda serie. No se sustituyó selectivamente la fila desfavorable. Hubo un error de ruta relativa en el comando de respaldo: se intentó copiar `outputs/results.csv` estando ya dentro de `outputs`. La copia falló y el siguiente comando sobrescribió el CSV inicial. Se conservan en el directorio de trabajo el registro de consola de la primera serie y el resumen de auditoría; **no se conserva su CSV completo**. Esta es una limitación real de trazabilidad, también declarada en el artículo. El CSV de entrega pertenece a la segunda serie. El primer render de Quarto falló al comprobar que la primera serie contenía errores; ese intento no produjo un PDF válido.

## Segunda batería y cambios de análisis

La segunda batería terminó con 80 filas, 786695 respuestas correctas y 35 errores. Orden 31: gRPC/C=32/4096 bytes, 20 `AioRpcError:StatusCode.CANCELLED`, 1119.3279728 s. Orden 75: REST/C=32/4096 bytes, 15 `TimeoutError`, 31.623736 s. Se conservaron **todas** las filas. Se guardó correctamente un respaldo completo de esta segunda batería en el directorio de trabajo. No se identificó la causa; se evita afirmar que la serie fue estable.

Se retiró el requisito inicial de cero errores del análisis, manteniendo la validación de 80 filas y cinco repeticiones por condición. Los errores aparecen explícitamente en el documento, y las barras de la figura se cambiaron de intervalos t a mediana y rango observado, ante la falta de justificación de normalidad/estacionariedad. Este cambio se declara como posterior a la observación de anomalías, no como decisión previa. La tabla conserva medias de todas las ejecuciones. La contribución de IA y la actividad de escritorio compartido son posibles interferencias, pero no se demostró que causaran los incidentes.

## Declaración de integridad y revisión pendiente

### Verificación técnica final realizada por Codex

- `python -m py_compile outputs/benchmark.py`: completado correctamente.
- CSV: 80 filas, cinco repeticiones por combinación y orden único. Se comprobaron `rps = requests/elapsed_s`, orden p50 <= p95 <= p99, media RSS <= máximo RSS y suma de `error_types` igual a `errors`.
- SHA-256 de `results.csv`: `576d58e4c44faa535d75766fe3b475a9934c77770745757d637832b0005b0a30`.
- Quarto 1.11.9 compiló el PDF final con Jupyter, pdflatex, clase IEEEtran Conference, Times 10 pt, citas natbib y estilo IEEEtran. El resultado tiene **tres páginas Letter**, dentro del rango exigido.
- La instalación inicial de IEEEtran con tlmgr requirió actualizar el gestor. La clase y el estilo se obtuvieron del espejo CTAN de MIT y se instalaron en `texmf-local`; Quarto resolvió además dependencias de español y LaTeX. No se usó otro generador para sustituir Quarto.
- Se corrigió un fallo de `longtable` en dos columnas generando una tabla LaTeX `tabular` desde los mismos datos. Se corrigió también una figura demasiado ancha, que ahora ocupa una columna. Se renderizaron las tres páginas finales con Poppler y se inspeccionaron visualmente: texto, figura, tabla, citas y cinco referencias legibles, sin superposición.
- Se inicializó Git localmente. El contenido de entrega se limita a los ocho archivos solicitados; los registros y archivos auxiliares se mantienen fuera de esa carpeta. No se ha publicado un repositorio remoto ni creado una URL pública.

Los datos del CSV entregado proceden de llamadas locales reales, no de valores inventados. Se declara asistencia sustancial de Codex en programación, experimentación, redacción y revisión, y asistencia de OpenCode en propuestas de código y maquetación. Las fuentes y sugerencias de IA se comprobaron y se rechazaron errores concretos, incluidos números ilustrativos y una asociación bibliográfica falsa.

**Pendiente de la investigadora:** leer el código y PDF, revisar hipótesis y límites, contrastar referencias, aceptar o corregir el análisis y registrar aquí la fecha y sus observaciones reales. Este documento no afirma una revisión humana ya efectuada. La responsabilidad académica corresponde a la autora y debe respetarse la política de su institución.

Al cerrar la preparación local, la publicación pública y la entrega en Moodle todavía no se habían realizado.

## Actualización posterior: publicación autorizada

La usuaria solicitó expresamente publicar los ocho archivos y proporcionó su cuenta `Nayda-villacres`. Tras resolver dificultades del control de ventanas, Codex accedió a su sesión de GitHub en Chrome y creó el repositorio público [investigacion-sistemas-distribuidos-u2](https://github.com/Nayda-villacres/investigacion-sistemas-distribuidos-u2). Se preparó la carga de los ocho archivos sin credenciales ni registros internos. La autorización de publicación no se interpreta como una revisión académica ya realizada. No se efectuó una entrega en Moodle.
