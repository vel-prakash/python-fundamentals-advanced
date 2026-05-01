# input() = prompts the user to enter data and returns it as a string

# -------- Basic Input --------

name = input("What is your name?: ")

print(f"Hello {name}!")

# -------- Input with Multiple Values --------

name = input("What is your name?: ")
age = input("How old are you?: ")

print(f"Hello {name}!")
print(f"You are {age} years old")

# -------- Type Casting Example --------

name = input("What is your name?: ")
age = int(input("How old are you?: "))

age += 1
 
print(f"Hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old")