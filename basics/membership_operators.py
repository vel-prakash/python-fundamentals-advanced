# Membership Operators
# Used to test whether a value exists within a sequence or collection.
#
# Supported collections:
# - Strings
# - Lists
# - Tuples
# - Sets
# - Dictionaries
#
# Operators:
# 1. in
# 2. not in

# -------- String Membership --------

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter not in word:
    print(f"'{letter}' is not in the word.")
else:
    print(f"'{letter}' is in the word.")

# -------- Set Membership --------

students = {"Spongebob", "Patrick", "Sandy"}

student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a student.")
else:
    print(f"Student '{student}' was not found.")

# -------- Dictionary Membership --------

grades = {
    "Sandy": "A",
    "Squidward": "B",
    "Spongebob": "C",
    "Patrick": "D"
}

student = input("Enter the name of a student: ")

if student in grades:
    # Access the grade using the student's name as the dictionary key
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"Student '{student}' was not found.")

# -------- Email Validation --------

email = "python@gmail.com"

if "@" in email and "." in email:
    print("The email address is valid.")
else:
    print("The email address is invalid.")