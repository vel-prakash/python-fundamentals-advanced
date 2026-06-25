# Main Guard
# The main guard determines whether a Python file
# is executed directly or imported as a module.
#
# Benefits:
# - Prevents code from running when the file is imported
# - Allows functions and classes to be reused
# - Defines the program's entry point

def main():
    """Program entry point."""
    print("Hello")

if __name__ == "__main__":
    main()