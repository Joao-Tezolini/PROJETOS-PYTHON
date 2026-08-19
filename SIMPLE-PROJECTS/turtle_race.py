from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
colors = ["red", "orange", "yellow", "green", "LightSkyBlue","MediumBlue", "purple"]
user_bet = screen.textinput(title="Turtle race!", prompt=f"Bet on which turtle will win! Choose a color {colors}: ")
all_turtles = []

y_pos = [-120, -80, -40, 0, 40, 80, 120]
for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winning turtle was {winning_color}!\n")
                is_race_on = False
            else:
                print(f"You've lost! The winning turtle was {winning_color}!\n")
                is_race_on = False

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
