from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.go_to_home()

    def move_turtle(self):
        self.forward(MOVE_DISTANCE)

    def go_to_home(self):
        self.goto(STARTING_POSITION)

    def player_reach(self):

        if self.ycor() >= 280:
            return True
        else:
            return False

