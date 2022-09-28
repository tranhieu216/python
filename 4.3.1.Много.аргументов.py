import turtle

def triangle(col, size):

    t.color(col)   
    t.fd(size)     
    t.lt(120)
    t.fd(size)     
    t.lt(120)
    t.fd(size)     
    t.lt(120)

t = turtle.Turtle()
t.shape('turtle')
t.width(3)

triangle('red', 30)

triangle('green', 60)

triangle('blue', 90)

turtle.done()