# -------- Python Temperature Converter --------

# -------- Input --------
temp = float(input("Enter the temperature: "))
unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")

# -------- Conversion --------
if unit == "C":
    temp = round((9 / 5 * temp) + 32, 2)
    print(f"The temperature in Fahrenheit is: {temp}°F")

elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 2)
    print(f"The temperature in Celsius is: {temp}°C")

# -------- Invalid Unit --------
else:
    print(f"{unit} is an invalid unit of measurement.")