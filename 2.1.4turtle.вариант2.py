import turtle

n = input()

def option(size):
    b = t.pos()
    
    if (n == 'Вариант 1'):
        t.fd(size)
        t.goto(b)
        t.lt(45)
        t.fd(size)
        t.goto(b)
        t.lt(45)
        t.fd(size)

    elif (n == 'Вариант 2'):
        for i in range(0, 4, 1):
            t.fd(size)
            t.goto(b)
            t.lt(30)

    elif (n == 'Вариант 3'):
        for i in range(0, 4, 1):
            t.fd(size)
            t.goto(b)
            t.lt(90)


t = turtle.Turtle()
t.shape('turtle')
t.width(5)
t.color('black')

option(100)

turtle.done()
