from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-200, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(F"LEVEL:{self.level}", move=True, align="right", font=('Courier', 18, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align="center", font=("Courier", 20, "bold"))

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
