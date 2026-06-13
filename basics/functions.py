# Functions are reusable blocks of code.
# Use parentheses () after the function name to call the function.


def happy_birthday(name, age):
    """Print a birthday message."""
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy birthday to you!")
    print()


happy_birthday("Bro", 25)
happy_birthday("Steve", 20)
happy_birthday("Joe", 30)


def display_invoice(username, amount, due_date):
    """Display invoice details."""
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")


display_invoice("Joe", 100.01, "01/02")


# The return statement ends a function
# and sends a value back to the caller.


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))


def create_name(first, last):
    """Return a properly formatted full name."""
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


full_name = create_name("spongebob", "squarepants")

print(full_name)