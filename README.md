# Investigación formativa individual · Tema 3

**Autora:** Villacres Martinez Nayda Antonela.  
**Asignatura:** Sistemas Distribuidos y Paradigmas de la Computación (ETL1TP50).  
**Carrera:** Ingeniería en Telemática, Octavo PAO.  
**Unidad 2:** Comunicación y Coordinación en Sistemas Distribuidos.  
**Tema:** Comparativa de Rendimiento y Consumo de Recursos entre Arquitecturas REST (HTTP/1.1) vs. gRPC (HTTP/2 Multiplexado) bajo Concurrencia de Clientes.  
**Entrega:** URL pública de GitHub; 14 de noviembre de 2026, 23:59, hora de Ecuador.  
**Estado del proyecto:** artículo y materiales reproducibles publicados; auditoría técnica, validación complementaria e interpretación de resultados documentadas.

## Estructura obligatoria, en el orden de la guía

```text
investigacion-sistemas-distribuidos-u2/
├── articulo.pdf
├── articulo.qmd
├── references.bib
├── _quarto.yml
├── benchmark.py
├── results.csv
├── README.md
└── PROMPTS_OPENCODE.md
```

Este es el orden de presentación solicitado. GitHub muestra su lista de archivos ordenada automáticamente por nombre; los nombres se mantienen exactamente como exige la guía.

## Abstract

Se comparan dos pilas reales de comunicación en Windows: un recurso REST con HTTP/1.1 y JSON y una llamada gRPC unaria con HTTP/2 y Protobuf. El servicio devuelve un campo de texto sin lógica de negocio. Se cruzan concurrencias 1, 8, 32 y 64 y cargas útiles de 256 y 4096 bytes, con cinco repeticiones por condición y orden aleatorizado. El script captura rendimiento, latencias p50/p95/p99, errores, tiempo de CPU y RSS del servidor. Quarto calcula resultados y visualizaciones directamente desde el CSV. La comparación describe implementaciones completas en loopback sin TLS; no aísla el efecto causal de HTTP/2 ni predice comportamiento sobre una red externa. Se exponen sesgos de carga cerrada, resolución de contadores, ausencia de aislamiento y asistencia de IA.

## Los ocho archivos

| Archivo | Función |
|---|---|
| articulo.pdf | Artículo IEEE Conference compilado con Quarto |
| articulo.qmd | Texto, análisis y figura ejecutable |
| references.bib | Cinco publicaciones académicas con DOI |
| _quarto.yml | Configuración IEEEtran y motor Jupyter |
| benchmark.py | Cliente, servidores y captura experimental |
| results.csv | Una fila por ejecución real; 80 condiciones/repeticiones |
| README.md | Ficha técnica y reproducción |
| PROMPTS_OPENCODE.md | Consultas reales, correcciones y límites de integridad |

## Reproducción en Windows

