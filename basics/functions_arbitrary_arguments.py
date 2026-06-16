# ============================================================
# *args and **kwargs Examples
# ============================================================
#
# *args   : Allows a function to accept multiple positional arguments.
# **kwargs: Allows a function to accept multiple keyword arguments.
#
# Parameter order when defining functions:
# 1. Positional arguments
# 2. Default arguments
# 3. *args
# 4. **kwargs
#
# ============================================================


def add(*args):
    """Return the sum of all positional arguments."""

    total = 0

    for arg in args:
        total += arg

    return total


print("Sum:", add(1, 2, 3))


# ============================================================


def display_name(*args):
    """Display all name components on a single line."""

    for arg in args:
        print(arg, end=" ")

    print()  # Move to the next line after printing the name


display_name("Dr.", "Spongebob", "Squarepants", "III")


# ============================================================


def print_address(**kwargs):
    """Display address information from keyword arguments."""

    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(
    street="487 Rose Street",
    apt="100",
    city="Detroit",
    state="MI",
    zip="54321"
)

print()


# ============================================================


def shipping_label(*args, **kwargs):
    """Print a formatted shipping label."""

    # Print recipient name
    for arg in args:
        print(arg, end=" ")

    print()

    # Print street address
    if "apt" in kwargs:
        print(kwargs.get("street"))
        print(kwargs.get("apt"))

    elif "pobox" in kwargs:
        print(kwargs.get("street"))
        print(kwargs.get("pobox"))

    else:
        print(kwargs.get("street"))

    # Print city, state, and ZIP code
    print(
        f"{kwargs.get('city')}, "
        f"{kwargs.get('state')} "
        f"{kwargs.get('zip')}"
    )


shipping_label(
    "Dr.",
    "Spongebob",
    "Squarepants",
    "III",
    street="487 Rose Street",
    pobox="PO Box #1001",
    city="Detroit",
    state="MI",
    zip="54321"
)