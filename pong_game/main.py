from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("pink")
screen.setup(width=800, height=600)
screen.title("m's ping pong arena")

paddle = Turtle()

# Creating the paddle
paddle.shape("square")
paddle.resizemode("user")
paddle.color("black")
paddle.shapesize(stretch_wid=5, stretch_len=1)

# Changing the paddle position
paddle.penup()
paddle.goto(x=350, y=0)


def move_up():
    new_y = paddle.ycor() + 20
    paddle.goto(x=350, y=new_y)


def move_down():
    new_y = paddle.ycor() - 20
    paddle.goto(x=350, y=new_y)


screen.listen()
screen.onkey(fun=move_up, key="Up")
screen.onkey(fun=move_down, key="Down")

# print(screen.window_height())
# print(screen.window_width())
screen.exitonclick()
