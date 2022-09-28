import turtle

t = turtle.Turtle()

def sq1(size):
    t.begin_fill()
    t.color('blue', 'violet')

    for i in range(4):
        t.fd(size)
        t.lt(90)

    t.end_fill()

def sq2(size):
    t.begin_fill()
    t.color('red', 'yellow')

    for i in range(4):
        t.fd(size)
        t.rt(90)

    t.end_fill()

t.lt(180)
sq2(100)
t.lt(180)
sq1(100)

turtle.done()