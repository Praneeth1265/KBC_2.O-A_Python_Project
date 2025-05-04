# KBC-2.O - A Python Project
An interactive Python based quiz game for meme enthusiasts, built using the Tkinter library, that displays a meme after each answer based on correctness. 
Features a dynamic leaderboard that ranks players by the virtual cash they've earned throughout the game

-----------------------------------------------------------------------------------------------------------------------------------------------------

- How It Works
>Startup and Instructions:
  Upon launching the game, background music plays while the user is shown game instructions.

>Name Entry:
  The user is prompted to enter their name. If skipped, a meme pops up as a humorous reminder. The name is later used for the leaderboard.

>Difficulty Selection via Dice Roll:
  The user rolls a virtual dice to randomly determine the difficulty level of the quiz.

>Quiz Time (10 Questions):
  No time constraints—this is a fun quiz, not a competitive exam! 😄
  After each question, a meme is displayed to keep the tone light-hearted.

>Scoring and Cash System:
  The user receives a score (number of correct answers) and a virtual cash amount based on performance.

>Catch: One wrong answer wipes out all accumulated cash, regardless of how many correct answers preceded it. However, the score remains intact.
  This twist adds excitement and intensity to the game.

>Leaderboard:
  A leaderboard button reveals a popup window displaying the top players sorted by score and cash won. Data is saved to a local CSV file.

-----------------------------------------------------------------------------------------------------------------------------------------------------

- Features
  <>Background music and leaderboard theme

  <>Dice-based difficulty assignment

  <>Meme popups after every question and user interaction

  <>Persistent leaderboard with CSV storage

  <>No internet required — fully offline

  <>Built with tkinter, pygame, and Python standard libraries

-----------------------------------------------------------------------------------------------------------------------------------------------------

- Technologies Used
Python 3.x
tkinter – for GUI
pygame – for audio
csv, random, os, time – standard libraries

-----------------------------------------------------------------------------------------------------------------------------------------------------

- Project Structure
```
KBC_2.O-A_Python_Project/
├── KBC_2.O.py
├── leaderboard.csv
├── Dice_Images/
│   └── images{1-6}/
├── Memes/
│   └── meme images/
├── Music/
│   ├── Instructions.mp3
│   ├── Timer.mp3
│   └── Leaderboard.mp3
└── README.md
```

-----------------------------------------------------------------------------------------------------------------------------------------------------

- How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Praneeth1265/KBC_2.O-A_Python_Project.git
   cd KBC_2.O-A_Python_Project
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Install dependencies (if pygame not installed):
   ```bash
   pip install pygame
   ```

4. Run the game:
   ```bash
   python KBC_2.O.py
   ```
