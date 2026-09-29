from openai import OpenAI
from dotenv import load_dotenv
import json

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

def extract_linear_prediction_parameters(query: str):
    response = client.responses.create(
        model="gpt-5.4-mini",
        instructions=(
            "Extrae los parámetros necesarios para una predicción de regresión lineal simple. "
            "Responde únicamente con un objeto JSON con las claves beta_0, beta_1 y x. "
            "No realices el cálculo de la predicción."
        ),
        input=query
    )

    parameters_text = response.output_text.strip()
    try:
        parameters = json.loads(parameters_text)
    except json.JSONDecodeError:
        return None

    required_parameters = {"beta_0", "beta_1", "x"}

    if not required_parameters.issubset(parameters):
        return None

    if not all(isinstance(parameters[key], (int, float)) for key in required_parameters):
        return None

    return parameters
    