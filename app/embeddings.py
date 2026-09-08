from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

def create_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )

    return response.data[0].embedding

def create_embeddings(texts):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )

    embeddings = []

    for item in response.data:
        embeddings.append(item.embedding)

    return embeddings

if __name__ == "__main__":

    test_text = "La regresión lineal modela la relación entre variables."
    test_embedding = create_embedding(test_text)
    print(len(test_embedding))
    print(test_embedding[:5])

    test_texts = [
        "¿Qué es una regresión lineal?",
        "¿Cómo se interpreta el coeficiente beta 1?"
    ]

    test_embeddings = create_embeddings(test_texts)
    print(len(test_embeddings))
    print(len(test_embeddings[0]))