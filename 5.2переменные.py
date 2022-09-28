import turtle

def middleLine(size):
    t.color('blue')
    t.fd(size)

    # middle - переменная (variable).
    # В переменную можно записать (write) число
    # и потом прочитать (read)
    middle = size / 2   # запишем в переменную middle число size/2
    t.bk(middle)        # прочитаем число из переменной middle

    t.color('red')
    t.dot(5)

t = turtle.Turtle()
t.width(3)

middleLine(200)

turtle.done()