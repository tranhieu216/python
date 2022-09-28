import turtle


def triangle():
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)

def ornament():

    t.color('red')
    triangle()
    t.lt(45)


    t.color('green')
    triangle()
    t.lt(45)


    t.color('blue')
    triangle()

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

ornament()   
t.lt(45)
ornament()


turtle.done()