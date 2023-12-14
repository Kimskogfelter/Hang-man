# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

# variables that stores words used for the different lists
words_easy = ['cat', 'dog', 'bear', 'lion', 'hat',]
words_medium = ['pizza', 'tiger', 'zebra',]
words_hard = ['hippopotamus', 'hamburger', 'spaceship', 'kindergarden',]

# variables that randomizes a word from the different lists
random_word_easy = random.choice(words_easy)
random_word_medium = random.choice(words_medium)
random_word_hard = random.choice(words_hard)

# variables that will store the correct and wrong guesses
correct_guess = []
wrong_guess = []

''' loop that will check if the guess letter is correct or not and
continue until the word is complete or the man is hanged '''
while True:
    # variable for the guess the user will choose
    guess = input("Guess a letter: ")

    # checks if the guessed letter is on the choosen word
    if guess in random_word_easy:
        correct_guess.append(guess)
        print(correct_guess)
    else:
        wrong_guess.append(guess)
        print(wrong_guess)
