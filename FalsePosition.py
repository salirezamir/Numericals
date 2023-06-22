import math

def f(x):
    return x**3 - 2*x - 5

def false_position(a, b, tol=1e-6, N=100):
    if f(a) * f(b) >= 0:
        return "ERROR_BOLTZANO"
    for i in range(N):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if abs(f(c)) < tol:
            return c
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return "ERROR_i>N"

print(false_position(1, 3))
