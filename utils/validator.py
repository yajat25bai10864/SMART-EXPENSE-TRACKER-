def validate_amount(amount: float) -> bool:
    """Return True if amount is a positive number, False otherwise."""
    return isinstance(amount, (int, float)) and amount > 0