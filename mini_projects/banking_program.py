# Banking Program
# A simple command-line banking application that allows users
# to check their balance, deposit money, and withdraw funds.


def show_balance(balance):
    """Display the current account balance."""

    print("=" * 30)
    print(f"Current Balance: ${balance:.2f}")
    print("=" * 30)


def deposit():
    """Prompt the user to deposit money."""

    print("=" * 30)
    amount = float(input("Enter an amount to deposit: "))
    print("=" * 30)

    if amount < 0:
        print("Invalid amount. Please enter a positive value.")
        return 0

    return amount


def withdraw(balance):
    """Prompt the user to withdraw money."""

    print("=" * 30)
    amount = float(input("Enter an amount to withdraw: "))
    print("=" * 30)

    if amount > balance:
        print("Insufficient funds.")
        return 0

    elif amount < 0:
        print("The amount must be greater than zero.")
        return 0

    return amount


def main():
    """Run the Banking Program."""

    balance = 0
    is_running = True

    while is_running:

        print("=" * 30)
        print("      Banking Program")
        print("=" * 30)
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("=" * 30)

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)

        elif choice == "2":
            balance += deposit()

        elif choice == "3":
            balance -= withdraw(balance)

        elif choice == "4":
            is_running = False

        else:
            print("=" * 30)
            print("Invalid choice. Please try again.")
            print("=" * 30)

    print("=" * 30)
    print("Thank you for using the Banking Program!")
    print("Have a great day!")
    print("=" * 30)


if __name__ == "__main__":
    main()