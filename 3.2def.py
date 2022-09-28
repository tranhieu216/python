import turtle


# Это новая команда - функция
# Назовем ее triangle()
# def пишем с начала строки без пробелов
def triangle():
    # здесь пишем команды - рисовать треугольник
    # команды надо начать с <TAB> (отступа)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
    t.fd(100)
    t.lt(120)
# Здесь закончилась новая команда triangle


# Новая функция ornament()
# triangle() можно вызвать внутри функции ornament()
def ornament():
    # код в функции пишем с отступом <TAB>


    t.color('red')
    # выполняется новая команда triangle
    triangle()
    t.lt(45)


    t.color('green')
    # еще раз выполняется новая команда triangle
    triangle()
    t.lt(45)


    t.color('blue')
    # вызывать (выполнять) новые команды можно сколько хочешь
    triangle()
# Здесь закончилась функция ornament


# Это место для выполнения команд. Новых и старых.
t = turtle.Turtle()
t.shape('turtle')
t.width(3)


ornament()          # вызов функции ornament


turtle.done()