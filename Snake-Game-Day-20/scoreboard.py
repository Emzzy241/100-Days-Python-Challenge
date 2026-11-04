from turtle import Turtle

# cleaning up our code
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # Updating our snake game using file management system to keep track of our high score
        # utilizing what was learnt to ready high score value from data.txt file
        # file = open("data.txt")
        # contents = file.read()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        # self.high_score = int(contents)
        # print(self.high_score)
        # turtle = Turtle()
        # change color before writing
        self.color("white")
        self.penup()
        self.goto(0, 260)
        # self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.update_scoreboard()
        # WRONG: It was supposed to be self.write(), upon every creation of snake object, a new scoreboard is also created
        # turtle.write(arg=f"Score: {score}", align="center", font=("Arial", 8, "normal"))
        # turtle.write()
        self.hideturtle()
        
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)
   
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
            # with open("data.txt", mode="w") as file:
            #     contents = file.write(int(self.high_score))
            #     print(contents)
        self.score = 0
         
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
    # We want to start making our high score functionality, no need for game_over() method.
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)
