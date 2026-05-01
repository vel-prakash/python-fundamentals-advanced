# Typecasting = the process of converting a variable from one data type to another
# str(), int(), float(), bool()

# -------- Variables --------

name = "Oliver"
age = 22
gpa = 3.2
is_student = True

# -------- Checking Types --------

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# -------- Type Casting --------

age = float(age)
print(age)

gpa = int(gpa)
print(gpa)

# ----------- Important Concept -----------

# String + String → concatenation

age = str(age)
print(age)
print(type(age))

age += "1"
print(age)

# Summary
# Mainly used: print(type(variable)), age = float(age), int(), str()