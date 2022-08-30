from turtle import Turtle, Screen
import random

bubu = Turtle()
bubu.shape("classic")
bubu.color("pink")


# drawing a square
#steps = 4
# while steps > 0:
# bubu.forward(100)
# bubu.right(90)
#steps -= 1

# drawing a dashed line
# for x in range(15):
# bubu.forward(10)
# bubu.penup()
# bubu.forward(10)
# bubu.pendown()

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
