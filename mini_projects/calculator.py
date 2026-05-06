# -------- Python Calculator --------

# -------- Input --------
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# -------- Calculation --------
if operator == "+":
    result = num1 + num2
    print(f"Result: {result}")
elif operator == "-":
    result = num1 - num2
    print(f"Result: {result}")
elif operator == "*":
    result = num1 * num2
    print(f"Result: {result}")
elif operator == "/":
    result = num1 / num2
    print(f"Result: {result}")

# -------- Invalid Operator --------
else:
    print(f"{operator} is not a valid operator.")