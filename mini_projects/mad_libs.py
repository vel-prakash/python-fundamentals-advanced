# Mad Libs Game
# Word game where you create a story
# by filling in blanks with random words

# -------- Input --------
adjective1 = input("Enter an adjective (description): ")
noun = input("Enter a noun (person, place, thing): ")
adjective2 = input("Enter an adjective (description): ")
verb = input("Enter a verb ending with 'ing': ")
adjective3 = input("Enter an adjective (description): ")

# -------- Story --------
print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun}.")
print(f"{noun} was {adjective2} and {verb}")
print(f"I was {adjective3}!")