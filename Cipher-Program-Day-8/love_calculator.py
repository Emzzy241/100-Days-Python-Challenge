# Love Calculator
# 💪 This is a difficult challenge! 💪 

# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

# 2. Then check for the number of times the letters in the word LOVE occurs.   

# 3. Then combine these numbers to make a 2 digit number and print it out. 

# e.g.

# name1 = "Angela Yu" name2 = "Jack Bauer"

# T occurs 0 times 

# R occurs 1 time 

# U occurs 2 times 

# E occurs 2 times 

# Total = 5 

# L occurs 1 time 

# O occurs 0 times 

# V occurs 0 times 

# E occurs 2 times 

# Total = 3 



# Love Score = 53





# Example Input 

# calculate_love_score("Kanye West", "Kim Kardashian")

# Example Output

# 42





# How to test your code and see your output?



# Udemy coding exercises do not have a console, so you cannot use the input() function. You will need to call your function with hard-coded values like so:



# def calculate_love_score(name1, name2):
#   # your code here
 
# # Call your function with hard coded values
# calculate_love_score("Kanye West", "Kim Kardashian")


def calculate_love_score(name1, name2):
    sum_total = 0
    total1 = 0
    total2 = 0
    for letter in name1:
        if letter == "t" or letter == "r" or letter == "u" or letter == "e":
            total1 += 1
    for letter2 in name2:
        if letter2 == "t" or letter2 == "r" or letter2 == "u" or letter2 == "e":
            total2 += 1 
    sum_total = total1 + total2
    print(total1)
    print(total2)
    print(sum_total)

calculate_love_score("Angela Yu", "Jack Bauer")