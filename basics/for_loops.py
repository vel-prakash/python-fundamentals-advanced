# -------- For Loops --------
# Executes a block of code a fixed number of times
# Can iterate over ranges, strings, sequences, and more

# -------- Basic Range Loop --------
for x in range(1, 11):
    print(x)

# -------- Range Loop with Step --------
for x in range(1, 11, 2):
    print(x)

# -------- Reverse Loop --------
for x in reversed(range(1, 11)):
    print(x)
print("HAPPY NEW YEAR!")

# -------- Range Loop with Different Step --------
for x in range(1, 11, 3):
    print(x)

# -------- String Iteration --------
credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)

# -------- Continue Statement --------
# Skips the specified iteration
for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

# -------- Break Statement --------
# Stops the loop completely
for x in range(1, 21):
    if x == 13:
        break # stops
    else:
        print(x)