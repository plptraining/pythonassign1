# Create a simple Python program that asks the user to input two numbers and a mathematical operation 
# (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

print("Welcome to our Basic Calculator Program, Yippe!!!")
number1 = float(input("Enter first numbers: "))
number2 = float(input("Enter second numbers: "))
operation =  input("Enter mathemaical operator of your choice: (+, -, / or x): ")

if operation == "+":
    answer = number1 + number2
    print(f"The answer is {number1} + {number2} = {answer}")
elif operation == "-":
    answer = number1 - number2
    print(f"The answer is {number1} - {number2} = {answer}")
elif operation == "x":
    answer = number1 * number2
    print(f"The answer is {number1} x {number2} = {answer}")
elif operation == "/":
    if number2 != 0:
        answer = number1 / number2
        print(f"The answer is {number1} / {number2} = {answer}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")


