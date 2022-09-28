import turtle
import math

def sq(col, x):

    t.pencolor(col)
    for i in range(4):
        t.fd(x)
        t.lt(90)
    t.fd(x / 2)

def sqin(col, x):

    y = x / math.sqrt(2)
    t.lt(45)
    sq(col, y)

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

sq('blue', 200)
sqin('black', 200)

turtle.done()
