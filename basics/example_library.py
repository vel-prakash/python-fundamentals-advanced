# Example Library
# This module contains reusable functions that can be
# imported and used by other Python files.

def favorite_food(food):
    """Display the user's favorite food."""
    print(f"Your favorite food is {food}")

def main():
    """Demonstrate the functions in this module."""
    print("Running example_library.py")
    favorite_food("Pizza")
    print("Goodbye!")

if __name__ == "__main__":
    main()