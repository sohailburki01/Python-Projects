import random
import string

def generate_password(length):
    """Generate a random strong password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Password length must be greater than 0.")
        else:
            print("Generated Password:", generate_password(length))
    except ValueError:
        print("Please enter a valid number.")
