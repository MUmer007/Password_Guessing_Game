# Password_Guessing_Game

Password Guessing Game (Python)
📖 Overview

This project is a Password Guessing Game built using Python.
The player selects a difficulty level, and the program randomly chooses a secret word. The goal is to guess the correct password by making repeated attempts until the correct word is found.

The game is interactive, beginner-friendly, and helps build logical thinking.

🎯 Objective

Practice Python fundamentals

Learn how to use the random module

Understand loops and conditionals

Improve string comparison logic

Build an interactive console-based game

🧠 Difficulty Levels

The game offers three difficulty levels, each with different word complexity:

🟢 Easy

Short and simple words
Example: cat, dog, sun

🟡 Medium

Moderate-length words
Example: garden, window, planet

🔴 Hard

Long and complex words
Example: algorithm, psychology, infrastructure

🎮 How the Game Works

The user selects a difficulty level.

A random word is chosen based on the selected level.

The user repeatedly guesses the password.

The game counts the number of attempts.

The game ends when the correct password is guessed.

A hint system shows correct letters in the correct position using * for unknown characters.

🧠 Concepts Used

Lists

Random selection (random.choice)

Loops (while)

Conditional statements (if, elif, else)

String comparison

User input handling

Counters and attempts tracking

📂 Project Structure
📁 password-guessing-game
 ├── password_game.py
 └── README.md

▶️ How to Run

Make sure Python 3 is installed.

Open terminal or command prompt.

Navigate to the project directory.

Run the program:

python password_game.py

🖥 Sample Gameplay
Welcome to the Password Guessing Game!
Choose a difficulty level (easy, medium, hard): medium

Guess the Secret Password!
Enter your guess: garden
Incorrect guess. Try again!
Enter your guess: window
Congratulations! You've guessed the word 'window' in 2 attempts.

💡 Hint System

After the game ends, a hint is displayed:

Correct letters in correct positions are shown

Incorrect positions are replaced with *

Example:

Hint: w*nd**

📌 Notes

Difficulty defaults to easy if an invalid input is given

The game continues until the correct word is guessed

Attempt count helps measure performance

🧑‍💻 Author

Muhammad Umer Shaikh


🚀 Future Improvements

Limit number of attempts

Show hints after each incorrect guess

Add score system

Create GUI version

Add multiplayer mode

⭐ Support

If you like this project:

⭐ Star the repository

🍴 Fork it

🎮 Add your own word lists

📜 License

This project is intended for educational and learning purposes.
Free to use, modify, and share.
