"""CodeAlpha Python Internship - Task 1: Hangman Game
A simple text-based Hangman game played in the console.
"""

import random

WORDS = ["python", "internship", "developer", "variable", "function"]
MAX_WRONG = 6

STAGES = [
    "\n  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
    "\n  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
    "\n  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
    "\n  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
    "\n  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
    "\n  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
    "\n  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========",
]


def display_word(word, guessed):
    """Return the word with unguessed letters shown as underscores."""
    return " ".join(ch if ch in guessed else "_" for ch in word)


def get_guess(guessed):
    """Keep asking until the player enters a valid, new single letter."""
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
        elif guess in guessed:
            print("You already guessed that letter. Try another one.")
        else:
            return guess


def play_game():
    word = random.choice(WORDS)
    guessed = set()
    wrong = 0

    print("=== Welcome to Hangman! ===")
    print(f"The word has {len(word)} letters. You have {MAX_WRONG} wrong guesses.")

    while wrong < MAX_WRONG:
        print(STAGES[wrong])
        print("\nWord:", display_word(word, guessed))
        print(f"Wrong guesses left: {MAX_WRONG - wrong}")
        print("Guessed letters:", " ".join(sorted(guessed)) or "-")

        guess = get_guess(guessed)
        guessed.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            wrong += 1
            print(f"Sorry, '{guess}' is not in the word.")

        if all(ch in guessed for ch in word):
            print("\nWord:", display_word(word, guessed))
            print("Congratulations! You won! 🎉")
            return

    print(STAGES[MAX_WRONG])
    print(f"\nGame over! The word was: {word}")


def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
