import turtle

def dashes(size):

    t.color('blue')
    t.fd(size/3)

    t.color('red')
    t.fd(size/3)

    t.color('blue')
    t.fd(size/3)

t = turtle.Turtle()
t.width(3)

dashes(200)

turtle.done()