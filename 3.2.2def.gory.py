import turtle

def pik(size):
    t.fd(size)
    t.rt(120)
    t.fd(size)

def gory():
    t.lt(60)
    pik(100)
    t.lt(60)

t = turtle.Turtle()
t.shape('turtle')
t.width(5)
t.pencolor('blue')
t.pensize(5)

for i in range(3):
    gory()
    
turtle.done()