from fastapi import FastAPI
from app.rag import initialize_rag, generate_rag_answer
from app.calculation_router import detect_calculation_type, execute_linear_prediction
from pydantic import BaseModel
from app.web import get_chat_page

app = FastAPI()

chunks, chunk_embeddings = initialize_rag()

class QuestionRequest(BaseModel):
    question: str

@app.get("/")
def root():
    return {"message": "Statistics AI Tutor API"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/chat")
def chat():
    return get_chat_page()

@app.post("/ask")
def ask(request: QuestionRequest):

    calculation_type = detect_calculation_type(request.question)

    if calculation_type == "linear_prediction":
        calculation = execute_linear_prediction(request.question)

        if calculation is None:
            return {
                "answer": "Necesito los valores de beta_0, beta_1 y x para realizar la predicción.",
                "sources": []
            }

        return {
            "answer": f"El valor predicho es {calculation['result']}.",
            "sources": []
        }

    answer = generate_rag_answer(
        request.question,
        chunks,
        chunk_embeddings
    )

    return answer