import turtle

t = turtle.Turtle()

t.color('blue', 'green')

t.begin_fill()

for i in range(2):
    t.fd(100)
    t.lt(60)
    t.fd(100)
    t.lt(120)


t.end_fill()

turtle.done()