from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-5.4-mini",
    input="Explica en una frase qué es una regresión lineal."
)

print(response.output_text)

print("Statistics AI Tutor")