import random

def number_guessing_game():
    # Generate random number between 1 and 100
    secret_number =67 
    attempts = 0
    print("🎲 Welcome to the Number Guessing Game!")
    print("Guess the number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess <secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! enter 100 or 100 below !Try again.")
            else:
                print(f"🎉 Correct! The number was {secret_number}.")
                print(f"You guessed it in {attempts} attempts.")
                break  # End game
        except ValueError:
            print("❌ Invalid input. Please enter a number.")

# Run the game
number_guessing_game()
