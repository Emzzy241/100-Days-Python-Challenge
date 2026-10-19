# Learnt a lot in today, the Day-12, and I am super happy about that actually.
# From scope, global and local scope, to understanding how there is nothing like a block scope 
# In python where within an if/elif/else statement, a variable declared in there would just be
# treated as a normal variable, and not that the variable will be seen as some form variable
# Within an if/elif/else scope.

# Now, let us build day-12 program, the Number Guessing Game

# import random
# from art import logo

# # print("Welcome to the Number Guessing Game!")
# # print("I'm thinking of a number between 1 and 100")
# # print(f"The number to be guessed is: {random_number}")

# # Global variables for 
# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# attempts = 0
# game_over = False
# should_continue = True

# # while should_continue:
# def set_difficulty(): 
#     difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")   
#     if difficulty == "easy":
#         return EASY_LEVEL_TURNS
#     elif difficulty == "hard":
#         return HARD_LEVEL_TURNS
#     else:
#         print("Sorry, I did not get that")


# def check_answer(user_guess, actual_guess, attempts):
#     """Checks answer against guess, returns the number of turns remaining."""
#     # global attempts # Needed to be able to use the global variables defined above.

#     if user_guess < actual_guess:
#         print("Too Low.")  
#         return attempts - 1   
#     elif user_guess > actual_guess:
#         print("Too high.")
#         return attempts - 1   
#     elif user_guess == actual_guess:
#         print("congratulations, you guessed correctly!")
#         print("You win!!!")
#         return
#     else:
#         print("Something went wrong, please try again. :-(")

# def game():
#     print("Welcome to the Number Guessing Game!")
#     print(logo)
#     print("I'm thinking of a number between 1 and 100")
#     random_number = random.randint(1, 100)
#     print(f"Pssst, the number to be guessed is: {random_number}")
#     attempts = set_difficulty()

#     # Global variable

#     guess = 0
#     while guess != random_number:
#         print(f"You have {attempts} attempts remaining to guess the number.")

#         guess = int(input("Make a guess: "))
        
#         attempts = check_answer(guess, random_number, attempts)
#         if attempts == 0:
#             print("You've run out of guesses. You lose.")
#             return
#         elif guess != random_number:
#             print("Guess again")
        
# game()

import os
import random
from art import LOGO

# Makes ANSI colors work in Windows terminals too
os.system("")

# ---------- Styling ----------
RESET, BOLD, DIM = "\033[0m", "\033[1m", "\033[2m"
RED, GREEN, YELLOW = "\033[91m", "\033[92m", "\033[93m"
BLUE, MAGENTA, CYAN = "\033[94m", "\033[95m", "\033[96m"

# ---------- Settings ----------
LEVELS = {"easy": 10, "hard": 5}
LOW, HIGH = 1, 100
DEBUG = False  # set True to peek at the secret number while testing

# ---------- Logo ----------
# 69 columns wide, so it fits in a standard 80-column terminal.

LOGO_WIDTH = 69

# 256-color codes running from cyan through blue to magenta.
GRADIENT = [51, 45, 39, 33, 63, 99, 135, 171]


def paint(text, *styles):
    return "".join(styles) + str(text) + RESET


def print_logo():
    """Prints the logo with a color gradient from top to bottom."""
    lines = LOGO.strip("\n").split("\n")
    for i, line in enumerate(lines):
        # Map this row's position (0 to 1) onto the gradient list.
        shade = GRADIENT[int(i / len(lines) * len(GRADIENT))]
        print(f"\033[1;38;5;{shade}m{line}{RESET}")
    tagline = "Can you crack the code?"
    print(paint(tagline.center(LOGO_WIDTH), DIM))
    print()


def divider():
    print(paint("─" * 46, DIM))


def attempts_bar(left, total):
    """Visual meter of remaining attempts, e.g. ♥♥♥♡♡"""
    color = GREEN if left > total / 2 else YELLOW if left > 1 else RED
    return paint("♥" * left, color) + paint("♡" * (total - left), DIM)


def temperature(diff):
    """Hint on how close the guess was."""
    if diff <= 3:
        return paint("🔥 Burning hot!", RED, BOLD)
    if diff <= 10:
        return paint("♨  Warm", YELLOW)
    if diff <= 25:
        return paint("🌤  Lukewarm", CYAN)
    return paint("❄  Cold", BLUE)


def set_difficulty():
    while True:
        choice = input(
            f"Choose a difficulty — {paint('easy', GREEN)} or {paint('hard', RED)}: "
        ).strip().lower()
        if choice in LEVELS:
            return LEVELS[choice]
        print(paint("  Please type 'easy' or 'hard'.", YELLOW))


def get_guess():
    while True:
        raw = input(paint("Make a guess: ", BOLD)).strip()
        if raw.isdigit() and LOW <= int(raw) <= HIGH:
            return int(raw)
        print(paint(f"  Enter a whole number between {LOW} and {HIGH}.", YELLOW))


def check_answer(guess, answer, attempts):
    """Prints feedback and returns the attempts left."""
    if guess == answer:
        return attempts
    direction = paint("Too low ▲", MAGENTA) if guess < answer else paint("Too high ▼", MAGENTA)
    print(f"  {direction}   {temperature(abs(guess - answer))}")
    return attempts - 1


def game():
    print_logo()
    print(f"I'm thinking of a number between {paint(LOW, BOLD)} and {paint(HIGH, BOLD)}.\n")

    answer = random.randint(LOW, HIGH)
    if DEBUG:
        print(paint(f"[debug] the number is {answer}", DIM))

    total = attempts = set_difficulty()
    guesses = 0

    while attempts > 0:
        divider()
        print(f"Attempts left: {attempts_bar(attempts, total)}  ({attempts})")
        guess = get_guess()
        guesses += 1

        if guess == answer:
            divider()
            print(paint(f"🎉 You got it! The number was {answer}.", GREEN, BOLD))
            print(paint(f"   Solved in {guesses} guess{'es' if guesses != 1 else ''}.", GREEN))
            return
        attempts = check_answer(guess, answer, attempts)

    divider()
    print(paint("💀 You've run out of guesses. You lose.", RED, BOLD))
    print(f"   The number was {paint(answer, BOLD)}.")


def main():
    while True:
        game()
        print()
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print(paint("\nThanks for playing! 👋", CYAN))
            break
        print("\n" * 50)


if __name__ == "__main__":
    main()

# You can put the code inside python tutor to really se what is going on.
# if difficulty == "easy":
#         attempts = 10
#     elif difficulty == "hard":
#         attempts = 5
#     else:
# def keep_playing_game():
#     print(f"You have {attempts} attempts remaining to guess the number.")
#     guess = int(input("Make a guess: "))

#     if guess < random_number:
#         print("Too Low. Please try again")  
#         attempts -= 1   
#     elif guess > random_number:
#         print("Too high. Guess Again")
#         attempts -= 1   
#     elif guess == random_number:
#         print("congratulations, you guessed correctly!")
#         print("You win!!!")
#         return
#     else:
#         print("Something went wrong, please try again. :-(")


# print(attempts)

# while should_continue:
#     if attempts >= 1:
#         check_answer()
#     elif attempts <= 0:
#         print(f"You have {attempts} attempts left. You ran out of attempts. Sorry, You lose :-(")
#         should_continue = False

# plat_again = input("Would you like to play again? ")

# Its only when you struggle that you get better at programming.
