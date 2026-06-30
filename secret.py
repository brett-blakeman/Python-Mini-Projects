import random

secret = random.randint(1, 10)

guess = int(input("Guess the secret number between 1 and 10: "))

if guess == secret:
    print("Congratulations! You guessed the secret number.")
else:
    print(f"Sorry, the secret number was {secret}.")