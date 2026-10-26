# Today we wil be learning about OOP right in python
# Already began on me notes and me iPad (iPhone), done and done.... Let us continue here now.

# import turtle
# from turtle import Turtle, Screen

# # timmy = turtle.Turtle()
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# print(timmy.position())

# # Object Attributes
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# Exploring python packages
# print("|")

# instead of having to do prettytable.PrettyTable multiple times.
from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)