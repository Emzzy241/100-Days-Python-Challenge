# Welcome to Day-13, Today we will be learning about Debugging. Which is the process of removing bugs from your code. Dr. Angela.
# Remember, Testing is the process of hunting for bugs, according to Prof. Amos Bajeh from the University Of Ilorin, My Alumni, and he is an
# astute Professor, and one of the best, he is one of the best Computer Science Professors I ever encountered in the whole world

# Techniques on finding and ridding bugs from our code. Grace Hopper is one who found the very first ever bug. She was one of the first programmers
# and pioneers of the job we are taking now. She found a moth in her code which was found in a relay preventing her code from running properly
# We no longer deal with moths these days, but we still encounter bugs. Everyone gets bugs, we create them, so don't be scared of a bug.

# How t o deal with it:
# 1. Describe the problem

# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")

# my_function()

# Describe th eProblem - Write your answers as comments:
# 1. What is the for loop doing? The for loop is to loop from 1-19
# 2. When is the function meant to print "You got it"? --> The function is meant to print You got it if i equals 20
# 3. What are your assumptions about the value of i? My assumptions about the value i is thinking i will be equal to 20, when we know
# the range() function starts from 1-19, because range(1 = inclusive, 20 = exclusive). The assumption is i will definitely get to 20.
# i will never ever get to 20. So our assumption is never gonna be reached.
# Fix: Change range(1, 21) and not 20. When you face problems, describe it, and test your assumptions and deduce which assumption is actually false.

# Step-2: Reproduce the Bug.
# The reason is if you encounter it once and don't encounter it the next time, that becomes a really difficult bug to fix. 
# These types of error are deadly. The important thing here is to reproduce the error, when does that error actually occur?

# from random import randint
# dice_images = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(0, 5)
# print(dice_images[dice_num])

# randint(a=inclusive, b=inclusive)
# Describing the Problem, lists starts from 0, and ends at 5 (depicting 5 items in the list). But here, we did randint(1, 6), 
# which is terribly gonna fail as soon as we get to the index 6.
# It happens when at 6th position. To reproduce, she did: dice_num = 6, but I did: range(6, 6) to consistently reproduce the error
# Final fix, no matter how many times we run our code, we never get that error again: dice_num = randint(0, 5)

# Step-3: Play Computer: THis skill of pretending to be a computer, reading through your code and imagining what you will do each time
# is a very very useful skill actually. Especially when debugging.
# Millennial, Gen Z. Baby Boomer.

# year = int(input("What's your year of birth? "))

# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year >= 1994:
#     print("You are a Gen Z.")

# Run through the code line by line and evaluate each statement and follow the logic to check what it evaluates to.
# The if statement is similar to specifying a range actually. The range would be 1980 < year < 1994, however the 1994 never
# gets printed out. Looking at the elif too, we are never getting to 1994 itself, it checks if year > 1994.
# That is why when we insert 1994, nothing gets printed out. That is one edge case we did not account for in our code.
# She used True and False to break down the problem actually. Playing computer is similar to evaluating the logic actually.
# year = 1994.

# if True and False:
# elif False:
    # Since no code is left now, nothing gets printed out when year = 1994
# To fix, we simply change any of our conditions (if or elif), and make it <= or >=

# Step-4: FIX THE ERRORS
# When editor or console is given you errors, fix the error first

# try:
#     age = int(input("How old are you? "))
# except ValueError:
#     print("You have typed in an invalid number. Please try again with a numerical response such as 15.")
#     age = int(input("How old are you? "))



# if age > 18:
#     print(f"You can drive at age {age}")

# The first error, compile-time error, not indenting the print statement very well above,
# The second error was now a run-time error, user supplied the value: twelve as their age, which caused our program to crash 
# TO fix the error, she went to copy: ValueError: invalid literal for int() with base 10:, not ValueError: invalid literal for int() with base 10: 'twelve'
# Because that 'twelve' is specific to your code actually, and she pasted the error in Google, and added 'python' The programming language.
# A Stack Overflow helped out. The computer doesn't know how to turn 'twelve' to 12, the integer.
# Easiest way is to tell user not to do that, but you cannot really control users... Let us explore the try...catch block.
# We can catch that error so it won't destroy our code. So we take the dangerous code line.

# Note, the errors don't always help you with debugging, these are the most frustrating errors here, because nobody is helping you out here.
# There is no errors you can check, no red lines, nothing nothing, just rely on your strength as a programmer
#     print("You can drive at age {age}")
# Experience comes in really handy with debugging, the more bugs you solve, the better you get at it.
# Go on Stack Overflow, and see if you can help in solving people's bugs.

# Step-5: print() statement, print() is your friend. It will help you to debug your code.

# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(f"Number of pages {pages}")
# print(f"Number of words per page:  {word_per_page}")
# print(total_words)
# print("Number of words per page: " + pages)

# Our assumption is that the total words will be printed out, which is not so actually. The line: word_per_page == int(input("Number of words per page: "))
# Is not equating word_per_page, it is comparing word per page with the value user enters in.It evaluates if 0 == 250 (if we enter 250)

# Step-6: Use a Debugger. Pythontutor.com, and using debugger in thorny.

import random
import maths

def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])

# She used debugger in pycharm, debuggers in these IDEs are very similar actually. A break point can be created in the gutter of our code
# A break point puts a break on the code at that particular line. Step-Over and Step-Into was done on PyCharm actually.
# Our goal: Step into other files written by us. We used Step-Into-My-Code button, which ignores the library functions, that library function right there.
# Also, he Threats & Variables and Console tabs can help in PyCharm. We can use THreats & Variables to trace the values for our loops
# The other tab is the console, which shows what gets printed. THe most useful thing is being able to see these values as you go from step to step.
# In VSCode, the step into under debugger works as Step-Into-My-Code button similar to pycharm, and does not step into the module
# The problem was that we are overwriting what is in new_item, check this line:     b_list.append(new_item)
# It is only after we have broken out of the loop that we then append the latest value of new_item into  ur b_list.
# The issue was actually with indentation, we are supposed to indent the append into the b_list upon every new_item value that is generated, and not the final new_item value
# The Debugger is very useful, it is almost as if you put a print statement on every line of your code, and you can isolate it properly, and deduce what each og the values are.


# Debugging Final Tips:
# 7. Take a break. Keep string at the code won't give you the answer
# 8. Ask a Friend, not your friend print(), but an actual human. A friend looking at your code won't make same assumptions you are making, and it is vice versa.
# 9. Run Often, run your code often. Don't wait after you are done, from time to time, keep running your code. Better to solve tiny tiny bugs than a 100 bugs at once
# 10. Stack Overflow, a way you come across with other Developers and you can ask the Oracle, Stack Overflow. Only ask on Stack Overflow when you are certain no one else has encountered your own bug.
# Everyone gets bugs, keep creating bugs, keep creating them, you will only get better at solving them. Come back to tis lesson if you are facing a bug.
# Every bug you catch is like lifting a dumb bell in the gym. The more reps you do, the better you get. 
# Confidence is earned, keep solving problems and you've gat this. You still have lots of challenges to solve mehn. Will come back to solve them all pretty soon.