from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
            new_segment = Turtle()
            new_segment.color("white")
            new_segment.shape("square")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def increase_length(self):
        self.add_segment(self.segments[-1].position())


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(UP)
        else:
            pass

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(DOWN)
        else:
            pass
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(LEFT)
        else:
            pass

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(RIGHT)
        else:
            pass
