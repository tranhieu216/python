import turtle

def write(text):
    t.write(text, font = ('Arial', 18, 'nomal'))

def tri(x1, y1, x2, y2, x3, y3):
    t.pu()
    t.goto(x1, y1)
    t.write(t.pos())
    t.pd()
    t.goto(x2, y2)
    t.write(t.pos())
    t.goto(x3, y3)
    t.write(t.pos())
    t.goto(x1, y1)

t = turtle.Turtle()
t.shape('turtle')
t.width(5)
t.color('blue')

tri(-200, 0, 100, 0, -200, 200)

turtle.done()
