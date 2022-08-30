from turtle import Turtle, Screen
import random

bubu = Turtle()
bubu.shape("classic")
bubu.color("pink")


# TODO: Draw a number of polygons with different colored lines.
colors = ["pink", "red", "brown", "yellow", "green", "aquamarine",
          "indigo", "wheat", "seagreen", "slategrey", "purple", "orange", "blue"]

no_of_sides = 3
while no_of_sides < 11:
    angle = 360 // no_of_sides
    bubu.color(random.choice(colors))

    for side in range(no_of_sides):
        bubu.forward(100)
        bubu.right(angle)
    no_of_sides += 1


screen = Screen()
screen.exitonclick()
