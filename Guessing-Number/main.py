""" This random let us create random numbers between
any numbers of our choice and the sys module
help us exit the program successfully """
import random
import sys


def main():
    """This function prompts the user for input
    to choose a level to play."""
    choose_level = input("Type 'easy'  or 'hard' : ").lower().strip()
    if choose_level == "easy":
        easy_level()
    elif choose_level == "hard":
        hard_level()
    else:
        print("Invalid Input!")


def make_bet():
    """ This function creates an opponent for you and you can bet as well """
    opponents = ['Asfand', 'Faizan', 'Sulaeman', 'Asad', 'Fawad', 'Mani'] # NOQA
    opponent_bet = [20, 30, 40, 50, 60, 70, 80, 90, 100]
    opponent = random.choice(opponents)
    name = input("Your name: ")
    bet_amount = int(input("How much you wanna bet? $"))
    print(f"Your Opponent is: {opponent}")
    print(f"{name} bet: {bet_amount} | {opponent} bet: {random.choice(opponent_bet)}")


def easy_level():
    """This is an easy version of guessing the number
    game with at least 10 tries"""
    make_bet()
    tries = 10
    random_number = random.randint(1, 30)  # NOQA
    while True:  # NOQA
        try:
            user_choice = int(input("Enter your guess: "))  # NOQA
            if user_choice == random_number:
                sys.exit("Congratulation! You guessed it right. You Win!")
            elif user_choice > random_number:
                tries -= 1
                print("Your guess is a larger than expected.")
                print(f"You have {tries} attempts left to guess the number.")
            elif user_choice < random_number:
                tries -= 1
                print("Your guess is a smaller than expected.")
                print(f"You have {tries} attempts left to guess the number.")
            if tries == 0:
                sys.exit("Out of attempts. You Lose!")
        except ValueError:
            sys.exit("Invalid Input! You were supposed to enter a number")


def hard_level():
    """This is a hard version of guessing the number
    game with only 5 tries"""
    make_bet()
    tries = 5
    random_number = random.randint(1, 30)  # NOQA
    while True:  # NOQA
        try:
            user_choice = int(input("Enter your guess: "))  # NOQA
            if user_choice == random_number:
                sys.exit("Congratulation! You guessed it right. You Win!")
            elif user_choice > random_number:
                tries -= 1
                print("Your guess is a larger than expected.")
                print(f"You have {tries} attempts left to guess the number.")
            elif user_choice < random_number:
                tries -= 1
                print("Your guess is a smaller than expected.")
                print(f"You have {tries} attempts left to guess the number.")
            if tries == 0:
                sys.exit("Out of attempts. You Lose!")
        except ValueError:
            sys.exit("Invalid Input! You were supposed to enter a number")


if __name__ == "__main__":
    main()
