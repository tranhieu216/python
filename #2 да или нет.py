#2 да или нет?!
print('Ввестите да или нет')
string1 = input()
string2 = input()
if (string1 == 'да' and string2 == 'да') or (string1 == 'да' and string2 == 'нет') or (string1 == 'нет' and string2 == 'нет') or (string1 == 'нет' and string2 == 'да'):
    print('ВЕРНО')
else:
    print('НЕВЕРНО')