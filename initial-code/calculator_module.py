# calculator_module.py

def calculate(first_number, second_number, operation):
    """
    Perform the given operation on two numbers.

    Parameters:
    - first_number: The first number (float or int).
    - second_number: The second number (float or int).
    - operation: The operation to perform (str), one of: 'add', 'subtract', 'multiply', 'divide'.

    Returns:
    - The result of the operation (float or int).
    """
    if operation == 'add':
        return first_number + second_number
    elif operation == 'subtract':
        return first_number - second_number
    elif operation == 'multiply':
        return first_number * second_number
    elif operation == 'divide':
        if second_number == 0:
            raise ValueError("Cannot divide by zero.")
        return first_number / second_number
    else:
        raise ValueError("Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'.")
