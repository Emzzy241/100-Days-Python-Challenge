# import colorgram

# # Extract 6 colors from an image.
# colors = colorgram.extract('./image.jpg', 40)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
    
# print(rgb_colors)
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(124, 181, 211), (199, 174, 15), (247, 226, 234), (222, 232, 240), (26, 121, 168), (178, 13, 44), (237, 204, 87), (239, 148, 73), (220, 122, 162), (232, 241, 235), (25, 144, 72), (216, 80, 124), (7, 172, 211), (214, 59, 26), (66, 21, 54), (239, 77, 44), (247, 156, 189), (8, 184, 151), (161, 56, 107), (10, 30, 72), (74, 28, 23), (128, 208, 234), (13, 48, 132), (167, 193, 164), (101, 116, 184), (252, 156, 151), (167, 24, 19), (3, 88, 57), (111, 217, 215), (4, 73, 47), (182, 183, 209), (10, 89, 105), (239, 199, 12), (86, 79, 20)]
# got rid of first color: (244, 242, 238)

# Now let us begin work and create our hirst painting. Paint a painting by 10X10 rows of spots. 
# Look at documentation of turtle, how to move, and how to be able to create these painting. From documentation, we have a .dot(size, color)

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    
    if dot_count % 10 == 0:    
        # turning the turtle to the left
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)

        # Moving it forward
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()

# doing for _ if you have nothing to put in it.

# By simplifying doing tim.penup... By drawing dots, we do not need our pen to go down at all, it all just works.... No need to add pendown again
# Making the turtle hide. show_title(), hide_turtle()
# Well, after over 5 hours, one is finally done with Day-18.... Day-18 really really pushed me mehn, I just went harder. We thank God for strength.
# I still gotta explore many of the things I actually learnt in this project.... A perfect example is that python package called colorgram
# Ability to extract colors, not even near colors but very very similar colors. That is just actually mind blowing mehn.... I gotta study it properly, use on different images,
# And essentially get very better at python. All these skills actually ad up to each other mehn, and yeah.... The Season Of Crackness is still upon us mehn. We keep pushing.
