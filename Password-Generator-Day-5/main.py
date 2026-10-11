# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")
# print(fruits)

# First coding challenge for Day-5

# student_scores = [150, 142, 185, 120, 184, 149, 24, 59, 68, 78, 65, 89, 199]

# total_exam_score = sum(student_scores)
# print(total_exam_score)

# sum = 0
# # replicating the sum functionality.
# for score in student_scores:
#     sum += score
# print(sum)

# Challenge: Replicating the max() function using all that has been learnt so far.
# print(max(student_scores))

# max = 0
# for score in student_scores:
#     if score >= 199:
#         max = score
#     else:
#         max += score
# print(max)... Given the case where you don't even know he maximum number in the array.

# Dr. Angela way
# max_score = 0
# for score in student_scores:
#     if score > max_score: # At first stage, the max_score is still zero, while the first score in the student_scores is 150
#         max_score = score

# print(max_score)

# for loops and the range() function

# for number in range(1, 11, 3):
#     print(number)

# Solving the gauss challenge
# sum = 0
# for number in range(1, 101):
#     sum += number
# print(sum)

# Final Challenge of the day
import random

# A complete list of alphanumeric characters and standard password symbols
lowercase_letters = [
    # Lowercase letters (a-z)
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
]

uppercase_letters = [  # Uppercase letters (A-Z)
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

    # Numbers (0-9)
numbers = [   '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    # Common Special Characters / Symbols
special_characters =[ '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
    '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', 
    ',', '.', '<', '>', '/', '?', '|', '\\', '~', '`', '"', "'"
]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', 
    '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', 
    ',', '.', '<', '>', '/', '?', '|', '\\', '~', '`', '"', "'"]

nr_letters = int(input("How many letters would you like in your password? \n"))
nr_symbols = int(input("How many numbers would you like? \n"))
nr_numbers = int(input("How many numbers would you like? \n"))

# Easy level
password = ""

# for char in range(1, nr_letters + 1):
#     # 1 - 4
#     # random_char = random.choice(letters)
#     # password += random_char # A shorter version now
#     password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#     password += random.choice(numbers)

# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# print(password)

# Making the code a lot tidier now
# for char in range(0, nr_letters):
#     password += random.choice(letters)

# for char in range(0, nr_symbols):
#     password += random.choice(special_characters)

# for char in range(0, nr_numbers):
#     password += random.choice(numbers)

# print(password)

# Hard
# Tackling the hard level. Instead of using a string, and concatenating thing in it, use a list. Instead of adding it to a string, we add it into a list
password_list = []

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(special_characters))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")


# print("Welcome to the PyPassword Generator!")
# letter_numbers = int(input("How many letters would you like in your password?"))
# symbol_numbers = int(input("How many numbers would you like?"))
# numbers = int(input("How many numbers would you like?"))

# password_ans1 = lowercase_letters[random.randint(1, 26)]
# password_ans2 = uppercase_letters[random.randint(1, 26)]
# password = "abc"
# print(f"Here is your password: {password_ans1} {password_ans2}")
# Let's just watch the video quickly, I have to get going to church
