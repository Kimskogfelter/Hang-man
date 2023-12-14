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
I love games myself so I knew that I wanted to make some kind of game. When I finally saw that you could make hangman with python I knew that this was the game I wanted to make. I loved to play hangman as a kid during breaks on the whiteboard in the classroom. My hangman has 3 different degrees of difficulty, easy, medium and hard. The player then get 6 lives/attemps to try and guess the correct word that the computer randomizes from lists that I have made.  

### UX DESIGN

---

#### USER STORIES

- #### As a first time user

  - I want to be intriged to play the game
  - I want to feel amused by the game
  - I want to feel exited when playing the game
  - I want a break from everything else around me and get a quick brain workout
  
- #### As a returning and frequent user

  - I want to get a break and get a quick brain workout
  
#### All users are enabled to play both on the computer and on their mobile phones

### STRUCTURE

---

#### STARTING PAGE

- The first page a user enters is the starting page. It has the heading text "Super Mario Memory Game" and a picture of Mario riding on Yoshis back with a little star friend next to them.

![picture of the starting page](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/start-page.webp)

#### GAME AREA PAGE

- The game area contains the memory game. It got 12 different cards that the user can click on and pair them in order to continue and win the game.

![picture of the game area page](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/game-page.webp)

#### WINNING PAGE

- When the user wins the game a window pops up that says congratulations. The user can then choose to click on a "play again" button to play again.

![picture of the winning page](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/win-result-page.webp)

### FEATURES

---

#### STARTING PAGE

- #### HEADING

  - The heading text is at the top of the website and contains the text "Super Mario - Memory Game". Its purpose is to make the user understand what type of game it is that they are going to play.

![picture of the heading on the starting page](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/heading.webp)

- #### IMAGE
  
  - The image of Super Mario on Yoshi is under the heading to make the user understand that the game is about Super Mario

![picture of the image with Super Mario and Yoshi on the starting page](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/image-startpage.webp)

- #### "LETS GO" BUTTON
  
  - Under Super Mario and Yoshi is a button that says "Lets go!". If the user click on the button it takes them to the game page.

![picture of the "lets go" button on the starting page](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/letsgo-button.webp)

#### GAME AREA PAGE

- #### MOVES SECTION

  - The memory game has a section that counts how many moves the user does during the game

![picture of the moves section](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/moves.webp)

- #### TIMER SECTION

  - The timer starts as soon as the user press "play" and stops when the player completes or pause the game.

![picture of the timer section](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/timer.webp)

- #### MEMORY CARDS

  - The memory cards is used to play the game. The user click on one to switch the card and then chooses another one in hope that they are the matching pair.
  - The front of the cards is the question block from the Super Mario game.

![picture of the front memory cards](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/memorycards.webp)

- When a user click on one card a creature from the Super Mario game appears.

![picture of a clicked memory card](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/memorycards-clicked.webp)

- #### RESTART BUTTON

  - At the bottom of the game area is a restart" button which the user can click on to restart the game.

![picture of the "play/pause" button](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/restart-button.webp)

- #### WINNING DIV
  
  - When a user wins the game a div pops up with the text "You made it! Congratulations!"
  - A button appears below the text that says "Play One More Time" which the user can press to restart the game and play again

![picture of the content that pops up when the user wins the game](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/winning-div.webp)

### COLOR SCHEME

---

- The color scheme through both pages is a #red background and #white text with a #black border around the text. The buttons to start/pause the game got a grey background color.

### TECHNOLOGIES

---

- [https://validator.w3.org/nu/] to validate html code
- [https://jigsaw.w3.org/css-validator/] to validate css code
- [https://freepngimg.com/] for images
- favicon from [https://fontawesome.com/icons/block-question?f=classic&s=duotone&pc=%23dcb218&sc=%23dcb218]
- used [https://favicon.io/favicon-converter/] to generate the favicon
- [https://www.remove.bg/] to remove background from favicon

### WIREFRAMES

---

#### STARTING PAGE

![Starting page made in wireframes](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/wireframes/start-page-wireframe.webp)

#### GAME PAGE

![Game page made in wireframes](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/wireframes/game-area-wireframe.webp)

#### WINNING PAGE

![Winning page made in wireframes](https://raw.githubusercontent.com/Kimskogfelter/Super-Mario/main/assets/images/readme/wireframes/win-result-wireframe.webp)

### TESTING

---

- I tested the website in Chrome, Firefox and Edge browser to see that all pages loaded and that every button and function was working correctly.
- The site is also responsive which I tested in google chromes devtools by selecting different screensizes and test each function
- I tested that all text is easy to read and to understand
- The code got valified through both HTML, CSS and JS validators

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
