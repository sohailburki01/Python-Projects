""" Enhanced password generator with better practices and features """
import random
import string
import pyperclip  # Optional: for clipboard functionality
from colorama import Fore, init

# Initialize colorama for cross-platform color support
init(autoreset=True)


def main():
    """Main function that handles user interaction and password generation"""
    print(Fore.CYAN + "="*50)
    print(Fore.CYAN + "       PASSWORD GENERATOR")
    print(Fore.CYAN + "="*50 + "\n")

    while True:
        user_choice = input(
            Fore.YELLOW + "Choose password strength:\n"
            "  1) 'weak' - lowercase letters only\n"
            "  2) 'medium' - letters and numbers\n"
            "  3) 'strong' - letters, numbers, and symbols\n"
            "  4) 'custom' - customize your password\n"
            "  5) 'exit' - quit the program\n"
            + Fore.WHITE + "Your choice: "
        ).lower().strip()

        if user_choice in ['weak', '1']:
            weak_password()
        elif user_choice in ['medium', '2']:
            medium_password()
        elif user_choice in ['strong', '3']:
            strong_password()
        elif user_choice in ['custom', '4']:
            custom_password()
        elif user_choice in ['exit', '5', 'quit']:
            print(Fore.GREEN + "Thank you for using Password Generator!")
            break
        else:
            print(Fore.RED + "Invalid input! Please try again.\n")

        if user_choice in ['weak', 'medium', 'strong', 'custom', '1', '2', '3', '4']:
            another = input(
                Fore.YELLOW + "\nGenerate another password? (yes/no): ").lower()
            if another not in ['yes', 'y']:
                print(Fore.GREEN + "Thank you for using Password Generator!")
                break
            print()  # Add spacing


def get_valid_length(min_length=4, max_length=128):
    """Get valid password length from user"""
    while True:
        try:
            length = int(
                input(Fore.WHITE + f"Enter password length ({min_length}-{max_length}): "))
            if min_length <= length <= max_length:
                return length
            else:
                print(
                    Fore.RED + f"Please enter a number between {min_length} and {max_length}")
        except ValueError:
            print(Fore.RED + "Please enter a valid number")


def get_valid_input(prompt, max_value):
    """Get valid integer input from user"""
    while True:
        try:
            value = int(input(Fore.WHITE + prompt))
            if 0 <= value <= max_value:
                return value
            else:
                print(
                    Fore.RED + f"Please enter a number between 0 and {max_value}")
        except ValueError:
            print(Fore.RED + "Please enter a valid number")


def display_password(password, strength):
    """Display the generated password with formatting"""
    strength_colors = {
        'Weak': Fore.RED,
        'Medium': Fore.YELLOW,
        'Strong': Fore.GREEN,
        'Custom': Fore.CYAN
    }

    print("\n" + "="*50)
    print(f"{strength_colors[strength]}Password Strength: {strength}")
    print(f"{Fore.WHITE}Your password: {strength_colors[strength]}{password}")
    print("="*50)

    # Optional: Copy to clipboard (requires pyperclip)
    try:
        pyperclip.copy(password)
        print(Fore.GREEN + "✓ Password copied to clipboard!")
    except:
        pass  # pyperclip might not be installed


def weak_password():
    """Generate a weak password using only lowercase letters"""
    length = get_valid_length()
    password = ''.join(random.choices(string.ascii_lowercase, k=length))
    display_password(password, 'Weak')


def medium_password():
    """Generate a medium password using letters and numbers"""
    print(Fore.CYAN + "\nMedium Password Configuration:")
    length = get_valid_length()

    # Use both uppercase and lowercase letters with numbers
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choices(characters, k=length))

    # Ensure at least one letter and one number
    if not any(c.isalpha() for c in password):
        password = password[:-1] + random.choice(string.ascii_letters)
    if not any(c.isdigit() for c in password):
        password = password[:-1] + random.choice(string.digits)

    # Shuffle to randomize
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    display_password(password, 'Medium')


def strong_password():
    """Generate a strong password using letters, numbers, and symbols"""
    print(Fore.CYAN + "\nStrong Password Configuration:")
    # Strong passwords should be at least 8 chars
    length = get_valid_length(min_length=8)

    # Define character sets
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    all_characters = string.ascii_letters + string.digits + symbols

    # Generate password ensuring complexity
    password = []
    # Ensure at least one of each type
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.digits))
    password.append(random.choice(symbols))

    # Fill the rest randomly
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle to randomize
    random.shuffle(password)
    password = ''.join(password)

    display_password(password, 'Strong')


def custom_password():
    """Generate a custom password with user-specified requirements"""
    print(Fore.CYAN + "\nCustom Password Configuration:")

    # Get user preferences
    use_lowercase = input(
        Fore.WHITE + "Include lowercase letters? (yes/no): ").lower() in ['yes', 'y']
    use_uppercase = input(
        Fore.WHITE + "Include uppercase letters? (yes/no): ").lower() in ['yes', 'y']
    use_digits = input(
        Fore.WHITE + "Include numbers? (yes/no): ").lower() in ['yes', 'y']
    use_symbols = input(
        Fore.WHITE + "Include symbols? (yes/no): ").lower() in ['yes', 'y']

    # Build character pool
    char_pool = ""
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += "!@#$%^&*()_+-=[]{}|;:,.<>?"

    if not char_pool:
        print(Fore.RED + "You must select at least one character type!")
        return

    length = get_valid_length()

    # Generate password
    password = []

    # Ensure at least one of each selected type
    if use_lowercase and length >= 1:
        password.append(random.choice(string.ascii_lowercase))
    if use_uppercase and length >= 2:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits and length >= 3:
        password.append(random.choice(string.digits))
    if use_symbols and length >= 4:
        password.append(random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?"))

    # Fill remaining length
    remaining = length - len(password)
    password.extend(random.choices(char_pool, k=remaining))

    # Shuffle
    random.shuffle(password)
    password = ''.join(password)

    display_password(password, 'Custom')


def check_password_strength(password):
    """Analyze and display password strength metrics"""
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
        feedback.append(Fore.GREEN + "✓ Good length")
    elif len(password) >= 8:
        score += 1
        feedback.append(Fore.YELLOW + "○ Moderate length")
    else:
        feedback.append(Fore.RED + "✗ Too short")

    # Character variety checks
    if any(c.islower() for c in password):
        score += 1
        feedback.append(Fore.GREEN + "✓ Contains lowercase")
    if any(c.isupper() for c in password):
        score += 1
        feedback.append(Fore.GREEN + "✓ Contains uppercase")
    if any(c.isdigit() for c in password):
        score += 1
        feedback.append(Fore.GREEN + "✓ Contains numbers")
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        score += 2
        feedback.append(Fore.GREEN + "✓ Contains symbols")

    # Display feedback
    print("\nPassword Strength Analysis:")
    for item in feedback:
        print(f"  {item}")

    if score >= 6:
        print(Fore.GREEN + f"\nStrength Score: {score}/7 - STRONG")
    elif score >= 4:
        print(Fore.YELLOW + f"\nStrength Score: {score}/7 - MEDIUM")
    else:
        print(Fore.RED + f"\nStrength Score: {score}/7 - WEAK")


if __name__ == "__main__":
    main()
