


# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     print(key)
#     # pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     print(row)

# Fully understand the above to be able to now be able to start tackling the Todo 1 & 2


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas


# First we read from the csv file
data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data.to_dict())

#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
# {new_item for item in list}
# Equating it now:
# remember that string, list, tuple, range are all series and list comprehension can work on all of them
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)






# Other Learnings from python REPL:
# $ python
# Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# >>> students_scores = {student:random.randint(1, 100) for student in names}
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <dictcomp>
# NameError: name 'random' is not defined
# >>> import random
# >>> students_scores = {student:random.randint(1, 100) for student in names}
# >>> students_scores
# {'Alex': 40, 'Beth': 98, 'Caroline': 86, 'Dave': 4, 'Eleanor': 33, 'Freddie': 33}
# >>> students_scores
# {'Alex': 40, 'Beth': 98, 'Caroline': 86, 'Dave': 4, 'Eleanor': 33, 'Freddie': 33}
# >>> students_scores = {student:random.randint(1, 100) for student in names}
# >>> passed_students = {student:random.randint(1, 100) for (student, score) in students_scores.items if student.score > 30}
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'builtin_function_or_method' object is not iterable
# >>> passed_students = {student:random.randint(1, 100) for (student, score) in students_scores.items() if student.score > 30}
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <dictcomp>
# AttributeError: 'str' object has no attribute 'score'
# >>> passed_students = {student:random.randint(1, 100) for (student, score) in students_scores.items() if student.score > 30}
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <dictcomp>
# AttributeError: 'str' object has no attribute 'score'
# >>> passed_students = {student:score for (student, score) in students_scores.items() if student.score > 30}
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <dictcomp>
# AttributeError: 'str' object has no attribute 'score'
# >>> passed_students = {student:score for (student, score) in students_scores.items() if score >= 30}
# >>> passed_students
# {'Dave': 76, 'Eleanor': 37, 'Freddie': 56}
# >>> exit()

