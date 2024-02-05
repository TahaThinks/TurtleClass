import turtle
from turtle import Turtle, Screen
from random import randrange,choice


tim = Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
tim.pensize(5)
tim.speed('fastest')

for _ in range(500):
    tim.pencolor(choice(colours))
    tim.forward(30)
    tim.setheading(choice(directions))

screen = Screen()
screen.exitonclick()
