# -------- Format Specifiers --------

# Format Specifiers:
# {value:flags}
# Formats values using different formatting options

price1 = 12.34
price2 = -987.658
price3 = 3.14159
price4 = 1.231
price5 = 1200.561
price6 = -1902.323

# -------- Decimal Precision --------
print(f"Price 1 is {price1:.1f}")
print(f"Price 2 is {price2:.2f}")
print(f"Price 3 is {price3:.3f}")

# -------- Right Alignment --------
print(f"Price 1 is ${price1:>10}")

# -------- Zero Padding --------
print(f"Price 2 is ${price2:010}")

# -------- Left Alignment --------
print(f"Price 3 is ${price3:<10}")

# -------- Center Alignment --------
print(f"Price 4 is {price4:^10}")
print(f"Price 5 is {price5:^10}")

# -------- Display Positive Sign --------
print(f"Price 4 is {price4:+}")
print(f"Price 1 is {price1:+}")
print(f"Price 2 is {price2:+}")

# -------- Space Before Positive Numbers --------
print(f"Price 3 is {price3: }")
print(f"Price 4 is {price4: }")
print(f"Price 2 is {price2: }")

# -------- Comma Separator --------
print(f"Price 5 is {price5:,}")

# -------- Combined Format Specifiers --------
print(f"Price 6 is {price6:+,.2f}")
print(f"Price 5 is {price5:+,.2f}")