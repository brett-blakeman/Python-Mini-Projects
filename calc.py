op1 = int(input("Enter the first number: "))
exp = input("Enter the operator (+, -, *, /): ")
op2 = int(input("Enter the second number: "))

if exp == "+":
    result = op1 + op2
    print(f"The sum of {op1} and {op2} is {result}")
elif exp == "-":
    result = op1 - op2
    print(f"The difference of {op1} and {op2} is {result}")
elif exp == "*":
    result = op1 * op2
    print(f"The product of {op1} and {op2} is {result}")
elif exp == "/":
    if op2 != 0:
        result = op1 / op2
        print(f"The quotient of {op1} and {op2} is {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please use +, -, *, or /.")