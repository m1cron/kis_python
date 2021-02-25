import math

def func1(n, m):
    sum = 0
    for i in range(n):
        for j in range(m):
            sum += (math.log(j+1) - math.fabs(i+1) + 22)
    return sum

def func2(n, m):
    sum = 0
    for i in range(n):
        for _ in range(m):
            sum += (i+1 + ((i+1)**7))
    return sum

def f13(n, m):
    return 62 * func1(n,m) - func2(n,m)