import turtle

def rectangle(x1, y1, w, h):
    t.pu()
    t.goto(x1, y1)
    i = t.pos()

    t.goto(x1 + w / 2, y1 + h / 2)
    p1 = t.pos()

    t.goto(x1 - w / 2, y1 + h / 2)
    p2 = t.pos()

    t.goto(x1 - w / 2, y1 - h / 2)
    p3 = t.pos()

    t.goto(x1 + w / 2, y1 - h / 2)
    p4 = t.pos()

    t.goto(i)
    t.pd()

    t.begin_fill()
    t.color('green')
    t.goto(p1)
    t.goto(p2)
    t.goto(i)
    t.end_fill()

    t.begin_fill()
    t.color('yellow')
    t.goto(p2)
    t.goto(p3)
    t.goto(i)
    t.end_fill()

    t.begin_fill()
    t.color('blue')
    t.goto(p3)
    t.goto(p4)
    t.goto(i)
    t.end_fill()

    t.begin_fill()
    t.color('red')
    t.goto(p4)
    t.goto(p1)
    t.goto(i)
    t.end_fill()


t = turtle.Turtle()
t.width(3)
t.shape('turtle')


rectangle(-100, -50, 100, 300)


turtle.done()

