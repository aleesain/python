import random
import turtle
from turtle import Turtle, Screen

# Random Walk
turtle.colormode(255)
tom = Turtle()
tom.shape("arrow")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tom_color = (r, g, b)
    return tom_color


def ran_walk():
    directions = [0, 90, 180, 270]
    tom.setheading(random.choice(directions))
    tom.forward(50)


for _ in range(200):
    tom.speed("fastest")
    tom.pensize(10)
    tom.color(random_color())
    ran_walk()
screen = Screen()
screen.exitonclick()