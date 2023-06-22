import math

def f(x):
    return (1/(2+x))

def fixedPoint(x_0, tol=1e-6, N=100):
    x_1 = x_0
    for i in range(N):
        x_2 = f(x_1)
        if abs(x_2 - x_1) < tol:
            return x_2
        x_1 = x_2
    return "ERROR"

print(fixedPoint(0.4142))