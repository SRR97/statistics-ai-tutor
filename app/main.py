from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

print("Statistics AI Tutor")

while True:

    question = input("Tu pregunta: ")

    if question.lower() == "salir":
        break

    response = client.responses.create(
        model="gpt-5.4-mini",
        input=question
    )

    print(response.output_text)

