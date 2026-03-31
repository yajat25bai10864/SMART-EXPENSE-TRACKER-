import numpy as np

from typing import Optional

def predict_spending(data: list) -> Optional[float]:
    """Predict the next expense amount using linear regression on past amounts.

    Args:
        data: List of expense dicts, each containing at least an 'amount' key.

    Returns:
        The predicted amount as a float, or None if there is insufficient data.
    """
    if len(data) < 2:
        print("Not enough data to make a prediction (need at least 2 expenses).")
        return None

    amounts = [exp["amount"] for exp in data]
    days = list(range(len(amounts)))

    # Fit a degree-1 polynomial (straight line) to the amounts over time.
    coeffs = np.polyfit(days, amounts, 1)
    model = np.poly1d(coeffs)

    prediction = round(float(model(len(amounts))), 2)
    print(f"Predicted next expense: Rs. {prediction}")
    return prediction