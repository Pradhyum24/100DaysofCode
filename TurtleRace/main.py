import random
from turtle import Turtle,Screen
is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which jimmyle will the win the race? Enter a color: ")

colors=["red","orange","yellow","green","blue","purple"]
vertices=[(-230,0),(-230,40),(-230,80),(-230,-40),(-230,-80),(-230,-120)]
turtles=[]
for i in range(6):
    jimmy = Turtle(shape="turtle")
    jimmy.penup()
    jimmy.color(colors[i])
    jimmy.goto(vertices[i])
    turtles.append(jimmy)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"you have won! {winning_turtle} is the winner.")
            else:
                print(f"You have lost! {winning_turtle} is the winner.")
        random_distance = random.randint(1,10)
        turtle.forward(random_distance)















screen.exitonclick()