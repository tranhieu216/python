#3 калькулятор
a = float(input())
b = float(input())
c = input()
if c == '+':
    print('a + b = ', a + b)
elif c == '-':
    print('a - b = ', a - b)
elif c == '*':
    print('a * b = ', a * b)
elif (c == '/') and (b == 0):
    print('888888')
elif (c == '/'):
    print('a / b = ', a / b)
else:
    print('888888')