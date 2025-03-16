# math_operations.py

def add(a, b):
    """
    Function to add two numbers, with a check for negative numbers.
    Returns the sum if both numbers are non-negative, otherwise returns a warning message.
    """
    if a < 0 or b < 0:
        return "Warning: Negative numbers are not allowed."
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def exponentiate(a, b):
    return a ** b

def modulo(a, b):
    return a % b
