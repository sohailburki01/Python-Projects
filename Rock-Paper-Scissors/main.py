""" The random module will help in creating a random choice
between Rock Paper and sys module help us exit the program """
import random
import sys


def main():
    """This function calls the play_game function"""
    print("-- ROCK PAPER SCISSORS --")
    user_choice = input("Do you wanna play a game of Rock Paper Scissors: ").lower()
    if user_choice == "yes":
        play_game()
    elif user_choice == "no":
        sys.exit("Bye")
    else:
        print("Invalid Input -- Type 'yes' or 'no' ")


def play_game():
    """This function create a random choice and let
    you play with the computer"""
    wins = 0
    loses = 0
    while True:
        all_choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(all_choices)
        user_choice = input("Choose One: Rock | Paper | Scissors: ").title()

        if user_choice == computer_choice:
            print(
                f"Your choice: {user_choice} || Computer choice: {computer_choice} -- Match Tie!"
            )
        elif user_choice == "Rock" and computer_choice == "Paper":
            print("Paper wins against Rock")
            print(
                f"Your choice: {user_choice} || Computer choice: {computer_choice} -- You Lose!"
            )
            loses += 1
        elif user_choice == "Paper" and computer_choice == "Rock":
            print("Paper wins against Rock")
            print(
                f"Your choice: {user_choice} || Computer choice: {computer_choice} -- You Win!"
            )
            wins += 1
        elif user_choice == "Rock" and computer_choice == "Scissors":
            print("Rock wins against Scissors")
            print(
                f"Your choice: {user_choice} || Computer choice: {computer_choice} -- You Win!"
            )
            wins += 1
        elif user_choice == "Scissors" and computer_choice == "Rock":
            print("Rock wins against Scissors")
            print(
                f"Your choice: {user_choice} || Computer choice: {computer_choice} -- You Lose!"
            )
            loses += 1
        elif user_choice == "Scissor" and computer_choice == "Paper":
            print("Scissors wins against Paper")
            print(
                f"Your choice: {user_choice} || Computer choice: {computer_choice} -- You Win!"
            )
            wins += 1
        elif user_choice == "Paper" and computer_choice == "Scissors":
            print("Scissors wins against Paper")
            print(
                f"Your choice: {user_choice} || Computer choice: {computer_choice} -- You Lose!"
            )
            loses += 1

        if wins >= 3:
            sys.exit("Congratulation! You won the game.")
        elif loses >= 3:
            sys.exit("Oops! Computer won the game. You Lose.")


if __name__ == "__main__":
    main()
