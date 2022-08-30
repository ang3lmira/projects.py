import turtle as t
import random

# TODO: draw a  random walk
directions = [0, 90, 180, 270]
bubu = t.Turtle()
t.colormode(255)

bubu.shape("classic")
bubu.color("pink")
bubu.pensize(10)
bubu.speed(10)


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    final_colors = (r, g, b)
    return final_colors


for x in range(500):
    bubu.forward(40)
    bubu.color(random_color())
    bubu.setheading(random.choice(directions))
