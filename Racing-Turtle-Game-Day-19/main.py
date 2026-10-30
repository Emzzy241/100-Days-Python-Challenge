# # Welcome to Day-19, Today we will be learning:
# # More Turtle Graphics, Event Listeners, Higher Order Functions, state and Multiple Instances
# # We will be making Etch a Sketch, one of Dr. Angela's favorite game.
# # Also make a turtle racing game, bet on a turtle that will win the game, the first turtle to reach right edge of screen
# # Higher Order Functions.... Turtle Event Listeners. listen(), onkey() | onkeyrelease() onkeypress(), onclick, onscreenclick(),
# # ontimer(), mainloop() | done()

# # listen(): It allows the turtle screen to start listening & waiting for events user might create

# # from turtle import Turtle, Screen

# # tim = Turtle()
# # screen = Screen()

# # def move_forward():
# #     tim.forward(10)

# # screen.listen()
# # screen.onkey(key="space", fun=move_forward) # listen when a space bar is pressed, and trigger this move function


# # screen.exitonclick()
# # To bind a keystroke to an event in our code, we need to use an event listener.... onkey(fun, key)... Now we are controlling our turtle with a key stroke.

# # Challenge: Make an Etch-a-Sketch Application
# # W -> Forwards
# # S -> Backwards
# # A -> Counter-Clockwise
# # D -> Clockwise
# # C -> Clear Drawings and put your key back in the center.

# from turtle import Turtle, Screen

# tim = Turtle()
# screen = Screen()

# def move_forwards():
#     tim.forward(10)
    
# def move_backwards():
#     # tim.right(180)
#     tim.backward(10)
    
# # def move_counter_clockwise():
# #     tim.circle(90)
    
# # def move_clockwise():
# #     tim.setheading(0)
# #     tim.circle(90)
    
# def turn_left():
#     new_heading = tim.heading() + 10 # tim.left(10 degrees) will also work
#     tim.setheading(new_heading)

# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
    
# # 2 clear() methods, one is for the turtle and the other is clearscreen(). clear() will delete everything including the turtle. the turtle we want is just to wipe all that has been drawn

# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
    
    

# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="c", fun=clear)

# # Object states, this is the next.....

# # screen.onkey()

# screen.exitonclick()



from turtle import Turtle, Screen
import random

# tim = Turtle(shape="turtle")
# tom = Turtle(shape="turtle")
# bob = Turtle(shape="turtle")
# ron = Turtle(shape="turtle")
# non = Turtle(shape="turtle")
# bon = Turtle(shape="turtle")
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",  prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "violet"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    # THe above line, x=-230... If a turtle is 40px wide (turtles are 40X40), 
    # then to get the turtle to the starting line, we have to subtract half of the width of the turtle... 250-20=230... Play around with these values, change it to higher, or lower... Going forward, assumptions will be made on you already knowing/understanding it.
    # Playing around with the x=-230 value, when I made it to actually equal 250, something changed, half of the turtles body was being cutoff actually
    # One can go down the route of consistently guessing things and trying to make progress from there, however, that wouldn't really be a right way to go about with things
    # Given that a turtle's measurement is 40x40, if half of the turtle is shown upon equating x=-250 (half of our width=500px), this just tells us we need to reduce
    # we need to reduce where exactly it is that the turtle is going to horizontally, on the x-axis. Now for the y_position, 
    # that one is fairly simple, we had a range of coordinate for that one, and we kept decreasing it by 30 to create that vertical gap between our turtles. Thank you Jesus for understanding.
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

# So the race does not start prematurely, even before user makes their bet

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            # once a winner has clinched the position of winner, we want to terminate the while loop, so we don't wound up getting more than 1 winner
            is_race_on = False
            winning_color = turtle.pencolor()
            # print(turtle.color())
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                
            
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
    

# The movement should be random... forward(0, 10)

# tom.color(colors[1])
# tom.color(colors[2])
# tom.color(colors[3])
# tom.color(colors[4])
# tom.color(colors[5])
# print(user_bet)


# tim.goto(-230, -100)
# tom.goto(-250, -120)
# bon.goto(-190, -120)
# ron.goto(-190, -120)
# non.goto(-190, -120)
# ron.goto(-190, -120)

screen.exitonclick()

# One day, I know it within me, I am gonna be big, and gonna be a very very good programmer.
# Keep building, keep winning, keep growing. Dr. Angela did recommend that some of these projects should essentially have no limitations in your hands
# One can turn some of these projects into something very very big, and much more better.