from turtle import Turtle

import random

COLORS = ['red', "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUMBER_OF_CARS = (5, 2, 1, 7, 9)


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_cars = random.randint(1, 6)
        if random_cars == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.hideturtle()
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def set_level(self):
        self.car_speed += MOVE_INCREMENT
