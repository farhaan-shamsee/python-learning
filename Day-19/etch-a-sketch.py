import turtle as t

tim = t.Turtle()
screen = t.Screen()

screen.listen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_right():
    tim.right(5)


def move_left():
    tim.left(5)


def clear_screen():
    t.resetscreen()


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
