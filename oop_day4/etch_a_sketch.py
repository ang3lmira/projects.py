from turtle import Turtle, Screen

bubu = Turtle()
screen = Screen()


def move_forwards():
    bubu.fd(100)


def move_backwards():
    bubu.bk(100)


def move_clockwise():
    bubu.right(90)


def move_counter_cw():
    bubu.setheading(90)
    bubu.left(90)


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_counter_cw)
screen.onkey(key="d", fun=move_clockwise)
#screen.onkey(key="s", )

screen.exitonclick()
