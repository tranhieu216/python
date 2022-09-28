#1 Регистрация почты

print('ввустите пользователем логин')
login = input()
if '@' in login:
    print('Некорректный логин')

print('ввустите резервный адрес')
address = input()
if '@' not in address:
    print('Некорректный адрес')
else:
    print('ok')