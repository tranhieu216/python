import turtle
import math

def square(x, y, size):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.dot(10)

    half = size / 2

    t.pu()
    t.fd(half)       
    t.lt(90)
    t.fd(half)       
    t.lt(90)
    t.pd()

    t.color('blue')
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)

    d = math.sqrt(2) * size

    t.lt(45)
    t.fd(d)         

t = turtle.Turtle()
t.width(5)

square(0, 0, 100)

turtle.done()