# 🎲 Task 2 – Number Guessing Game (CLI)

## 📖 Description
This project is a simple **command-line interactive game** where the player tries to guess a secret number.  
It demonstrates Python basics such as loops, conditionals, exception handling, and user input.

---

## 📝 Features
- Generates a secret number (currently set to `67` for testing).
- Accepts multiple guesses until the correct number is found.
- Provides hints:
  - `"Too low! Try again."`
  - `"Too high! enter 100 or 100 below !Try again."`
- Tracks the number of attempts.
- Handles invalid inputs gracefully (e.g., letters instead of numbers).

---

## 🎯 Skills Practiced
- Using the `random` module (can be extended to generate random numbers).
- Loops (`while True`) for repeated guessing.
- Conditionals (`if-elif-else`) for hints.
- Exception handling (`try-except`) for invalid input.
- String formatting for user-friendly messages.

---

## ⚙️ How to Run
1. Save the file as `number_guessing_game.py`.
2. Run the program:bash
   python number_guessing_game.py
