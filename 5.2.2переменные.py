import turtle
import math

def square(x, y, size):
    # перейти в (x, y) и нарисовать точку
    t.pu()
    t.goto(x, y)
    t.pd()
    t.dot(5)

    # вычислить размер до вершины
    # результат записать в переменную half
    half = size / 2

    # перейти в вершину
    t.pu()
    t.fd(half)       # читаем число из переменной half
    t.lt(90)
    t.fd(half)       # читаем число из переменной half
    t.lt(90)
    t.pd()

    # нарисовать квадрат
    t.color('blue')
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)

    # вычислить длину диагонали
    # результат записать в переменную d
    d = math.sqrt(2) * size

    # нарисовать диагональ
    t.lt(45)
    t.fd(d)         # читаем число из переменной d

t = turtle.Turtle()
t.width(5)

square(0, 0, 100)

turtle.done()