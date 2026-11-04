# Well, we are moving on right on to Day-20... We really need that Day-20 mehn
# I do not yet know what will be learn today, however I am stocked and ready to see what Dr. Angela has for me on Day-20.... Let's go!!!
# But first, I gotta build an Automatic Payment thingy for a Paypal Hackathon. I am off now, but I will be back soon

# We building a snake game, similar to the one of the Nokia 3310. The game can also keep track of the scores, and simulataneously to 
# Breaking it into 7 steps. First Step on Day-1, The 2nd Day wil house the 4 last steps
# On Day-21 we will continue and build the last 4 steps of the game.

# The 7 Steps are:
# TODO-1: Create a snake body
# TODO-2: Move the snake
# TODO-3: Control the Snake
# TODO-4: Detect collision with food
# TODO-5: Create a scoreboard.
# TODO-6: Detect Collision with wall. W
# TODO-7: Detect collision with tail.

# Let us begin....
# TODO-1: Create a snake body


# from turtle import Screen, Turtle --> It has been greyed out, no need for it again... No usage of it in this file
from turtle import Screen
import random
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


# starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# segments = []

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
# screen.onkey("Up")
# screen.onkey(key="Up", fun=snake.up)
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
    

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect collision with food. distance(x, y=None).
    # The distance method works by comparing the distance from this turtle to whatever is put inside the parenthesis
    # x = a number or a pair/vector of numbers or a turtle instance
    # Y = a number if x is a number, else None
    
    if snake.head.distance(food) < 15:
        # print("snake collided with food")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()
    
    # Detect collision with tail.
    # for segment in snake.segments:
    for segment in snake.segments[1:]:
        # a way to bypass the snake head
        if segment == snake.head:
            pass
        # TODO: To slice out the segment actually
        
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            # game_is_on = False
            # scoreboard.game_over()
        # No longer any need for the elif below, just one if is now sufficient
        # elif snake.head.distance(segment) < 10:
        #     game_is_on = False
        #     scoreboard.game_over()
    # if head collides with any segment in the tail:
    # trigger game_over


screen.exitonclick()

