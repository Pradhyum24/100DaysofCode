from turtle import Turtle,Screen

jimmy = Turtle()
screen = Screen()

def move_forward():
    jimmy.forward(5)
def move_backward():
    jimmy.backward(5)
def move_clockwise():
    jimmy.right(5)
def move_anti_clockwise():
    jimmy.left(5)
def clear():
    jimmy.reset()



screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s" , fun=move_backward)
screen.onkey(key="a" , fun=move_anti_clockwise)
screen.onkey(key="d" , fun=move_clockwise)
screen.onkey(key="c" , fun=clear)















screen.exitonclick()