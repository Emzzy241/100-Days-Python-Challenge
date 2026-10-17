import art
# Day10, lessons to be learnt: Functions with outputs

# Starting first video, we talk more on functions. We have explored 2 types of cunctions: 
# Functions that stand alone
# Functions that allows for inputs, gives ability to modify input, and depnding on final.

# This function


# def my_function():
#     result = 3 * 2
#     return result

# def format(f_name,l_name):
#     return f_name + l_name

# print(my_function())

# Now Starting out immediaely

# def format_name(f_name, l_name):
#     return (f_name + l_name).title()

# print(format_name("rhoda", " SANDRA"))

# def format_name(f_name, l_name):
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()

#     return f"{formatted_f_name} {formatted_l_name}"
#     # print(f"{formatted_f_name} {formatted_l_name}")

# formatted_string = format_name("rhoda", "SANDRA")
# print(formatted_string)

# output = len("Dynasty")

# return can be used in multiple spaces of our code

# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You did not provide valid inputs" # This line escapes the function and escape the function early
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"Result: {formatted_f_name} {formatted_l_name}"

# print(format_name(input("What is your first name?"), input("What is your last name?")))

# Moving on to DocStrings, I think it is the Lecture before we finally begin building our calculator App.

# def outer_function(a, b):
#     def inner_function(c, d):
#         return c + d
#     return inner_function(a, b)
# result = outer_function(5, 10)
# print(result)

# def inner_function(c, d):
#         return c + d
#     return inner_function(a, b) 
# Easy to understand, the inner function was broken out of very early, actually, and the outer_function was then broken out of with the line:
# return inner_function(a, b) .... The output of the outer function is the function being called, 
# and passing in the parameters, a, b which is 5, 10.
# From Udemy, a = 5, which means c = 5. b = 10. which means d = 10. The output of inner_function becomes the output of outer_function.
# I broke down the code into chunks and was able to fully understand it, separating the functions actually.

# def my_function(a):
#     if a < 40:
#         return
#         print("Terrible")
#     if a < 80:
#         return "Pass"
#     else:
#         return "Great"
# print(my_function(25))
# Explanation: The return keyword will exit the function and prevent the rest of code from being executed.

# Now, Now we feast, and we get right into the building the actual Calculator Program.

# def add(n1, n2):
#     return n1 + n2

# # Note, to store a function 

# my_favorite_operation = add

# print(my_favorite_operation(2, 3))

# Back right into it now,
# TODO: Write out the other 3 functions: subtract, multiply, and divide.
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values, keys = "+", "-", "*", "/"

operations = { 
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
# remember not to trigger the functions with parenthesis, this is because we are storing it, and not actually making use of it just yet. 
# No need for parenthesis for now

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 by 8 using the dictionary
print(operations["*"](4, 8))

# TODO: Final lap, let us now build out out application. And build out all functionality labeled with bullet points
# First, Program asks user to type first number, then what operation, then asks for second number.

# print("Welcome to the calculator App :-)")
# first_number = float(input("Enter the first number: "))
# operation_to_perform = input("Enter the operation you would like to perform: '+', '-', '/', '*' ")
# second_number = float(input("Enter the second number: "))

# if operation_to_perform == "+":
#     result = operations["+"](first_number, second_number)
#     print(result)
# if operation_to_perform == "-":
#     result = operations["-"](first_number, second_number)
#     print(result)
# if operation_to_perform == "/":
#     result = operations["/"](first_number, second_number)
#     print(result)
# if operation_to_perform == "*":
#     result = operations["*"](first_number, second_number)
#     print(result)

def calculator():
    should_accumulate = True

    print("Welcome to the calculator App :-)")
    first_number = float(input("Enter the first number: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_to_perform = input("Enter the operation you would like to perform: ")
        second_number = float(input("Enter the second number: "))
        answer = operations[operation_to_perform](first_number, second_number)

        print(f"{first_number} {operation_to_perform} {second_number} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start afresh. ")

        if choice == "y":
            first_number = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()

# Another attempt would have been wrapping everything inside another while loop, that is also correct
    # My attempt
# def continue_calculation(last_result):
#     operation_to_perform = input("Enter the operation you would like to perform: '+', '-', '/', '*' ")
#     second_number = float(input("Enter the second number: "))

#     if operation_to_perform == "+":
#         result = operations["+"](last_result, second_number)
#         # print(result)
#     if operation_to_perform == "-":
#         result = operations["-"](last_result, second_number)
#         # print(result)
#     if operation_to_perform == "/":
#         result = operations["/"](last_result, second_number)
#         # print(result)
#     if operation_to_perform == "*":
#         result = operations["*"](last_result, second_number)
#         # print(result)
#     # should_accumulate = False


#     return f"The Result is: {result}"
# def calculator(first_number, second_number):

    # if operation_to_perform == "+":
    #     result = operations["+"](first_number, second_number)
    #     # print(result)
    # if operation_to_perform == "-":
    #     result = operations["-"](first_number, second_number)
    #     # print(result)
    # if operation_to_perform == "/":
    #     result = operations["/"](first_number, second_number)
    #     # print(result)
    # if operation_to_perform == "*":
    #     result = operations["*"](first_number, second_number)

        # print(result)
    # should_accumulate = False
    # print(result)
    # return f"The result is: {result}"

        # while should_accumulate:
    # return result
# print(calculator)
# result_from_calculation = calculator(first_number=first_number, second_number=second_number)
# # result_from_calculation = calculator()
# # Bullet Points 1-4 all done, and working.
# user_wants_to_continue = input(f"Would you like to continue with {result_from_calculation}, previous result? Type 'y' for yes and 'n' for no")

# while should_accumulate:
#     if user_wants_to_continue == "y":
#         should_accumulate = True
#         continue_calculation(calculator(first_number=first_number, second_number=second_number))

#     elif user_wants_to_continue == "n":
#         print("Let us now perform a new calculation...")
#         calculator()