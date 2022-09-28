import turtle

def square(x, y, size):
    # перейти в (x, y) и нарисовать точку
    t.pu()
    t.goto(x, y)
    t.pd()
    t.dot(10)


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
    p = t.pos()      # запишем точку в переменную p
    t.fd(size)
    t.lt(90)
    t.fd(size)
    t.lt(90)


    # нарисовать диагональ
    t.goto(p)        # прочитаем точку из переменной p

t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('red')

square(-200, 50, 100)

turtle.done()
