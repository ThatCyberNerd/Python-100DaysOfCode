from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("The Pong Game")
screen.tracer(0)

l_paddle = Paddle(-370, 0)
r_paddle = Paddle(360, 0)
ball = Ball()

screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.04)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.vertical_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 and ball.xcor() < 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 and ball.xcor() > -350:
        ball.horizontal_bounce()

    if ball.xcor() > 380:
        scoreboard.increase_left_score()
        scoreboard.update_scoreboard()
        ball.reverse()

    elif ball.xcor() < -380:
        scoreboard.increase_right_score()
        scoreboard.update_scoreboard()
        ball.reverse()

screen.exitonclick()
