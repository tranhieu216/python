import turtle

def write(text):
        t.write(text, font=('Arial', 18, 'normal'))

def coord():
        x = int(t.xcor())
        y = int(t.ycor())
        write((x, y))

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

def rect(x1, y1, x2, y2, rect_col, text_col):

    t.pu()
    t.goto(x1, y1)
    coord()
    t.pd()

    t.begin_fill()
    t.color(text_col, rect_col)

    t.goto(x2, y1)
    coord()

    t.goto(x2, y2)
    coord()

    t.goto(x1, y2)
    coord()

    t.goto(x1, y1)
    coord()

    t.end_fill()

rect(-10, -20, 200, 150, "green", "red")

turtle.done()