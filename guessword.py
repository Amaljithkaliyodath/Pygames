import random


# List of words for the game
WORDS = ["python", "programming", "computer", "science", "algorithm", "function", "variable", "loop", "condition", "object"]

# Choose a random word from the list
word = random.choice(WORDS)

# Create an empty list to represent the word
guess_word = ["_"] * len(word)

# Set the number of guesses allowed
num_guesses = 7

# Set the game status to running
game_running = True

# List of guessed letters
guessed_letters = []

# Main game loop
while game_running:
    # Print the current game state
    print("Current word: ", " ".join(guess_word))
    print("Guessed letters: ", guessed_letters)
    print("You have ", num_guesses, " guesses left.")

    # Get the user's guess
    guess = input("Enter your guess: ").lower()

    # Check if the guess is a letter
    if len(guess) == 1 and guess.isalpha():
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You have already guessed that letter.")
        else:
            # Add the letter to the list of guessed letters
            guessed_letters.append(guess)

            # Check if the letter is in the word
            if guess in word:
                # Update the word list with the correct guess
                for i in range(len(word)):
                    if word[i] == guess:
                        guess_word[i] = guess
            else:
                # Decrease the number of guesses left
                num_guesses -= 1

                # Check if the user has run out of guesses
                if num_guesses == 0:
                    game_running = False
                    print("You have run out of guesses. The word was ", word)
    else:
        print("Invalid input. Please enter a single letter.")

    # Check if the user has guessed the word
    if "_" not in guess_word:
        game_running = False
        print("Congratulations! You have guessed the word: ", word)