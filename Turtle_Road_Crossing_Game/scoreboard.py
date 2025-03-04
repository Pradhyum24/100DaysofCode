from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-290,270)
        self.hideturtle()
        self.level=1
        self.write(arg=f"Level {self.level}",move=False,align="left",font=("Courier", 24, "normal"))

    def update(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level {self.level}",move=False,align="left",font=("Courier", 24, "normal"))

    def game_over(self):

        self.goto(0,0)
        self.write(arg="GAME OVER",move=False,align="left",font=("Courier", 24, "normal"))
