#6 Собери число

print('введите трехзначное число')
n = int(input()) #234 : cba

a = n % 10      #4
a1 = n // 10    #23

b = a1 % 10     #3
c = a1 // 10   #2

s1 = a + b
s2 = b + c 

if s1 < s2 and (s1 / 10) < 1:
    print( 10 * s2 + s1)
elif s1 < s2 and (s1 / 10) >= 1:
    print(100 * s2 + s1)
elif s1 > s2 and (s2 / 10) < 1:
    print( 10 * s1 + s1)
elif s1 > s2 and (s2 / 10) >= 1:
    print(100 * s2 + s1)