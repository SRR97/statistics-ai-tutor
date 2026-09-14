from fastapi import FastAPI
from app.rag import initialize_rag, generate_rag_answer
from pydantic import BaseModel

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

@app.post("/ask")
def ask(request: QuestionRequest):

    answer = generate_rag_answer(
        request.question,
        chunks,
        chunk_embeddings
    )

    return {"answer": answer}