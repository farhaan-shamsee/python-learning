# import colorgram
import random
import turtle as t

# colors = colorgram.extract('image.jpg', 30)
# palette = []
#
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     palette.append(new_color)

color_list = [(212, 154, 97), (52, 108, 132), (178, 78, 33), (198, 143, 34), (123, 80, 97), (116, 155, 171), (124, 175, 158), (228, 197, 129), (194, 85, 105), (54, 38, 20), (12, 51, 65), (189, 123, 142), (54, 120, 115), (41, 169, 126), (167, 21, 31), (225, 94, 78), (4, 30, 28), (39, 32, 34), (243, 163, 159), (81, 148, 168), (164, 27, 22), (239, 163, 167), (104, 123, 159), (164, 209, 193), (21, 81, 93), (29, 85, 81)]

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)
tim.speed(0)
tim.penup()
tim.hideturtle()
"""
setting the position of the turtle to left bottom corner
"""
tim.setpos(-260, -230)

for i in range(10):
    # the loop should run 10 *10 times.
    # at begining of each loop turtle moves 50 points vertically i.e on y axis to draw the dots in new line
    tim.goto(-230, -(230-(50*i+1)))
    for j in range(10):
        tim.fd(50)
        tim.dot(20, random.choice(color_list))
screen = t.Screen()
screen.exitonclick()