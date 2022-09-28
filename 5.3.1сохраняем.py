import turtle
import math


def square(x, y, size):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.dot(5)

    half = size / 2

    t.pu()
    t.fd(half)       
    t.lt(90)
    t.fd(half)       
    t.lt(90)
    t.pd()

    t.color('blue')
    p1 = t.pos()
    t.fd(size)
    t.lt(90)
    p2 = t.pos()
    t.fd(size)
    t.lt(90)
    p3 = t.pos()      
    t.fd(size)
    t.lt(90)
    p4 = t.pos()      
    t.fd(size)
    t.lt(90)

    t.goto(p3)
    t.goto(p2)
    t.goto(p4)        


t = turtle.Turtle()
t.width(3)
t.color('red')


square(-100, -50, 100)


turtle.done()