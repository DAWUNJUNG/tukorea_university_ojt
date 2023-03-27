import turtle
from turtle import *
import random

for i in range(3):
    col = random.randint(0, 2)
    sel = random.randint(0, 1)
    if 0 == col:
        turtle.pencolor('yellow')
    elif 1 == col:
        turtle.pencolor('blue')
    elif 2 == col:
        turtle.pencolor('red')
    if 0 == sel:
        turtle.forward(100)
    elif 1 == sel:
        turtle.circle(50)
    turtle.right(45)

exitonclick()