# -------- Conditional Expressions --------
# A one-line shortcut for the if-else statement (ternary operator)
# Prints or assigns one of two values based on a condition
# Syntax: X if condition else Y

# -------- Positive or Negative --------
num = 5
print("Positive" if num > 0 else "Negative")

# -------- Even or Odd --------
num = 6
result = "Even" if num % 2 == 0 else "Odd"
print(result)

# -------- Maximum Number --------
a = 6
b = 7

max_num = a if a > b else b
print(max_num)

# -------- Minimum Number --------
min_num = a if a < b else b
print(min_num)

# -------- Age Status --------
age = 20
status = "Adult" if age >= 18 else "Child"
print(status)

# -------- Weather Condition --------
temperature = 35
weather = "Hot" if temperature >= 30 else "Cold"
print(weather)

# -------- User Role --------
user_role = "admin"
access_level = "Full Access" if user_role == "admin" else "Denied Access"