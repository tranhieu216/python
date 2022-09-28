import turtle

def spileft(size):
    t.fd(size / 2)
    t.rt(90)
    t.fd(size)
    t.rt(90)
    t.fd(size)
    t.rt(90)
    t.fd(size * 2)
    t.rt(90)
    t.fd(size * 1.5)

def spiright(size):
    t.fd(size * 1.5)
    t.rt(90)
    t.fd(size * 2)
    t.rt(90)
    t.fd(size)
    t.rt(90)
    t.fd(size)
    t.rt(90)
    t.fd(size / 2)

def spidownleft(size):
    t.fd(size / 2)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size * 2)
    t.lt(90)
    t.fd(size * 1.5)

def spidownright(size):
    t.fd(size * 1.5)
    t.lt(90)
    t.fd(size * 2)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size / 2)

def uzorup(size):
    spileft(size)
    spiright(size)

def uzordown(size):
    spidownleft(size)
    spidownright(size)

def uzor(size):
    uzorup(size)
    t.up()
    t.fd(size * 2)
    t.down()
    uzordown(size)

def uzor2(size):
    uzor(size)
    t.up()
    t.fd(size * 2)
    t.down()
    uzor(size)

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.pencolor('red')

uzor2(50)

turtle.done()
