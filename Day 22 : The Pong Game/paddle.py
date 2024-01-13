from turtle import Turtle

MOVEMENT_SPEED = 20
class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_len=1, stretch_wid=4)
        self.penup()
        self.goto(xcor, ycor)
    def up(self):
        new_y = self.ycor() + MOVEMENT_SPEED
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVEMENT_SPEED
        self.goto(self.xcor(), new_y)


