# Bitácora de OpenCode e integridad académica

## Alcance de OpenCode y declaración de herramientas

OpenCode 2.2.7, instalado en la computadora de la autora y utilizado desde la terminal de Windows, fue el copiloto consultado para propuestas de código Python, revisión del diseño experimental, bloques Quarto con `label` y `fig-cap`, y formato BibTeX. Las consultas históricas y sus respuestas se conservan más abajo, incluidas sugerencias descartadas o corregidas. No se atribuye a esas consultas la ejecución de los benchmarks.

**Declaración complementaria de asistencia:** también se utilizó Codex para implementar y auditar el código, ejecutar comandos y experimentos, comprobar referencias, redactar y compilar el documento, y publicar los archivos. Esta participación ocurrió y se mantiene declarada para que la documentación no sugiera un uso exclusivo de OpenCode. La identificación de funciones de cada herramienta es una declaración de procedencia, no una atribución a OpenCode de actividades ajenas. La autora aportó la revisión declarada y las valoraciones personales registradas.

### Verificación previa al ajuste documental

Antes de esta revisión se cotejaron los registros locales JSONL de OpenCode y las acciones de esta sesión. Se identificaron cinco consultas con respuestas sustantivas, una consulta inicial fallida por autenticación, una revisión de archivos sin una auditoría final utilizable y su intento de continuación sin respuesta utilizable. Las respuestas verificadas respaldan únicamente los aportes indicados en la tabla.

| Registro local | Aporte efectivamente observado | Límite o corrección |
|---|---|---|
| `opencode-directo.jsonl` | Auditoría del diseño y propuestas de integración de CSV/Quarto. | Varias advertencias eran hipotéticas y no describían fallos presentes en el script. |
| `opencode-standalone.jsonl` | Limitaciones metodológicas, configuración IEEEtran y bloque Quarto basado en CSV. | Se adaptaron nombres de columnas y controles al proyecto real. |
| `opencode-beam.jsonl` | Ejemplo de figura con `label` y `fig-cap`. | Se descartaron cifras ilustrativas y afirmaciones técnicas incorrectas. |
| `opencode-codigo.jsonl` | Propuesta de esqueleto y ejemplo BibTeX. | Interpretó C como lenguaje C y asoció un DOI al artículo equivocado; no se adoptaron esos errores. |
| `opencode-correccion.jsonl` | Creación de un esqueleto de corutinas tras aclarar el significado de C. | Se corrigió la selección del proceso para CPU; el esqueleto no produjo las mediciones publicadas. |

Se conserva el historial de prompts, incidencias, atribuciones y respuestas humanas que sigue. La revisión documental concentra la explicación de OpenCode en el artículo y el README y remite aquí a la declaración completa; no elimina una herramienta efectivamente utilizada ni modifica retrospectivamente la autoría de las acciones. No se ejecutaron nuevos prompts a OpenCode para atribuirlos a etapas anteriores. Los datos, el benchmark, la bibliografía científica, las conclusiones y las limitaciones del experimento se mantienen.

## Historial de desarrollo y revisión

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

**Estado al finalizar la preparación local:** estaba pendiente la revisión de la investigadora. La responsabilidad académica corresponde a la autora y debe respetarse la política de su institución. Véase la confirmación posterior registrada al final de esta bitácora.

Al cerrar la preparación local, la publicación pública y la entrega en Moodle todavía no se habían realizado.

## Actualización posterior: publicación autorizada

