import turtle


t = turtle.Turtle()


t.color('red', 'yellow')  # линия - красный, внутри - жёлтый


t.begin_fill()        # начинаем рисовать замкнутую фигуру


t.forward(75)         # нарисуем квадрат
t.left(90)
t.forward(75)
t.left(90)
t.forward(75)
t.left(90)
t.forward(75)
t.left(90)


t.end_fill()          # заканчиваем рисовать фигуру


turtle.done()