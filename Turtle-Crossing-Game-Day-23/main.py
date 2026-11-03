import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) # To Turn off the tracer

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Creates one car every 0.1 seconds (not point 1 seconds)
    car_manager.create_car()
    car_manager.move_cars()
    
    # Detect collision with car
    for car in car_manager.all_cars:
        # If player is < 20px from center of the car, then it probably means that it has collided with the car.
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
            
screen.exitonclick()
    


# Project was broken down into 5 parts:
# 1. Move the turtle with keypress --> Completed.
# 2. Create and move the cars --> Completed.
# 3. Detect collision with car --> Completed.
# 4. Detect when turtle reaches the other side --> Completed.
# 5. Create a scoreboard --> 