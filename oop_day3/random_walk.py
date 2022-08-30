from turtle import Turtle, Screen
import random

# TODO: draw a  random walk
colors = ["pink", "red", "brown", "yellow", "green", "aquamarine",
          "indigo", "wheat", "seagreen", "slategrey", "purple", "orange", "blue"]

directions = [0, 90, 180, 270]

bubu = Turtle()
bubu.shape("classic")
bubu.color("pink")
bubu.pensize(10)
bubu.speed(10)


for x in range(10000):
    bubu.forward(40)
    bubu.color(random.choice(colors))
    bubu.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
