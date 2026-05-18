# -------- Shopping Cart Program --------

foods = []
prices = []
total = 0

# -------- Add Items to Cart --------
while True:

    food = input("Enter a food item to buy (q to quit): ")

    if food.lower() == "q":
        break

    else:
        price = float(input(f"Enter the price of {food}: $"))

        foods.append(food)
        prices.append(price)

# -------- Display Shopping Cart --------
print("------ YOUR CART ------")

for food in foods:
    print(food, end=" ")

# -------- Calculate Total --------
for price in prices:
    total += price

# -------- Display Total --------
print()
print(f"Your total is: ${total:.2f}")