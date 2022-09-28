import turtle

def snowline(size):
    t.pencolor('blue')
    t.fd(size)
    b = t.pos()
    t.rt(45)
    for i in range(3):
        t.fd(size / 3)
        t.goto(b)
        t.lt(45)

def snowflake(size):
    o = t.pos()
    for i in range(6):
        snowline(size)
        t.goto(o)
        t.rt(30)

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

#snowline(100)
snowflake(100)

turtle.done()