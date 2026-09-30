# Statistics AI Tutor

Statistics AI Tutor es un asistente académico conversacional para un curso de Estadística. Combina recuperación semántica de notas de clase con generación de respuestas mediante un modelo de lenguaje, y además incluye un enrutador para cálculos estadísticos soportados localmente.

> **Estado:** desarrollo activo. La versión actual ya incluye carga de documentos PDF, chunking, embeddings, similitud coseno, recuperación semántica, RAG con fuentes, API FastAPI, interfaz web y una ruta de cálculo para predicción lineal.

## Objetivo

Permitir que un estudiante formule preguntas en lenguaje natural sobre el material del curso y reciba respuestas contextualizadas, sustentadas en los documentos disponibles y acompañadas de referencias a las fuentes recuperadas.

## Funcionalidades implementadas

- Carga de múltiples PDF desde `data/`.
- División del contenido en chunks con solapamiento.
- Generación de embeddings con `text-embedding-3-small`.
- Caché local de embeddings para evitar recalcularlos cuando el corpus no cambia.
- Similitud coseno y recuperación de los chunks más relevantes.
- Pipeline RAG para generar respuestas a partir del contexto recuperado.
- Referencias al documento y página utilizados.
- Detección de consultas que pueden resolverse mediante cálculo local.
- Predicción lineal con parámetros `beta_0`, `beta_1` y `x`.
- API con FastAPI.
- Interfaz web conversacional.
- Casos de prueba para evaluar recuperación semántica.

## Arquitectura

```text
Usuario
  ↓
Interfaz web
  ↓
FastAPI
  ↓
Router de consulta
  ├── Cálculo estadístico local
  └── Pipeline RAG
        ↓
     Retrieval
        ↓
   Contexto relevante
        ↓
       LLM
        ↓
Respuesta + fuentes
```

## Estructura del proyecto

```text
statistics-ai-tutor/
├── app/
│   ├── api.py
│   ├── calculation_router.py
│   ├── document_loader.py
│   ├── embeddings.py
│   ├── main.py
│   ├── rag.py
│   ├── retriever.py
│   ├── similarity.py
│   ├── statistical_calculations.py
│   ├── text_splitter.py
│   └── web.py
├── data/                    # Material académico autorizado
├── docs/
├── evaluation/
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Requisitos

- Python 3.13.x (probado con Python 3.13.1)
- Una API key de OpenAI

## Instalación local

```bash
git clone <URL-DEL-REPOSITORIO>
cd statistics-ai-tutor
python -m venv .venv
```

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

Luego agrega tu API key en `.env`:

```text
OPENAI_API_KEY=tu_api_key
```

## Ejecutar la API

```powershell
uvicorn app.api:app --host 127.0.0.1 --port 8000
```

Después abre:

- `http://127.0.0.1:8000/health` para comprobar el estado de la API.
- `http://127.0.0.1:8000/chat` para utilizar la interfaz conversacional.

### Primera ejecución

El repositorio no publica el archivo de caché de embeddings. En la primera ejecución, `initialize_rag()` procesa los PDF y genera los embeddings del corpus antes de guardar el caché local en `cache/chunk_embeddings.pkl`. Esto requiere una API key válida y genera consumo de la API de embeddings.

En ejecuciones posteriores, si los textos del corpus no han cambiado, los embeddings se cargan desde caché.

## Endpoints principales

- `GET /` — información básica de la API.
- `GET /health` — comprobación de estado.
- `GET /chat` — interfaz web.
- `POST /ask` — recibe una pregunta y devuelve una respuesta y sus fuentes.

Ejemplo de request:

```json
{
  "question": "¿Qué es la regresión lineal?"
}
```

## Tecnologías

- Python
- FastAPI / Uvicorn
- OpenAI API
- `text-embedding-3-small`
- NumPy
- PyPDF
- Retrieval-Augmented Generation (RAG)
- Git / GitHub

## Validación reproducible

Antes de preparar esta versión para publicación se comprobó en Windows con Python 3.13.1 que:

- `pip install -r requirements.txt` finaliza correctamente en un entorno virtual nuevo.
- Las dependencias principales importan sin errores.
- La API inicia correctamente con Uvicorn.
- `GET /health` responde `ok`.
- La interfaz `/chat` carga correctamente.
- La ruta local de predicción lineal devuelve el resultado esperado para un caso de prueba.
- El flujo RAG completo responde correctamente y muestra las fuentes recuperadas.

## Seguridad

- `.env` está excluido de Git.
- `.venv`, `.venv_test`, cachés de Python y el caché de embeddings están excluidos de Git.
- Se incluye `.env.example` sin credenciales reales.
- Antes de publicar se revisó el historial Git disponible buscando patrones típicos de secretos de OpenAI, sin encontrar coincidencias.

## Material académico

Los documentos incluidos en `data/` forman parte del material utilizado por el proyecto y su difusión/publicación está autorizada.

## Roadmap

- Ampliar el enrutador de cálculos estadísticos.
- Añadir más pruebas automáticas del pipeline RAG.
- Mejorar evaluación cuantitativa de retrieval y calidad de respuesta.
- Refinar experiencia de usuario de la interfaz web.
- Documentar despliegue en nube.

## Licencia

El código fuente de este proyecto se distribuye bajo la **MIT License**. Esto permite usar, copiar, modificar, publicar, distribuir, sublicenciar y vender copias del software, siempre que se conserve el aviso de copyright y la licencia.

Consulta el archivo [`LICENSE`](LICENSE) para ver el texto completo.

> **Nota sobre el material académico:** los documentos incluidos en `data/` se publican con autorización para su difusión. La licencia MIT se aplica al software del proyecto; cualquier reutilización del material académico debe respetar los términos aplicables a dicho contenido.
