# Statistics AI Tutor

Statistics AI Tutor es un asistente académico conversacional basado en Inteligencia Artificial Generativa, diseñado para apoyar la consulta y comprensión de los contenidos de un curso de Estadística.

El sistema utilizará una arquitectura de **Retrieval-Augmented Generation (RAG)** para recuperar información relevante de las notas de clase antes de generar una respuesta, buscando que las explicaciones estén sustentadas en el material académico proporcionado.

## Objetivo

Desarrollar un asistente académico que permita a los estudiantes realizar consultas en lenguaje natural sobre los contenidos del curso y obtener respuestas comprensibles, contextualizadas y acompañadas de referencias al material utilizado.

## Funcionalidades previstas

- Consulta de conceptos estadísticos.
- Explicación de fórmulas y supuestos.
- Recuperación semántica de información desde las notas de clase.
- Generación de respuestas mediante RAG.
- Referencias al material académico utilizado.
- Identificación de preguntas que no pueden responderse con el material disponible.
- Resolución de cálculos estadísticos soportados por el sistema.
- Interfaz web conversacional.
- Evaluación reproducible del desempeño del asistente.

## Arquitectura prevista

El sistema seguirá, de manera general, el siguiente flujo:

`Usuario → Interfaz web → API → Sistema RAG → Recuperación de información → LLM → Respuesta con fuentes`

## Tecnologías

El proyecto contempla inicialmente el uso de:

- Python
- Git
- GitHub
- FastAPI
- Modelos de lenguaje de gran escala (LLM)
- Embeddings
- Base de datos vectorial
- Retrieval-Augmented Generation (RAG)

Las tecnologías específicas podrán ajustarse durante el desarrollo y la evaluación del proyecto.

## Estructura actual

```text
statistics-ai-tutor/
├── app/                    # Código fuente de la aplicación
├── docs/                   # Documentación del proyecto
├── .gitignore              # Archivos excluidos del control de versiones
├── README.md               # Presentación general del proyecto
└── requirements.txt        # Dependencias de Python