Requisitos: Python 3.12, Quarto, TinyTeX con IEEEtran, acceso a instalación de paquetes. Se utilizaron Quarto 1.11.9 y OpenCode 2.2.7. Desde una copia del repositorio, en PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install aiohttp==3.14.5 grpcio==1.85.1 protobuf==7.36.2 psutil==7.2.2 numpy==2.5.4 pandas==3.1.1 matplotlib==3.11.2 scipy==1.18.1 jupyter
$env:QUARTO_PYTHON = (Resolve-Path .venv/Scripts/python.exe).Path
quarto install tinytex
quarto render articulo.qmd
```

Si TinyTeX ya está instalado, omitir su instalación. Quarto puede descargar IEEEtran en la primera compilación. El PDF se reconstruye a partir de los datos conservados y **no ejecuta nuevamente el benchmark**. Las dependencias transitivas pueden variar; las versiones directas y la plataforma del experimento están también en el CSV. No se promete reproducción bit a bit del rendimiento.

Para repetir primero una comprobación funcional pequeña, sin alterar el CSV entregado:

```powershell
python benchmark.py --seconds 0.3 --warmup 0.2 --repeats 1 --concurrency 1 8 --sizes 256 --output smoke.csv
```

Para repetir las 80 ejecuciones y guardar un conjunto independiente:

```powershell
python benchmark.py --seconds 3 --warmup 1 --repeats 5 --concurrency 1 8 32 64 --sizes 256 4096 --seed 20261113 --output results-nuevo.csv
```

Para recalcular el artículo con el nuevo conjunto, conservar una copia del CSV original, sustituir `results.csv` por el nuevo y renderizar. El análisis exige 80 filas y cinco repeticiones por condición; conserva y reporta los errores, sin suprimirlos. Los archivos adicionales de pruebas y del entorno virtual deben permanecer fuera del repositorio de entrega. La ejecución requiere varios minutos por arranques, calentamiento y medición; las interrupciones del entorno pueden prolongarla considerablemente. Ambos servidores escuchan únicamente en 127.0.0.1 y puertos efímeros.

## Interpretación de columnas

- `protocol`, `concurrency`, `payload_bytes`, `repeat`, `order`, `seed`: tratamiento y aleatorización. El tamaño es texto ASCII útil, no bytes en el cable.
- `requests`, `errors`, `error_types`, `elapsed_s`, `rps`: respuestas verificadas, fallos, recuento JSON por tipo de error, duración real con drenaje y solicitudes correctas por segundo.
- `mean_ms`, `p50_ms`, `p95_ms`, `p99_ms`: latencias de llamadas correctas, con interpolación lineal; incluyen validación.
- `server_cpu_s`, `server_cpu_pct`, `server_cpu_us_req`: CPU del servidor, porcentaje de un núcleo y microsegundos por solicitud.
- `server_rss_mean_mib`, `server_rss_max_mib`, `rss_samples`: RSS total muestreada aproximadamente cada 20 ms; no memoria incremental.
- `client_cpu_s`: CPU del generador durante la ventana, para contextualizar su coste.
- `timestamp_utc` y las columnas finales: instante de finalización, versiones y características del sistema. UTC difiere cinco horas de Ecuador continental.

No hay trazas individuales por llamada: se conservan agregados por ejecución para mantener exactamente la estructura pedida. Las p95 no deben combinarse como si fueran percentiles globales. La figura usa medianas y rangos observados, sin interpretarlos como intervalos de confianza.

## Resultados e incidencias reales

El CSV de entrega conserva la segunda batería completa: **80 ejecuciones, 786695 respuestas correctas y 35 errores**. En orden 31, gRPC/C=32/4096 bytes registró 20 cancelaciones y 1119.33 s; en orden 75, REST/C=32/4096 bytes registró 15 timeouts y 31.62 s. No se identificó la causa de las interrupciones. No se eliminaron esas filas ni se afirma que la serie sea estable. A C=64, el rendimiento medio gRPC/REST fue aproximadamente 0.49 con 256 bytes y 0.41 con 4096 bytes; describe esta ejecución local y no un ganador universal.

Una primera batería también presentó una anomalía. Su CSV completo se perdió por un fallo de respaldo seguido de sobrescritura; la bitácora y el artículo lo declaran. No se oculta esta limitación de trazabilidad. Las pruebas reales y los errores forman parte del resultado, sin garantía de una calificación determinada.

## Revisión humana antes de entrega

La revisión técnica asistida comprendió el funcionamiento del benchmark, la generación de clientes concurrentes, las unidades de medición y la coherencia de los resultados. Se contrastaron las condiciones de prueba de REST y gRPC y se identificaron factores que limitan la comparación, especialmente la serialización, la gestión de conexiones y la ejecución en un mismo equipo. Las verificaciones, incidencias y recomendaciones se detallan en `PROMPTS_OPENCODE.md`.

Como responsable del trabajo, considero que REST presentó un mejor rendimiento en las pruebas realizadas. Sin embargo, estos resultados corresponden a un entorno local y pueden verse influidos por los recursos del equipo, la concurrencia y las variaciones durante la ejecución. Por ello, no es correcto afirmar que REST sea superior a gRPC en todos los escenarios: la elección de una arquitectura debe considerar las condiciones de red, las características de la aplicación y sus requisitos de rendimiento.

La validación complementaria se conserva en la bitácora y no reemplaza las mediciones del artículo. El PDF mantiene la batería experimental original, con sus incidencias declaradas. La asistencia de Codex y OpenCode se reconoce expresamente; la interpretación y la responsabilidad académica corresponden a la investigadora.

## Repositorio público y entrega

Repositorio público: [Nayda-villacres/investigacion-sistemas-distribuidos-u2](https://github.com/Nayda-villacres/investigacion-sistemas-distribuidos-u2). Su raíz contiene los ocho archivos exigidos. Para la entrega en Moodle se debe pegar únicamente la URL del repositorio en el cuadro de texto de la tarea. La publicación en GitHub no realiza automáticamente esa entrega.

## Referencias e indexación

Se verificaron metadatos mediante páginas de editor, repositorios de autores y DOI/Crossref. Las publicaciones ACM son localizables en ACM Digital Library y DBLP; el artículo de Niswar et al. cuenta con registro Scopus 85198037286 en el portal institucional de Hasanuddin. No se atribuyen cuartiles ni indexaciones no comprobadas. Los enlaces resolubles están en `references.bib` mediante DOI.
