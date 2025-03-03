from functools import update_wrapper
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(arg=self.l_score, move=False, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(arg=self.r_score, move=False, align="center", font=("Courier", 80, "normal"))


    def l_point(self):
        self.clear()
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.update_scoreboard()

