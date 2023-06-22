import math

def newtonInterpolation(x, y, x_0):
    n = len(x)
    f = [[None] * n for _ in range(n)]
    for i in range(n):
        f[i][0] = y[i]
    for j in range(1, n):
        for i in range(n-j):
            f[i][j] = (f[i+1][j-1] - f[i][j-1]) / (x[i+j] - x[i])
    p = f[0][0]
    for j in range(1, n):
        tmp = f[0][j]
        for i in range(j):
            tmp *= (x_0 - x[i])
        p += tmp
    return p

x = [0.1, 0.2, 0.3, 0.4, 0.5]
y = [1.002, 1.045, 1.091, 1.14, 1.192]
x_0 = 0.25

print(newtonInterpolation(x, y, x_0))
