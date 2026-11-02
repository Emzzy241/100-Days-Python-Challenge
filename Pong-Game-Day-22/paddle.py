from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        # to get all attributes of turtle class, we had to initialize the base class
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        # paddle.goto(350, 0)
        
    def go_up(self):
    # x won't go up. When moving vertically, focus is not on horizontal
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)