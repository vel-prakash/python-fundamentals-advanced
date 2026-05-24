import random

# -------- Random Integers --------

# Generates a random integer between 1 and 6
number = random.randint(1, 6)
print(number)

# Generates a random integer between a custom range
low = 1
high = 100

number = random.randint(low, high)
print(number)

# -------- Random Floating-Point Numbers --------

# Generates a random floating-point number between 0 and 1
number = random.random()
print(number)

# -------- Random Choice --------

options = ("rock", "paper", "scissors")

option = random.choice(options)
print(option)

# -------- Shuffling a List --------

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

random.shuffle(cards)

print(cards)