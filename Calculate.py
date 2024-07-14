#1. Calculate Addition,Subtraction,Multiplication and Division from 2 numbers provided by user input.
def calculate_operations(num1, num2):
    
    addition = num1 + num2

    subtraction = num1 - num2
    
    multiplication = num1 * num2
    
    if num2 != 0:
        division = num1 / num2
    else:
        division = "Undefined (division by zero)"
    
    
    return addition, subtraction, multiplication, division


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


results = calculate_operations(num1, num2)

addition, subtraction, multiplication, division = results


print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
