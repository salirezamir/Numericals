import math

def f(x):
    return x**3 - 2*x - 5

def df(x):
    return 3*x**2 - 2

def newton_raphson(x0, tolerance=1e-6, N=1000):
    for i in range(N):
        fx = f(x0)
        if abs(fx) < tolerance:
            return x0
        dfx = df(x0)
        if dfx == 0:
            return "ERROR_dfx=0"
        x0 = x0 - fx / dfx
    return "ERROR_i>N"

print(newton_raphson(2))
