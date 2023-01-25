from turtle import Turtle, Screen
import pandas


screen = Screen()
screen.title("U.S. States Game")
screen.setup(width=1000,height=800)
image = "blank_states_img.gif"
draw = Turtle()
screen.addshape(image)
draw.penup()
draw.hideturtle()
dan = Turtle()

dan.shape(image)



state_number = 0

data = pandas.read_csv("50_states.csv")
while state_number < 50:
    answer_state = screen.textinput(title=f"Guess the State {state_number}/50", prompt="What is a name of a State?")
    answer_state.title()

    for state in data["state"]:
        if answer_state == state:
            current_state = data[data.state == f"{answer_state}"]
            current_state_x = current_state.x
            current_state_y = current_state.y
            draw.goto(int(current_state_x), int(current_state_y))
            draw.write(arg=f"{answer_state}", align="center", font=("Times New Roman", 12, "normal"))
            state_number += 1
else:
    draw.goto(0,0)
    draw.write(arg="Well Done!", align="center", font=("Arial", 50, "normal"))


screen.exitonclick()
