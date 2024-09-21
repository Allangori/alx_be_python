num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
function = input ("Choose the operation (+, -, *, /): ")

match function:
    case "+" :
        sum = num1 + num2
        print("The sum of the two numbers is: ",sum)
    case "-" :
        difference = num1 - num2
        print("The difference of the two numbers is: ",difference)
    case "*" :
        product = num1 * num2
        print("The product of the two numbers is: ",product)
    case "/" :
        division = num1 / num2
        
        if num1 and num2 != "0" :
            division = num1 / num2
            print ("The division of the two numbers is: ",division)
        elif num1 or num2 == "0":
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation")
