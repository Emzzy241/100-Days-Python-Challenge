# # In Python,  the indentation really matters
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))

# if height != 120:
#     print("You can ride the rollercoaster")
# else:
#     print("Sorry you have to grow taller before you can ride.")

# New coding challenge
# print("Welcome to checkerNum")
# number_to_check = int(input("What is the number you want to check?"))

# if number_to_check % 2 == 1:
#     print("It is an odd number")
# else:
#     print("It is an even number")

# Checking the price now, an extra condition in our code.
# Nested if / else statements

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm?"))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("What is your age"))
#     if age <= 12:
#         bill = 5
#         print("Child tickets are $5.")
#     # elif age >= 45 and age <= 55: ... Either this or the one below, but this one is easier to read though.
#     elif 45 <= age <= 55:
#         print("Everything is going to be alright. Have a free ride on us.")
#     elif age <= 18:
#         print("Youth tickets are $7.")
#         bill = 7
#     else:
#         print("Adult tickets are $12.")
#         bill = 12


#     wants_photo = input("Do you want a photo taken? Type y for Yes and n for No.")
    
    
#     if wants_photo == "y":
#         bill += 3
#     print(f"Your bill is: ${bill}")
#     # print(f"Your final bill is {bill}")

# else:
#     print("Sorry you have to grow taller before you can ride.")




# print("Welcome to Python Pizza Deliveries!")
# size = input("what size pizza do you want? S, M, or L: ")
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# # todo: 
# bill = 0
# if size == "S":
#     bill += 15
#     # print(f"You ordered small pizza, your bill ${bill}")
# elif size == "M":
#     bill += 20
#     # print(f"You ordered medium pizza, your bill is ${bill}")
# elif size == "L":
#     bill += 25
#     # print(f"You ordered large pizza, your bill is ${bill}")
# else:
#     print("You typed the wrong inputs.")

# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}.")

# How I did it though:
# if pepperoni == "Y":
#     bill += 5
#     print(f"With pepperoni added , your pizza is now ${bill}")
# elif pepperoni == "N":
#     print(f"Without pepperoni added, your pizza remains ${bill}")
# else:
#     print("You typed the wrong inputs.")

# if extra_cheese == "Y":
#     bill += 5
#     print(f"With extra cheese, your pizza price is now ${bill}")
# elif extra_cheese == "N":
#     print(f"Without extra cheese, your pizza price remains ${bill}")
# else:
#     print("You typed the wrong inputs.")

# Final Project that we will be making though.
print("Welcome to the Treasure Island")
print("Your mission id to find the treasure.")
choice1 = input("You're at a cross_road, where do you want to go? Type 'left'  or 'right': \n").lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake'
                    'There is an island in the middle of the lake.'
                    'Type wait to wait for a host.'
                    'Type "swim" to swim across. \n').lower()
    if choice2 == "wait":
        choice3 = input("You arrived at the island unarmed. There is a house with 3 doors. "
                        "One red, One yellow, One blue. Which color do you choose?: \n").lower()
        if choice3 == "red":
            print("It's a room ful of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print("You entered a room of beasts. Game Over.")
        else:
            print("You choose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game over!")
else:
    print("You fell into a hole. Game Over.")


    # Modify it, and add more conditions or make the game messages better.