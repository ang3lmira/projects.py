import turtle as t
import random
bubu = t.Turtle()
t.colormode(255)
bubu.speed(0)

screen = t.Screen()


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    final_colors = (r, g, b)
    return final_colors


# TODO: draw a spirograph
# for x in range(36):
    # bubu.color(random_color())
    # bubu.circle(60)
    # bubu.left(10)

def draw_spiro(gap_size):
    for x in range(int(360 // gap_size)):
        bubu.color(random_color())
        bubu.circle(100)
        bubu.setheading(bubu.heading() + gap_size)
    screen.exitonclick


draw_spiro(60)
