number1 = int(input("Enter the first number = "))
operator = input("Enter the operator(+,-,*,/) = ")
number2 = int(input("Enter the second number = "))

if operator == "+":
    print("addition: ",number1 + number2)
elif operator == "-":
    print("subtraction: ",number1 - number2)
elif operator == "*":
    print("multiplication: ",number1 * number2)
elif operator == "/":
    print("division: ",number1 / number2)
else:
    print("Not a valid operator")