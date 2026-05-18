# -------- Nested Loops --------
# A nested loop is a loop inside another loop.
# The outer loop controls the rows.
# The inner loop controls the columns.

# -------- Basic Nested Loop Example --------
for x in range(3):

    for y in range(1, 10):
        print(y, end="")

    print()

# -------- Pattern Generator --------
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use: ")

# -------- Generate Pattern --------
for x in range(rows):

    for y in range(columns):
        print(symbol, end="")

    print()