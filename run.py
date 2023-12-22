import random
from time import sleep

# variables that stores words used for the different lists
words_easy = ['boo', 'toad', 'luna', 'bow',]
words_medium = ['lakitu', 'luigi', 'kamek', 'peach', 'yoshi', 'mario',
                'bowser', 'goomba']
words_hard = ['rosalina', 'polterpup', 'wiggler', 'waluigi',
              'blooper',]

# variables that randomizes a word from the different lists
random_word_easy = random.choice(words_easy)
random_word_medium = random.choice(words_medium)
random_word_hard = random.choice(words_hard)

# variables that will store the correct and wrong guesses
correct_guess = ['_'] * len(random_word_easy, random_word_medium, \ 
                            random_word_hard)
wrong_guess = []


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

# main game loop
# prints out the initial strings when the game starts


while True:
    print('')
    print('Hi and welcome to')
    print('')

    print('██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗')
    print('██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║')
    print('███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║')
    print('██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║')
    print('██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║')
    print('╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝')
    print('')
    print('░██████╗██╗░░░██╗██████╗░███████╗██████╗░'
          '███╗░░░███╗░█████╗░██████╗░██╗░█████╗░')
    print('██╔════╝██║░░░██║██╔══██╗██╔════╝██╔══██╗'
          '████╗░████║██╔══██╗██╔══██╗██║██╔══██╗')
    print('╚█████╗░██║░░░██║██████╔╝█████╗░░██████╔╝'
          '██╔████╔██║███████║██████╔╝██║██║░░██║')
    print('░╚═══██╗██║░░░██║██╔═══╝░██╔══╝░░██╔══██╗'
          '██║╚██╔╝██║██╔══██║██╔══██╗██║██║░░██║')
    print('██████╔╝╚██████╔╝██║░░░░░███████╗██║░░██║'
          '██║░╚═╝░██║██║░░██║██║░░██║██║╚█████╔╝')
    print('╚═════╝░░╚═════╝░╚═╝░░░░░╚══════╝╚═╝░░╚═╝'
          '╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░╚════╝░')
    print('')
    print('███████╗██████╗░██╗████████╗██╗░█████╗░███╗░░██╗')
    print('██╔════╝██╔══██╗██║╚══██╔══╝██║██╔══██╗████╗░██║')
    print('█████╗░░██║░░██║██║░░░██║░░░██║██║░░██║██╔██╗██║')
    print('██╔══╝░░██║░░██║██║░░░██║░░░██║██║░░██║██║╚████║')
    print('███████╗██████╔╝██║░░░██║░░░██║╚█████╔╝██║░╚███║')
    print('╚══════╝╚═════╝░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝')
    print('')
    print('   ',  '------')
    print('   ',  '|    |')
    print('   ',  '|     ')
    print('   ',  '|     ')
    print('   ',  '|     ')
    print('   ',  '|     ')
    print('--------------')
    print('')
    print('The category is different characters from the Super Mario games.')
    print('')
    print('You got 3 different difficulties to choose from:')
    print('Easy, medium and hard.')
    print('')
    print('The easy difficulty got up til 4 letters.')
    print('The medium difficulty got up til 6 letters.')
    print('And the hard difficulty got up til 9 letters.')
    print('')
    print('You got 6 tries to guess the correct word.')

    # functions that shows how many letters the choosen word have
    def update_correct_letters(correct_guess):
        for letter in correct_guess:
            print(letter, end=' ')
        print()

    # function that starts the hangman game
    def play_game(random_word_easy, random_word_medium, random_word_hard):
        # prints out how many letters the choosen word has
        print('The word has', len(random_word_easy, random_word_medium, \ 
                                  random_word_hard), 'letters')
        print('')

        # Initialize variables at the beginning
        wrong_guess = []
        correct_guess = ['_'] * len(random_word_easy, random_word_medium, \
                                    random_word_hard)
        doRunGame = True

        while doRunGame:  
            # prints the string below between the guessed letters
            print("=================================")

            # variable for the guess the user will choose
            print('')
            guess = input("Guess a letter: ")

            # Check if the guessed input is more than one letter
            if len(guess) == 1:

                # checks if the guessed letter is on the choosen word
                # and puts it in the correct guess index if true
                if guess in random_word_easy, random_word_medium, \ 
                            random_word_hard:
                    # prints out the lifes
                    print('')
                    lifes(len(wrong_guess))
                    print('')
                    index = 0
                    for i in random_word_easy, random_word_medium, random_word_hard:
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
                    if guess not in wrong_guess:
                        wrong_guess.append(guess)
                        print('')
                        lifes(len(wrong_guess))
                        print('')
                        hangman_parts(len(wrong_guess))
                        update_correct_letters(correct_guess)
                    else:
                        print('You already guessed that')
                    # prints out if the user guessed a wrong letter
                    print('')
                    print(f'Wrong letter {wrong_guess}')
            else:
                print("Please guess only one letter at a time.")
            # checks if the wrong guesses is more then 5
            # then prints the losing statement
            if len(wrong_guess) > 5:
                print(f'The correct word was {random_word_easy,
                      random_word_medium, random_word_hard}')
                print()
                print('█▄█ █▀█ █░█  █░░ █▀█ █▀ █▀▀ █') 
                print('░█░ █▄█ █▄█  █▄▄ █▄█ ▄█ ██▄ ▄') 
                print('')
                print('█▀▀ ▄▀█ █▀▄▀█ █▀▀  █▀█ █░█ █▀▀ █▀█ ░')
                print('█▄█ █▀█ █░▀░█ ██▄  █▄█ ▀▄▀ ██▄ █▀▄ ▄')
                print('')
                play_again = input("Do you want to play again? (yes/no): ")
                if play_again == 'yes':
                    doRunGame = False
                    continue  # Start a new game with a new difficulty
                else:
                    print("Thanks for playing. Goodbye!")
                    exit()

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
                play_again = input("Do you want to play again? (yes/no): ")
                if play_again == 'yes':
                    doRunGame = False
                    continue  # Start a new game with a new difficulty
                else:
                    print("Thanks for playing. Goodbye!")
                    exit()

# Main game loop
# Check if the entered difficulty is valid
while True:
    difficulty = input("Please choose a degree of difficulty "
                       "('easy', 'medium', or 'hard'): ")

    if difficulty in ('easy', 'medium', 'hard'):
        print('')
        print(f'Let me think of a {difficulty} word...')
        waiting_time()

        if difficulty == 'easy':
            play_game(random_word_easy)
        elif difficulty == 'medium':
            play_game(random_word_medium)
        elif difficulty == 'hard':
            play_game(random_word_hard)
       
        break  # Exit the loop if a valid difficulty is provided
    else:
        print("Invalid difficulty.")
