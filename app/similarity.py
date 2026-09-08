import numpy as np
from embeddings import create_embedding

def cosine_similarity(vector_a, vector_b):
    dot_product = np.dot(vector_a, vector_b)
    norm_a = np.linalg.norm(vector_a)
    norm_b = np.linalg.norm(vector_b)
    similarity = dot_product / (norm_a * norm_b)
    return similarity

text_1 = "¿Qué es una regresión lineal?"
text_2 = "Los planetas orbitan alrededor del Sol."

embedding_1 = create_embedding(text_1)
embedding_2 = create_embedding(text_2)

result = cosine_similarity(embedding_1, embedding_2)
print(result)