""" The random module help us choose a random word from a list of words
and the sys module helps us in exiting the program """
import random
import sys

words_list = ['python', 'code', 'tech', 'programming', 'love', 'hate', 'passion']
chosen_word = random.choice(words_list)
print(chosen_word)

correct_word = []
for _ in chosen_word:
    correct_word.append('_')
print(' '.join(correct_word))

LIVES = 6

while True:
    guess = input("Guess a letter: ")

    if guess in correct_word:
        print("You have already guessed this letter.")
        LIVES -= 1

    if guess not in chosen_word:
        LIVES -= 1
        print("You guessed a wrong letter.")

    for index in range(len(correct_word)):
        letter = chosen_word[index]

        if letter == guess:
            correct_word[index] = letter
    print(' '.join(correct_word))

    if LIVES == 0:
        sys.exit("You Lose.")
    if '_' not in correct_word:
        sys.exit("You Win.")
