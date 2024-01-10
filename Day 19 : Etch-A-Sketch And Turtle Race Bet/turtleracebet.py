from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=500)
screen.bgcolor("coral")

all_turtles = []
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_coordinates = [-70, -40, -10, 20, 50, 80, 110]
is_game_on = False

user_bet = screen.textinput(title="Turtle Race Betting", prompt="Which turtle will win? Enter a color from VIBGYOR :").lower()

for turtle_index in range(0,7):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.goto(x=-290, y=y_coordinates[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        distance = random.randint(1,10)
        turtle.forward(distance)
        if turtle.xcor() > 272:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations, You Win! The {winning_color} turtle won.")
            else:
                print(f"Sorry, You Lose! The {winning_color} turtle won.")
            is_game_on = False

screen.exitonclick()
