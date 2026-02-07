"""
Password Generator Program
Generates weak, medium, or strong passwords based on user choice
"""

import random
from colorama import Fore, Style


# Function to generate a weak password (only lowercase letters)
def generate_weak_password():
    letters = "abcdefghijklmnopqrstuvwxyz"

    length = int(input("Enter password length: "))

    # Randomly select letters
    password = random.choices(letters, k=length)

    print(Fore.GREEN + "Your weak password is: " + "".join(password))


# Function to generate a medium password (letters + numbers)
def generate_medium_password():
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"

    letter_count = int(input("How many letters do you want? "))
    number_count = int(input("How many numbers do you want? "))

    # Generate parts of password
    password_letters = random.choices(letters, k=letter_count)
    password_numbers = random.choices(numbers, k=number_count)

    # Combine and shuffle
    password = password_letters + password_numbers
    random.shuffle(password)

    print(Fore.YELLOW + "Your medium password is: " + "".join(password))


# Function to generate a strong password (letters + numbers + symbols)
def generate_strong_password():
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "~@#$%^&*()?/<>|"

    letter_count = int(input("How many letters do you want? "))
    number_count = int(input("How many numbers do you want? "))
    symbol_count = int(input("How many symbols do you want? "))

    # Generate password parts
    password_letters = random.choices(letters, k=letter_count)
    password_numbers = random.choices(numbers, k=number_count)
    password_symbols = random.choices(symbols, k=symbol_count)

    # Combine all and shuffle
    password = password_letters + password_numbers + password_symbols
    random.shuffle(password)

    print(Fore.RED + "Your strong password is: " + "".join(password))


# Main function to control program flow
def main():
    print(Style.BRIGHT + "Password Generator")
    print("Choose password strength: weak / medium / strong")

    choice = input("Enter your choice: ").lower()

    if choice == "weak":
        generate_weak_password()
    elif choice == "medium":
        generate_medium_password()
    elif choice == "strong":
        generate_strong_password()
    else:
        print(Fore.RED + "Invalid choice! Please try again.")


# Program execution starts here
if __name__ == "__main__":
    main()
