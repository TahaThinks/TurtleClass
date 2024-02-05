import turtle
from turtle import Turtle, Screen
from random import randint
turtle.colormode(255)

tim = Turtle()
sides = list(range(3, 20))


def line_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    print(r, g, b)
    tim.pencolor((r, g, b))

def draw_shape(side, angle):
    line_color()
    for _ in range(side):
        tim.forward(100)
        tim.right(angle)


for shape_side in sides:
    draw_shape(shape_side, 360 / shape_side)



screen = Screen()
screen.exitonclick()
