from turtle import Screen
from  paddle import Paddle
import time
from ball import Ball
from Scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("PingPong Game")
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_forward,"Up")
screen.onkey(r_paddle.move_backward,"Down")
screen.onkey(l_paddle.move_forward,"w")
screen.onkey(l_paddle.move_backward,"s")


game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(ball.move_speed)
    ball.move()


    #detects the collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detects the collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #DETECTS THE R_PADDLE MISS..
    if ball.xcor() > 380 :
        ball.reset()
        scoreboard.l_point()

    # DETECTS THE L_PADDLE MISS..
    if ball.xcor() <  -380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()