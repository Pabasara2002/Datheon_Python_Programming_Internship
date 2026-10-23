import random

# ASCII Art for Hangman stages (0 to 6 incorrect guesses)
HANGMAN_PICS = [
    """
       +---+
           |
           |
           |
          ===""",
    """
       +---+
       O   |
           |
           |
          ===""",
    """
       +---+
       O   |
       |   |
           |
          ===""",
    """
       +---+
       O   |
      /|   |
           |
          ===""",
    """
       +---+
       O   |
      /|\\  |
           |
          ===""",
    """
       +---+
       O   |
      /|\\  |
      /    |
          ===""",
    """
       +---+
       O   |
      /|\\  |
      / \\  |
          ==="""
]

def load_words(filename="google-10000-english-no-swears.txt"):
    """Loads words from the provided English word list file."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            words = [line.strip().lower() for line in f if line.strip() and line.strip().isalpha()]
        return words if words else ["datheon", "python", "internship", "hangman"]
    except FileNotFoundError:
        # Fallback list if file is missing
        return ["datheon", "python", "internship", "hangman", "developer"]

def play_hangman():
    print("========================================")
    print("   WELCOME TO HANGMAN GAME - DATHEON    ")
    print("========================================")
    
    # Load words and select a random word
    words = load_words()
    secret_word = random.choice(words)
    
    guessed_letters = set()
    incorrect_guesses = 0
    max_mistakes = 6

    while incorrect_guesses < max_mistakes:
        # Display current ASCII stage art
        print(HANGMAN_PICS[incorrect_guesses])
        
        # Display masked string with spacing (e.g., _ A _ H E O N)
        formatted_display = " ".join([letter.upper() if letter in guessed_letters else "_" for letter in secret_word])
        
        print(f"\nWord: {formatted_display}")
        print(f"Guessed Letters: {', '.join(sorted(list(guessed_letters))).upper() if guessed_letters else 'None'}")
        print(f"Remaining Mistakes Allowed: {max_mistakes - incorrect_guesses}")

        # Check for victory condition
        if all(letter in guessed_letters for letter in secret_word):
            print("\n" + "="*40)
            print("🎉 VICTORY! YOU GUESSED THE WORD CORRECTLY! 🎉")
            print(f"The secret word was: {secret_word.upper()}")
            print("="*40)
            break

        # Get user input
        guess = input("\nGuess a letter: ").lower().strip()

        # Input validation
        if not guess or len(guess) != 1 or not guess.isalpha():
            print("⚠️ Invalid input! Please enter a single alphabetical letter.")
            continue

        # Prevent duplicate penalty deduction / notification
        if guess in guessed_letters:
            print(f"ℹ️ You already guessed '{guess.upper()}'! No penalty applied.")
            continue

        guessed_letters.add(guess)

        # Evaluate guess
        if guess in secret_word:
            print(f"✅ Correct! '{guess.upper()}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"❌ Incorrect! '{guess.upper()}' is not in the word.")

    else:
        # Defeat / Game Over Screen
        print(HANGMAN_PICS[max_mistakes])
        print("\n" + "="*40)
        print("💀 DEFEAT! GAME OVER! YOU RAN OUT OF ATTEMPTS. 💀")
        print(f"The secret word was: {secret_word.upper()}")
        print("="*40)

if __name__ == "__main__":
    play_hangman()