from turtle import *
import random
for i in range(5):
    for j in range(10):
        c = ['red', 'blue', 'yellow', 'green']
        color(c[random.randint(0, 3)], c[random.randint(0, 3)])
        sel = random.randint(0, 4)
        if (0 == sel):
            forward(random.randint(50, 100))
        elif (1 == sel):
            right(random.randint(90, 360))
        elif (2 == sel):
            begin_fill()
            circle(random.randint(-100, -20))
            end_fill()
        elif (3 == sel):
            forward(random.randint(30, 50))
        elif (4 == sel):
            circle(random.randint(20, 100))
        a = float(random.randint(-300, 300))
        b = float(random.randint(-300, 300))
    goto(a, b)
exitonclick()