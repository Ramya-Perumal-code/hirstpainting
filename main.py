import turtle

from turtle import Turtle, Screen
import random

hist_list = [(240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
timmy = Turtle()
# Your colormode is probably set to 1.0, so either the individual color coordinates need to be floats in the range 0 to 1, or you need to set the colormode to 255.
turtle.colormode(255)
timmy.shape("arrow")

color = random.choice(hist_list)
print(color)
timmy.hideturtle()
timmy.penup()

times = 0
current_pos = timmy.ycor() - 200
while times < 10:
    timmy.setpos(-250, current_pos)
    for _ in range(0, 11):
        color = random.choice(hist_list)
        timmy.dot(20, color)
        timmy.forward(50)
    timmy.home()
    current_pos += 50
    times += 1


screen = Screen()
screen.exitonclick()