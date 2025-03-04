import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up,"Up")
screen.onkey(player.move_down,"Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    random_chance = random.randint(1,6)
    if random_chance == 1:
        car_manager.create_cars()

    car_manager.move()

    for car in car_manager.cars :
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() == 290:
        player.reset()
        car_manager.level += 1
        scoreboard.update()




screen.exitonclick()
