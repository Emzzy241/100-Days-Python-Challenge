# Today we will be using pandas, one of python's most popular modules... 
# comma separated values is the abbreviation of csv

# # read() took care of this:
#  python main.py
# ['day,temp,condition\nMonday,12,Sunny\nTuesday,14,Rain\nWednesday,15,Rain\nThursday,14,Cloudy\nFriday,21,Sunny\nSaturday,22,Sunny\nSunday,24,Sunny']

# # But readlines took care of this one
# User@Dynasty MINGW64 ~/Desktop/Mini-Desktop/100DaysOfCode-Dr. Angela Yu/US-States-Game-Day-25 (main)
# $ python main.py
# ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']


# weather_list = []

# with open("weather-data.csv") as data_file:
#     contents = data_file.readlines()
#     weather_list.append(contents)
#     print(contents)
    
    
# To manually clean the items in our list, it will take time, instead we used an in-built handler that can handle python files
# import csv


# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)

# pandas, a python data analysis that is super helpful & powerful to perform data analysis with python
# pandas.pydata.org, pandas is well documented actually

# import pandas

# Thew only thing that is not optional to pass into pandas.read_csv() is the path to our csv file
# data = pandas.read_csv("weather-data.csv")
# print(type(data))
# print(type(data["temp"])) # a series data type
# Python identifies the column and then is able to print it out for us.... It is doing this in a smart way by taking the column and then automatically printing the items under that column
# pandas knows how to find the data by just specifying the column name... 3 lines as opposed to 7 lines actually
# In pandas docs, 2 major data types: Series and DataFrame. A DataFrame is equivalent to your whole table, so every single sheet (excel sheet or google sheet ) is a dataframe
# print(type(data)) # a dataframe data type
# print(type(data["temp"])) # a series data type

# The series, the other pandas datatype is equivalent to a list, it is similar to a single column in your table 
# whole table is like a dataframe in pandas... A dataframe can actually be converted to different formats using various methods.

# data_to_dict = data.to_dict()
# # print(data_to_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# average = sum(temp_list) / len(temp_list)
# print(average)

# Alternatively, it can be done like this:
# print(data["temp"].mean())
# ... iN ADDITION TO THE mean, you can get other things like the median, the mode, etc, jst by calling the right method on the data series
# print(data["temp"].max())

# print(data["condition"])

# print(data.condition)

# Note, you column name must match your key; e.g; Condition must not be: condition

# getting rows
# print(data[data.day == "Monday"])

# for temp in data["temp"]:
#     if temp == data["temp"].max():
#         print(data.day == )
#     else:
#         continue

# accessing and printing the data 
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# # How to create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# Handling the large squirrel data in .csv format
# figuring out how many squirrels that we have based on their color

import pandas

data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv") # after reading the csv file, we now have the dataframe and from that we can get what we need
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)

# constructing our dataframe after getting our values
data_dict = {
    "Fur_Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

# print(data_dict)
# Now turning our dictionary into a dataframe
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")