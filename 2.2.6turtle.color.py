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

sq1(100)
t.lt(180)
t.up()
t.fd(50)
t.down()
sq2(100)

turtle.done()