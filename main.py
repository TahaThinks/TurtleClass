import turtle
from turtle import Turtle, Screen
from random import randrange, choice, randint
from typing import Tuple

turtle.colormode(255)

# tim = Turtle()
# directions = [0, 90, 180, 270]
# tim.pensize(5)
# tim.speed('fastest')

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


# for _ in range(500):
#     tim.pencolor(random_color())
#     tim.forward(30)
#     tim.setheading(choice(directions))

tom = Turtle()
tom.pensize(3)
tom.speed("fast")

for _ in range(100):
    tom.color(random_color())
    tom.circle(100)
    tom.setheading(tom.heading()+10)



screen = Screen()
screen.exitonclick()
