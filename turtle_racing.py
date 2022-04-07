import random
import turtle
from turtle import Turtle, Screen

turtle.title("Turtle Race")
turtle.listen()
screen = Screen()
is_race_on = False
screen.setup(width=550, height=450)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-180, -110, -40, 30, 100, 170]
turtles = []

user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race? Enter Color:")
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-255, y=y_positions[turtle_index])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 240:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've WON! The {winning_color} turtle is the winner.")
                is_race_on = False
            else:
                print(f"You've Lost! The {winning_color} turtle is the winner.")
                is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
