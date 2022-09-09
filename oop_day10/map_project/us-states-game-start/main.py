import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

image = "map_project/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("map_project/us-states-game-start/50_states.csv")
all_states = data.state.to_list()

answer_state = screen.textinput(
    title="Guess the state", prompt="What's another state's name?").lower()

# check validity of users answer
if answer_state in all_states:
    t = turtle.Turtle()
    t.color("pink")
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(state_data.state)

# if right, write state name on its position.


screen.exitonclick()
