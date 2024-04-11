def calculate_CAPM(risk_free_rate, beta, market_return):
    """
    Calculates the expected return of an investment using the Capital Asset Pricing Model (CAPM).

    Parameters:
    - risk_free_rate (float): The risk-free rate of return.
    - beta (float): The beta of the investment.
    - market_return (float): The expected return of the market.

    Returns:
    - float: The expected return of the investment.
    """
    expected_return = risk_free_rate + beta * (market_return - risk_free_rate)
    return expected_return

# Example usage
risk_free_rate = 0.02  # 2% risk-free rate
beta = 1.5  # Investment's beta
market_return = 0.10  # 10% expected market return

expected_return = calculate_CAPM(risk_free_rate, beta, market_return)
print(f"The expected return of the investment is: {expected_return*100:.2f}%")
