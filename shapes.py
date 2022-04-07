from turtle import Turtle, Screen
import random

tom = Turtle()
tom.shape("arrow")
tom.color("MidnightBlue")

colors = ["navy", "tomato", "dark slate blue", "chartreuse", "green", "light sky blue", "deep pink", "dark cyan"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tom.forward(100)
        tom.left(angle)


for sides in range(3, 11):
    tom.color(random.choice(colors))
    draw_shape(sides)

screen = Screen()
screen.exitonclick()
