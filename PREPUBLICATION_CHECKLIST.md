# Pre-publication checklist

## Validado

- [x] Python 3.13.1 confirmado.
- [x] Instalación limpia con `pip install -r requirements.txt` exitosa.
- [x] Imports principales (`fastapi`, `openai`, `pypdf`, `dotenv`, `numpy`) correctos.
- [x] API inicia con Uvicorn.
- [x] `GET /health` responde correctamente.
- [x] `/chat` carga correctamente.
- [x] Ruta local de predicción lineal probada con resultado 14 para `beta_0=2`, `beta_1=3`, `x=4`.
- [x] Flujo RAG probado de extremo a extremo con respuesta y fuentes correctas.
- [x] `.env`, entornos virtuales y cachés excluidos de la versión pública.
- [x] `.env.example` incluido.
- [x] `requirements.txt` normalizado a UTF-8 e incluye NumPy.
- [x] Material académico autorizado para publicación.
- [x] Búsqueda de patrones típicos de secretos de OpenAI en el historial Git disponible sin coincidencias.

## Pendiente antes de hacer público

- [x] MIT License añadida al código fuente.
- [ ] Crear commit final de preparación para publicación.
- [ ] Revisar el repositorio en GitHub antes de cambiar su visibilidad a público.
- [ ] Añadir URL final del repositorio al CV y LinkedIn.
