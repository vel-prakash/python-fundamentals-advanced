# Mini Project: Shopping Cart Program

# -------- Input --------
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

# -------- Calculation --------
total = price * quantity

# -------- Output --------
print(f"You have bought {quantity} x {item}")
print(f"Your total is: ${total}")