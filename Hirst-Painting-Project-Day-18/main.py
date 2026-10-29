# Welcome to Day-18, Let us nw do some paintings!!! Whoosh!!!

# Today, we will be learning about; Turtle Graphics, Tuples, and Importing Modules
# A Damien Hirst Painting was sold for 1.2 million Dollars, We will be using python turtle to build amazing artwork.
# from turtle import Turtle, Screen
import turtle as t
import random

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# # timmy_the_turtle.forward(100)
# # timmy_the_turtle.right(90)
# # timmy_the_turtle.left(100)
# # timmy_the_turtle.left(100)


# # fIRST CHALLENGE
# # timmy_the_turtle.forward(100)
# # timmy_the_turtle.right(90)
# # timmy_the_turtle.forward(100)
# # timmy_the_turtle.right(90)
# # timmy_the_turtle.forward(100)
# # timmy_the_turtle.right(90)
# # timmy_the_turtle.forward(100)

# for _ in range(4):
#     timmy_the_turtle.right(90)
#     timmy_the_turtle.forward(100)
# # timmy_the_turtle.

# Second challenge: Draw a Dashed Line

# tim = Turtle()

# keep_drawing = 0

# tim.forward(10)
# tim.penup()
# tim.forward(10)
# tim.pendown()

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
    
# Re-Writing it using while loop now.
# while keep_drawing < 15:
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     keep_drawing += 1

# tim.pendown()
# tim.forward(5)
# tim.gap(10)

# for _ in range(51):
    # tim.forward(10)
#     tim.dot(10, "red")
  
 
 
#  Challenge 3: Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon & decagon... Each side should be 100 
# NOTE: Each side that we are required to draw, when we divide 360 degrees by number of sides, we get the angle needed to rotate
 
tim = t.Turtle()
t.colormode(255) 

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

random_color()

# first is triangle
# 360/3 = 180

# tim.forward(100)
# tim.right(45)
# tim.forward(100)
# tim.left(45)
# tim.forward(100)

# tim.forward(100)
# tim.right(120)
# tim.forward(100)
# tim.right(120)
# tim.forward(100)

# tim.left(150)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)

# tim.forward(100)
# tim.left(30)
# tim.forward(100)
# tim.left(120)
# tim.forward(100)

# # For hexagon now

# tim.forward(100)
# tim.right(60)
# tim.forward(100)
# tim.right(60)
# # Continue the pattern...


# Correction:
# num_sides = 5
# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# def draw_shapes(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         tim.forward(100)
#         tim.right(angle)
    
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shapes(shape_side_n)


# Challenge 4: Draw a Random Walk... Random Walk is used many a time in Mathematics to view different real world status. For example, 
# the financial status of a gambler, the path of a molecule in liquid or gas.
# Program your turtle into a random walk, speed up your turtle so it can walk faster
# Still using our colors list

# directions = [0, 90, 180, 270]  # 0 is facing East, 90 is facing North, 180 is facing West, 270 is facing South... From the East-to-the-West-to-the-North-to-the-South
# tim.pensize(15)
tim.speed("fastest")

def draw_spiral_graph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        # current_heading = tim.heading()
        tim.setheading(tim.heading() + size_of_gap)
        
draw_spiral_graph(5)

screen = t.Screen()
screen.exitonclick()

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
    

# Challenge 5: Make a Spirograph
    
# To thicken our color 
# To speed our colors movement, the animation speed of turtle as it draws.
    
# tim.left(82)
# tim.forward(100)
# tim.forward(100)
# tim.left(100)
# tim.forward(100)
# tim.right(90)
# tim.left(100)
# tim.left(100)
# tim.forward(100)

# Finally moving to the actual Hirst Project,

# Damien Hirst, sells arts that look really simple but are not though.
# We used colorgram, a package that extracts colors from python. We searched: Hirst Color Painting

 
# # timmy_the_turtle.up()

# # Importing modules

# import heroes

# print(heroes.gen())



# Put it at the end
# Programmers figure out how to use modules using the documentation. 
# No need to read the entirety of the documentation, you can use it hand in hand with Stack Overflow
# Put the keyword needed, and at the end, type in: Stack Overflow
# TK is short for the module TK Interface.
# TK can be used to create a Graphical User Interface. Think back to the Apple Lisa 1m first ever interface with a GUI
# Before GUI, we had TUI, Terminal User Interface. GUI can show images, allow clicks, drag-and-drop, and much more instead of just accepting texts like TUI
# READING DOCUMENTATION IS A KEY SKILL FOR DEVELOPERS... THESE CHALLENGES CAN LEAD TO STRUGGLE, BUT STRUGGLE IS GOOD. MORE STRUGGLE, MORE STRENGTH
# PYCHARM HAS A VERY SIMPLE WAY OF CHANGING THE NAME OF AN IDENTIFIER.

# screen = Screen()
# screen.exitonclick()

# print()