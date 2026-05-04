# -------- Import --------
import math

# -------- Input --------
a = float(input("Enter length of side A (cm): "))
b = float(input("Enter length of side B (cm): "))

# -------- Calculation --------
c = math.sqrt(a**2 + b**2)

# -------- Output --------
print(f"Side C is: {round(c, 2)} cm")