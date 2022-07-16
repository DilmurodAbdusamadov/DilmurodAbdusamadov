from turtle import Turtle, Screen

tim = Turtle("arrow")
screen = Screen()
tim.shapesize(1, 1)
tim.pensize(10)

current_angle = 0


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def counter_clockwise():
    tim.left(current_angle + 10)


def clockwise():
    tim.right(current_angle + 10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=counter_clockwise)
screen.onkeypress(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()