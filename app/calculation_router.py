from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

LINEAR_PREDICTION = "linear_prediction"
NO_CALCULATION = "none"

def detect_calculation_type(query: str):
    response = client.responses.create(
        model="gpt-5.4-mini",
        instructions=(
            "Clasifica la pregunta del estudiante. "
            "Responde únicamente con 'linear_prediction' si la pregunta solicita "
            "calcular una predicción usando un modelo de regresión lineal simple. "
            "En cualquier otro caso, responde únicamente con 'none'."
        ),
        input=query
    )

    calculation_type = response.output_text.strip()

    if calculation_type not in (LINEAR_PREDICTION, NO_CALCULATION):
        return NO_CALCULATION

    return calculation_type