from turtle import Turtle

START_POSITION = (0, -280)
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(START_POSITION)
        self.left(90)

    def move_turtle(self):
        self.forward(20)