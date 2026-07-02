def add_numbers(a, b):
    # Intentional Bug 1: Returns a - b instead of a + b
    return a - b

def divide_numbers(a, b):
    # Intentional Bug 2: Fails to handle ZeroDivisionError
    return a / b
