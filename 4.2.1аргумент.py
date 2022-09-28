import turtle

def sq(col):
    t.pencolor(col)
    for i in range(4):
        t.fd(100)
        t.lt(90)

def triangle(col):
    t.pencolor(col)
    for i in range(3):
        t.fd(100)
        t.lt(120)

t = turtle.Turtle()
t.shape('turtle')
t.width(5)

sq('yellow')
t.lt(45)
sq('green')

t.lt(135)
triangle('red')
t.lt(90)
triangle('blue')