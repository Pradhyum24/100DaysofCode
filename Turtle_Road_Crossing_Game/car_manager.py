import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.cars=[]
        self.level = 0

    def create_cars(self):
        new_car = Turtle()
        new_car.color(random.choice(COLORS))
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1,stretch_len=2)
        new_car.penup()
        new_car.goto(300,random.randint(-250,250))
        self.cars.append(new_car)

    def move(self):
        if self.level >= 1:
            for i in range(len(self.cars) - 1):
                self.cars[i].backward(STARTING_MOVE_DISTANCE +(self.level * MOVE_INCREMENT) )
        else :
            for i in range(len(self.cars)-1):
                self.cars[i].backward(STARTING_MOVE_DISTANCE)



