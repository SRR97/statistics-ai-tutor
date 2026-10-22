from unittest.mock import patch

from fastapi.testclient import TestClient


def test_ask_returns_linear_prediction_explanation():
    with patch("app.rag.initialize_rag", return_value=([], [])):
        from app.api import app

    client = TestClient(app)

    calculation = {
        "calculation_type": "linear_prediction",
        "parameters": {
            "beta_0": 2.5,
            "beta_1": 0.8,
            "x": 20
        },
        "result": 18.5
    }

    with (
        patch(
            "app.api.detect_calculation_type",
            return_value="linear_prediction"
        ),
        patch(
            "app.api.execute_linear_prediction",
            return_value=calculation
        ),
        patch(
            "app.api.generate_calculation_explanation",
            return_value="La predicción calculada es 18.5."
        )
    ):
        response = client.post(
            "/ask",
            json={"question": "Calcula una predicción lineal"}
        )

    assert response.status_code == 200
    assert response.json() == {
        "answer": "La predicción calculada es 18.5.",
        "sources": []
    }

def test_ask_linear_prediction_without_parameters():
    with patch("app.rag.initialize_rag", return_value=([], [])):
        from app.api import app

    client = TestClient(app)

    with (
        patch(
            "app.api.detect_calculation_type",
            return_value="linear_prediction"
        ),
        patch(
            "app.api.execute_linear_prediction",
            return_value=None
        ),
        patch(
            "app.api.generate_calculation_explanation"
        ) as mock_explanation
    ):
        response = client.post(
            "/ask",
            json={"question": "Calcula una predicción lineal"}
        )

    assert response.status_code == 200
    assert "beta_0" in response.json()["answer"]
    assert "beta_1" in response.json()["answer"]
    assert "x" in response.json()["answer"]
    assert response.json()["sources"] == []

    mock_explanation.assert_not_called()

def test_ask_uses_rag_for_conceptual_questions():
    with patch("app.rag.initialize_rag", return_value=([], [])):
        from app.api import app

    client = TestClient(app)

    expected_answer = {
        "answer": "La desviación estándar mide la dispersión de los datos.",
        "sources": []
    }

    with (
        patch(
            "app.api.detect_calculation_type",
            return_value=None
        ),
        patch(
            "app.api.generate_rag_answer",
            return_value=expected_answer
        ) as mock_rag,
        patch(
            "app.api.execute_linear_prediction"
        ) as mock_calculation
    ):
        response = client.post(
            "/ask",
            json={"question": "¿Qué es la desviación estándar?"}
        )

    assert response.status_code == 200
    assert response.json() == expected_answer

    mock_rag.assert_called_once()
    mock_calculation.assert_not_called()