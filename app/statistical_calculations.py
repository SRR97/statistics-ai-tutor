def calculate_linear_prediction(beta_0: float, beta_1: float, x: float) -> float:
    if not all(isinstance(value, (int, float)) for value in (beta_0, beta_1, x)):
        raise TypeError("beta_0, beta_1 y x deben ser valores numéricos.")
    
    y_hat = beta_0 + beta_1 * x
    return y_hat