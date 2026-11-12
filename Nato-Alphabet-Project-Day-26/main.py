# On Day-26 we will be learning about Lists and Dictionary Comprehensions... It also helps to cut down a lot of the code we will be writing when we are working with lists and dictionaries
#By the end of today, we will build a project to use the NATO Phonetic Alphabet so that we can spell out various things on the telephone... 
# For example spelling ANGEL, they might not understand your name, so you will say something like; A for Alpha, N for November, G for Golf, E for Echo, Lima, Alpha

# List Comprehension --> It is very unique to the python programming language.
# A List Comprehension is a case where you create a new list from a previous list, previously w did it with for loop


name = "Dynasty"
letters_list = [letter for letter in name]
# print(letters_list)

# Dictionary Comprehensions
# Also super useful... It allows us to create a new dictionary from the values in a list or a dictionary
# new_dict = {new_key:new_value for item in list}
# Taking a step further, creating a new dictionary based off of the values of the previous dictionary
# new_dict = {new_key:new_value for {key,value} in dict.items()}
# new_dict = {new_key:new_value for {key,value} in dict.items() if test}

student_score = {
    "Alex": 89,
    "Beth": 98
}

# Looping through a list
# >>> students_scores = {student:random.randint(1, 100) for student in names}
# {'Alex': 40, 'Beth': 98, 'Caroline': 86, 'Dave': 4, 'Eleanor': 33, 'Freddie': 33}
# Looping through a dictionary
# passed_students = {student:radom.randint(1, 100) for student in students_scores}

# >>> passed_students = {student:score for (student, score) in students_scores.items() if score >= 30}

# Next Lesson: Looping through DataFrames
student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(value)
    
# In a lot of way, you can consider python data frame as a dictionary

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
for (key, value) in student_data_frame.items():
    print(value)
    
# pandas has an in-built loop called iterrows which allows us to loop through each of the rows of the data frame rather than each of the columns
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
    # so each of these rows is a pandas data series object, we can tap into it and get the value under a particular column by using dot notation

# {new_key:new_value for(index, row) in df.iterrows()}
# Take the csv file and do:
# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# TODO 2: Create a list of phonetic code words from a word that the user inputs.