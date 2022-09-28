import turtle


def write(text):
        t.write(text, font=('Arial', 18, 'normal'))


t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('red')


def line(x1, y1, x2, y2):
    t.pu()
    t.goto(x1, y1)
    t.pd()
    write(t.pos())
    t.goto(x2, y2)
    write(t.pos())

line(-200, 50, 100, -50)


turtle.done()