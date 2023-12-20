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
    for letter in correct_guess_hard:
        print(letter, end=' ')
    print()


# main function for EASY difficulty
def easy_difficulty():
    # prints out how many letters the choosen word has
    print('The word has', len(random_word_easy), 'letters')

    while True:   
        # prints the string below between the guessed letters
        print("==========================")

        # variable for the guess the user will choose
        guess = input("Guess a letter: ")

        # Check if the guessed input is more than one letter
        if len(guess) == 1:

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
                    update_correct_letters_easy()
                else:
                    print('You already guessed that')
                # prints out if the user guessed a wrong letter
                print(f'Wrong letter {wrong_guess}')
        else:
            print("Please guess only one letter at a time.")
        # checks if the wrong guesses is more then 5
        # then prints the losing statement
        if len(wrong_guess) > 5:
            print(f'The correct word was {random_word_easy}')
            print('Game Over. You lose!')
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
        # prints the string below between the guessed letters
        print("==========================")

        # variable for the guess the user will choose
        guess = input("Guess a letter: ")

        # Check if the guessed input is more than one letter
        if len(guess) == 1:

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
                    update_correct_letters_medium()
                else:
                    print('You already guessed that')
                # prints out if the user guessed a wrong letter
                print(f'Wrong letter {wrong_guess}')
        else:
            print("Please guess only one letter at a time.")
        # checks if the wrong guesses is more then 5
        # then prints the losing statement
        if len(wrong_guess) > 5:
            print(f'The correct word was {random_word_medium}')
            print('Game Over. You lose!')
            break
        # prints the winning statement
        if '_' not in correct_guess_medium:
            print('You won! Congratulations!')
            break

# main function for HARD difficulty


def hard_difficulty():
    # prints out how many letters the chosen word has
    print('The word has', len(random_word_hard), 'letters')

    # Initialize variables at the beginning
    wrong_guess = []
    correct_guess_hard = ['_'] * len(random_word_hard)

    while True:      
        # prints the string below between the guessed letters
        print("==========================")

        # variable for the guess the user will choose
        guess = input("Guess a letter: ")

        # Check if the guessed input is more than one letter
        if len(guess) == 1:

            # checks if the guessed letter is on the chosen word
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
                    update_correct_letters_hard()
                else:
                    print('You already guessed that')
                # prints out if the user guessed a wrong letter
                print(f'Wrong letter {wrong_guess}')
        else:
            print("Please guess only one letter at a time.")
        # checks if the wrong guesses are more than 5
        # then prints the losing statement
        if len(wrong_guess) > 5:
            print(f'The correct word was {random_word_hard}')
            print('Game Over. You lose!')
            break
        if '_' not in correct_guess_hard:
            print('You won! Congratulations!')
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again == 'yes':
                # Reset variables for a new game
                correct_guess_hard = ['_'] * len(random_word_hard)
                wrong_guess = []
                # ... (any other variables you need to reset)
                continue  # Start a new game
            else:
                print("Thanks for playing. Goodbye!")
                break  # Exit the loop


# prints out the initial strings when the game starts
print('Hi and welcome to')
print('')

print('██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗')
print('██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║')
print('███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║')
print('██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║')
print('██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║')
print('╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝')
print('')
print('   ',  '------')
print('   ',  '|    |')
print('   ',  '|     ')
print('   ',  '|     ')
print('   ',  '|     ')
print('   ',  '|     ')
print('--------------')
print('')
print('You got 3 different difficulties to choose from:')
print('Easy, medium and hard.')
print('')
print('You got 6 tries to guess the correct word.')

# Map difficulty names to their corresponding functions
difficulty_functions = {
    'easy': easy_difficulty,
    'medium': medium_difficulty,
    'hard': hard_difficulty
}

# Check if the entered difficulty is valid
while True:
    difficulty = input("Please choose a degree of difficulty "
                        "('easy', 'medium', or 'hard'): ")

    chosen_difficulty_function = difficulty_functions.get(difficulty)

    if chosen_difficulty_function:
        print(f'Let me think of a {difficulty} word...')
        waiting_time()
        chosen_difficulty_function()  # Call the chosen difficulty function
        break  # Exit the loop if a valid difficulty is provided
    else:
        print("Invalid difficulty.")
