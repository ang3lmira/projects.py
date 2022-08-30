from turtle import Turtle, Screen
import random

bubu = Turtle()
bubu.shape("classic")
bubu.color("pink")

# TODO: drawing a square

steps = 4
while steps > 0:
    bubu.forward(100)
    bubu.right(90)
    steps -= 1


screen = Screen()
screen.exitonclick()
