import turtle
from turtle import Turtle, Screen
from random import randrange,choice


tim = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tim.pensize(5)
tim.speed('fast')

for _ in range(500):
    tim.pencolor(choice(colours))
    angle = randrange(90, 360, 90)
    tim.forward(50)
    tim.right(angle)
    # print(angle)



screen = Screen()
screen.exitonclick()
