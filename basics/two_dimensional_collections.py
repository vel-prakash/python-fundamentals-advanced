# -------- Two-Dimensional Collections --------
# A 2D collection stores multiple collections inside another collection.
# Commonly used for grids, tables, and matrix-style data.

# ==================================================
# ---------------- Grocery Example -----------------
# ==================================================

fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

# -------- Nested List --------
groceries = [fruits, vegetables, meats]

# -------- Display Entire Collection --------
print(groceries)

# -------- Accessing Collections --------
print(groceries[2])

print(groceries[2][0])

# ==================================================
# -------- Two-Dimensional List Example ------------
# ==================================================

grocery_items = [["apple", "orange", "banana", "coconut"],
           ["celery", "carrots", "potatoes"],
           ["chicken", "fish", "turkey"]]

# -------- Display 2D List --------
print(grocery_items)

# -------- Loop Through 2D List --------
for collection in grocery_items:

    for item in collection:
        print(item, end=" ")

    print()

# ==================================================
# --------------- Number Pad Example ----------------
# ==================================================

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

# -------- Display Number Pad --------

for rows in num_pad:

    for num in rows:
        print(num, end=" ")

    print()