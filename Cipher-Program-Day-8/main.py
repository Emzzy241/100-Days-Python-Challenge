# Today, we will be finally building the caesar cipher program actually.
# First, functions with inputs.

from art import logo
# def greet():
#     print("Hello there")
#     print("How do you do?") # nobody in Britain actually says this
#     print("Isn't the weather nice?") # A greeting you will hear a lot in Britain

# greet()


# Function that allows for inputs

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")

# name is the parameter, the argument is the actual piece of data being passed into a function.
# For example, something = 123, here, the parameter is something, and the argument is 123... 
# Parameter is the name of that data., that is the difference. The argument is the actual value of the data. KNOW WHAT THEY MEAN.

# greet_with_name("Gilfoyle")

# 3rd for Day-8, we go even further and create a function with more than 1 input
# def greet_with(name, location):
#     print(f"Hi there, my name is {name}, and I am located in the {location}")

# def greet_with(name, location):
#     print(f"Hello {name},")
#     print(f"What is it like in {location}")

# greet_with(name="Emmanuel", location="UK") # This can make your line of code longer though, and you will now be the one to decide which one you want to stick with 

# Positional Argument, in python
# Keyword Arguments, with this, instead of just adding the arguments anyhow, we can add the parameter name in front of these arguments
# Just to provide better information. With keyword arguments, now, people would know which argument comes first, and which one comes last.
# TODO: Love Calculator and the one before it though...

# Time to tackle the Caesar Cipher. Caesar Cipher is this way of encoding texts, that was seen as early as during the time of Julius Caesar
# So when he had this top secret military messages, he will shift each letter of the alphabet by a certain predetermined amount.
# How it works, to code the letter E from ABCDEFGH, AT THIS POINT
# Check your note from time to time.... Let us break this problems into chunks now. 

# TODO-1: Create a function called "encrypt()" that takes "original_text" and "shift_amount" as 2 inputs.
# TODO-2: Inside the "encrypt()" function, shift each letter of the "original_text" by the shift amount and print the encrypted text.
# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?, it gave us an index out of range error.
# TODO-3: Call the "encrypt" function and pass in the user inputs. You should

# To complete the task, you need a built-in function called index which allows us to find the position of any item in a list.
# fruits = ["Apple", "Pear", "Orange"]
# print(fruits.index("Pear"))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# alphabet_lowercase = [chr(i) for i in range(ord('a'), ord('z') + 1)]
# print(alphabet_lowercase)


# TODO-2: hello 2
# def encrypt(original_text, shift_amount):
#     ciphered_output = ""

#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         # shifted_position = shifted_position % len(alphabet)
#         shifted_position %= len(alphabet) # Fixes TODO-4
#         ciphered_output += alphabet[shifted_position]
#         # "Take the current shifted_position, divide it by 26 (the length of the alphabet), and replace it with the remainder.", By finding the remainder, your code forces the index to gracefully loop right back to the beginning of the alphabet loop without breaking!

#     print(f"Here is the encoded result: {ciphered_output}")

#     # print(original_text)
#     # print(shift_amount)
#     # print(f"Here is the encoded result: {ciphered_output}")

# encrypt(original_text=text, shift_amount=shift)

# Done with STage-3, our program can now encode a text, now we need it to be able to decode a text.
# The decryption part of our program.

# TODO-1: Create a function called "decrypt()" that takes "original_text" and "shift" 2 inputs
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' backwards in the alphabet
# by the shift amount and the decrypted text.
# TODO-3: Combine the encrypt() and decrypt() functions into one function called 'caesar()'
# Use the value of the user chosen 'direction' variable to determine which function to show

# def decrypt(original_text, shift_amount):
#     decrypted_output = ""

#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         decrypted_output += alphabet[shifted_position]

#     print(f"Here is the decoded result: {decrypted_output}")


# decrypt(original_text=text, shift_amount=shift)



# def caesar(direction):

#     if direction == "encode":
#         encrypt(original_text=text, shift_amount=shift)
#     elif direction == "decode":
#         decrypt(original_text=text, shift_amount=shift)
#     else:
#         print("Sorry, I did not get that. Kindly try again")
# caesar(direction)
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
                            shift_amount *= -1 # This changes the sign
                            # This was inside the forloop, which means that every time, it flips and runs again, and keeps negating the sign.
    
    for letter in original_text:
        if letter not in alphabet:
            print("Sorry, what you entered is not an alphabet, try again")
            return
        else:
            shifted_position = alphabet.index(letter) + shift_amount # Now, we use plus, because we now know if it is decode, that the sign will change
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")

should_continue = True
while should_continue:
    print("Welcome to Caesar Cipher, what would you like to do today?")
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ["encode", "decode"]:
        print("Sorry, I did not get that. Exiting the App. Try Again")
        break 
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart_app = input("Would you like to go again?: enter 'yes' to go again or 'no' to end program: \n").lower()
    if restart_app == "yes":
        should_continue = True
    elif restart_app == "no":
        should_continue = False
        print("Bye Bye :-(")
    else:
        print("Sorry, I did not get that, try again.")



# print()
# print("")

# if restart_app == "no":
#     should_continue = False
#     print("Goodybye :-(")
# if restart_app == "yes":
#     should_continue = True
# elif restart_app == "no":
#     should_continue = False
#     print("Bye Bye :-(")
# else:
#     print("Sorry, I did not get that, try again.")
# Stage-3: TODOs
# TODO-1: Import and print the logo from art.py when the program starts.

# TODO-2: What happens if the user enters a number/symbol/space
# TODO-3: Cam you figure out a way to restart the cipher program