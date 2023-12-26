import random
from time import sleep

# variables that stores words used for the different lists
words_easy = ['boo', 'toad', 'luna', 'bow',]
words_medium = ['luigi', 'kamek', 'peach', 'yoshi', 'mario', 'bowser',
                'goomba', 'lakitu',]
words_hard = ['rosalina', 'polterpup', 'wiggler', 'waluigi',
              'blooper',]

# variables that randomizes a word from the different lists
random_word_easy = random.choice(words_easy)
random_word_medium = random.choice(words_medium)
random_word_hard = random.choice(words_hard)

# variables that will store the correct and wrong guesses
correct_guess = ['_'] * len(random_word_easy or random_word_medium
                            or random_word_hard)
wrong_guess = []

# function that adds waiting time


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


# function to show how many tries the user got
# left before the game is over

def lifes(y):
    if y == 0:
        print('♥ ♥ ♥ ♥ ♥ ♥')        
    if y == 1:
        print('♥ ♥ ♥ ♥ ♥ ♡')     
    if y == 2:
        print('♥ ♥ ♥ ♥ ♡ ♡')     
    if y == 3:
        print('♥ ♥ ♥ ♡ ♡ ♡')     
    if y == 4:
        print('♥ ♥ ♡ ♡ ♡ ♡')  
    if y == 5:
        print('♥ ♡ ♡ ♡ ♡ ♡')   
    if y == 6:
        print('♡ ♡ ♡ ♡ ♡ ♡')


# print out word by word


def print_word_by_word(text, delay=0.1):
    words = text.split()
    for word in words:
        print(word, end=' ', flush=True)
        sleep(delay)
    print()

# print out letter by letter


