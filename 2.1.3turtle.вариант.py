import turtle

n = input()

if (n == 'Вариант 1'):
    def option(size):
        for i in range(3):
            t.fd(size)
            t.lt(90)
elif (n == 'Вариант 2'):
    def option(size):
        for i in range(3):
            t.lt(90)
            t.fd(size)
elif (n == 'Вариант 3'):
    def option(size):
        t.fd(size)
        t.lt(90)
        t.fd(size / 2)
        t.lt(180)
        t.fd(size)

t = turtle.Turtle()
t.shape('turtle')
t.width(5)
t.color('black')

option(100)

turtle.done()
