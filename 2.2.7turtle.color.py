
# Вариант: номер варианта
import turtle

n = input()
t = turtle.Turtle()

def sq1(size):
    t.begin_fill()
    t.color('red', 'yellow')

    for i in range(5):
        t.fd(size)
        t.lt(72)

    t.end_fill()

def sq2():
    t.begin_fill()
    t.color('red', 'yellow')

    for i in range(5):
        t.fd(30)
        t.rt(72)
        t.fd(30)
        t.lt(144)

    t.end_fill()

if (n == 'Вариант 1'):
    sq1(100)
elif (n == 'Вариант 2'):
    sq2()

turtle.done()