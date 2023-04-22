import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for i in range(6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + i * 40)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winning color ")
            else:
                print(f"You've lost! The {winning_color} is the winning color ")

        turtle.forward(random.randint(0, 10))


screen.exitonclick()
