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

- #### The game got 3 different difficulties that the user can choose from in the beginning of the game. Easy, medium and hard. The easy difficulty got up to 4 letters in the choosen word, the medium got up to 6 letters and the hard got up to 9 letters. 

![picture of the part where the user choose the difficulty level](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/heading.webp)

#### SHOWING LIFES

- #### The player got 6 tries to guess the correct word. That is shown as hearts above the picture of the hangman so the player easy can see how many tries he/she got left before they lose. 

![picture of the hearts that shows how many lifes the player got left](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/image-startpage.webp)

#### INPUT VALIDATION

- #### CHOOSEN DIFFICULTY INPUT
    - Here the game checks if the choosen difficulty level is correct. If the player has written something else then easy, medium or hard they get a message that tells them that its invalid and they need to choose either easy, medium or hard.

![picture of the message that comes when the player write something else then easy, medium or hard when choosing a difficulty](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/letsgo-button.webp)

- #### GUESS A LETTER INPUT
    - When the player is going to guess a letter the game checks for several things. The first thing it checks if its the player only guessed one letter. If he/she guessed more then one letter the game shows a message that they need to guess at one letter at a time. 

![picture of the message that comes when the player guess more then one letter](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/letsgo-button.webp)

    - The second thing the game checks is if the letter is correct or not. If the letter is correct it gets printed out so the player can see where the correct letter is in the choosen word.

![picture that shows where the correct letters are shown in the game](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/letsgo-button.webp)

    - If the guessed letter is wrong the player gets a message that says wrong letter and then shows the letter next to it. Each time the player guess a wrong letter that letter gets printed out next to the text wrong letter. In that way the player can keep track on which letter they already has guessed that are wrong.

![picture that shows the "wrong letter" message](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/letsgo-button.webp)

    - The third thing the game checks is if the guessed letter already has been guessed. If its already been guessed the player get a message that says "You already guessed that"

![picture that shows the message that pops up if the player already has guessed a letter they choose to guess](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/letsgo-button.webp)

- #### PLAY AGAIN INPUT

    - When the player wins or loses the game he/she get to choose if they want to play again or not. The game then checks if the input the player has choosen is either "yes" or "no". If "yes" the game restarts from where the player get to choose a new difficulty level. 

![picture that shows the message that pops up if the player want to restart the game](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/letsgo-button.webp)

    - If the player choose "no" the game ends. 

![picture that shows the message that pops up if the player want to end the game](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/letsgo-button.webp)

    - If the player write something else then "yes" or "no" a message pop up saying that the message is invalid. And then asks them again if they want to play again, and to choose either "yes" or "no"

![picture that shows the message that pops up if the player write a invalid input](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/letsgo-button.webp)

#### DATA MODEL
- #### 

  - 

![picture of ](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/moves.webp)

### TECHNOLOGIES

---

- PEP8 to validate python code
- [https://fsymbols.com/generators/] to generate the text for the print "hangman", "You won! Congratulations", "Game over! You lose" and the hearts which shows the lifes

### TESTING

---

- I tested the game works as it should in Chrome, Firefox and Edge browser
- I tested that all text is easy to read and to understand
- The code got valified through PEP8 that is built in in the IDE i use

#### BUGS

- when I was finishing the page i noticed that the content on the index page wasnt centered on all devices. To  fix the issue i added min-height to both the html and body, and then the index-body which solved the issue because the body height tas stuck to the center of the page before that.
- saw that when you press the "restart game" button when you have pressed one memory card and dont have pressed another one to be compared with, that card is "used" when you have restarted the game and is compared to the first card you choose. Unfortunately I dont got the time to try and fix that issue.

#### LIGHTHOUSE

#### I also tested the website in Lighthouse with the result below

- #### Starting Page - Mobile version

![lighthouse result for starting page, mobile version](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/lighthouse/lighthouse-startpage-mobile.webp)

- #### Starting Page - Desktop version

![lighthouse result for starting page, desktop version](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/lighthouse/lighthouse-startpage-desktop.webp)

- #### Game Page - Mobile version

![lighthouse result for game page, mobile version](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/lighthouse/lighthouse-gamepage-mobile.webp)

- #### Game Page - Desktop version

![lighthouse result for game page, desktop version](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/lighthouse/lighthouse-gamepage-desktop.webp)

### DEPLOYMENT

---
    This project was deployed to Github.com. The following steps shows how you do it:

1. Log in to your Github.
2. Go to the Super Mario repository in Github: [https://github.com/Kimskogfelter/Super-Mario]
3. Select Settings in the repository navigation menu at the top.
4. Select Pages at the left handside of the website.
5. Choose: Deploy from a branch as Source.
6. Choose: Main as branch and /root as folder and press save.
7. Wait a few minutes and press the Code menu to the top left.
8. At the right handside go to Deployment.
9. Then press the ![picture of the deployment icon on github](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/deployment-icon.webp) to go to the live website.

### ISSUES

---

- Ive been having a really hard time to understand javascript. Its been alot happening at home during this time with the kids having to be home due to us moving to a new home and my husbands mom dying. The funural was 1 december so I havent been having the time to finish the project as I would like to. Im aware that I can have used to little own code, hopefully thats not the case.

### CREDITS

---

#### CODE

- I looked on these two tutorials on youtube to help me make the game [https://www.youtube.com/watch?v=Ff--def_1q0][https://www.youtube.com/watch?v=7sVnul-StrU]

#### All the thanks to the lovely students on slack for helping out when needed and my mentor Ronan for being so supportive and helpfull
