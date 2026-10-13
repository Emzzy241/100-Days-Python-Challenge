# # We building the hangman game Today, on Day-7
# For & whil;e loop
# # lists
# If/Else
# Range, Strings, Modules, etc.,

import random
from hangman_art import logo, stages
from hangman_words import word_list

# Game Setup
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

game_over = False
correct_letters = []
lives = 6

# For debugging / testing purposes (you can remove this print if you want it secret)
print(chosen_word)

print(logo)

# Initialize the placeholder display
placeholder = ""
for _ in range(word_length):
    placeholder += " _ "
print(f"Word to guess: {placeholder}")

# Main Game Loop
while not game_over:
    print(f"\n*********************** {lives}/6 LIVES LEFT ***********************")
    guess = input("Guess a letter: ").lower()

    # Check if the user already guessed this letter
    if guess in correct_letters:
        print(f"You've already guessed '{guess}'. Try a different letter.")

    display = ""

    # Build the current display based on correct guesses
    for letter in chosen_word:
        if letter == guess:
            display += letter
            if guess not in correct_letters:
                correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += " _ "

    print(f"Word to guess: {display}")

    # Handle incorrect guesses
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed '{guess}', that's not in the chosen word. You lose a life.")
        
        if lives == 0:
            game_over = True
            print(f"************************************* IT WAS '{chosen_word}'. You lose! ****************************************")

    # Handle win condition
    if "_" not in display:
        game_over = True
        print("************************************* You win! ****************************************")

    # Print the current hangman stage art
    print(stages[6 - lives])


# 
# import random
# from hangman_art import stages, logo
# from hangman_words import word_list
# # from hangman_art import logo

# # import stages
# # word_list = ["aardvark", "baboon", "camel"]

# # stages = [
# #     """
# #   +---+

# #   |   |
# #       |
# #       |
# #       |
# #       |
# # =========""",
# #     """
# #   +---+

# #   |   |
# #   O   |
# #       |
# #       |
# #       |
# # =========""",
# #     """
# #   +---+

# #   |   |
# #   O   |

# #   |   |
# #       |
# #       |
# # =========""",
# #     """
# #   +---+

# #   |   |
# #   O   |
# #  /|   |
# #       |
# #       |
# # =========""",
# #     """
# #   +---+

# #   |   |
# #   O   |
# #  /|\\  |
# #       |
# #       |
# # =========""",
# #     """
# #   +---+

# #   |   |
# #   O   |
# #  /|\\  |
# #  /    |
# #       |
# # =========""",
# #     """
# #   +---+

# #   |   |
# #   O   |
# #  /|\\  |
# #  / \\  |
# #       |
# # =========""",
# # ]


# # TODO-1: FOR STEP-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
# # TODO-1: FOR STEP-2 create a "placeholder" with the same number of blanks as the word

# chosen_word = random.choice(word_list)
# placeholder = ""
# print(chosen_word)
# word_length = len(chosen_word)
# for char in range(word_length):
# # for char in range(len(chosen_word)):
#     placeholder += " _ "
# print(placeholder)


# # TODO 2: FOR STEP-1: Ask user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# # guess = input("Guess a letter: ").lower()
# # print(guess)
# # TODO-3: For Step-1, Check if the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it i
# # And "wrong" if it is not.
# # My mistake is that I thought there was a need for a counter
# # for letter in chosen_word:
# #     if (letter == guess):
# #         print("Right")
# #     else:
# #         print("Wrong")

# # Extending this function to do
# # TODO-2: FOR STEP-2: Create a "display" that puts the guess letter in the right position and a blank in the rest of the strings.

# # TODO: Change the for loop so that you keep the previous correct 

# # guess_amounts = 1

# game_over = False

# correct_letters = []
# lives = 6

# # TODO-1: Create a variable lives to keep track of the number of lives left
# # TODO-2: iF GUESS IS NOT A LETTER IN chosen word, Then keep running
# # If lives = 0, then the game stops and says: you lose.
# # TODO-3: Print the hangman stages so that it evaluates to the hangman individual stages

# # What I came up with, but this ain't gonna work.
# print(logo)
# while not game_over:
#     print(f"***********************{lives}/6 LIVES LEFT***********************")
#     guess = input("Guess a letter: ").lower()
#     # if guess in correct_letters or not in correct_letters:

#     # TODO-4, STEP-5:
#     if guess in correct_letters:
#          print(f"You've already guessed {guess}")

#          print(f"You already guessed {guess}")
#     display = ""
#     # if letter == guess:
#     for letter in chosen_word:
#             if letter == guess:
#                 # Instead of printing right or wrong, we print display
#                 display += letter
#                 correct_letters.append(guess)
#                 # if letter == guess:
#                 #      print(f"You already guesses {guess} previously, try again")
#             elif letter in correct_letters:
#                  display += letter
#             else:
#                 display += " _ "
#         # print(lives)
#     print(f"Word to guess: " + display)

#     # TODO-2, sTEP-4: iF GUESS IS NOT A LETTER in the chosen word, then reduce "lives" by 1.
#     # If lives goes down to 0 then the game should end it should print "You lose"
#     if guess not in chosen_word:
#          lives -= 1
#          print(f"You guessed '{guess}', that's not in the chosen word. You lose a life.")
#          if lives == 0:
#               game_over = True

#             # TODO-7, STEP-5: Update the print statement below to give user the correct word they've been trying to guess
#               print(f"*************************************IT WAS '{chosen_word}' You lose!****************************************")

#     if "_" not in display:
#          game_over = True
#          print("You win.")

#         #  TODO-3, Step-4: Print the ASCII art from "stages"
#         # that corresponds to the current number of "lives" the user has remaining
#     print(stages[6 - lives])

#     # print(stages[lives])
    
#     # guess_amounts += 1
    
# # print(guess_amounts)
# # while guess_amounts < len(chosen_word):
# #     guess = input("Guess a letter: ").lower()
# #     # if letter == guess:
# #     for letter in chosen_word:
# #             if (letter == guess):
# #                 # Instead of printing right or wrong, we print 
# #                 display += letter
# #             else:
# #                 display += " _ "
# #     print(display)
    
# #     guess_amounts += 1
    
# # print(guess_amounts)



# # Moving on to Step-2:

# # Last one, number-5
# # TODO: Todo number 1, 2, 3 were easy peasy to solve
# # TODO-4: If the user has entered a letter they've already guessed, print the letter and tell them they already guessed that letter correctly. No life deducted
# # TODO-5: If the letter they guessed is not in the chosen_word, print out the letter. print out the letter and let them know it's not in the word. e.g., you guessed d, that's not in the word, You lose a life.
# # TODO-6, For Step-5: Update the code below to tell the user how many lives they have left. Talking about the lives they have left. I already did that.

