import random
import turtle as t
# from turtle import Turtle, Screen

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


direction = [0, 90, 180, 270]

tim.speed(0)
tim.pensize(1)
size = 5
for i in range(int(360/size)):
    tim.pencolor(random_colour())
    # tim.forward(30)
    # tim.setheading(random.choice(direction))
    tim.circle(100)
    tim.right(size)


screen = t.Screen()
screen.exitonclick()
