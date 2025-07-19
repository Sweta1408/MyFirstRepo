
def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operator = input("Enter an operator (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))
            
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            else:
                print("Invalid operator!")
                continue
            
            print(f"The result is: {result}")
        except ValueError:
            print("Invalid input! Please enter numerical values.")
        except ZeroDivisionError:
            print("Error! Division by zero.")
        
        choice = input("Do you want to perform another calculation? (y/n): ").lower()
        if choice != 'y':
            break
 
calculator()
 
