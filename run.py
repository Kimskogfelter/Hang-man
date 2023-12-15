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

# variables for the different difficulties
Easy = random_word_easy
Medium = random_word_medium
Hard = random_word_hard

# prints out the initial strings when the game starts
print('Hi and welcome to hangman.')
print('You got 3 different difficulties to choose from:')
print('Easy, Medium and Hard.')
print('You got 6 tries to guess the correct word.')
print('   ',  '------')
print('   ',  '|    |')
print('   ',  '|     ')
print('   ',  '|     ')
print('   ',  '|     ')
print('   ',  '|     ')
print('--------------')
difficulty = input("Please choose a degree of difficulty: ")

# function that makes the user wait between choices
def waiting_time():
    for i in range(5):
        print('.', end="")
        sleep(.5)
    print()

waiting_time()

# prints out how many letters the choosen word has
print('The word has', len(random_word_easy), 'letters')

# variables that will store the correct and wrong guesses
correct_guess_easy = ['_'] * len(random_word_easy)
correct_guess_medium = ['_'] * len(random_word_medium)
correct_guess_hard = ['_'] * len(random_word_hard)
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
    for i in correct_guess_easy:
        print(i, end=' ')
    print()

update_correct_letters()


''' loop that will check if the guess letter is correct or not and
continue until the word is complete or the man is hanged '''
# main loop for EASY difficulty
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
                correct_guess_easy[index] = guess
            index += 1
        update_correct_letters()
        hangman_parts(len(wrong_guess))
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
    # checks if all the letters are correct and prints the winning statement
    if '_' not in correct_guess_easy:
        print('You won!')
        break

# main loop for MEDIUM difficulty
while True:

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
        update_correct_letters()
        hangman_parts(len(wrong_guess))
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
    # checks if all the letters are correct and prints the winning statement
    if '_' not in correct_guess_medium:
        print('You won! Congratulations!')
        break

# main loop for HARD difficulty
while True:

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
        update_correct_letters()
        hangman_parts(len(wrong_guess))
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
    # checks if all the letters are correct and prints the winning statement
    if '_' not in correct_guess_hard:
        print('You won! Congratulations!')
        break
