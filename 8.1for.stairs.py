import turtle

def stairs(size, n):
    # до цикла
    p = t.pos()         # запомнили точку старта
    t.lt(90)

    # цикл - повторить много раз
    for i in range(n):  # повторить n раз
        t.fd(size)
        t.rt(90)
        t.fd(size)
        t.lt(90)

    # закончились отступы - закончился цикл
    # после цикла возвращаемся назад
    t.color('red')
    t.goto(p)           # вернулись в точку старта


t = turtle.Turtle()
t.shape('turtle')
t.width(3)
t.color('blue')


stairs(50, 3)


turtle.done()