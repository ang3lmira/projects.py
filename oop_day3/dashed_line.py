from turtle import Turtle, Screen
import random

bubu = Turtle()
bubu.shape("classic")
bubu.color("pink")


# TODO: drawing a dashed line
for x in range(15):
    bubu.forward(10)
    bubu.penup()
    bubu.forward(10)
    bubu.pendown()

screen = Screen()
screen.exitonclick()
