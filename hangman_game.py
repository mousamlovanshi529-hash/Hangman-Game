# Hangman Game

import random

# List of words
words = ["python", "computer", "programming", "hangman", "student"]

# Randomly select a word from the list
word = random.choice(words)

# Store letters guessed by the player
guessed_letters = []

#Limit of wrong attempts
attempts = 6

print("====Welcome to Hangman Game!====")

# Continue the game until attempts become 0
while attempts > 0:

    # Variable to display the current word status
    display_word = ""

    # Check each letter in the selected word
    for letter in word:
        if letter in guessed_letters:
            # Show guessed letters
            display_word += letter + " "
        else:
             # Hide unguessed letters
            display_word += "_ "
    
    # Display the word with guessed letters
    print("\nWord:", display_word)

    # Check if the player has guessed the whole word
    if "_" not in display_word:
        print("Congratulations! You Win,you guessed the word:", word)
        break

    #  Take user input
    guess = input("Enter a letter: ").lower()

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    # Save guessed letter
    guessed_letters.append(guess)

    # Check if the guessed letter is in the word
    if guess in word:
        print(guess , " is Correct latter !")
    else:
        # Reduce attempts for a wrong guess
        attempts -= 1
        print(guess , "is !!Wrong!!")
        print("Attempts left:", attempts)
        
# Game over message
if attempts == 0:
    print("\n Game Over!")
    print("The word was:", word)