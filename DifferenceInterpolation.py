import math

def backwardInterpolation(x, y, x_0):
    n = len(x)
    h = x[1] - x[0]
    b = [[y[i] for i in range(n)]]
    for j in range(1, n):
        row = []
        for i in range(n - j):
            row.append(b[j-1][i+1] - b[j-1][i])
        b.append(row)
    p = b[0][n-1]
    q = (x_0 - x[n-1]) / h
    for i in range(1, n):
        p += (b[i][n-i-1] * q) / math.factorial(i)
        q *= (q + i)
    return p

def forwardInterpolation(x, y, x_0):
    n = len(x)
    h = x[1] - x[0]
    f = [[y[i] for i in range(n)]]
    for j in range(1, n):
        row = []
        for i in range(n - j):
            row.append(f[j-1][i+1] - f[j-1][i])
        f.append(row)
    p = f[0][0]
    q = (x_0 - x[0]) / h
    for i in range(1, n):
        p += (f[i][0] * q) / math.factorial(i)
        q *= (q - i)
    return p

x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
y = [1.0, 1.221, 1.492, 1.835, 2.274, 2.718]
x_0 = 0.3

if (abs(max(x)-x_0)>abs(min(x)-x_0)):
    print(backwardInterpolation(x, y, x_0))
else :
    print(forwardInterpolation(x, y, x_0))
