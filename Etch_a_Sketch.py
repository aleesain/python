import turtle
from turtle import Turtle, Screen
turtle.title("Etch a Sketch")
turtle.listen()
tom = Turtle()
screen = Screen()


def move_forward():
    tom.forward(10)

def move_backward():
    tom.back(10)

def move_right():
    tom.right(10)

def move_left():
    tom.left(10)

def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()


turtle.onkey(key="w", fun=move_forward)
turtle.onkey(key="s", fun=move_backward)
turtle.onkey(key="a", fun=move_left)
turtle.onkey(key="d", fun=move_right)
turtle.onkey(clear, "c")
screen.exitonclick()
