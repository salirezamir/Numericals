import math

def f(x):
    return x**3 - 2*x - 5

def bisection(a, b, tol=1e-6, N=100):
    if f(a) * f(b) >= 0:
        return "ERROR_BOLTZANO"
    for i in range(N):
        c = (a + b) / 2.0
        if abs(f(c)) < tol:
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return "ERROR_i>N"

print(bisection(1, 3))
