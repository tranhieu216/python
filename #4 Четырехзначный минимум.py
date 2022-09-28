#4 Четырехзначный минимум
import math

n = int(input()) #2345 : dcba

a = n % 10      #5
a1 = n // 10    #234

b = a1 % 10     #4
b1 = a1 // 10   #23

c = b1 % 10     #3
d = b1 // 10    #2

s = a + b + c + d
p = a * b * c * d

if a+b+c==0: #3 số 0
    print(d,c,b,a)
elif c*b==0 and b*a==0 and a*c==0 and a+b+c!=0: #2 số 0
    d = min(d, a+b+c)
    a = s - d
    print(d,0,0,a)
elif (d*a==0 or d*b==0 or d*c==0) and (c*b!=0 or b*a!=0 or a*c!=0): #1 số 0
    if s == a + b + c:
        s = a + b + c
        p = a * b * c
    elif s == a + b + d:
        s = a + b + d
        p = a * b * d
    elif s == a + c + d:
        s = a + c + d
        p = a * c * d
    elif s == b + c +d:
        s = b + c + d
        p = b * c * d
    a = max(a,b,c,d)
    S = s - a
    P = p / a
    D = S * S -  4 * P 
    d = int((S - math.sqrt(D)) / 2)
    b = int((S + math.sqrt(D)) / 2)
    print(d,0,b,a)
elif a*b!=0 and b*c!=0 and c*a!=0: #ko có số 0
    a = max(a,b,c,d)
    d = min(a,b,c,d)
    S = s - (a + d)
    P = p / (a * d)
    D = S * S -  4 * P 
    c = int((S - math.sqrt(D)) / 2)
    b = int((S + math.sqrt(D)) / 2)
    print(d,c,b,a)