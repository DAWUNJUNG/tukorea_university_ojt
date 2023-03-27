import turtle
from turtle import *
import random

col = random.randint(0, 2)
if 0 == col:
    turtle.pencolor('yellow')
elif 1 == col:
    turtle.pencolor('blue')
elif 2 == col:
    turtle.pencolor('red')

turtle.circle(50)

exitonclick()