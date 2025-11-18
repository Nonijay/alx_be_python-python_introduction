num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        print(f"the result is: {num1 + num2}")
    case "-":
        print (f"the result is: {num1 - num2}")
    case "*":
        print (f"the result is: {num1 * num2}")
    case "/":
        if num2 != 0:
            print (f"the result is: {num1 / num2}")
        else : 
            # Error Handling for division of 0
            print ("Error: cannot divide by zero")
    case _:
        print ("Error: Enter a valid operation choice. please use +, -, *, /.")
    
    