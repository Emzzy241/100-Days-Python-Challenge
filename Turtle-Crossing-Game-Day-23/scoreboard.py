from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup() # TO avoid drawing a path to where we ae doing to with the goto() method.
        self.goto(-280, 250)    
        self.update_scoreboard()    
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="Left", font=FONT)
        
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="Center", font=FONT)
        
# TODO: One of me future goals is actually to be able to pick any of these projects that I have been building so far... 
# And just re-build every one of them. One might need to re-use some of the steps that Dr. Angela specified if I cannot be able to come up with my own steps
# God help me.... Utilizing things like spaced repetition would really help actually, to ensure one is truly truly reading and understanding what one is building. 
# Advice from Dr. Angela; Try to create all the games by yourself, and continue to make it better, make the game your own and make it way!!!! Much better.
# The thinking part is the major part, and not just the coding part. Ma'am Kim, a mentor of mine also told me about the thinking being the thing that matters the most