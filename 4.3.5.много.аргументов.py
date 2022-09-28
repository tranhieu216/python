import turtle

def snowline(col, x):

    b = t.pos()
    t.pencolor(col)
    t.fd(x * 2)

    for i in range(3):
        t.rt(45)
        t.fd(x)
        t.rt(180)
        t.fd(x)
        t.rt(90)
    t.goto(b)
    
def snowflake(col, x):

    for i in range(6):
        snowline(col, x)
        t.rt(75)

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

snowflake('blue', 30)

turtle.done()