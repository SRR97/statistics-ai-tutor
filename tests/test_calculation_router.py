from unittest.mock import patch, Mock

from app.calculation_router import (
    detect_calculation_type,
    extract_linear_prediction_parameters,
    execute_linear_prediction,
    generate_calculation_explanation,
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


def test_extract_invalid_json():
    with patch("app.calculation_router.client.responses.create") as mock_create:
        mock_create.return_value = Mock(
            output_text="Los parámetros son beta_0=2.5, beta_1=0.8 y x=20"
        )

        result = extract_linear_prediction_parameters(
            "Calcula una predicción lineal"
        )

        assert result is None
        mock_create.assert_called_once()


def test_extract_missing_parameters():
    with patch("app.calculation_router.client.responses.create") as mock_create:
        mock_create.return_value = Mock(
            output_text='{"beta_0": 2.5, "beta_1": 0.8}'
        )

        result = extract_linear_prediction_parameters(
            "Calcula una predicción lineal"
        )

        assert result is None
        mock_create.assert_called_once()


def test_extract_invalid_parameter_types():
    with patch("app.calculation_router.client.responses.create") as mock_create:
        mock_create.return_value = Mock(
            output_text='{"beta_0": 2.5, "beta_1": "incorrecto", "x": 20}'
        )

        result = extract_linear_prediction_parameters(
            "Calcula una predicción lineal"
        )

        assert result is None
        mock_create.assert_called_once()


def test_execute_linear_prediction():
    parameters = {
        "beta_0": 2.5,
        "beta_1": 0.8,
        "x": 20
    }

    with patch(
        "app.calculation_router.extract_linear_prediction_parameters",
        return_value=parameters
    ) as mock_extract:

        result = execute_linear_prediction(
            "Calcula la predicción lineal"
        )

        assert result == {
            "calculation_type": "linear_prediction",
            "parameters": parameters,
            "result": 18.5
        }

        mock_extract.assert_called_once()


def test_execute_linear_prediction_without_parameters():
    with patch(
        "app.calculation_router.extract_linear_prediction_parameters",
        return_value=None
    ) as mock_extract:

        result = execute_linear_prediction(
            "Calcula una predicción lineal"
        )

        assert result is None
        mock_extract.assert_called_once()


def test_generate_calculation_explanation():
    calculation = {
        "calculation_type": "linear_prediction",
        "parameters": {
            "beta_0": 2.5,
            "beta_1": 0.8,
            "x": 20
        },
        "result": 18.5
    }

    with patch("app.calculation_router.client.responses.create") as mock_create:
        mock_create.return_value = Mock(
            output_text="La predicción es 18.5."
        )

        result = generate_calculation_explanation(
            "Explica la predicción lineal",
            calculation
        )

        assert result == "La predicción es 18.5."
        mock_create.assert_called_once()

        arguments = mock_create.call_args.kwargs
        assert "18.5" in arguments["input"]