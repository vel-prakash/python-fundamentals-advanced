# variables = A container for a value (string, integer, float, boolean)
#             A variable behaves as if it was the value it contains

# Topic: Strings
# Concept: Variable assignment + f-string formatting

first_name = "James"
food = "pizza"
email = "James@gmail.com"

print(first_name)

print(f"Hello, {first_name}!")
print(f"You like {food}.")
print(f"Your email is: {email}")

# Topic: Integers
# Concept: Storing numbers and printing using f-strings

age = 25
quantity = 3
num_of_students = 30

print(f"You are {age} years old.")
print(f"You are buying {quantity} items.")
print(f"Your class has {num_of_students} students.")

# Topic: Float
# Concept: Storing decimal values and formatting output

price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price:.2f}")
print(f"Your gpa is {gpa}")
print(f"You ran {distance} km")

# Topic: Boolean
# Concept: Using True/False values in conditions and output

is_student = True
for_sale = False
is_online = True

print(f"Are you a student? {is_student}")
print(f"Is that item for sale? {for_sale}")
print(f"Are you online? {is_online}")