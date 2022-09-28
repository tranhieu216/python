import turtle

t = turtle.Turtle()
t.pensize(4)

def sq(size):
    t.begin_fill()

    t.color('red', 'yellow')

    for i in range(4):
        t.fd(size)
        t.lt(90)
    t.end_fill()

for i in range(3):
    sq(100)
    t.lt(45)

turtle.done()