# Slot Machine Game
# A simple command-line slot machine game where players
# place bets, spin the reels, and win payouts based on matching symbols.

import random

def spin_row():
    """Generate a row containing three random slot symbols."""

    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]
    row = []

    for _ in range(3):
        symbol = random.choice(symbols)
        row.append(symbol)

    return row

def print_row(row):
    """Display the generated slot machine row."""

    print("=" * 25)
    print(" | ".join(row))
    print("=" * 25)

def get_payout(row, bet):
    """Calculate the player's payout based on matching symbols."""

    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20

    return 0

def main():
    """Run the Slot Machine game."""

    balance = 100

    print("=" * 35)
    print("      Python Slot Machine")
    print("=" * 35)
    print("Symbols:")
    print("🍒  🍉  🍋  🔔  ⭐")
    print("=" * 35)

    while balance > 0:
        print(f"\nCurrent Balance: ${balance}")

        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds.")
            continue

        if bet <= 0:
            print("Bet amount must be greater than zero.")
            continue

        balance -= bet

        row = spin_row()

        print("\nSpinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}!")
        else:
            print("Sorry, you lost this round.")

        balance += payout

        play_again = input("\nWould you like to spin again? (Y/N): ").upper()

        if play_again != "Y":
            break

    print("\n" + "=" * 40)
    print(f"Game Over! Your final balance is ${balance}.")
    print("=" * 40)

if __name__ == "__main__":
    main()