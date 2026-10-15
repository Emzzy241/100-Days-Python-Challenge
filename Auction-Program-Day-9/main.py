# Day-8 of 100DaysOfCode
# Dictionary and Nesting

from art import logo

# A gavel built out of ascii is the logo of our program
# There are loud and silent auctions actually.
# A simple program, everybody drops their own bid and our program prints out who bid the highest and give us a winner

# First Dictionaries, and even mostly Dictionaries, then later we will also be exploring Dictionaries

# Dictionaries in python, similar to dictionaries in real life.
# Dictionaries allow us to group together and tag related pieces of information.
# A great way to think about dictionaries in form of a table where every dictionary has 2 parts in it.

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you easily call over and over again",
# }

# # print(programming_dictionary)

# programming_dictionary["Loop"] = "The action of doing something over and over again"
# # print(programming_dictionary)

# empty_dictionary = {}

# programming_dictionary = {}
# print(programming_dictionary)

# programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

# Looping inside a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nested List in Dictionary

# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"]
# }

# print lille 
# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
# Challenge-2 print out letter D from nested_list

# print(nested_list[2][1])

# travel_log = {
#     "France": {
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 8
#     },
#     "Germany": {
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#          "total_visits": 5
#     }
# }

# print(travel_log["Germany"]["cities_visited"][2])

# For the Quizzes in Day-9
# dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3
# }

# # for key in dict:
# #     dict[key] += 1
# #     print(dict[key])

# # print(dict[1])

# order = {
#     "starter": {1: "Salad", 2: "Soup"},
#     "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
#     "dessert": {1: ["Ice Cream"], 2: []}
# }

# print(order["main"][2][0])

# FInally building a blind Auction Program
# Clears entire screen so other people cannot see my own bid and if there is still another person that wants to build, it clears person-b's bid
# At the end, we type n for no more bids, and the person with highest bid gets given the program.
# Your version of the code, print out a new line character, because there might be a big issue with clearing the screen and it still remembers someone's bid.
# For we, we should do: print("\n" + 100)

# print("Hello")
# print("\n" * 100)
# print("Hello, once again.")
# I need an ascii art of the gavel to store in my art.py file
# Create a dictionary where each peron's name is the key, their bid is now the value to that key.

print(logo[0])
print("Welcome to the Blind Auction Program")
print("Let us begin to get our bidders in")

# add_more_bidders = True


# print(bidders)

# The bids should be outside the while loop to prevent always creating a new bids dictionary

bids = {}

# list_of_bid_prices = []

# Functionality for comparing bidders
# Will rewrite my own function
# def find_highest_bidder(bidding_dictionary):
#     for bidder in bidding_dictionary:
#         bid_amount = bidding_dictionary[bidder]
#         list_of_bid_prices.append(bid_amount)
#         print(max(list_of_bid_prices))
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")
            # My code below also works
            # list_of_bid_prices.append(bid_amount)
            # highest_bid = bid_amount
            # print(highest_bid)
            # print(max(list_of_bid_prices))
        # if bidding_dictionary[bidder]:
        #     print(bidding_dictionary[bidder])


continue_bidding = True

while continue_bidding:
    name = input("Enter the name of the bidder \n")
    price = int(input(f"Enter {name} price \n"))
    bids[name] = price
    should_continue = input("Are there any more bidders? Type 'yes' or 'no' \n")
    if should_continue == "no":
        # print(bids)
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n" * 100)
        # break
        # name = input("Enter the name of the bidder \n")
        # bid = int(input(f"Enter {name} bid \n"))
        # add_should_continue = True
    # else:
        # bidders = {name1: bid1}
        add_more_bidders = False
    # print(bidders)


