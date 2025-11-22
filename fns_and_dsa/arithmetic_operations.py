def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation on num1 and num2.

    operation must be one of: 'add', 'subtract', 'multiply', 'divide'
    Division by zero is handled and returns a clear error message.
    """
    op = operation.strip().lower()

    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Invalid operation"