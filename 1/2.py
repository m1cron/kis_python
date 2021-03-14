import math

def func1(x):
    return 71*((math.log(x) + math.cos(x))**5) - 50*(x**4)

def func2(x):
    return (x**6) - math.exp(x) + 45

def func3(x):
    return math.log((x**6)) - x + 20

def func4(x):
    return ((27*(x**5) + 6*(x**6))/83) - 7*(x**4)

def f12(x):
    if x < 59:
        return func1(x)
    elif 59 <= x < 108:
        return func2(x)
    elif 108 <= x < 135:
        return func3(x)
    elif x >= 135:
        return func4(x)