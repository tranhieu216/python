import turtle

def write(text):
        t.write(text, font=('Arial', 18, 'normal'))

def middleline(x1, x2):

    t.pencolor('blue')

    t.pu()
    t.goto(x1, 0)
    t.pd()
    write(t.pos())

    d = x2 - x1
    t.fd(d/2)
    write(t.pos())
    t.dot(10)
    t.fd(d/2)
    write(t.pos())

t = turtle.Turtle()
t.width(5)
t.shape('turtle')

middleline(-200, 100)

turtle.done()
