# -------- Python Weight Converter --------

# -------- Input --------
weight = float(input("Enter your weight: "))
unit = input("Is this weight in Kilograms or Pounds? (K/L): ")

# -------- Conversion --------
if unit == "K":
    weight = weight * 2.205
    unit = "lbs."
    print(f"Converted weight: {round(weight, 2)} {unit}")

elif unit == "L":
    weight = weight / 2.205
    unit = "kgs."
    print(f"Converted weight: {round(weight, 2)} {unit}")

# -------- Invalid Unit --------
else:
    print(f"{unit} is not a valid unit.")