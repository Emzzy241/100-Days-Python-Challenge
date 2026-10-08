# # Subscripting
# print("Hello"[-5])

# # String
# print("123" + "345")

# # Integer -> whole numbers
# print(123 + 345)

# # Large numbers
# print(123_456_789)

# # float = floating point number
# print(3.14159)

# # Boolean
# print(True)
# print(False)

# print(len("12345"))

# print(type("Hello"))
# print(type(12345))
# print(type(123_456_678.765))
# print(type(True))
# print(int('123') + int("456"))

# # print("Number of letters in your name: " + str(len(input("Enter your name"))))

# # or breaking things down:
# name_of_the_user = input("Enter your name: ")
# length_of_name = len(name_of_the_user)

# print(type("Number of letters in your name: ")) # str
# print(type(length_of_name)) # int

# print("Number of letters in your name: " + str(length_of_name))

# Mathematical Operations... Still in Day-2

# print("My age: " + str(12))
# print(123 + 456)
# print(7 - 3)
# print(3 * 2)
# print(2 ** 4) # 2 raised to the power of 4, 
# print(type(6 // 3))

# # PEMDAS: The Order of priority
# # ()
# # ** exponents
# # * or /
# # + or -

# print(3 * 3 + 3 / 3 - 3)

# 2nd to the last lecture

# bmi = 84 / 1.65 ** 2
# print(bmi)
# print(int(bmi))
# print(round(bmi))
# print(round(bmi, 2))

# Assignment operator, allows to accumulate the result of our operation
# score = 0
# score += 1
# print(score)

# FStrings
# print("Your score is: " + score)

# score = 0
# height = 1.0
# is_winning = True

# print(f"Your score is = {score}. Your height is {height}. You are winning is {is_winning}")

# name=input("What is your name?")
# print(f"Hello, {name}")


# Final Challenge: The Tip Calculator
# print(150 * 1.12 / 5)

# My Way:
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip_amount = float(input("How much tip would you like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill? "))
amount_each_person_pays = round((total_bill * (1.0 + (tip_amount / 100)) / total_people), 2)
print(f"Each person should pay: ${amount_each_person_pays}")


# How she did it:
print("Welcome to the another tip calculator")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")

# Day-2 // Completed
