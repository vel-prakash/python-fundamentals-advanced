# Keyword arguments are arguments passed using parameter names.
# They improve readability and allow arguments to be supplied
# in any order.
#
# Argument types:
# 1. Positional
# 2. Default
# 3. Keyword
# 4. Arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

# When mixing positional and keyword arguments,
# positional arguments must come first.
hello("Hello", last="Squarepants", title="Mr.", first="Spongebob")

for x in range(1, 11):
    print(x, end=" ")

print()

# The 'end' keyword argument controls what is printed
# after each call to print().

# The 'sep' keyword argument specifies the separator
# placed between multiple values.
print("1", "2", "3", "4", "5", sep=" - ")

def get_phone(country_code, area_code, prefix, line_number):
    return f"{country_code}-{area_code}-{prefix}-{line_number}"

phone_num = get_phone(
    country_code=1,
    area_code=123,
    prefix=456,
    line_number=7890,
)

print(phone_num)