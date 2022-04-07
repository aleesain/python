# import colorgram
import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
turtle.title("Hirst Painting")
# rgb_colors = []
# colors = colorgram.extract('OIP.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     new_color = (r, b, g)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
color_list = [(207, 102, 155), (57, 128, 107), (162, 43, 82), (125, 97, 79), (122, 171, 156), (126, 159, 175), (195, 39, 142), (226, 130, 198), (188, 109, 89), (191, 145, 131), (14, 57, 44), (53, 19, 38), (51, 128, 164), (59, 114, 121), (218, 70, 90), (159, 32, 22), (41, 33, 31), (8, 28, 30), (81, 165, 146), (238, 162, 167), (156, 21, 28), (23, 91, 80), (233, 173, 168), (173, 188, 206), (106, 157, 126), (26, 84, 87)]
tom = Turtle()
tom.hideturtle()
tom.setheading(220)
tom.penup()
tom.forward(390)
tom.setheading(0)



def move_tom():
    for _ in range(10):
        tom.dot(30, random.choice(color_list))
        tom.forward(65)


for _ in range(10):
    tom.speed("fastest")
    move_tom()
    tom.setheading(90)
    tom.forward(55)
    tom.setheading(180)
    tom.forward(650)
    tom.setheading(360)


screen = Screen()
screen.exitonclick()
