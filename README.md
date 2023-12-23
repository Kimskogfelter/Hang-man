![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

# Welcome to my third project

## HANGMAN 

![picture of the mockup of the website](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/mockup-supermario.webp)

### PURPOSE

---

When I searched online for inspiration on what to make for my third project I wanted it to be something that most people recognize and understand. 
I love games myself so I knew that I wanted to make some kind of game. When I finally saw that you could make hangman with python I knew that this was the game I wanted to make. I loved to play hangman as a kid during breaks on the whiteboard in the classroom. 

---

### HOW TO PLAY

My hangman has 3 different degrees of difficulty, easy, medium and hard. The player then get 6 lives/attemps to try and guess the correct word that the computer randomizes from lists that I have made.  
The choosen word are shown with "_" for each letter. The game also tells the user how many letter the word has in the beginning after the difficulty level is selected.
The lifes are shown as hearts above the hangman picture. So the player easy can see how many tries he/she got left before the game ends. The player wins the gamer if he/she can guess the correct word without losing all the lifes. The players lose if all lifes are lost. When the game is over the player can choose if they want to plat again or not. If they choose to play again the game restart from where the player can choose the difficulty level. If they choose not to play again the game ends. 

### FEATURES

---

#### DIFFICULTY LEVELS

- The game got 3 different difficulties that the user can choose from in the beginning of the game. Easy, medium and hard. The easy difficulty got up to 4 letters in the choosen word, the medium got up to 6 letters and the hard got up to 9 letters. 

![picture of the part where the user choose the difficulty level](https://raw.githubusercontent.com/Kimskogfelter/Hangman/main/assets/images/readme/choose-degree-of-difficulty.webp)

#### SHOWING LIFES

- The player got 6 tries to guess the correct word. That is shown as hearts above the picture of the hangman so the player easy can see how many tries he/she got left before they lose. 

![picture of the hearts that shows how many lifes the player got left](https://raw.githubusercontent.com/Kimskogfelter/Hangman/main/assets/images/readme/showing-lifes.webp)

#### INPUT VALIDATION

- #### CHOOSEN DIFFICULTY INPUT
    - Here the game checks if the choosen difficulty level is correct. If the player has written something else then easy, medium or hard they get a message that tells them that its invalid and they need to choose either easy, medium or hard.

![picture of the message that comes when the player write something else then easy, medium or hard when choosing a difficulty](https://raw.githubusercontent.com/Kimskogfelter/Hangman/main/assets/images/readme/choose-degree-of-difficulty-invalid-message.webp)

- #### GUESS A LETTER INPUT
    - When the player is going to guess a letter the game checks for several things. The first thing it checks if its the player only guessed one letter. If he/she guessed more then one letter the game shows a message that they need to guess at one letter at a time. 

![picture of the message that comes when the player guess more then one letter](https://raw.githubusercontent.com/Kimskogfelter/Hangman/main/assets/images/readme/guessing-more-then-one-letter-message.webp)

    - The second thing the game checks is if the letter is correct or not. If the letter is correct it gets printed out so the player can see where the correct letter is in the choosen word.

![picture that shows where the correct letters are shown in the game](https://raw.githubusercontent.com/Kimskogfelter/Hangman/main/assets/images/readme/correct-guessed-letters.webp)

    - If the guessed letter is wrong the player gets a message that says wrong letter and then shows the letter next to it. Each time the player guess a wrong letter that letter gets printed out next to the text wrong letter. In that way the player can keep track on which letter they already has guessed that are wrong.

![picture that shows the "wrong letter" message](https://raw.githubusercontent.com/Kimskogfelter/Hangman/main/assets/images/readme/wrong-letters.webp)

    - The third thing the game checks is if the guessed letter already has been guessed. If its already been guessed the player get a message that says "You already guessed that"

![picture that shows the message that pops up if the player already has guessed a letter they choose to guess](https://raw.githubusercontent.com/Kimskogfelter/Hangman/main/assets/images/readme/you-already-guessed-that-message.webp)

- #### PLAY AGAIN INPUT

    - When the player wins or loses the game he/she get to choose if they want to play again or not. The game then checks if the input the player has choosen is either "yes" or "no". If "yes" the game restarts from where the player get to choose a new difficulty level. 

![picture that shows the message that pops up if the player want to restart the game](https://raw.githubusercontent.com/Kimskogfelter/Hangman/main/assets/images/readme/do-you-want-to-play-again-yes.webp)

    - If the player choose "no" the game ends. 

![picture that shows the message that pops up if the player want to end the game](https://raw.githubusercontent.com/Kimskogfelter/Hangman/main/assets/images/readme/do-you-want-to-play-again-no.webp)

    - If the player write something else then "yes" or "no" a message pop up saying that the message is invalid. And then asks them again if they want to play again, and to choose either "yes" or "no"

![picture that shows the message that pops up if the player write a invalid input](https://raw.githubusercontent.com/Kimskogfelter/Hangman/main/assets/images/readme/do-you-want-to-play-again-invalid-answer.webp)

#### DATA MODEL
- The game uses arrays to store the different words which are used for the different difficulties. It also stores the correct and wrong guess in a temporary array. The correct guess array stores the correct letters that the player has guessed, and the wrong guess array stores all the wrong letters who then prints out to the player during the game. When the correct array no longer has any "_" in it the player wins and the win statement is printed out. If the player fails to guess the correct word for 6 tries the losing statement is printed. The 6 tries is stored on the wrong guess array. If the player choose to play again when the game is over the array for the choosen word randomizes a new word through a random.choice generator. So the user dont have to guess on the same word again. The arrays for the correct and wrong answer gets reseted so the game dont store the letters from the last game. The game also uses inputs so the player can choose which difficulty level they want and if they want to play again when the game is over.    



### TECHNOLOGIES

---

- PEP8 to validate python code
- [https://fsymbols.com/generators/] to generate the text for the print "hangman", "You won! Congratulations", "Game over! You lose" and the hearts which shows the lifes

### TESTING

---

- I tested the game works as it should in Chrome, Firefox and Edge browser.
- I tested that the guess letter input was working as it should by putting wrong inputs such as no letter, double letter or the same letter twice or more to see that the correct prints was printed out.
- I tested that the prints was working trough out the process of making the game by running just that part of the function or method.
- I tested that the variables which generates a random word was working by playing again when the game was over to see that another word was generated and not the same one that i had in the game before. 
- I tested that the play again input "yes" worked as it should by choosing "yes" so the game restarts where the player can choose a difficulty. 
- I tested that the play again input "no" worked as it should by choosing "no" when the game is over to see that the console ends the game. 
- I tested that each function was going through each stage correctly and didnt miss anything or produced any errors
- I tested that all text is easy to read and to understand
- The code got valified through PEP8 that is built in in the IDE i use

#### BUGS

- Ive noticed one bug that only appears sometimes. Its that the game sometimes only print one correct guessed letter ive if the correct word got more then one of that letter. Ive debugged the game by using the word "boo" and "luigi". I have tried the following things to try and locate where the bug happends:
    - I tried to guess "o" as the first correct guessed letter in the first game the console runs. The bug didnt show. The game printed out both "o"
    - I tried to guess the "b" first then the "o". The bug didnt show. The game printed out both "o"
    - I tried to guess the wrong letter 5 times so I only got 1 life left and the guessed "o". The bug didnt show. The game printed out both "o"
    - I tried to guess "l" as the correct first letter for the word "luigi". Then guess a wrong letter, to then guess "i". The bug didnt show. Both "i" still printed out
    - I tried to end the game early by typing CTRL+C in the terminal. And then restart a new game after that by usin the "up arrow" so the terminal starts the game by printing out "python3 run.py" to see if the bug was going to show. The game still printed out both "i". 
    - I tried to run several games after eachother by winning or losing the game and choose to play again. The bug still didnt show and printed both "o" to the word boo, and both "i" to the word luigi
I still havent found what makes this bug appear.

### DEPLOYMENT

---
#### This project was deployed via Github to Heroku. Make sure that you have added your dependencies to the requirements.txt file before you do this or it might not work. The following steps shows how you deploy it to Heroku:

1. Log in to your Github and deploy your repository.
2. Make a account on the Heroku website if you dont got one already [https://id.heroku.com/login]
3. Fork or clone your repository
4. Set the buildbacks to Python as the first one, and NodeJS as the second
5. Link your Heroku accoun to the correct repository
6. Click on deploy

### CREDITS

---

#### CODE

- I looked on these two tutorials on youtube to help me make the game [https://www.youtube.com/watch?v=Ff--def_1q0][https://www.youtube.com/watch?v=7sVnul-StrU]

#### All the thanks to the lovely students on slack for helping out when needed and my mentor Ronan for being so supportive and helpfull
