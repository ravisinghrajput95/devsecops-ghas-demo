"""
Utility functions for the demo app.
Includes simple input validation and arithmetic operations.
"""

def validate_input(data: dict) -> bool:
    """Ensure input has numeric 'a' and 'b' keys."""
    if not isinstance(data, dict):
        return False
    if "a" not in data or "b" not in data:
        return False
    return isinstance(data["a"], (int, float)) and isinstance(data["b"], (int, float))

def calculate_sum(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b
