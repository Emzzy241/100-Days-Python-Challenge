#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
# .readlines() Read lines not read line does is it returns all the lines in a file as a list where each line is an item in the list object. Using it, Each line gets added into a list
# .replace() it will replace a specified phrase with another specified phrase. E.g; "I like bananas", txt.replace("bananas", "apples") => I like apples
# .strip() it removes the extra spaces at the beginning and at the end of a string. A space in between another word, this method keeps the space in between the words

# .redlines() method returns a list containing each line in the file as a list item.

# Remember, python constants are defined using CAPITAL LETTERS at the top
PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip() # to take our the new lines that were doing; Dear... and comma on another line
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        # We are still inside our for loop, and that is why we are able to create a file for each individual name inside our invited_names.txt, and we also did something brilliant, utilizing f strings to dynamically change our file names.
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)
        
# And just like that, we automate things up and be able to create many files for many letters.
# Dr. Angela says there is no right solution, but how you thought of thinking, how usable is the code and how efficient is the code
# To quote The godfather of computer programming, Donald Mufe, the guy who wrote; The Art of Computer Programming, and many other books that are super influential and super hard to understand 
# He says; Premature optimization is not a great thing, do not try to make your code the most efficient as possible, instead you should aim for readability
# Can other programmers look at your code and understand what you have done immediately?? If that is true, then you have actually succeeded.
# That is the goal and the bar you should measure your code by. Similar to writing, you write so that other people understand what you are saying.
# Same with programming, its not about shortening your code to the shortest amount of lines, it is about making your code expressive, readable, and as easily understood by as many people as possible.
# Once you've gotten to a Senior Developer, you will now begin to have your own preference on style, syntax, and much more. But at this stage, optimize for readability. Dr. Angela