import math

def f11(x):
    c = ((x**4)/67)-(x**3) - ((math.cos((x**4)/30) + math.fabs(x))/ (math.exp((x**3) + math.fabs(x)) + 92*x)) + math.sqrt(19*(x**3)+(x**4)+61)
    return c