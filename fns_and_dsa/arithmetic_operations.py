def perform_operation ( num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2
    elif num1 == 0 or num2 == 0 and operation == 'divide':
        print("Can't divide a number by zero")
    else :
        print('Choose a function to be performed.')
        
    

