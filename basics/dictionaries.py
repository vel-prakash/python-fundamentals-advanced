# -------- Dictionaries --------
# A dictionary stores data in {key:value} pairs.
# Dictionaries are ordered, changeable, and do not allow duplicate keys.

# ==================================================
# ---------------- Dictionary Setup ----------------
# ==================================================

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# ==================================================
# ---------------- Accessing Values ----------------
# ==================================================

# Returns the value associated with a key
print(capitals.get("USA"))
print(capitals.get("India"))

# Returns None if the key does not exist
print(capitals.get("Japan"))

# ==================================================
# ---------------- Checking Keys -------------------
# ==================================================

# Checks whether the key exists in the dictionary
if capitals.get("Russia"):
    print("That capital exists")

else:
    print("That capital doesn't exist")

# ==================================================
# --------------- Updating Dictionary --------------
# ==================================================

# Adds a new key-value pair
capitals.update({"Germany": "Berlin"})

# Updates an existing value
capitals.update({"USA": "Detroit"})

# ==================================================
# ---------------- Removing Items ------------------
# ==================================================

# Removes a specific key-value pair
capitals.pop("USA")

# Removes the last inserted key-value pair
capitals.popitem()

print(capitals)
# ==================================================
# ---------------- Displaying Keys -----------------
# ==================================================

keys = capitals.keys()

for key in capitals.keys():
    print(key)


# ==================================================
# ---------------- Displaying Items ----------------
# ==================================================

items = capitals.items()

for key, value in capitals.items():
    print(f"{key}: {value}")


# ==================================================
# ---------------- Displaying Values ---------------
# ==================================================

values = capitals.values()

for value in capitals.values():
    print(value)

# ==================================================
# ---------------- Clearing Dictionary -------------
# ==================================================

capitals.clear()

print(capitals)