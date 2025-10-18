# Hangman-Game


Goal:

The goal of this project is to create a simple, text-based version of the classic Hangman game. The player attempts to guess a secret word one letter at a time, with a limited number of incorrect guesses allowed.

Key Features:

Predefined Word List: The game uses a small, internal list of 5 hardcoded words ("PYTHON", "ALPHABET", etc.) for selection.

Guess Limit: Players are limited to 6 incorrect guesses before the game ends.

Visual Feedback: The current status of the hangman figure is displayed using ASCII art after each incorrect guess.

Input Validation: The program ensures the user enters a single, valid, and previously un-guessed letter.

Console I/O: The entire game runs using basic console input and output (no external graphics or audio required).

How to Run:

Ensure you have Python 3 installed.

Save the code as hangman_game.py.

Open your terminal or command prompt.

Run the script using the following command:

python hangman_game.py


Concepts Demonstrated:

random module (for selecting a word)

while loop (for the main game flow)

if-else statements (for processing guesses)

Strings and Lists (for handling words and status display)

Sets (for tracking guessed letters efficiently)
