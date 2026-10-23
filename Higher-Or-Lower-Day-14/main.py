# Building the Higher or Lower Game
# I couldn't spend an hour tackling this game due to power issues mehn, but the game really does seem easy
# from game_data import data 
# from art import logo
# import random

# print(logo)

# # Generate a Random number we will use to look-up things
# account_a =  random.choice(data)
# account_b =  random.choice(data)

# print(account_a)
# print(account_b)

# guess = input("Enter who you think has more followers")

# def check_answer(guess, a_followers, b_followers):
#     if a_followers > b_followers:
#         print("You got it right.")
#         return guess == "a"
#     print("You got it wrong.")
#     return guess == "b"

# print(data[0])

# Breaking the problem down with Dr. Angela

# Display art
from art import logo, vs
from game_data import data
import random

"""Format the account data into printable format."""
def format_data(account):
    """Takes the account data and returns the printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_description}, from {account_country}")

def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and returns if they got it right or wrong"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

print(logo)
score = 0
game_should_continue = True

account_b = random.choice(data)

while game_should_continue:
    # Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    # Ensuring account a and b are not the same
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    # Format the account_data into a printable format


    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Clear the screen
    print("\n" * 20)
    print(logo)

    # Check if user is correct.
    ## Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    ## Use if statement ot check if user is correct.
    if is_correct:
        score += 1
        print(f"You're right!. Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score {score}")
        game_should_continue = False
# Give user feedback on their guess.

# score keeping
# did with score 

# Make the game repeatable.
# Done with the while loop

## Move the previous account at B to the position A if they get it right
# Last but not the least

# A tiny guide for writing docstrings in python, determine what are its inputs, and what are the functions outputs.