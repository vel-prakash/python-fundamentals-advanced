# if statement: Executes code only if a condition is True
# else: Executes when the condition is False

# -------- If-Elif-Else Example --------
age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up.")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sign up.")

# -------- Yes/No Input Example --------
response = input("Would you like to have some food? (Y/N): ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")

# -------- Empty Input Check --------
name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}!")

# -------- Boolean Example --------
for_sale = True

if for_sale:
    print("This item is for sale.")
else:
    print("This item is NOT for sale.")

# -------- Online Status Example --------
online = False

if online:
    print("The user is online.")
else:
    print("The user is offline.")