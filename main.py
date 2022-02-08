from turtle import Turtle, Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossing Game")
screen.bgcolor("white")
screen.tracer(0)

screen.listen()
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()
    screen.onkey(player.move_turtle, "Up")
    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
        if player.player_reach():
            player.go_to_home()
            cars.set_level()
            scoreboard.increase_level()
screen.exitonclick()
