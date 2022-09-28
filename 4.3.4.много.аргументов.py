import turtle

def snowline(col, x):

    t.pencolor(col)
    t.fd(x * 2)

    for i in range(3):
        t.rt(45)
        t.fd(x)
        t.rt(180)
        t.fd(x)
        t.rt(90)

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

snowline('blue', 100)

turtle.done()