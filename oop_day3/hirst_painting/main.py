import turtle
import random

turtle.colormode(255)
bubu = turtle.Turtle()
bubu.speed(0)

list_of_colors = [(171, 154, 50), (18, 21, 57), (227, 169, 195), (15, 35, 17), (35, 31, 14), (218, 79, 55), (143, 85, 96), (171, 25, 10), (146, 160, 149), (235, 172,
                                                                                                                                                            159), (187, 87, 101), (95, 111, 99), (46, 47, 110), (36, 17, 35), (166, 22, 35), (182, 179, 219), (180, 202, 179), (114, 137, 122), (220, 208, 21)]

bubu.penup()
bubu.hideturtle()
bubu.setheading(225)
bubu.forward(300)
bubu.setheading(0)
number_dots = 101

for dot_count in range(1, number_dots):
    bubu.dot(10, random.choice(list_of_colors))
    bubu.penup()
    bubu.fd(50)
    bubu.pendown

    if dot_count % 10 == 0:
        bubu.setheading(90)
        bubu.fd(50)
        bubu.setheading(180)
        bubu.fd(500)
        bubu.setheading(0)


screen = turtle.Screen()
screen.exitonclick()
