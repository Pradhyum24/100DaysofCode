import turtle
from turtle import Turtle

import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_name_writer = Turtle()
state_name_writer.penup()
state_name_writer.hideturtle()

guessed_state =[]

data = pandas.read_csv("50_states.csv")
all_states = data["state"].tolist()


while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 are correct", prompt="Whats another state name?").title()
    user_answer_df = data[data["state"] == answer_state]

    if answer_state == "Exit":
        break

    if not user_answer_df.empty and  answer_state not in guessed_state:
        x_coordinate = user_answer_df["x"].values
        y_coordinate = user_answer_df["y"].values
        state_name_writer.goto(x_coordinate[0],y_coordinate[0])
        state_name_writer.write(answer_state, align="center", font=("Arial", 10, "normal"))
        guessed_state.append(answer_state)

not_guessed_states = []
for state in all_states:
    for guess in guessed_state:
        if state != guess:
            not_guessed_states.append(state)

len(not_guessed_states)
df = pandas.DataFrame(not_guessed_states)
df.to_csv("Notguessed.csv")