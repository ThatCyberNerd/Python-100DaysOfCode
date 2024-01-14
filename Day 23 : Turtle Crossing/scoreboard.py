from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-180, 270)
        self.level = 1
        self.write(f"Level : {self.level}", align="right", font=("Courier", 15, "normal"))

    def update_level(self):
        self.clear()
        self.write(f"Level : {self.level}", align="right", font=("Courier", 15, "normal"))

    def increase_level(self):
        self.level += 1

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER!", align="center", font=("Courier", 20, "normal"))
