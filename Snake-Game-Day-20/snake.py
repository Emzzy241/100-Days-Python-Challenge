from turtle import Screen, Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    # Instantiating a snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
        
        # Our snake body consists of 3 squares, which are each turtles that must be lined up next to each other along the horizontal axis.

        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)


    # For Moving our snake:
    # for seg_num in range(start=2, stop=0, step=-1):
        # Look at the array, we have 3 elements in the array.... Start from element 2, 
        # so cube with coordinate (-40, 0) becomes cube with coordinate (-20,0), and coordinate (0,0) becomes cube at (-20,0)
        # The range function is not really python itself but C, so we cannot use start, stop, step
        
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Getting the 2nd to last segment coordinate
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # Now telling the last segment o go to position of 2nd to last position
            self.segments[seg_num].goto(new_x, new_y)
        
        self.head.forward(MOVE_DISTANCE)
        # self.head.left(90)
        
    def up(self):
        # To turn the snake upward, the segment we are most interested in is the first segment actually
        # rest of the body will follow
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            # The real snake game, if it is already going down, it is not allowed to go up
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
# Since it is now inside a class, it is no longer just segments, but now: self.segments.
# How we essentially move is simple, we move last segment to 2nd to last,
# We move first segment to 2nd to last... So the snake essentially follows where the head is going.
# By the end of our game, we have classes for snake, food, scoreboard. All of these classes ill be in separate files.
# Cleaning up our code now.

# for _ in range(3):
#     snake = Turtle("square")
#     snake.color("white")
#     snake.goto(random.choice(starting_positions))

# snake_one = Turtle("square")
# snake_one.color("white")
# # snake_one.penup

# snake_two = Turtle("square")
# snake_two.color("white")
# snake_two.goto(x=-20, y=0)
# # snake_two.goto(x=-240, y=30)

# snake_three = Turtle("square")
# snake_three.color("white")
# snake_three.goto(x=-40, y=0)
# snake_three.goto(x=-260, y=30)

# We see 3 squares on top of each other, and because this is a 2D image, we can probably only see just 1 square.
