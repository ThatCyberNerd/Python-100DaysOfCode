from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from cars import Car
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Road Crossing")
screen.bgcolor("grey")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = Car()


screen.listen()
screen.onkeypress(player.move_turtle, "Up")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    car_manager.create_cars()
    car_manager.move_cars()

    if player.ycor() > 280:
        player.goto(0, -280)
        scoreboard.increase_level()
        scoreboard.update_level()
        car_manager.increase_speed()

    for car in car_manager.all_cars:
        if abs(player.xcor() - car.xcor()) <= 20 and abs(player.ycor() - car.ycor()) <= 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
