# Building a Pong Game, this game is much more harder than the snake game actually

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# paddle = Turtle()
screen = Screen()
screen.tracer(0)
paddle_right = Paddle((350, 0))
ball = Ball()
paddle_left = Paddle((-350, 0))
scoreboard = Scoreboard()

screen.setup(width=800, height=600)
screen.bgcolor("black")

screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()
        # To see what is happening to the position of the ball
        # print(ball.y_move)
        # print(ball.x_move)
        # When the ball needs to bounce off the top and bottom wall, we reverse the y-move instead of adding, and that moves it in the opposite direction
        
    # Detect collision with right paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    # Detect when right paddle misses
    if ball.xcor() > 380:
        # restart and put ball at the center
        ball.reset_position()
        scoreboard.l_point()
        # print(ball.x_move)
        # print(ball.y_move)
                
    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        # print(ball.x_move)
        # print(ball.y_move)

screen.exitonclick()