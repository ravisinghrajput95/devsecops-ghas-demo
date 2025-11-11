def validate_input(data):
    if not isinstance(data, dict):
        return False
    if "a" not in data or "b" not in data:
        return False
    return isinstance(data["a"], (int, float)) and isinstance(data["b"], (int, float))

def calculate_sum(a, b):
    return a + b
