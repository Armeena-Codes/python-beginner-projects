# Number Guessing Game - Python Beginner Project 4
# Created by Armeena-Codes
import random

print("=== Number Guessing Game by Armeena ===")
secret = random.randint(1, 100)

while True:
    guess = int(input("Guess number between 1-100: "))
    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed {secret}!")
        break