def print_letter_by_letter(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print()

# prints out the initial strings when the game starts


while True:
    print('')
    print_letter_by_letter('Hi and welcome to')
    print_letter_by_letter('')

    print_word_by_word('██╗░░██╗░█████╗░███╗░░██╗░██████╗'
                       '░███╗░░░███╗░█████╗░███╗░░██╗')
    print_word_by_word('██║░░██║██╔══██╗████╗░██║██╔════╝'
                       '░████╗░████║██╔══██╗████╗░██║')
    print_word_by_word('███████║███████║██╔██╗██║██║░░██╗'
                       '░██╔████╔██║███████║██╔██╗██║')
    print_word_by_word('██╔══██║██╔══██║██║╚████║██║░░╚██╗'
                       '██║╚██╔╝██║██╔══██║██║╚████║')
    print_word_by_word('██║░░██║██║░░██║██║░╚███║╚██████╔╝'
                       '██║░╚═╝░██║██║░░██║██║░╚███║')
    print_word_by_word('╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░'
                       '╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝')
    print_word_by_word('')
    print_word_by_word('░██████╗██╗░░░██╗██████╗░███████╗██████╗░'
                       '███╗░░░███╗░█████╗░██████╗░██╗░█████╗░')
    print_word_by_word('██╔════╝██║░░░██║██╔══██╗██╔════╝██╔══██╗'
                       '████╗░████║██╔══██╗██╔══██╗██║██╔══██╗')
    print_word_by_word('╚█████╗░██║░░░██║██████╔╝█████╗░░██████╔╝'
                       '██╔████╔██║███████║██████╔╝██║██║░░██║')
    print_word_by_word('░╚═══██╗██║░░░██║██╔═══╝░██╔══╝░░██╔══██╗'
                       '██║╚██╔╝██║██╔══██║██╔══██╗██║██║░░██║')
    print_word_by_word('██████╔╝╚██████╔╝██║░░░░░███████╗██║░░██║'
                       '██║░╚═╝░██║██║░░██║██║░░██║██║╚█████╔╝')
    print_word_by_word('╚═════╝░░╚═════╝░╚═╝░░░░░╚══════╝╚═╝░░╚═╝'
                       '╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░╚════╝░')
    print_word_by_word('')
    print_word_by_word('███████╗██████╗░██╗████████╗██╗░█████╗░███╗░░██╗')
    print_word_by_word('██╔════╝██╔══██╗██║╚══██╔══╝██║██╔══██╗████╗░██║')
    print_word_by_word('█████╗░░██║░░██║██║░░░██║░░░██║██║░░██║██╔██╗██║')
    print_word_by_word('██╔══╝░░██║░░██║██║░░░██║░░░██║██║░░██║██║╚████║')
    print_word_by_word('███████╗██████╔╝██║░░░██║░░░██║╚█████╔╝██║░╚███║')
    print_word_by_word('╚══════╝╚═════╝░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝')
    print_letter_by_letter('')
    print_letter_by_letter('   ',  '------')
    print_letter_by_letter('   ',  '|    |')
    print_letter_by_letter('   ',  '|     ')
    print_letter_by_letter('   ',  '|     ')
    print_letter_by_letter('   ',  '|     ')
    print_letter_by_letter('   ',  '|     ')
    print_letter_by_letter('--------------')
    print_letter_by_letter('')
    print_letter_by_letter('The category is different characters from the'
                           'Super Mario games.')
    print_letter_by_letter('')
    print_letter_by_letter('You got 3 different difficulties to choose from:')
    print_letter_by_letter('Easy, medium and hard.')
    print_letter_by_letter('')
    print_letter_by_letter('The easy difficulty got up til 4 letters.')
    print_letter_by_letter('The medium difficulty got up til 6 letters.')
    print_letter_by_letter('And the hard difficulty got up til 9 letters.')
    print_letter_by_letter('')
    print_letter_by_letter('HOW TO PLAY:')
    print_letter_by_letter('To guess a letter or choose a input')
    print_letter_by_letter('just write the letter or word directly in the' 
                           'terminal')
    print_letter_by_letter('and press ENTER')
    print_letter_by_letter('')
    print_letter_by_letter('You got 6 tries to guess the correct word.')
    print_letter_by_letter('Good luck!')

    # functions that shows how many letters the choosen word have
    def update_correct_letters(correct_guess):
        for letter in correct_guess:
            print(letter, end=' ')
        print()

    # function that starts the hangman game
    def play_game(random_word):
        # prints out how many letters the choosen word has
        print('The word has', len(random_word), 'letters')
        print('')

        # Initialize variables at the beginning
        wrong_guess = []
        correct_guess = ['_'] * len(random_word)
        doRunGame = True

        while doRunGame:
            # prints the string below between the guessed letters
            print("=================================")

            # variable for the guess the user will choose
            print('')
            guess = input("Guess a letter: \n")

            # Check if the guessed input is more than one letter
            if len(guess) == 1:

                # checks if the guessed letter is on the choosen word
                # and puts it in the correct guess index if true
                if guess in correct_guess:
                    print('You already guessed that')
                elif guess in random_word:
                    # prints out the lifes
                    print('')
                    lifes(len(wrong_guess))
                    print('')
                    index = 0
                    for i in random_word:
                        if i == guess:
                            correct_guess[index] = guess
                        index += 1
                    hangman_parts(len(wrong_guess))
                    update_correct_letters(correct_guess)
                # checks if the guessed letter already is guessed or not
                # either prints out more of the hangman if the guess is wrong
                # print out that the user has used that
                # letter already if the letter is already used
                else:
                    if guess in wrong_guess:
                        print('You already guessed that')
                    elif guess not in wrong_guess:
                        wrong_guess.append(guess)
                        print('')
                        lifes(len(wrong_guess))
                        print('')
                        hangman_parts(len(wrong_guess))
                        update_correct_letters(correct_guess)
                    # prints out if the user guessed a wrong letter
                    print('')
                    print(f'Wrong letter {wrong_guess}')
            else:
                print("Please guess only one letter at a time.")
            # checks if the wrong guesses is more then 5
            # then prints the losing statement
            if len(wrong_guess) > 5:
                print(f'The correct word was {random_word}')
                print()
                print('█▄█ █▀█ █░█  █░░ █▀█ █▀ █▀▀ █')
                print('░█░ █▄█ █▄█  █▄▄ █▄█ ▄█ ██▄ ▄')
                print('')
                print('█▀▀ ▄▀█ █▀▄▀█ █▀▀  █▀█ █░█ █▀▀ █▀█ ░')
                print('█▄█ █▀█ █░▀░█ ██▄  █▄█ ▀▄▀ ██▄ █▀▄ ▄')
                print('')
                while True:
                    play_again = input("Do you want to play again?" 
                                       "(yes/no):\n")
                    if play_again == 'yes':
                        doRunGame = False
                        break  # Start a new game with a new difficulty
                    elif play_again == 'no':
                        print("Thanks for playing. Goodbye!")
                        exit()
                    else:
                        print("Invalid answer.")

            if '_' not in correct_guess:
                print('')
                print('█▄█ █▀█ █░█  █░█░█ █▀█ █▄░█ █')
                print('░█░ █▄█ █▄█  ▀▄▀▄▀ █▄█ █░▀█ ▄')
                print('')

                print('█▀▀ █▀█ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █░█'
                      '█░░ ▄▀█ ▀█▀ █ █▀█ █▄░█ █▀')
                print('█▄▄ █▄█ █░▀█ █▄█ █▀▄ █▀█ ░█░ █▄█'
                      '█▄▄ █▀█ ░█░ █ █▄█ █░▀█ ▄█')
                print('')
                while True:
                    play_again = input("Do you want to play again?"
                                       "(yes/no): \n")
                    if play_again == 'yes':
                        doRunGame = False
                        break  # Start a new game with a new difficulty
                    elif play_again == 'no':
                        print("Thanks for playing. Goodbye!")
                        exit()
                    else:
                        print("Invalid answer.")    
    # main game loop
    # Check if the entered difficulty is valid
    while True:

        difficulty = input("Please choose a degree of difficulty ('easy',"
                           "'medium', or 'hard'): \n")
        if difficulty == 'easy':
            # variable that randomizes a word from the easy list
            random_word_easy = random.choice(words_easy)
            # variable that adds the randomized word to the random_word var
            random_word = random_word_easy
            print('')
            print(f'Let me think of a {difficulty} word...')
            waiting_time()
            play_game(random_word)
        elif difficulty == 'medium':
            # variable that randomizes a word from the medium list
            random_word_medium = random.choice(words_medium)
            # variable that adds the randomized word to the random_word var
            random_word = random_word_medium
            print('')
            print(f'Let me think of a {difficulty} word...')
            waiting_time()
            play_game(random_word)
        elif difficulty == 'hard':
            # variable that randomizes a word from the hard list
            random_word_hard = random.choice(words_hard)
            # variable that adds the randomized word to the random_word var
            random_word = random_word_hard
            print('')
            print(f'Let me think of a {difficulty} word...')
            waiting_time()
            play_game(random_word)
        else:
            print("Invalid difficulty.")
