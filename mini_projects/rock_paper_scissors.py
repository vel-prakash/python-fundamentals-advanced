# -------- Rock Paper Scissors Game --------

import random

options = ("rock", "paper", "scissors")

running = True

# -------- Main Game Loop --------
while running:

    player = None
    computer = random.choice(options)

    # -------- Player Input Validation --------
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"\nPlayer: {player}")
    print(f"Computer: {computer}")

    # -------- Determine Winner --------
    if player == computer:
        print("It's a tie!")

    elif player == "rock" and computer == "scissors":
        print("You win!")

    elif player == "paper" and computer == "rock":
        print("You win!")

    elif player == "scissors" and computer == "paper":
        print("You win!")

    else:
        print("You lose!")

    # -------- Play Again --------
    if not input("\nPlay again? (y/n): ").lower() != "y":
        running = False

print("Thanks for playing!")