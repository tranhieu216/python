import turtle

def dash(col, size):

    t.pencolor(col)

    t.pd()
    t.fd(size)
    
    t.pu()
    t.fd(size)

    t.pd()
    t.fd(size)

def dtri(col, size):

    for i in range(3):
        dash(col, size)
        t.lt(120)

t = turtle.Turtle()
t.shape('turtle')
t.width(5)

dtri('red', 100)

turtle.done()
