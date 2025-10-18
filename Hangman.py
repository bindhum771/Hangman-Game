import random
import sys
from typing import List, Set

# --- Configuration ---
# 1. Small list of 5 predefined words
WORD_LIST: List[str] = ["PYTHON", "ALPHABET", "PROGRAM", "KEYBOARD", "CODING"]

# 2. Limit incorrect guesses to 6 (this is the number of stages in the HANGMAN_STAGES list)
MAX_INCORRECT_GUESSES = 6

# Text representations of the hangman stages
HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           -
    """,
    """
       -----
       |   |
       O   |
           |
           |
           -
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           -
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           -
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           -
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           -
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           -
    """
]

def get_word() -> str:
    """Selects a random word from the WORD_LIST."""
    return random.choice(WORD_LIST)

def display_game_status(
    word_to_guess: str,
    guessed_letters: Set[str],
    incorrect_guesses: int
) -> str:
    """
    Displays the current state of the word, the hangman graphic, and letters already guessed.
    
    Returns:
        The partially guessed word string (e.g., P Y _ H O N).
    """
    
    # Display the current hangman stage based on incorrect guesses
    print(HANGMAN_STAGES[incorrect_guesses])

    # Build the masked word
    display_word = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
            
    print("\nWord: " + display_word)
    
    # Display guessed letters
    guessed_list = sorted(list(guessed_letters))
    print(f"Incorrect Guesses Left: {MAX_INCORRECT_GUESSES - incorrect_guesses}")
    print(f"Letters Guessed: {', '.join(guessed_list)}\n")
    
    return display_word.replace(" ", "")

def get_guess(guessed_letters: Set[str]) -> str:
    """
    Prompts the user for a single letter guess and validates the input.
    """
    while True:
        guess = input("Enter a letter to guess: ").strip().upper()
        
        if len(guess) != 1 or not 'A' <= guess <= 'Z':
            print("Invalid input. Please enter a single English letter (A-Z).")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        else:
            return guess

def hangman_game():
    """Main function to run the Hangman game."""
    print("Welcome to Hangman!")
    print(f"You have {MAX_INCORRECT_GUESSES} incorrect guesses before you lose.")
    
    # Game state variables
    word = get_word()
    guessed_letters: Set[str] = set()
    incorrect_guesses: int = 0
    
    # Main game loop
    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        
        # 1. Display current status
        current_display = display_game_status(word, guessed_letters, incorrect_guesses)
        
        # 2. Check for win condition
        if "_" not in current_display:
            print("\n*** CONGRATULATIONS! You guessed the word! ***")
            print(f"The word was: {word}")
            return
            
        # 3. Get and process guess
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

    # Loop ends if incorrect_guesses == MAX_INCORRECT_GUESSES
    
    # Display final stage
    print(HANGMAN_STAGES[MAX_INCORRECT_GUESSES])
    
    print("\n--- GAME OVER ---")
    print(f"You ran out of guesses. The word was: {word}")

if __name__ == "__main__":
    try:
        hangman_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)
