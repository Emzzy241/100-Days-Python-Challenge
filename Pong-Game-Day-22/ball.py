from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        # The below keeps printing 10
        # print(self.y_move)
        # print(self.x_move)
        # But as soon as we bounce() the ball, it gets multiplied by -1, and the ball starts moving in the wrong direction
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        # An high school math to get our pong program to start moving in the right direction
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1
        # print(self.x_move)
        # print(self.y_move)
        self.move_speed * 0.9
        

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()