import turtle

def petal(size):
    t.pencolor('orange')
    t.fd(size)
    t.color('red')
    t.stamp()
    t.color('orange')
    t.bk(size)

def flower(size):
    t.seth(0)
    petal(size)

    t.seth(20)
    petal(size)

    t.seth(45)
    petal(size)

    t.seth(90)
    petal(size)

    t.seth(-20)
    petal(size)

    t.seth(-45)
    petal(size)

    t.seth(-90)
    petal(size)


t = turtle.Turtle()
t.shape('turtle')
t.width(5)

flower(100)

turtle.done()