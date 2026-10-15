import pytest

from app.statistical_calculations import calculate_linear_prediction


def test_linear_prediction_with_positive_values():
    result = calculate_linear_prediction(
        beta_0=2.5,
        beta_1=0.8,
        x=20
    )

    assert result == 18.5


def test_linear_prediction_with_negative_slope():
    result = calculate_linear_prediction(
        beta_0=10,
        beta_1=-2,
        x=3
    )

    assert result == 4


def test_linear_prediction_with_invalid_input():
    with pytest.raises(TypeError):
        calculate_linear_prediction(
            beta_0="abc",
            beta_1=0.8,
            x=20
        )


def test_linear_prediction_with_decimal_values():
    result = calculate_linear_prediction(
        beta_0=1.25,
        beta_1=0.5,
        x=3.5
    )

    assert result == pytest.approx(3.0)