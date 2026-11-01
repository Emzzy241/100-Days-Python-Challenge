from turtle import Turtle
import random

class Food(Turtle):
    # Food renders itself on screen, everything a snake touches it, the food moves to another location on screen
    def __init__(self):
        # calling turtle's init method into the food class
        super().__init__()
        self.shape("circle")
        self.penup()
        # By default it is 20 by 20, with the below, we make it 10 by 10
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        
        # All of the above will be initialized, anything we initialize a new food object from the food class
        # when you initialize a new object from the class, the init gets called.
        
        # refresh, and not reset please (reset is one of he methods in turtle class that we inherited)
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)