La usuaria solicitó expresamente publicar los ocho archivos y proporcionó su cuenta `Nayda-villacres`. Tras resolver dificultades del control de ventanas, Codex accedió a su sesión de GitHub en Chrome y creó el repositorio público [investigacion-sistemas-distribuidos-u2](https://github.com/Nayda-villacres/investigacion-sistemas-distribuidos-u2). Se preparó la carga de los ocho archivos sin credenciales ni registros internos. La autorización de publicación no se interpreta como una revisión académica ya realizada. No se efectuó una entrega en Moodle.

Los ocho archivos se publicaron y se verificó su acceso mediante la API pública de GitHub sin autenticación. Sus identificadores de contenido coincidieron con los ocho archivos locales.

## Confirmación posterior de revisión humana

Después de la publicación, la autora comunicó en el chat: «Ya lo revise», y solicitó presentar los archivos en el orden de la guía. Se registra su confirmación de revisión, sin atribuirle observaciones concretas, cambios de análisis o una auditoría línea por línea no descritos. El README incorpora la estructura en el orden solicitado; la lista nativa de GitHub conserva su orden automático por nombre. El PDF es el compilado anterior a esta confirmación y no se modificaron los resultados experimentales.

También se confirmó que OpenCode fue ejecutado desde su instalación local de Windows: `opencode v2.2.7`, localizado por PowerShell en `C:\Users\Nani\AppData\Roaming\npm\opencode.ps1`. Codex realizó gran parte de la programación, experimentación y redacción; OpenCode aportó las consultas y respuestas documentadas, incluidas propuestas corregidas. No se atribuye todo el trabajo exclusivamente a OpenCode.

## Auditoría asistida solicitada por la investigadora

La autora pidió a Codex explicar `benchmark.py` por secciones y líneas, volver a ejecutar el experimento, revisar unidades y comparabilidad, interpretar los resultados y documentar las intervenciones. Esta sección registra la revisión técnica hecha por Codex para ayudar a la autora. Las observaciones siguientes no se presentan como palabras, conclusiones personales o aprobaciones específicas de la investigadora.

### Paso 1. Lectura del código por líneas

La numeración corresponde al archivo de 124 líneas publicado. No se cambió el benchmark durante esta auditoría, para conservar la correspondencia entre código y mediciones. Las líneas vacías separan secciones y no ejecutan acciones.

| Línea(s) | Explicación y observación de auditoría |
|---|---|
| 1 | Documenta que se trata de una prueba real por loopback. La frase por sí sola no prueba el origen de los datos: se contrasta con ejecución y registros. |
| 2 | Importa argumentos CLI, concurrencia asíncrona, CSV, fechas UTC, JSON y procesos separados. |
| 3 | Importa información del equipo, aleatorización, estadística y relojes. |
| 4 | Importa `Path`, que no se utiliza. Es código innecesario, sin efecto sobre los resultados. |
| 5–9 | Carga aiohttp/HTTP, gRPC, psutil y las herramientas para definir Protobuf dinámicamente. |
| 11–12 | Describe el contrato lógico: una cadena `text`, enviada y devuelta por un servicio eco. Es un comentario equivalente al esquema; no es un archivo `.proto` compilado. |
| 13 | Crea un descriptor Protobuf proto3 con paquete `bench`. |
| 14 | Añade el mensaje `Payload` y su campo número 1, de tipo cadena (`type=9`). |
| 15 | Registra el descriptor en un pool independiente. |
| 16 | Obtiene la clase de mensaje que puede serializar y deserializar Protobuf, evitando archivos adicionales y `protoc`. |
| 18 | Define el servidor asíncrono; `ready` es el extremo de un pipe para comunicar al padre el puerto asignado. |
| 19–20 | Selecciona REST y define su manejador de solicitudes. |
| 21 | Verifica HTTP/1.1. Usa `assert`: no ejecutar con `python -O`, que desactiva las aserciones. |
| 22 | Lee y deserializa el JSON recibido. |
| 23 | Devuelve el mismo texto en JSON. No realiza base de datos ni trabajo de negocio. |
| 24 | Registra el recurso POST `/echo`. |
| 25 | Prepara el servidor y desactiva el registro de accesos, reduciendo interferencia de escritura por solicitud. |
| 26 | Escucha en 127.0.0.1 y puerto 0, para que Windows asigne un puerto libre. |
| 27 | Envía al padre el puerto real. Accede al atributo privado `_server`: funciona en la versión probada, pero requiere revisión si se actualiza aiohttp. |
| 28–29 | Selecciona gRPC y define un eco con la misma semántica de cadena. |
| 30 | Crea un servidor `grpc.aio`. |
| 31 | Registra el nombre de servicio `bench.Echo` mediante un manejador genérico. |
| 32 | Define la llamada unaria `Call` y convierte bytes de entrada en `Payload`. |
| 33 | Convierte `Payload` de salida a bytes Protobuf. |
| 34 | Abre puerto efímero en loopback, sin TLS, inicia el servidor e informa el puerto al padre. |
| 35 | Mantiene vivo el servidor esperando un evento que no se activa. El padre lo termina al acabar la ejecución. |
| 37 | Función de entrada del proceso hijo: crea su propio bucle asíncrono para el servidor. |
| 39 | Define una ejecución individual, parametrizada por pila, clientes, tamaño, duración, calentamiento, PID y puerto. |
| 40 | Genera texto ASCII repetido; inicializa latencias, errores y muestras. `psutil.Process(pid)` apunta al servidor, no al generador. |
| 41 | Inicializa los recursos cliente para poder cerrarlos al final. |
| 42–44 | REST reutiliza una sesión con límite de hasta C conexiones y timeout nominal de 10 s por solicitud. El límite del pool no demuestra que existan exactamente C conexiones TCP. |
| 45–46 | La llamada REST envía un POST con JSON y espera la respuesta. |
| 47 | Exige estado HTTP satisfactorio, deserializa JSON y comprueba que el contenido recibido sea idéntico. La validación está incluida en la latencia. |
| 48–50 | gRPC crea un canal compartido sin TLS y espera hasta 10 s su disponibilidad antes del calentamiento. |
| 51–52 | Configura la ruta del RPC y las conversiones de mensajes Protobuf. |
| 53–54 | Envía una llamada unaria con timeout nominal de 10 s y verifica el texto devuelto. El objeto Protobuf se construye dentro de la llamada medida. |
| 55–56 | Define un trabajador cliente y permite actualizar el contador de errores de la ejecución. |
| 57 | Mientras no venza el plazo, el trabajador inicia otra llamada. Es carga cerrada: cada cliente espera su respuesta antes de enviar la siguiente. |
| 58 | Captura un instante inicial con `perf_counter_ns`. Sus unidades son ns, pero eso no significa exactitud física de 1 ns. |
| 59–60 | Ejecuta y espera la operación real de red. |
| 61 | Guarda latencia de respuestas correctas durante la medición. Divide nanosegundos entre 1 000 000 para obtener milisegundos. No guarda latencias individuales en disco. |
| 62–64 | Si falla el calentamiento, aborta. Durante la medición cuenta el fallo y continúa sin reintentar esa solicitud. |
| 65–67 | Registra la clase de excepción y, para errores gRPC, su estado, agrupando los recuentos por tipo. |
| 68–70 | Muestrea RSS del proceso servidor y convierte bytes a MiB dividiendo entre 2^20. Intenta esperar 20 ms entre muestras; el intervalo real no es fijo porque comparte el bucle del cliente. |
| 71–73 | Ejecuta C trabajadores de calentamiento con `record=False`; sus latencias y errores no se mezclan con el CSV medido. |
| 74 | Lee CPU acumulada del servidor y CPU del cliente, e inicia la medición de tiempo transcurrido. |
| 75 | Inicia el muestreo de memoria y define el plazo nominal. |
| 76 | `asyncio.gather` programa C corutinas `worker` concurrentes. C son clientes lógicos, no C computadoras ni C procesos. |
| 77 | Espera a que terminen todos los trabajadores, mide la duración real y el consumo de CPU del cliente. Incluye el drenaje de llamadas en vuelo. |
| 78–79 | Lee CPU final del servidor, cancela el muestreador y espera su terminación. |
| 80 | Resta CPU de usuario y sistema iniciales a los valores finales; obtiene CPU-segundos del proceso servidor. |
| 81 | Ordena las latencias correctas. |
| 82–85 | Calcula percentiles por interpolación lineal entre observaciones vecinas. No calcula percentiles de llamadas fallidas. |
| 86 | Impide generar una fila sin ninguna respuesta correcta; una ejecución así abortaría y dejaría un CSV parcial. |
| 87 | Devuelve respuestas válidas, errores, tipos de error, duración real y throughput `N/T`. Cada fila resume una ejecución completa. |
| 88 | Devuelve media, p50, p95 y p99 de latencia en ms. |
| 89 | CPU total en s; CPU% = 100 × CPU-s/T; CPU por respuesta correcta = CPU-s × 10^6/N, en microsegundos. El trabajo consumido por fallos permanece en el numerador. |
| 90 | Devuelve media y máximo RSS observados, y cantidad de muestras. No es máximo absoluto ni memoria adicional atribuible al transporte. |
| 91 | Devuelve CPU-segundos del cliente; no mide su memoria. |
| 92–94 | Cierra sesión REST o canal gRPC aun cuando la ejecución lance una excepción. |
| 96–98 | Define la interfaz CLI: tres segundos de medición, uno de calentamiento y cinco repeticiones por defecto. |
| 99 | Concurrencias por defecto: 1, 8, 32 y 64. |
| 100 | Tamaños por defecto: 256 y 4096 bytes útiles; semilla de orden 20261113. |
| 101 | El destino por defecto es `results.csv`. Atención: la línea 105 lo abre en modo de sobrescritura. |
| 102 | Rechaza valores no positivos. No valida expresamente NaN/inf ni parámetros duplicados: usar valores finitos y la rejilla documentada. |
| 103 | Construye el producto cartesiano: 5 × 4 × 2 × 2 = 80 ejecuciones en la batería original. |
| 104 | Aleatoriza el orden con una semilla reproducible. No vuelve reproducibles los tiempos del sistema operativo. |
| 105–106 | Abre un CSV nuevo en UTF-8 e inicializa su escritor. Para la nueva validación se especificó otro destino, preservando el original. |
| 107–108 | Recorre los tratamientos y crea un servidor nuevo en un proceso separado por ejecución. |
| 109–111 | Espera hasta 20 s a que el servidor informe su puerto; si no arranca, aborta. |
| 112 | Ejecuta el cliente sobre ese PID y puerto reales. |
| 113–115 | Registra finalización UTC, orden, pila, C, tamaño, repetición, semilla, tiempos configurados y métricas observadas. |
| 116–117 | Añade CPU lógica, RAM y versiones. `platform.processor()` puede identificar familia de CPU sin dar su nombre comercial. |
| 118 | Escribe los nombres de columnas al recibir la primera ejecución completada. |
| 119 | Escribe y vacía el búfer de cada fila, limitando pérdida de filas por una interrupción posterior. No equivale a una garantía frente a corte eléctrico. |
| 120 | Muestra un resumen de progreso, throughput redondeado y errores; el CSV conserva mayor precisión. |
| 121–122 | Termina el proceso hijo y cierra el pipe. Es finalización forzada, fuera de la ventana medida; no caracteriza un apagado elegante del servicio. |
| 124 | Protege el arranque de procesos en Windows y ejecuta `main` cuando se invoca el script. |

### Comparabilidad de REST y gRPC

| Control | REST | gRPC | Dictamen |
|---|---|---|---|
| Operación | Eco de `text` | Eco de `text` | Misma semántica; sin base de datos. |
| Texto útil | ASCII de 256/4096 bytes | ASCII de 256/4096 bytes | Igual dato lógico. |
| Cliente | C corutinas secuenciales por trabajador | C corutinas secuenciales por trabajador | Igual máximo de llamadas lógicas pendientes, no igualdad de conexiones. |
| Reutilización | Sesión y pool de hasta C conexiones | Un canal compartido | Diferencia deliberada de pilas. |
| Codificación | JSON | Protobuf | Confusor: no se aísla el efecto de HTTP/2. |
| Transporte | HTTP/1.1 verificado por aserción | HTTP/2 del runtime gRPC | No se capturaron paquetes para una verificación independiente. |
| TLS/compresión | Sin TLS ni compresión habilitada | Sin TLS ni compresión habilitada | Comparación local sin costes de seguridad. |
| Entorno | 127.0.0.1, servidor hijo nuevo | 127.0.0.1, servidor hijo nuevo | Mismo equipo, sin aislamiento físico. |
| Tiempo | Mismos parámetros; tiempo real con drenaje | Mismos parámetros; tiempo real con drenaje | Las interrupciones pueden alargar la ventana; no hay watchdog externo. |
| Éxito | Estado HTTP y texto correctos | RPC y texto correctos | Se excluyen errores de los percentiles; se cuentan por separado. |
| Recursos | PID servidor | PID servidor | No se mide toda la máquina ni ambos clientes+servidores juntos. |

Una comprobación de serialización con las bibliotecas locales dio 268/4108 bytes de cuerpo JSON y 259/4099 bytes Protobuf para 256/4096 bytes útiles. No incluye HTTP, las tramas gRPC ni TCP; no es una captura de tráfico. Por tanto, `payload_bytes` no debe describirse como bytes transmitidos en el cable. El reloj local reportó QueryPerformanceCounter, monotónico, no ajustable y resolución nominal de 10^-7 s (100 ns). La unidad de retorno de `perf_counter_ns` no implica exactitud de 1 ns.

### Hallazgos y decisiones de esta auditoría

No se detectó inversión de unidades en las fórmulas implementadas. Se identificaron limitaciones que afectan la interpretación: carga cerrada, latencias de éxitos únicamente, posibilidad de ventanas anómalas sin watchdog externo, muestreo RSS no uniforme y factores de códec/conexión mezclados. La pérdida del CSV de la primera batería sigue siendo una limitación, no una anomalía corregida retroactivamente.

Se decidió mantener el código que produjo los datos publicados. No se afirma que la autora haya aprobado modificaciones específicas al algoritmo: no se aplicaron. Las mejoras recomendadas para una versión futura son validación explícita en lugar de `assert`, rechazo de NaN/inf, protección contra sobrescritura, watchdog externo y conservación de latencias individuales y muestras con marca temporal. Introducirlas requeriría versionar el código y repetir las mediciones, no reutilizar los resultados como si procedieran de esa versión mejorada.

Documentación primaria consultada para revisar la interpretación: [relojes de Python](https://docs.python.org/3.12/library/time.html), [API de psutil](https://psutil.readthedocs.io/), [conceptos de gRPC](https://grpc.io/docs/what-is-grpc/core-concepts/). La revisión de fórmulas y sus limitaciones se basa también en el código y en las ejecuciones locales, no en valores de rendimiento tomados de esas fuentes.

### Paso 2. Nueva ejecución y validación numérica

Se ejecutó realmente, desde la terminal local, sin sobrescribir los resultados publicados:

```powershell
python outputs/benchmark.py --seconds 2 --warmup 0.5 --repeats 3 --concurrency 1 8 32 64 --sizes 256 4096 --seed 20261114 --output work/results-validacion.csv
```

Resultado: **48 ejecuciones, 225734 respuestas correctas, cero errores**. Tiempo medido acumulado: **96.4831699 s**, excluyendo calentamiento y arranque de servidores. Las ventanas reales oscilaron entre **2.0000827 y 2.0481407 s**. La nueva prueba usa tres repeticiones y ventanas más cortas que la batería original; es una validación complementaria y no una reproducción idéntica de sus condiciones temporales. La semilla cambia el orden; no fija el rendimiento.

El CSV original conserva su SHA-256 `576d58e4c44faa535d75766fe3b475a9934c77770745757d637832b0005b0a30`. La nueva captura tiene SHA-256 `c3cff561919aa01ec9d4ebbe5da79ce206f60de52ab2b46d7ef5f4f5af201823`. Se incorpora completa más abajo para mantener los ocho archivos obligatorios sin añadir un noveno archivo al repositorio.

Un verificador independiente del benchmark comprobó, en ambas capturas: producto cartesiano completo, ausencia de tratamientos duplicados, órdenes únicos, C y tamaño correctos, número de repeticiones, parámetros temporales y semilla, finitud de las métricas numéricas, igualdad entre suma de errores por tipo y errores totales, `rps=N/T`, CPU%=100×CPU-s/T, CPU-us/respuesta=10^6×CPU-s/N, p50<=p95<=p99, media RSS<=máximo RSS y presencia de muestras. También comprobó que throughput×latencia media/1000 no excediera C, como control de consistencia de la concurrencia lógica. Todas esas comprobaciones pasaron.

Esto confirma coherencia de los agregados y que el programa ejecuta llamadas reales con validación de contenido. **No permite reconstruir** las latencias individuales del CSV original, demostrar de forma independiente cada instante histórico ni recuperar el CSV perdido de la primera batería. No se confunde consistencia algebraica con prueba absoluta de procedencia. La ejecución original fue realizada y documentada en esta sesión; la nueva prueba aporta evidencia adicional de funcionamiento.

### Paso 3. Interpretación propuesta a la investigadora

La siguiente tabla corresponde exclusivamente a la nueva validación. Son medias de tres ejecuciones por condición; CPU se refiere al servidor y RSS a la media de sus máximos muestreados.

| Texto útil | C | Pila | Respuestas/s | p95 ms | CPU us/respuesta | CPU % de un núcleo | RSS MiB |
|---:|---:|:---|---:|---:|---:|---:|---:|
|256|1|REST|1517.77|0.80|355.50|53.90|47.95|
|256|1|gRPC|1027.20|1.26|941.79|95.02|50.36|
|256|8|REST|3618.59|3.07|245.29|88.76|47.98|
|256|8|gRPC|1667.08|5.89|840.43|137.72|50.83|
|256|32|REST|4193.00|10.20|212.90|87.40|49.85|
|256|32|gRPC|1756.92|21.33|783.64|136.21|51.18|
|256|64|REST|4326.29|19.79|198.68|82.79|52.40|
|256|64|gRPC|1403.17|51.68|939.17|131.83|51.40|
|4096|1|REST|1404.70|0.87|344.50|48.17|47.79|
|4096|1|gRPC|891.77|1.38|1016.47|90.60|50.56|
|4096|8|REST|3751.23|3.07|238.47|87.73|48.14|
|4096|8|gRPC|1776.91|5.38|773.84|135.92|50.97|
|4096|32|REST|3842.73|11.04|239.31|89.76|50.18|
|4096|32|gRPC|1520.61|24.91|900.46|135.95|51.76|
|4096|64|REST|3390.52|22.47|255.89|86.75|52.81|
|4096|64|gRPC|1395.31|50.24|971.65|135.52|52.02|

En esta validación REST obtuvo mayor throughput, menor p95 y menor CPU por respuesta correcta en las ocho combinaciones C/tamaño. A C=64, REST completó aproximadamente 3.08 veces el throughput de gRPC con 256 bytes y 2.43 veces con 4096 bytes. Esto describe estas implementaciones locales, no una propiedad universal de REST.

El patrón de throughput favorable a REST coincide con las medias del CSV original, pero los valores absolutos variaron. La p95 original a C=64/256 bytes favorecía a gRPC (29.93 frente a 48.48 ms); en la nueva captura favorece a REST (19.79 frente a 51.68 ms). Esa inversión exige moderar las conclusiones sobre latencia. La segunda captura no borra los 35 errores ni las interrupciones del conjunto publicado.

La memoria no presenta un único ganador: en la nueva prueba, gRPC tiene mayor RSS a C=1/8/32, y algo menor a C=64. Las diferencias de alrededor de un MiB en C=64 no demuestran un ahorro sistemático ni proporcional al transporte. CPU gRPC superior al 100% es posible porque un proceso puede consumir más de un núcleo; no significa superar el 100% de toda la computadora de 16 CPU lógicas.

Posibles explicaciones, **no causas demostradas**: gestión de llamadas y flujos de gRPC, interacción entre Python y su núcleo nativo, políticas de conexión, códec, planificación y competencia por recursos del equipo. Aunque Protobuf codificó este texto con menos bytes de cuerpo, ese ahorro no aseguró mayor throughput. Para separar causas harían falta otros controles y medición de red. No se recomienda migrar cualquier servicio solo con estos datos.

### Paso 4. Registro de intervenciones y límites de autoría

- **Solicitado por la autora:** explicación por líneas, nueva ejecución, verificación de métricas/comparabilidad, ayuda interpretativa y registro honesto de intervenciones. Los prompts reales anteriores a OpenCode permanecen en esta misma bitácora; no se enviaron nuevos prompts a OpenCode durante la batería de validación.
- **Realizado por Codex:** revisión del archivo de 124 líneas, contraste de fórmulas y documentación primaria, comprobación de tamaños serializados/reloj, ejecución de 48 ensayos nuevos y verificación de ambas capturas. No se modificó `benchmark.py` ni `results.csv`.
- **Problemas identificados:** validaciones que desaparecen con `python -O`, sobrescritura por defecto del CSV, dependencia de un atributo privado aiohttp, validación incompleta de parámetros no finitos, ausencia de watchdog y trazas individuales, confusores de códec/conexión, muestreo no uniforme y sensibilidad de latencia entre series. La importación `Path` no utilizada es una limpieza pendiente, no un defecto de medición.
- **Correcciones realizadas en esta intervención:** documentación de unidades, controles, límites y nueva evidencia en esta bitácora. La captura nueva se guardó por separado; no se sustituyeron filas del artículo para favorecer una conclusión. Las correcciones de código de etapas anteriores siguen documentadas en las secciones precedentes.
- **Intervención humana efectivamente comunicada:** la autora había indicado «Ya lo revise» y ahora solicitó esta revisión guiada. No se afirma que haya escrito personalmente este análisis ni aprobado cada hallazgo técnico. Se le solicitó expresar si acepta la conclusión limitada al microbenchmark o desea matizarla; su respuesta específica debe registrarse cuando exista.

La conclusión propuesta es: «REST rindió mejor en este microbenchmark local, pero los confusores y la variación impiden generalizar a todas las redes y aplicaciones». Es una propuesta técnica de Codex que la autora debe valorar con su propio juicio; no se presenta como una declaración suya antes de recibir su respuesta.

### Valoración personal comunicada por la investigadora

Después de recibir los resultados y la explicación, la autora respondió en el chat:

> De acuerdo con los resultados obtenidos, considero que REST presentó un mejor rendimiento que gRPC en las pruebas realizadas. Sin embargo, también es importante reconocer que estos resultados corresponden a un entorno local y que existen factores que pudieron influir en las mediciones, como el consumo de recursos del equipo, la cantidad de clientes concurrentes y las variaciones durante la ejecución. Por esta razón, considero que no sería correcto afirmar que REST es superior a gRPC en todos los escenarios, ya que el comportamiento de ambas arquitecturas puede cambiar dependiendo de las condiciones de la red y de las características de cada aplicación.

Esta respuesta documenta su aceptación e interpretación de la conclusión limitada al escenario probado. No se transforma esa aceptación en una afirmación de cambios de código, ni en una aprobación individual de todas las mejoras futuras: el benchmark y el CSV original permanecen sin modificaciones. La autora reconoce los límites del entorno local y evita declarar superioridad universal de una arquitectura.

### Ampliación del análisis personal tras revisar las limitaciones

La autora indicó que había consultado las limitaciones documentadas y aportó el siguiente análisis académico:

> Después de revisar los resultados obtenidos, considero que REST presentó un mejor rendimiento que gRPC en las pruebas realizadas, especialmente al trabajar con diferentes cantidades de clientes concurrentes. Sin embargo, también observé que algunas ejecuciones presentaron errores y tiempos de respuesta elevados, lo que demuestra que los resultados no fueron completamente uniformes.
>
> Desde mi punto de vista, es importante considerar que las pruebas se realizaron en una sola computadora, donde el cliente y el servidor compartían recursos. Además, ambas arquitecturas utilizaron diferentes métodos de serialización y gestión de conexiones, lo que también pudo influir en su rendimiento.
>
> Por esta razón, considero que REST tuvo un mejor comportamiento en las condiciones evaluadas, pero no sería correcto afirmar que siempre es superior a gRPC. Para obtener una conclusión más amplia, sería necesario realizar pruebas en diferentes equipos y condiciones de red.

Esta intervención documenta que la autora examinó las limitaciones y relacionó su conclusión con la variación observada, las incidencias, los recursos compartidos y las diferencias entre pilas. Se conserva como valoración personal comunicada por ella. La referencia a ejecuciones con errores corresponde al conjunto original publicado; la validación complementaria de 48 ejecuciones registró cero errores. La interpretación no atribuye una causa demostrada a las interrupciones ni sustituye los datos experimentales. No se registra como una modificación del código o como una auditoría personal de cada línea que la autora no haya descrito.


### Captura completa de la nueva validación

El bloque siguiente conserva las 48 filas y todas las columnas de la captura complementaria; no sustituye `results.csv`. El hash indicado arriba corresponde al archivo CSV original de esta nueva captura, incluidos sus saltos de línea.

```csv
timestamp_utc,order,protocol,concurrency,payload_bytes,repeat,seed,warmup_s,target_s,requests,errors,error_types,elapsed_s,rps,mean_ms,p50_ms,p95_ms,p99_ms,server_cpu_s,server_cpu_pct,server_cpu_us_req,server_rss_mean_mib,server_rss_max_mib,rss_samples,client_cpu_s,python,os,cpu,logical_cpus,ram_gib,aiohttp,grpcio,psutil
2026-11-14T03:02:15.238644+00:00,1,gRPC,32,4096,3,20261114,0.5,2.0,2855,0,{},2.0220695000025444,1411.9198177888582,22.53366669001751,22.2961,25.185279999999995,26.962758,2.765625,136.77200511636815,968.6952714535902,51.47127403846154,51.57421875,130,1.515625,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:02:18.595492+00:00,2,gRPC,1,256,2,20261114,0.5,2.0,1897,0,{},2.0008031000033952,948.1192827004221,1.0530070110701106,1.0066,1.319319999999999,1.7266279999999998,1.828125,91.36956055280491,963.6926726410121,50.476501937984494,50.51171875,129,1.09375,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:02:21.955823+00:00,3,REST,32,4096,3,20261114,0.5,2.0,6836,0,{},2.0021731999877375,3414.29003247165,9.353118212404915,8.9933,12.203225,13.389109999999997,1.859375,92.86783980583638,271.9975131655939,50.32996875,50.33203125,125,1.984375,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:02:25.370984+00:00,4,gRPC,64,256,2,20261114,0.5,2.0,2846,0,{},2.0481407000042964,1389.5529735794175,45.48525386507379,44.11855,54.187349999999995,62.93728500000002,2.515625,122.82481374422778,883.9160224877021,51.446969696969695,51.49609375,132,1.546875,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:02:28.694943+00:00,5,REST,1,4096,3,20261114,0.5,2.0,2703,0,{},2.0003511999966577,1351.2627182689303,0.7384011098779134,0.7204,0.8862000000000001,1.1681460000000006,1.015625,50.77233437816804,375.739918608953,48.03125,48.03125,129,1.265625,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:02:31.999483+00:00,6,REST,1,256,1,20261114,0.5,2.0,2898,0,{},2.0002733999863267,1448.8019487835063,0.6886975845410628,0.6684,0.8295650000000001,1.168835000000001,1.03125,51.555452370013484,355.8488612836439,47.875,47.875,129,1.296875,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:02:35.306914+00:00,7,REST,32,256,3,20261114,0.5,2.0,7748,0,{},2.0020683000038844,3869.9978417244643,8.253186615900878,8.0181,10.61843,12.311662999999998,1.734375,86.62916245148254,223.84808982963347,49.76171875,49.76171875,125,1.984375,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:02:38.648019+00:00,8,gRPC,1,256,3,20261114,0.5,2.0,1831,0,{},2.000995400012471,915.0445823056808,1.09098470780994,1.0559,1.3751,1.655920000000002,2.0,99.95025475758392,1092.2992900054614,50.43740985576923,50.47265625,130,0.984375,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:02:41.983206+00:00,9,gRPC,1,4096,2,20261114,0.5,2.0,1735,0,{},2.0009532000112813,867.0867464517502,1.1513961383285303,1.1095,1.46226,1.741394,1.796875,89.80095086631059,1035.6628242074928,50.543786337209305,50.6796875,129,0.859375,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:02:45.294977+00:00,10,REST,8,256,3,20261114,0.5,2.0,7326,0,{},2.000616400007857,3661.871411216677,2.182467048867049,2.0115,3.043875,3.596225,1.875,93.72111515194199,255.93775593775592,47.953125,47.953125,129,1.984375,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:02:48.704642+00:00,11,gRPC,64,256,1,20261114,0.5,2.0,2831,0,{},2.046194900001865,1383.5436692748183,45.701625891910986,45.6262,51.664249999999996,53.644169999999995,2.71875,132.86857473828726,960.3496997527376,51.44605232007576,51.453125,132,1.796875,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:02:52.028566+00:00,12,gRPC,8,256,1,20261114,0.5,2.0,3261,0,{},2.0042551000078674,1627.0383944574717,4.909853817847286,4.6897,6.3328,7.083440000000001,2.765625,137.9876743229514,848.0910763569457,50.63384205426357,50.6953125,129,1.46875,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:02:55.238676+00:00,13,gRPC,8,4096,2,20261114,0.5,2.0,3159,0,{},2.004951200011419,1575.5994460024804,5.069836150680596,5.022,6.105169999999999,6.722834000000001,2.921875,145.73297345009487,924.9366888255777,50.87439437984496,50.9296875,129,1.59375,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:02:58.548224+00:00,14,REST,1,4096,1,20261114,0.5,2.0,2697,0,{},2.0001323000178672,1348.4108026133608,0.7399698553948832,0.722,0.90126,1.251868,0.953125,47.65309774715831,353.4019280682239,47.703125,47.703125,129,1.21875,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:03:01.904271+00:00,15,REST,32,4096,1,20261114,0.5,2.0,6907,0,{},2.0021343999833334,3449.818353881486,9.256960503836687,8.7872,12.26921,14.953946,1.796875,89.74797096613284,260.1527435934559,50.16796875,50.16796875,125,2.0,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:03:05.217327+00:00,16,gRPC,1,4096,1,20261114,0.5,2.0,1815,0,{},2.000117000017781,907.4469143474431,1.1002002754820936,1.0669,1.34083,1.7448999999999966,1.65625,82.80765575140235,912.534435261708,50.17366157945737,50.35546875,129,1.15625,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:03:08.620305+00:00,17,gRPC,64,256,3,20261114,0.5,2.0,2938,0,{},2.045368499995675,1436.4159807908513,44.04225241660994,43.762950000000004,49.19868,50.501147,2.859375,139.7975474837931,973.2385976855004,51.21724076704545,51.25,132,1.640625,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:03:11.984655+00:00,18,REST,64,256,3,20261114,0.5,2.0,6451,0,{},2.0152630000084173,3201.0710264481886,19.787052472484888,18.7961,26.2041,34.0346,1.640625,81.4099698150141,254.32103549837234,52.49691280241935,52.5234375,62,1.984375,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:03:15.290791+00:00,19,REST,64,256,1,20261114,0.5,2.0,10016,0,{},2.0030312000017148,5000.421361380405,12.762711591453675,12.244,16.477575,19.804875,1.65625,82.6871793109654,165.36042332268372,52.40350632440476,52.40625,84,1.96875,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:03:18.434709+00:00,20,gRPC,8,256,2,20261114,0.5,2.0,3932,0,{},2.0037364999880083,1962.3338697595875,4.071655595116988,4.0108999999999995,4.74138,5.149828,2.78125,138.80318095800746,707.3372329603255,50.82022165697674,50.9375,129,1.65625,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:03:21.654232+00:00,21,gRPC,32,4096,1,20261114,0.5,2.0,3523,0,{},2.024134299979778,1740.4971597167225,18.27234782855521,17.3574,24.11045,25.839685999999993,2.859375,141.26409497771795,811.6307124609708,51.74666030534351,51.79296875,131,1.765625,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:03:24.964194+00:00,22,REST,8,4096,1,20261114,0.5,2.0,6974,0,{},2.00085680000484,3485.5068088746434,2.292765098938916,2.1552,3.1908449999999995,3.6025449999999983,1.796875,89.8052774189364,257.6534270146258,47.96018629807692,47.9609375,130,2.0,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:03:28.096958+00:00,23,REST,1,4096,2,20261114,0.5,2.0,3029,0,{},2.0000826999894343,1514.4373780224194,0.6589563222185539,0.6795,0.83476,1.0197079999999996,0.921875,46.09184410248986,304.3496203367448,47.63671875,47.63671875,129,1.46875,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:03:31.409662+00:00,24,REST,1,256,2,20261114,0.5,2.0,2916,0,{},2.0004302999877837,1457.6863787845084,0.6844829218106996,0.67055,0.797775,0.9414199999999988,1.0625,53.113572615176274,364.3689986282579,48.06640625,48.06640625,128,1.203125,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:03:34.727172+00:00,25,REST,8,256,2,20261114,0.5,2.0,7143,0,{},2.0007005999796093,3570.249341692005,2.238402631947361,2.0535,3.1227799999999997,3.52452,1.796875,89.81228875616439,251.557468850623,47.90437257751938,47.90625,129,1.984375,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:03:38.127862+00:00,26,gRPC,64,4096,3,20261114,0.5,2.0,2870,0,{},2.0437613999820314,1404.2735125662089,45.06927411149826,44.88595,50.87019,52.896123,2.765625,135.3203461042133,963.6324041811847,52.03734611742424,52.1484375,132,1.6875,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:03:41.463477+00:00,27,REST,64,4096,1,20261114,0.5,2.0,6901,0,{},2.005326399987098,3441.3350365528527,18.46972637298942,18.1443,22.164,25.8585,1.734375,86.48841405624336,251.32227213447325,52.84765625,52.84765625,65,2.0,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:03:44.641609+00:00,28,REST,8,4096,3,20261114,0.5,2.0,8961,0,{},2.000584399997024,4479.191180343769,1.78438378529182,1.6393,2.6142,2.9012399999999956,1.71875,85.91239639790038,191.8033701595804,48.20703125,48.20703125,128,1.984375,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:03:47.791007+00:00,29,gRPC,8,4096,1,20261114,0.5,2.0,3837,0,{},2.0038630999915767,1914.8014652378843,4.1727286421683605,4.0852,4.931819999999999,5.434264,2.578125,128.65774114064166,671.9116497263487,50.88529554263566,50.92578125,129,1.515625,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:03:50.986324+00:00,30,gRPC,32,256,3,20261114,0.5,2.0,3060,0,{},2.0219365999801084,1513.400568558927,21.02124045751634,21.8343,25.791769999999996,27.847938999999997,2.765625,136.78099501375107,903.7990196078431,51.316736778846156,51.33984375,130,1.46875,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:03:54.303873+00:00,31,REST,8,4096,2,20261114,0.5,2.0,6580,0,{},2.0006162999779917,3288.986498846573,2.4297738145896655,2.23675,3.415715,3.9530390000000004,1.75,87.4730451820897,265.9574468085106,48.239855862403104,48.2421875,129,2.0,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:03:57.499853+00:00,32,gRPC,32,256,2,20261114,0.5,2.0,3853,0,{},2.0167109000030905,1910.5366069048844,16.67529953283156,16.4279,18.8019,20.967396,2.78125,137.91019823395303,721.8401245782508,51.24417067307692,51.25,130,1.671875,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:04:00.644169+00:00,33,REST,32,256,2,20261114,0.5,2.0,10196,0,{},2.001922299998114,5093.104762362458,6.272231786975285,5.9718,8.117550000000001,9.99533,1.765625,88.19647995337598,173.16839937230287,49.90234375,49.90234375,125,2.0,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:04:03.761658+00:00,34,REST,32,4096,2,20261114,0.5,2.0,9335,0,{},2.0014626999909524,4664.088918590488,6.8504110123192286,6.5681,8.636399999999997,10.85563,1.734375,86.65537459218402,185.7927155865024,50.05078125,50.05078125,126,2.0,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:04:06.910236+00:00,35,gRPC,8,4096,3,20261114,0.5,2.0,3687,0,{},2.003438100015046,1840.3363697497368,4.3416992948196365,4.2233,5.09012,5.974423999999983,2.671875,133.36448977285266,724.6745321399512,50.99778948643411,51.04296875,129,1.75,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:04:10.086179+00:00,36,gRPC,32,256,1,20261114,0.5,2.0,3727,0,{},2.0180703999940306,1846.8136691420796,17.245950469546553,17.0513,19.39907,20.636585999999998,2.703125,133.9460209122534,725.281727931312,50.93704927884615,50.953125,130,1.609375,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:04:13.419460+00:00,37,gRPC,32,4096,2,20261114,0.5,2.0,2850,0,{},2.0221291999914683,1409.4054919992375,22.577967228070175,22.38875,25.444164999999998,26.84422899999999,2.625,129.81366373677187,921.0526315789474,51.83945610687023,51.90234375,131,1.578125,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:04:16.733198+00:00,38,REST,64,4096,3,20261114,0.5,2.0,6787,0,{},2.0039548000204377,3386.802935840061,18.823861956681892,18.3646,22.13258,27.207668000000023,1.765625,88.10702716358637,260.14807720642403,52.7109375,52.7109375,65,2.0,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:04:19.925222+00:00,39,REST,64,256,2,20261114,0.5,2.0,9568,0,{},2.0027754999755416,4777.370204557049,13.35823970526756,13.00215,16.687815,18.284743,1.6875,84.25807086319001,176.36914715719064,52.26953125,52.26953125,85,1.984375,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:04:23.077350+00:00,40,gRPC,1,256,1,20261114,0.5,2.0,2437,0,{},2.000109499989776,1218.4332907835583,0.8193858022158391,0.7815,1.07616,1.3303319999999996,1.875,93.7448674689853,769.3885925318014,50.027283187984494,50.08203125,129,1.09375,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:04:26.309090+00:00,41,gRPC,64,4096,2,20261114,0.5,2.0,2803,0,{},2.0433894000016153,1371.7405013443763,46.13786307527649,45.9466,51.1488,52.960836,2.859375,139.93294670109083,1020.1123795932929,52.01207386363637,52.078125,132,1.546875,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:04:29.623633+00:00,42,REST,32,256,1,20261114,0.5,2.0,7241,0,{},2.002542200003518,3615.9038246421374,8.826595884546334,8.2878,11.8556,14.144600000000002,1.75,87.38891994370584,241.67932605993647,49.88671875,49.88671875,120,1.921875,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:04:32.765965+00:00,43,REST,1,256,3,20261114,0.5,2.0,3294,0,{},2.0002308000111952,1646.8099581216145,0.6058616272009715,0.60885,0.76305,0.9770750000000004,1.140625,57.02466935283748,346.2735276259866,47.91796875,47.91796875,129,1.203125,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:04:36.126251+00:00,44,REST,64,4096,2,20261114,0.5,2.0,6709,0,{},2.006625800015172,3343.423572022882,19.051832508570577,18.6194,23.122839999999993,25.354368,1.71875,85.65373773161915,256.18572067372185,52.87890625,52.87890625,64,2.0,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:04:39.450946+00:00,45,gRPC,8,256,3,20261114,0.5,2.0,2831,0,{},2.005142000009073,1411.8700820127403,5.657656517131755,5.5786,6.6085,7.321779999999991,2.734375,136.368147492179,965.8689509007418,50.8390867248062,50.87109375,129,1.46875,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:04:42.810995+00:00,46,gRPC,1,4096,3,20261114,0.5,2.0,1802,0,{},2.0005229999951553,900.7644500984812,1.1082911764705883,1.0826,1.3287849999999999,1.570491,1.984375,99.19281108014282,1101.2069922308547,50.49333817829457,50.65234375,129,1.078125,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:04:46.223373+00:00,47,gRPC,64,4096,1,20261114,0.5,2.0,2886,0,{},2.0469305999868084,1409.9159004309179,44.84689237699238,44.9689,48.694824999999994,50.31854,2.6875,131.29414353458392,931.2196812196812,51.72378077651515,51.828125,132,1.578125,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
2026-11-14T03:04:49.553594+00:00,48,REST,8,256,1,20261114,0.5,2.0,7252,0,{},2.0012912999955006,3623.6603836814284,2.2051670987313843,2.01835,3.040444999999999,3.635698,1.65625,82.7590666088302,228.38527302813017,48.06640625,48.06640625,129,1.984375,3.12.3,Windows-11-10.0.26200-SP0,"AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD",16,15.34320068359375,3.14.5,1.85.1,7.2.2
```

## Revisión final realizada por OpenCode

Esta sección registra una intervención real y posterior a las secciones anteriores. No sustituye ni reescribe el historial previo: se añade al final del archivo para conservar intactos los prompts, atribuciones e intervenciones humanas ya documentados.

### Solicitud recibida

La autora encargó a OpenCode, ejecutado localmente en Windows, la revisión final del proyecto. El texto completo de la solicitud se conserva fuera de `outputs` en `work/prompt-revision-final-opencode.txt` y se transcribe aquí de forma fiel:

```text
Eres OpenCode, ejecutado localmente en Windows, y la autora te encarga la revision final de su proyecto. Realiza tu mismo la revision y las correcciones documentales necesarias usando tus herramientas. No delegues en otros agentes. Responde en espanol.

Alcance: revisa todos los archivos de la carpeta outputs y los registros previos work/opencode-*.jsonl cuando sean necesarios para comprobar atribuciones. El tema sigue siendo REST HTTP/1.1 frente a gRPC HTTP/2 bajo concurrencia, autora Villacres Martinez Nayda Antonela.

Restricciones estrictas:
1. NO modifiques benchmark.py, results.csv, articulo.qmd, articulo.pdf, references.bib ni _quarto.yml. No ejecutes el benchmark, no renderices el PDF, no cambies resultados, conclusiones, cifras ni limitaciones. Esos seis archivos estan validados y deben conservar exactamente sus bytes.
2. Solo puedes modificar outputs/README.md y outputs/PROMPTS_OPENCODE.md, si es necesario. No crees un noveno archivo en outputs. No modifiques ni borres registros previos de work. No publiques en GitHub ni ejecutes git commit; eso es una operacion mecanica posterior del orquestador.
3. OpenCode es el asistente oficial designado por la autora PARA ESTA REVISION FINAL y las actividades pendientes. No afirmes que fue la unica IA utilizada en todo el desarrollo historico: los registros acreditan intervencion previa de Codex. Conserva de manera integra el historial existente de prompts, atribuciones reales e intervenciones humanas. No conviertas acciones previas de Codex en acciones de OpenCode ni ocultes esa procedencia.
4. El articulo y el README ya describen los aportes reales de OpenCode y remiten a la declaracion completa. Comprueba esa coherencia mediante lectura, sin cambiar el articulo validado. Puedes aclarar en el README el papel oficial de OpenCode en la revision actual con una frase sobria, sin presentarlo como ejecutor del benchmark historico. Evita menciones repetitivas o innecesarias de otras herramientas fuera de la declaracion de procedencia.
5. En PROMPTS_OPENCODE.md agrega una nueva seccion que registre ESTA intervencion real: la solicitud recibida, este prompt completo o su transcripcion fiel, tu version y modelo si puedes verificarlos, archivos que efectivamente leiste, comprobaciones que realmente hiciste, cambios documentales que efectivamente aplicaste y aspectos que no se pueden certificar. Identifica claramente esta revision como realizada por OpenCode y distingue la orquestacion mecanica del trabajo intelectual de revision. No afirmes pruebas o lecturas que no hayas realizado. No inventes fechas, metadatos, referencias o actividades.
6. Antes de editar, guarda o calcula hashes de los seis archivos protegidos, y al finalizar verifica que coincidan. Verifica que el historial anterior de la bitacora permanezca integro (por ejemplo agregando al final sin reemplazar su contenido anterior). Los prompts y valoraciones humanas previas deben permanecer literales. Revisa la estructura de ocho archivos y los requisitos ya declarados de la rubrica; no prometas una calificacion o cumplimiento de uso historico exclusivo de OpenCode.
7. Si detectas una incompatibilidad entre los requisitos y los hechos, dejala descrita de forma breve y neutral. Si hubiera un defecto que requiera editar un archivo protegido, reportalo sin editarlo.

Al finalizar devuelve: hallazgos, cambios aplicados con nombres de archivo, comandos de comprobacion realmente ejecutados y sus resultados. No hagas mas cambios despues de esa respuesta final. El contenido de este prompt tambien esta guardado fuera de outputs como registro de esta solicitud.
```

### Identificación de la revisión

- Realizada por: OpenCode, asistente oficial designado por la autora para esta revisión final.
- Versión verificada por comando: `opencode v2.2.7`.
- Modelo: el entorno de esta sesión lo identifica como Beam Free (proveedor OpenCode). No se verificó por comando un identificador más específico; no se afirma otro.
- Orquestación mecánica (publicación, commits o mover archivos) no se ejecutó aquí; corresponde al orquestador posterior. El trabajo intelectual de esta revisión consistió en leer, contrastar, documentar e indicar límites, sin ejecutar el benchmark ni renderizar el PDF.

### Archivos efectivamente leídos

En `outputs`: `articulo.pdf`, `articulo.qmd`, `references.bib`, `_quarto.yml`, `benchmark.py`, `results.csv`, `README.md` y `PROMPTS_OPENCODE.md`. En `work`: `prompt-revision-final-opencode.txt`, los registros `work/opencode-*.jsonl` procesados mediante `work/verificar-atribuciones.py`, inspección directa inicial de `work/opencode-revision-final.jsonl` y los scripts `work/verificar-atribuciones.py`, `work/verificar-bitacora.py`, `work/verificar-contenido-articulo.py`, `work/verificar-ajuste-documental.py` y `work/verify-publication.py`. También se leyeron `work/hashes-antes-revision-opencode.json`.

### Comprobaciones realmente realizadas

- Hashes SHA-256 de los seis archivos protegidos comparados con `work/hashes-antes-revision-opencode.json`: coinciden antes de editar.
- Estructura de ocho archivos en `outputs`: confirmada; no se creó un noveno archivo.
- `results.csv`: 80 filas, protocolos REST/gRPC, concurrencias 1/8/32/64 y tamaños 256/4096 bytes.
- `articulo.pdf`: 3 páginas; contiene "OpenCode" y no contiene "Codex".
- `README.md` y `articulo.qmd`: no contienen "Codex".
- Bitácora: conserva el bloque CSV de 48 filas de la validación complementaria.
- `opencode --version`: `opencode v2.2.7`.
- No se ejecutó `benchmark.py`, no se renderizó el PDF y no se modificaron datos, conclusiones, cifras ni limitaciones.

### Cambios documentales aplicados en esta revisión

- `outputs/README.md`: se añadió una frase sobria que aclara el papel oficial de OpenCode en esta revisión final y que la revisión documental no ejecuta el benchmark ni modifica los datos validados.
- `outputs/PROMPTS_OPENCODE.md`: se añadió esta sección al final, conservando íntegro el historial anterior.

### Aspectos que no se pueden certificar

- No se puede certificar de forma independiente el origen histórico de cada byte ni recuperar el CSV perdido de la primera batería.
- Los registros acreditan intervención previa de Codex; no se afirma que OpenCode haya sido la única herramienta utilizada en todo el desarrollo.
- La validación complementaria de 48 ejecuciones es previa y documentada; no se repitió en esta revisión.
- No se puede certificar una calificación, ni el cumplimiento de un uso histórico exclusivo de OpenCode.
- El registro `work/opencode-revision-final.jsonl` contiene llamadas a herramientas pero no una respuesta textual final utilizable; por eso no se usó como prueba de una auditoría concluida.

## Aclaración posterior sobre el cierre del registro

Tras finalizar la revisión anterior, `work/opencode-revision-final.jsonl` contiene un evento `text` final y un `step_finish` con motivo `stop`. Por tanto, la observación anterior sobre la ausencia de una respuesta textual final utilizable quedó superada y no debe leerse como indicación de que faltara una auditoría final una vez concluida la revisión. Esta aclaración se añade al final por una indicación técnica del orquestador dentro del alcance autorizado por la autora, sin reescribir el historial previo ni modificar otros archivos.