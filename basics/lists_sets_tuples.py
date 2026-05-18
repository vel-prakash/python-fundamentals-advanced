# -------- Lists, Sets, and Tuples --------
# List  -> Ordered and changeable collection
# Set   -> Unordered collection with unique values
# Tuple -> Ordered and unchangeable collection


# ==================================================
# -------------------- Lists ------------------------
# ==================================================

fruits = ["apple", "banana", "orange", "coconut"]


# -------- Accessing Elements --------
print(fruits[0:4])
print(fruits[::-1])


# -------- Useful Functions --------
print(len(fruits))
print("apple" in fruits)


# -------- Modifying a List --------
fruits[0] = "pineapple"
print(fruits)


# -------- Adding Elements --------
fruits.append("apple")
fruits.insert(1, "guava")
print(fruits)


# -------- Removing Elements --------
fruits.remove("pineapple")
print(fruits)


# -------- Sorting and Reversing --------
fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)


# -------- Searching and Counting --------
print(fruits.index("coconut"))
print(fruits.count("banana"))


# -------- Looping Through a List --------
for fruit in fruits:
    print(fruit)


# -------- Clearing a List --------
fruits.clear()
print(fruits)

# ==================================================
# --------------------- Sets ------------------------
# ==================================================

vegetables = {"carrot", "potato", "beetroot", "sweet potato", "sweet potato", "potato"}

# -------- Display Set --------
print(vegetables)


# -------- Membership Check --------
print("pineapple" in vegetables)


# -------- Adding Elements --------
vegetables.add("pineapple")
print(vegetables)


# -------- Removing Elements --------
vegetables.remove("pineapple")
print(vegetables)


# -------- Removing Random Element --------
vegetables.pop()
print(vegetables)


# -------- Clearing a Set --------
vegetables.clear()
print(vegetables)

# ==================================================
# -------------------- Tuples -----------------------
# ==================================================

foods = ("burger", "pizza", "pasta", "sandwich", "burger", "pizza")

# -------- Tuple Functions --------
print(foods.index("sandwich"))
print(foods.count("pizza"))

# -------- Looping Through a Tuple --------
for food in foods:
    print(food)

# -------- Help and Inspection Functions --------

# Displays documentation about strings
# help(str)

# Displays all available string methods
# print(dir(str))