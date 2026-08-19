# Etch a Sketch
# Draw anything with a continuous line

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# Defining movement directions

def move_forwards():
    tim.forward(10)

def turn_left():
    new_heading = tim.heading() + 5
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 5
    tim.setheading(new_heading)

def move_backwards():
    tim.backward(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()

# Does not feature continuous click, 1 click = 1 movement (change of angle with A or D / back and forth with S and W)

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
