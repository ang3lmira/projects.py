from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which of the turtles do you think will win the race? Enter the color of  turtle you predict will win:")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()

    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winner = turtle.pencolor()

            if winner == user_bet:
                # print(winner)
                print(f"You've won, the {winner} turtle is the winner!")
            else:
                print(f"You've lost, the {winner} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)
screen.exitonclick()
