import turtle as t
import random
import colorgram

t.colormode(255)

colors = (colorgram.extract('image.jpg', 10))

colors_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    colors_list.append(new_color)

color = random.choice

tim = t.Turtle()
screen = t.Screen()

tim.right(90)
tim.penup()
tim.forward(200)
tim.left(90)

for _ in range(10):
    for _ in range(10):
        tim.dot(20,random.choice(colors_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()

    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)

screen.exitonclick()
