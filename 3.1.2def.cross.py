import turtle

n = input()
t = turtle.Turtle()
t.pensize(4)

def cross(size):
    t.pencolor('blue')

    for i in range(4):
        t.fd(size)
        t.lt(180)
        t.fd(size)
        t.rt(90)

if (n == 'вариант 1'):

    cross(100)

    for i in range(2):
        t.lt(45)
        t.up()
        t.fd(50 * (2 ** 0.5))
        t.down()
        t.rt(45)
        cross(100)
elif (n == 'вариант 2'):

    t.lt(45)
    cross(100)

    for i in range(2):
        t.rt(45)
        t.up()
        t.fd(50 * (2 ** 0.5))
        t.down()
        t.lt(45)
        cross(100)

turtle.done()