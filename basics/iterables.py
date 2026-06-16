# ============================================================
# Iterables
# ============================================================
#
# An iterable is an object or collection that can return
# its elements one at a time, allowing it to be traversed
# (iterated over) using a loop.
#
# Common iterable types:
# - Lists
# - Tuples
# - Sets
# - Strings
# - Dictionaries
#
# ============================================================

# Iterate through a list
numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

print()

# Iterate through a list in reverse order
for number in reversed(numbers):
    print(number, end=" ")

print("\n")

# Iterate through a set
fruits = {"apple", "orange", "banana", "coconut"}

for fruit in fruits:
    print(fruit)

print()

# Iterate through a string character by character
name = "Bro Code"

for character in name:
    print(character, end=" ")

print("\n")

# Iterate through a dictionary using key-value pairs
my_dictionary = {
    "A": 1,
    "B": 2,
    "C": 3,
}

for key, value in my_dictionary.items():
    print(f"{key}: {value}")