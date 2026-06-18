# List Comprehensions
# A concise way to create lists using a single line of code.
#
# Syntax:
# [expression for item in iterable if condition]
#
# Benefits:
# - More concise than traditional loops
# - Improves readability
# - Useful for filtering and transforming data

# -------- Traditional Loop Example --------

doubles = []

for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)

# -------- Basic List Comprehensions --------

doubles = [x * 2 for x in range(1, 11)]
triples = [x * 3 for x in range(1, 11)]
squares = [x * x for x in range(1, 11)]

print(doubles)
print(triples)
print(squares)

# -------- String Transformations --------

fruits = ["apple", "orange", "banana", "coconut"]

fruits = [fruit.upper() for fruit in fruits]

print(fruits)

first_letters = [fruit[0] for fruit in fruits]

print(first_letters)

# -------- Filtering Numbers --------

numbers = [1, -2, 3, -4, 5, -6, 8, -7]

positive_nums = [number for number in numbers if number >= 0]
negative_nums = [number for number in numbers if number < 0]

even_nums = [number for number in numbers if number % 2 == 0]
odd_nums = [number for number in numbers if number % 2 == 1]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

# -------- Filtering Grades --------

grades = [85, 42, 79, 90, 56, 61, 30]

passing_grades = [grade for grade in grades if grade > 60]

print(passing_grades)