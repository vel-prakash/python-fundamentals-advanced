# Library Demo
# Demonstrates how to import functions
# from another Python module.

from example_library import *

def favorite_drink(drink):
    """Display the user's favorite drink."""
    print(f"Your favorite drink is {drink}")

def main():
    """Demonstrate imported and local functions."""
    print("Running library_demo.py")
    favorite_food("Sushi")
    favorite_drink("Coffee")
    print("Goodbye!")

if __name__ == "__main__":
    main()