import random
from turtle import goto

play = True

while play == True:
    print("Welcome To Rock, Paper, Scissors!" )
    choices = ["rock", "paper", "scissors"]
    secret_choice = ["gun"]
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_choice not in choices and user_choice not in secret_choice:
        print("Invalid choice. Please choose rock, paper, or scissors.")
    elif user_choice == computer_choice:
        print(f"Both players chose {user_choice}. It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):
        print(f"You chose {user_choice} and the computer chose {computer_choice}. You win!")
    elif user_choice == "gun":
        print(f"You chose the omnipotent {user_choice}!! The computer chose {computer_choice}. You win!")
    else:
        print(f"You chose {user_choice} and the computer chose {computer_choice}. You lose!")

    print("Thanks for playing!")
    pAgain = input("Do you want to play again? (yes/no): ").lower()
    if pAgain == "yes":
        print("Restarting the game...")
        play = True
    else:
        print("Goodbye!")
        play = False
        break
