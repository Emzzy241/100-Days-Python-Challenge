# Learning errrors and exceptions
# FileNotFound Error
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
    
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
    
# else:
#     content = file.read()
#     print(content)
    
# finally:
#     raise TypeError("This is an error that I made up.")
# doing the above, raising any error whether TypeError or KeyError, or FileNotFoundError, any error we raise at all, our program will be crashed because of this error
    # file.close()
    # print("File was closed")
    
    # pep 8 recommends that we do not use just: except:, but that we use it with a scope.... Using only except is too broad and can cover a lot of cases, but writing clean code? use except specifically for what you want to catch when the code within try block fails
    
# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# IndexError: List index is out of range
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# Life is not always going to go according to how you have planned it or how you think it will go
# Often times, life follows Murphy's Law which states that anything that can go wrong probably will eventually at some point go wrong, so we have to plan for these eventualities
# Just as your car is probably not going to break down, but you need breakdown cover just in case it does break down
# In programming we catch those exceptions... We fail more gracefully and decide what to happen when a failure occurs

# try: Something that might cause an exception

# except: Do this if there was an exception Execute this block od code if something goes wrong

# else: Do this if there were no exceptions, no problems/issues

# finally: To carry out no matter what happens, Do this no matter what happens.... Wether the try code fails or succeed

# raise: finally keyword to raise our own exceptions

# Next Lesson, Raising your own exceptions

# Why might you raise Errors Let's find out with this BMI Program... A height with 3m or more is valid code to computer, gabbage in gabbage out, buuuuuuuttttt!!!!!, it is not possible actually, and hence we raise an error

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human heights should not be over 3 meters.")

bmi = weight / height  ** 2
print(bmi)

# Moving to the NATO project we created some days ago

# A JSON contains a bunch of nested lists and dictionaries, and it has that key-value pair data structure... This is what we are aiming for, to store our data in this format, and load up this daa and search through it for a particular website we wan the information for
# Python has an inbuilt JSON library: json.dump -> Write, json.load() -> Read, json.update -> Update
# Off to the password manager app now... 

# Challenge 2: To Search for a website in the password manager.