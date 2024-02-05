from turtle import Turtle, Screen

tim = Turtle()


def dashed_color():
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


for _ in range(15):
    dashed_color()

screen = Screen()
screen.exitonclick()
