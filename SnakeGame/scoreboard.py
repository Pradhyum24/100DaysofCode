from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("Courier", 24, "normal"))

    def update(self):
        self.score +=1
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, align="center", font=("Courier", 24, "normal"))
