import string
import random
from colorama import Fore

# --- GLOBAL VARIABLES ---
letters = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation

def main():
    """This is the main function and it calls all the other function depending on user_choice"""
    user_choice = input(
        "Type 'weak' to get a weak password, 'medium' to get a medium one \nand 'strong' to get a strong password: "
    ).lower()
    if user_choice == "weak":
        weak_password()
    elif user_choice == "medium":
        medium_password()
    elif user_choice == "strong":
        strong_password()
    else:
        print(Fore.RED + "Invalid Input!")

def weak_password():
    """This function will generate a weak password for you"""
    user_choice = int(input("How long you need your password to be: "))
    password = random.choices(letters, k=user_choice)
    print("Here is your password: " + Fore.RED + "".join(password))

def medium_password():
    """This function will generate a medium password for you"""
    letter_choice = int(input("How much letters do you want in your password: "))
    number_choice = int(input("How much numbers do you want in your password: "))
    letter_password = random.choices(letters, k=letter_choice)
    number_password = random.choices(numbers, k=number_choice)
    password = letter_password + number_password
    random.shuffle(password)
    print("Here is your password: " + Fore.RED + "".join(password))

def strong_password():
    """This function will generate a strong password for you"""
    letter_choice = int(input("How much letters do you want in your password: "))
    number_choice = int(input("How much numbers do you want in your password: "))
    symbol_choice = int(input("How much symbols do you want in your password: "))
    letter_password = random.choices(letters, k=letter_choice)
    number_password = random.choices(numbers, k=number_choice)
    symbol_password = random.choices(symbols, k=symbol_choice)
    password = letter_password + number_password + symbol_password
    random.shuffle(password)
    print("Here is your password: " + Fore.RED + "".join(password))

if __name__ == "__main__":
    main()