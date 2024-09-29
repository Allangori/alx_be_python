["num1, num2, operation"]
def perform_operation(num1, num2, operation):
        if operation == 'add':
            return num1 + num2
        elif operation == 'subtract':
            return num1 - num2
        elif operation == 'multiply':
            return num1 * num2
        elif operation == 'divide':
            if num2 == 0:
              return "Error: Division by zero"  # Handling division by zero
            return num1 / num2
        else:
            return "Error: Invalid operation"  # Handling invalid operations
        