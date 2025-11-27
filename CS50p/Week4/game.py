import random
from cs50 import get_int

# Prompt user for level
while True:
    level = get_int("Level: ")

    if level > 0:
        break

# Generate random number between 1 and level inclusive
number = random.randint(1, level+1)

# Prompt user to guess number
while True:
    guess = get_int("Guess: ")

    if guess > 0:
        break

# Check guess against number
while True:
    if guess < number:
        print("Too small!")
    if guess > number:
        print("Too large!")
    if guess == number:
        print("Just right!")
        break
