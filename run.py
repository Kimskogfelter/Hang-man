# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from time import sleep

# variables that stores words used for the different lists
words_easy = ['cat', 'dog', 'bear', 'lion', 'hat',]
words_medium = ['pizza', 'tiger', 'zebra',]
words_hard = ['hippopotamus', 'hamburger', 'spaceship', 'kindergarden',]

# variables that randomizes a word from the different lists
random_word_easy = random.choice(words_easy)
random_word_medium = random.choice(words_medium)
random_word_hard = random.choice(words_hard)

# variables that will store the correct and wrong guesses
correct_guess_easy = ['_'] * len(random_word_easy)
correct_guess_medium = ['_'] * len(random_word_medium)
correct_guess_hard = ['_'] * len(random_word_hard)
wrong_guess = []

# function that makes the user wait between choices


def waiting_time():
    for i in range(5):
        print('.', end="")
        sleep(.5)
    print()

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


# functions that shows how many letters the choosen word have
def update_correct_letters_easy():
    for i in correct_guess_easy:
        print(i, end=' ')
    print()


def update_correct_letters_medium():
    for i in correct_guess_medium:
        print(i, end=' ')
    print()


def update_correct_letters_hard():
    for i in correct_guess_hard:
        print(i, end=' ')
    print()


# main function for EASY difficulty
def easy_difficulty():
    # prints out how many letters the choosen word has
    print('The word has', len(random_word_easy), 'letters')

    while True:

        # shows how many letters the word has
        update_correct_letters_easy()
       

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
                    correct_guess_easy[index] = guess
                index += 1
            hangman_parts(len(wrong_guess))
            update_correct_letters_easy()
        # checks if the guessed letter already is guessed or not
        # either prints out more of the hangman if the guess is wrong
        # print out that the user has used that
        # letter already if the letter is already used
        else:
            if guess not in wrong_guess:
                wrong_guess.append(guess)
                hangman_parts(len(wrong_guess))
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
        # prints the winning statement
        if '_' not in correct_guess_easy:
            print('You won!')
            break

# main function for MEDIUM difficulty


def medium_difficulty():
    # prints out how many letters the choosen word has
    print('The word has', len(random_word_medium), 'letters')

    while True:
        # shows how many letters the word has
        update_correct_letters_medium()
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('--------------')

        # prints the string below between the guessed letters
        print("-----------------------------")

        # variable for the guess the user will choose
        guess = input("Guess a letter: ")

        # checks if the guessed letter is on the choosen word
        # and puts it in the correct guess index if true
        if guess in random_word_medium:
            index = 0
            for i in random_word_medium:
                if i == guess:
                    correct_guess_medium[index] = guess
                index += 1
            hangman_parts(len(wrong_guess))
            update_correct_letters_medium()
        # checks if the guessed letter already is guessed or not
        # either prints out more of the hangman if the guess is wrong
        # print out that the user has used that
        # letter already if the letter is already used
        else:
            if guess not in wrong_guess:
                wrong_guess.append(guess)
                hangman_parts(len(wrong_guess))
            else:
                print('You already guessed that')
            # prints out if the user guessed a wrong letter
            print(f'You guessed the wrong letter{wrong_guess}')
        # checks if the wrong guesses is more then 5
        # then prints the losing statement
        if len(wrong_guess) > 5:
            print('Game Over. You lose!')
            print(f'The correct word was {random_word_medium}')
            break
        # prints the winning statement
        if '_' not in correct_guess_medium:
            print('You won! Congratulations!')
            break

# main function for HARD difficulty


def hard_difficulty():
    # prints out how many letters the choosen word has
    print('The word has', len(random_word_hard), 'letters')

    while True:

        # shows how many letters the word has
        update_correct_letters_hard()
        print('   ',  '------')
        print('   ',  '|    |')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('   ',  '|     ')
        print('--------------')

        # prints the string below between the guessed letters
        print("-----------------------------")

        # variable for the guess the user will choose
        guess = input("Guess a letter: ")

        # checks if the guessed letter is on the choosen word
        # and puts it in the correct guess index if true
        if guess in random_word_hard:
            index = 0
            for i in random_word_hard:
                if i == guess:
                    correct_guess_hard[index] = guess
                index += 1
            hangman_parts(len(wrong_guess))
            update_correct_letters_hard()
        # checks if the guessed letter already is guessed or not
        # either prints out more of the hangman if the guess is wrong
        # print out that the user has used that
        # letter already if the letter is already used
        else:
            if guess not in wrong_guess:
                wrong_guess.append(guess)
                hangman_parts(len(wrong_guess))
            else:
                print('You already guessed that')
            # prints out if the user guessed a wrong letter
            print(f'You guessed the wrong letter{wrong_guess}')
        # checks if the wrong guesses is more then 5
        # then prints the losing statement
        if len(wrong_guess) > 5:
            print('Game Over. You lose!')
            print(f'The correct word was {random_word_hard}')
            break
        # prints the winning statement
        if '_' not in correct_guess_hard:
            print('You won! Congratulations!')
            break


# prints out the initial strings when the game starts
print('Hi and welcome to hangman.')
print('You got 3 different difficulties to choose from:')
print('Easy, medium and hard.')
print('You got 6 tries to guess the correct word.')
print('   ',  '------')
print('   ',  '|    |')
print('   ',  '|     ')
print('   ',  '|     ')
print('   ',  '|     ')
print('   ',  '|     ')
print('--------------')
# Ask the user to choose a difficulty
difficulty = input("Please choose a degree of difficulty "
                   "('easy', 'medium', or 'hard'): ")

# Map difficulty names to their corresponding functions
difficulty_functions = {
    'easy': easy_difficulty,
    'medium': medium_difficulty,
    'hard': hard_difficulty
}

# Check if the entered difficulty is valid
chosen_difficulty_function = difficulty_functions.get(difficulty)
if chosen_difficulty_function:
    print(f'Let me think of a {difficulty} word...')
    waiting_time()
    chosen_difficulty_function()  # Call the chosen difficulty function
else:
    print("Invalid difficulty.")
    print("Please choose either 'easy', 'medium', or 'hard'.")


