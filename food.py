from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.50, stretch_wid=0.50)
        self.color("red")
        self.speed("fastest")
        self.new_food()
        
    def new_food(self):
        random_x = random.randrange(-260, 260, 20)
        random_y = random.randrange(-260, 260, 20)
        self.goto(random_x, random_y)
        
    def reset_food(self):
        self.hideturtle()
        self.new_food()