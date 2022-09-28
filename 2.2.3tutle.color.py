import turtle

t = turtle.Turtle()

t.color('yellow', 'red')

t.begin_fill()

for i in range(3):
    t.fd(100)
    t.lt(120)

t.end_fill()

turtle.done()