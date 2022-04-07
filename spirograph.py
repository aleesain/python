import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tom_color = (r, g, b)
    return tom_color


tom = Turtle()
tom.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tom.circle(100)
        tom.color(random_color())
        tom.setheading(tom.heading() + size_of_gap)


draw_spirograph(5)
screen = Screen()
screen.exitonclick()