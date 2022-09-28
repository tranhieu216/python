import turtle   # есть библиотека turtle
import math     # есть библиотека math


t = turtle.Turtle()  # вызываем функцию Turtle из библиотеки turtle
t.shape('turtle')
t.width(3)


t.fd(100)
t.lt(90)
t.fd(100)
t.lt(135)
t.fd(100*math.sqrt(2))


turtle.done()