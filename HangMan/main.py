""" The random module help us choose a random word from a list of words
and the sys module helps us in exiting the program """
import random
import string


def display_hangman(lives):
    """Display hangman ASCII art based on remaining lives"""
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |   
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |   
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   
           |   
           |
        --------
        """,
        """
           ------
           |    |
           |    
           |   
           |   
           |
        --------
        """
    ]
    return stages[lives]


def get_valid_input():
    """Get and validate user input"""
    while True:
        guess = input("\nGuess a letter: ").lower().strip()

        if len(guess) != 1:
            print("Please enter exactly one letter.")
            continue

        if not guess.isalpha():
            print("Please enter a valid letter (a-z).")
            continue

        return guess


def play_hangman():
    """Main game function"""
    # Word categories for better gameplay
    word_categories = {
        'programming': ['python', 'javascript', 'algorithm', 'function', 'variable', 'debugging', 'compiler'],
        'technology': ['computer', 'internet', 'software', 'hardware', 'database', 'network', 'security'],
        'general': ['rainbow', 'butterfly', 'adventure', 'mystery', 'journey', 'treasure', 'champion']
    }

    # Game setup
    print("\n" + "="*50)
    print(" "*15 + "WELCOME TO HANGMAN!")
    print("="*50)

    # Choose category (optional feature)
    print("\nCategories: programming, technology, general")
    category = input(
        "Choose a category (or press Enter for random): ").lower().strip()

    if category in word_categories:
        words_list = word_categories[category]
        print(f"\nCategory: {category.upper()}")
    else:
        words_list = [word for sublist in word_categories.values()
                      for word in sublist]
        print("\nCategory: RANDOM")

    # Initialize game variables
    chosen_word = random.choice(words_list)
    word_display = ['_'] * len(chosen_word)
    guessed_letters = set()
    incorrect_letters = set()
    lives = 6

    # Game loop
    while lives > 0 and '_' in word_display:
        # Display game state
        print("\n" + "-"*40)
        print(display_hangman(lives))
        print(f"Word: {' '.join(word_display)}")
        print(f"Lives remaining: {lives}")

        if incorrect_letters:
            print(f"Incorrect letters: {', '.join(sorted(incorrect_letters))}")

        # Get player input
        guess = get_valid_input()

        # Check if letter was already guessed
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        # Check if guess is in the word
        if guess in chosen_word:
            print(f"Good guess! '{guess}' is in the word.")
            # Update word display
            for i, letter in enumerate(chosen_word):
                if letter == guess:
                    word_display[i] = letter
        else:
            lives -= 1
            incorrect_letters.add(guess)
            print(f"Sorry, '{guess}' is not in the word.")
            if lives > 0:
                print(
                    f"You have {lives} {'life' if lives == 1 else 'lives'} left.")

    # Game over
    print("\n" + "="*50)
    if '_' not in word_display:
        print("🎉 CONGRATULATIONS! YOU WON! 🎉")
        print(f"The word was: {chosen_word.upper()}")
        print(
            f"You solved it with {lives} {'life' if lives == 1 else 'lives'} remaining!")
    else:
        print(display_hangman(0))
        print("💀 GAME OVER! YOU LOST! 💀")
        print(f"The word was: {chosen_word.upper()}")
    print("="*50)

    return play_again()


def play_again():
    """Ask if player wants to play again"""
    while True:
        choice = input(
            "\nWould you like to play again? (yes/no): ").lower().strip()
        if choice in ['yes', 'y']:
            return True
        elif choice in ['no', 'n']:
            print("\nThanks for playing! Goodbye!")
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def main():
    """Main program entry point"""
    while play_hangman():
        pass


if __name__ == "__main__":
    main()
