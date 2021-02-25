import math

def f14(n):
    if n==0:
        return 5
    else:
        return 0.25*f14(n-1) - math.sin(f14(n-1))