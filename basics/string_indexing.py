# -------- String Indexing and Slicing --------

# Indexing:
# Accesses individual characters using []

# Slicing:
# [start : end : step]
# - Starts at index 0
# - The end index is NOT included
# - Negative indexing starts from -1

credit_number = "1234-5678-9012-3456"

#  -------- Basic Indexing --------
print(credit_number[0])
print(credit_number[-1])

# -------- String Slicing --------
print(credit_number[:4])
print(credit_number[5:9])
print(credit_number[5:19])

# -------- Step Slicing --------
print(credit_number[::2])

# -------- Extract Last Four Digits --------
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

# -------- Reverse String --------
reversed_credit_number = credit_number[::-1]
print(reversed_credit_number)