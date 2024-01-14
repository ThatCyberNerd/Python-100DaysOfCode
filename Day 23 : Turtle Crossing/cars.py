from turtle import Turtle
import random

COLORS = ["blue", "red", "green", "orange", "yellow", "purple"]
STARTING_MOVE_DISTANCE = 7
MOVE_INCREMENT = 10


class Car:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1, 10)
        if random_chance == 1 or random_chance == 4 or random_chance == 7:
            new_car = Turtle("square")
            new_car.turtlesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += 5
