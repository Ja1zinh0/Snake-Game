
from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 25, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="CENTER", font=("Courier", 26, "normal"))
    
    def reset_scoreboard(self):
        self.score = 0
        self.update_score()
        self.clear()