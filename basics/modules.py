# Modules
# A module is a file that contains reusable code such as variables,
# functions, and classes.
#
# Benefits:
# - Organizes code into separate files
# - Improves code reusability
# - Makes large programs easier to maintain
#
# Modules can be:
# - Built-in modules (math, random, etc.)
# - Custom modules created by the user

# print(help("modules"))

# -------- Module Aliases --------

import math as m

print(m.pi)

# -------- Importing Specific Members --------

from math import e

print(e)

# -------- Name Conflict Example --------
# Avoid importing names directly when they may conflict
# with variables in your program.

import math

a, b, c, d, e = 1, 2, 3, 4, 5

print(math.e ** a)
print(math.e ** b)
print(math.e ** c)
print(math.e ** d)
print(math.e ** e)

# -------- Importing a Custom Module --------

import example_module

result = example_module.pi
result = example_module.square(3)
result = example_module.cube(3)
result = example_module.circumference(3)
result = example_module.area(3)

print(result)