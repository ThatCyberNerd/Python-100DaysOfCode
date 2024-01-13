from turtle import Turtle
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.penup()
        self.goto(new_x, new_y)
    def vertical_bounce(self):
        self.y_move *= -1

    def horizontal_bounce(self):
        self.x_move *= -1

    def reverse(self):
        self.goto(0,0)
        self.horizontal_bounce()

