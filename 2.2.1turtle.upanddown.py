import turtle

n = input()

t = turtle.Turtle()
t.shape('turtle')
t.width(5)
t.color('black')
    
if (n == 'Вариант 1'):
    for i in range(0, 4, 1):
        t.fd(50)
        t.up()
        t.fd(25)
        t.down()

elif (n == 'Вариант 2'):
    for i in range(0, 4, 1):
        t.fd(25)
        t.up()
        t.fd(50)
        t.down()

elif (n == 'Вариант 3'):
    for i in range(0, 2, 1):
        t.fd(50)
        t.up()
        t.fd(20)
        t.down()
        t.fd(10)
        t.up()
        t.fd(20)
        t.down()

turtle.done()
