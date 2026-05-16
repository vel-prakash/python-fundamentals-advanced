# -------- While Loops --------
# Executes code WHILE a condition remains True

# -------- Basic If Statement --------
name = input("Enter your name: ")

if name == "":
    print("You did not enter your name.")
else:
    print(f"Hello {name}!")

# -------- Name Validation --------
name = input("Enter your name: ")

while name == "":
    print("You did not enter your name.")
    name = input("Enter your name: ")

print(f"Hello {name}!")

# -------- Age Validation --------
age = int(input("Enter your age: "))

while age < 0:
    print("Age cannot be negative.")
    age = int(input("Enter your age: "))

print(f"You are {age} years old.")

# -------- Food Input Loop --------
food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}.")
    food = input("Enter another food you like (q to quit): ")

print("Goodbye!")

# -------- Number Validation --------
num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not a valid number.")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Your selected number is {num}.")