import turtle

def sq1(size):
    t.lt(90)
    t.fd(size * 0.5)
    for i in range(3):
        t.rt(90)
        t.fd(size)
    t.rt(90)
    t.fd(size * 0.5)

def sq2(size):
    t.pencolor('red')
    sq1(size)
    t.lt(45)
    t.pencolor('blue')
    for i in range(4):
        t.rt(90)
        t.fd(size)

t = turtle.Turtle()
t.shape('turtle')
t.width(5)

#sq1(100)
#sq2(100)