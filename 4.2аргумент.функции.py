import turtle


# col запомнит название цвета для треугольника
def triangle(col):
    # указываем col в другой команде
    t.color(col)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)


# Здесь закончилась новая команда triangle


# Это место для выполнения команд. Новых и старых.
t = turtle.Turtle()
t.shape('turtle')
t.width(3)


# Указываем цвет для треугольника 'red'
triangle('red')
t.lt(45)


# Указываем цвет для треугольника 'green'
triangle('green')
t.lt(45)


# Указываем цвет для треугольника 'blue'
triangle('blue')


turtle.done()