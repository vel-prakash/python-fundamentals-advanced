# -------- Compound Interest Calculator --------

# -------- Variable Initialization --------
principal = 0
rate = 0
time = 0

# -------- Principal Amount Input --------
while True:
    principal = float(input("Enter the principal amount: "))

    if principal <= 0:
        print("Principal cannot be less than or equal to zero.")
    else:
        break

# -------- Interest Rate Input --------
while True:
    rate = float(input("Enter the interest rate: "))

    if rate <= 0:
        print("Interest rate cannot be less than or equal to zero.")
    else:
        break

# -------- Time Input --------
while True:
    time = int(input("Enter the time in years: "))

    if time <= 0:
        print("Time cannot be less than or equal to zero.")
    else:
        break
# -------- Compound Interest Calculation --------
total = principal * pow((1 + rate / 100), time)

# -------- Output --------
print(f"Balance after {time} year(s): ${total:.2f}")