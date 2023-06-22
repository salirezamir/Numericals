import math

def lagrangeInterpolation(x, y, x_0):
    n = len(x)
    p = 0
    for i in range(n):
        tmp = y[i]
        for j in range(n):
            if j != i:
                tmp *= (x_0 - x[j]) / (x[i] - x[j])
        p += tmp
    return p

x = [0.1, 0.2, 0.3, 0.4, 0.5]
y = [1.002, 1.045, 1.091, 1.14, 1.192]
x_0 = 0.25

print(lagrangeInterpolation(x, y, x_0))
