# Randomization
import random


# import random
# import my_module

# random_integer = random.randint(1, 10)
# print(random_integer)

# print(my_module.my_favorite_number)


# random_integer = random.randint(1, 10)
# print(random_integer)

# Creating random floating point numbers

# random_number_0_to_1 = random.random() * 10

# print(random_number_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)

# Program either prints out heads or tails, whether it prints heads or tails depends on the random though

# print("Welcome to the heads or tails application")
# random_integer = random.randint(1, 10)

# print(f"The random number generated is: {random_integer}")
# print()

# if (random_integer % 2 == 0):
#     print("heads")
# else:
#     print("tails")

# Her own 
# random_heads_or_tails = random.randint(0, 1)

# if random_heads_or_tails == 0:
#     print("Heads")
# else:
#     print("Tails")

# Lists in Python

# states_of_america = [ "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", 
#     "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", 
#     "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", 
#     "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", 
#     "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", 
#     "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", 
#     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", 
#     "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", 
#     "Montana", "Washington", "Idaho", "Wyoming", "Utah", 
#     "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# # states_of_america[1] = "Pencilvenia"

# # states_of_america.append("Dynastyland")
# states_of_america.extend(["Dynastyland", "Angelaland", "Jack Bauer Land"])

# print(states_of_america)

# 1st Challenge in Day-4:
# print("Welcome to the bankers roulette game.")
# friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]

# random_number = random.randint(0, 4)

# print(random_number)

# if random_number == 0:
#     print(f"{friends[random_number]} gets to pay the bill")
# elif random_number == 1:
#     print(f"{friends[random_number]} gets to pay the bill")
# elif random_number == 2:
#     print(f"{friends[random_number]} gets to pay the bill")
# elif random_number == 3:
#     print(f"{friends[random_number]} gets to pay the bill")
# elif random_number == 4:
#     print(f"{friends[random_number]} gets to pay the bill")
# else:
#     print("The bill is on the house")

# # Her method, the python documentation: random.choice() choice takes a sequence, and a list is an example of a sequence.

# print(random.choice(friends))

# Learning: Nested Lists now

# states_of_america = [ "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", 
#     "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", 
#     "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", 
#     "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", 
#     "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", 
#     "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", 
#     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", 
#     "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", 
#     "Montana", "Washington", "Idaho", "Wyoming", "Utah", 
#     "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# num_of_states = print (len(states_of_america))

# print(states_of_america[num_of_states])

# Learning Nested Lists
# dirty_dozen_2019 = [
#     "strawberries",
#     "spinach",
#     "kale",
#     "nectarines",
#     "apples",
#     "grapes",
#     "peaches",
#     "cherries",
#     "pears",
#     "tomatoes",
#     "celery",
#     "potatoes"
# ]

# THis was also part of the quiz that was given.
# fruits = [ "strawberries", "nectarines", "apples", "grapes", "peaches", "cherries", "pears", "tomatoes" ]

# vegetables = [
#     "spinach",
#     "kale",
#     "celery",
#     "potatoes"
# ]


# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen[1][1]) # dirty_dozen has both fruits and vegetables, to get fruits, we have the first [1], we are now inside fruits,
# TO now get the item with index position 2 inside fruits that we ae currently in, we slap in an extra 1 into it.


# Final Project of the day --> Rock, Paper, Scissors.
rock = r"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = r"""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = r"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


# rock2 = r"""
#     -------
# ---'   ----)
#       (-----)
#       (-----)
#       (----)
# ---.--(---)
# """

# paper2 = r"""
#     -------
# ---'   ----)----
#           ------)
#           -------)
#          -------)
# --------------)
# """

# scissors2 = r"""
#     -------
# ---'   ----)----
#           ------)
#        ----------)
#       (----)
# ---.--(---)
# """

print("Welcome to Dynasty Tournament Rock Paper Scissors Game")
# userMove = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))

# computer_move = random.randint(0, 2)
# # print(computer_move)

# if (userMove == 0):
#     print("You choose rock")
#     print()
#     print(rock)
#     print("Computer chose:")
#     if (computer_move == 0):
#         print(rock)
#         print("It's a tie.")
#     elif (computer_move == 1):
#         print(paper)
#         print("You lose.")
#     elif (computer_move == 2):
#         print(scissors)
#         print("You win.")

# elif (userMove == 1):
#     print("You choose paper")
#     print()
#     print(paper)
#     print("Computer chose:")
#     if (computer_move == 0):
#         print(rock)
#         print("You win.")
#     elif (computer_move == 1):
#         print(paper)
#         print("It's a tie")
#     elif (computer_move == 2):
#         print(scissors)
#         print("You lose.")

# elif (userMove == 2):
#     print(scissors)
#     print("You choose scissors")
#     print()
#     print("Computer chose:")
#     if (computer_move == 0):
#         print(rock)
#         print("You lose.")
#     elif (computer_move == 1):
#         print(paper)
#         print("You win.")
#     elif (computer_move == 2):
#         print(scissors)
#         print("It's a tie.")
# elif (userMove >= 3 or userMove < 0):
#     print("Oops! You typed an invalid number. You lose.")
# else:
#     print("Oops! You typed an invalid number. You lose.")

# All done by thinking properly. Took over 20 minutes though.

# print(rock)

# Her way, we can actually use and and or, and also some bits of logic too in python 

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer choose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose.")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")