from unittest.mock import patch, Mock

from app.calculation_router import (
    detect_calculation_type,
    extract_linear_prediction_parameters,
)


def test_detect_linear_prediction():
    with patch("app.calculation_router.client.responses.create") as mock_create:
        mock_create.return_value = Mock(
            output_text="linear_prediction"
        )

        result = detect_calculation_type(
            "Calcula la predicción de una regresión lineal"
        )

        assert result == "linear_prediction"
        mock_create.assert_called_once()


def test_detect_no_calculation():
    with patch("app.calculation_router.client.responses.create") as mock_create:
        mock_create.return_value = Mock(
            output_text="none"
        )

        result = detect_calculation_type(
            "¿Qué significa el coeficiente de determinación R cuadrado?"
        )

        assert result == "none"
        mock_create.assert_called_once()


def test_detect_invalid_classification():
    with patch("app.calculation_router.client.responses.create") as mock_create:
        mock_create.return_value = Mock(
            output_text="unknown_calculation"
        )

        result = detect_calculation_type(
            "Realiza un cálculo estadístico"
        )

        assert result == "none"
        mock_create.assert_called_once()


def test_extract_linear_prediction_parameters():
    with patch("app.calculation_router.client.responses.create") as mock_create:
        mock_create.return_value = Mock(
            output_text='{"beta_0": 2.5, "beta_1": 0.8, "x": 20}'
        )

        result = extract_linear_prediction_parameters(
            "Calcula la predicción con beta_0=2.5, beta_1=0.8 y x=20"
        )

        assert result == {
            "beta_0": 2.5,
            "beta_1": 0.8,
            "x": 20
        }

        mock_create.assert_called_once()