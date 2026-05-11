# -------- String Methods --------

# -------- User Input --------
name = input("Enter your full name: ")

# -------- Length Method --------
# Returns the total number of characters
name_length = len(name)

# -------- Find Methods --------
# Returns the index of the first occurrence
first_o = name.find("o")

# Returns the index of the last occurrence
last_o = name.rfind("o")

# Returns -1 if character is not found
find_q = name.find("q")

# -------- Case Conversion Methods --------
# Capitalizes the first character
capitalized_name = name.capitalize()

# Converts all characters to uppercase
uppercase_name = name.upper()

# Converts all characters to lowercase
lowercase_name = name.lower()

# -------- Validation Methods --------
# Returns True if the string contains digits only
is_digits = name.isdigit()

# Returns True if the string contains alphabetic characters only
is_alpha = name.isalpha()

# -------- Output --------
print(name_length)
print(first_o)
print(last_o)
print(find_q)
print(capitalized_name)
print(uppercase_name)
print(lowercase_name)
print(is_digits)
print(is_alpha)

# -------- Phone Number Exercise --------
phone_number = input("Enter your phone number: ")

# Counts the number of dashes
dash_count = phone_number.count("-")

# Removes all dashes
formatted_phone_number = phone_number.replace("-", "")

# -------- Output --------
print(dash_count)
print(formatted_phone_number)


# -------- String Validation Exercise --------

# Username Rules:
# 1. Username must not exceed 12 characters
# 2. Username must not contain spaces
# 3. Username must contain letters only

username = input("Enter a username: ")

# Checks if the username is longer than 12 characters
if len(username) > 12:
    print("Your username can't be more than 12 characters.")

# Checks if the username contains spaces
elif not username.find(" ") == -1: 
    print("Your username can't contain spaces.")

# Checks if the username contains non-alphabetic characters
elif not username.isalpha():
    print("Your username can't contain numbers or special characters.")

# Valid username
else:
    print(f"Welcome {username}!")


# -------- Help Function --------

# Displays all available string methods
# Uncomment to explore Python string documentation
# print(help(str))