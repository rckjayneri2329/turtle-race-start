from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

x_axis = -230
y_axis = -120

racers = []

for index, color in enumerate(colors):
    racers.append(Turtle(shape="turtle"))
    racers[index].penup()
    racers[index].color(color)
    racers[index].goto(x=x_axis, y=y_axis)
    y_axis += 50

race_in_session = True

while race_in_session:
    for racer in racers:
        racer.forward(random.randint(1, 10))
        if racer.xcor() >= 250:
            winner = racer.color()
            race_in_session = False

print(winner)

screen.exitonclick()