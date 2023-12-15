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

# prints out how many letters the choosen word has
print('The word has', len(random_word_easy), 'letters')

# variables that will store the correct and wrong guesses
correct_guess = ['_'] * len(random_word_easy)
wrong_guess = []

# function that prints out the different parts of the hang man
# when the user guesses a wrong letter
def hangman_parts(x):
    if x == 0:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('--------------')
    if x == 1:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|    O')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('--------------')
    if x == 2:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|    O')
        print('   ',  '|   -|')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('--------------')
    if x == 3:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|    O')
        print('   ',  '|   -|-')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('--------------')
    if x == 4:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|    O')
        print('   ',  '|   -|-')
        print('   ',  '|    |')
        print('   ',  '|     ')
        print('--------------')
    if x == 5:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|    O')
        print('   ',  '|   -|-')
        print('   ',  '|    |')
        print('   ',  '|   / ')
        print('--------------')
    if x == 6:
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|    O')
        print('   ',  '|   -|-')
        print('   ',  '|    |')
        print('   ',  '|   / \\')
        print('---------------')


# function that shows how many letters the choosen word
def update_correct_letters():
    for i in correct_guess:
        print(i, end=' ')
    print()


update_correct_letters()

''' loop that will check if the guess letter is correct or not and
continue until the word is complete or the man is hanged '''
while True:

    # prints the string below between the guessed letters
    print("-----------------------------")

    # variable for the guess the user will choose
    guess = input("Guess a letter: ")

    # checks if the guessed letter is on the choosen word
    # and puts it in the correct guess index if true
    if guess in random_word_easy:
        index = 0
        for i in random_word_easy:
            if i == guess:
                correct_guess[index] = guess
            index += 1
        update_correct_letters()
    # checks if the guessed letter already is guessed
    else:
        if guess not in wrong_guess:
            wrong_guess.append(guess)
        else:
            print('You already guessed that')
        # prints out if the user guessed a wrong letter
        print(f'You guessed the wrong letter{wrong_guess}')
    # checks if the wrong guesses is more then 5
    # then prints the losing statement
    if len(wrong_guess) > 5:
        print('You lose!')
        print(f'The correct word was {random_word_easy}')
        break
    # checks if all the letters are correct and prints the winning statement
    if '_' not in correct_guess:
        print('You won!')
        break
