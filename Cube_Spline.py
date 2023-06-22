import numpy as np


def cube_spline(x, y):
    n = len(x) - 1
    A = np.zeros((4 * n, 4 * n))
    b = np.zeros(4 * n)
    # First's and End's of S(i)'s=Yi's
    for i in range(n):
        for j in range(4):
            A[2 * i, 4 * i + j] = x[i] ** (3 - j)
            A[2 * i + 1, 4 * i + j] = x[i + 1] ** (3 - j)
        b[2 * i] = y[i]
        b[2 * i + 1] = y[i + 1]
    # First derivation
    for i in range(n - 1):
        A[i + 2 * n, 4 * i] = 3 * x[i + 1] ** 2
        A[i + 2 * n, 4 * i + 1] = 2 * x[i + 1]
        A[i + 2 * n, 4 * i + 2] = 1
        A[i + 2 * n, 4 * (i + 1)] = -3 * x[i + 1] ** 2
        A[i + 2 * n, 4 * (i + 1) + 1] = -2 * x[i + 1]
        A[i + 2 * n, 4 * (i + 1) + 2] = -1
    # Second derivation
    for i in range(n - 1):
        A[i + 3 * n - 1, 4 * i] = 6 * x[i + 1]
        A[i + 3 * n - 1, 4 * i + 1] = 2
        A[i + 3 * n - 1, 4 * (i + 1)] = -6 * x[i + 1]
        A[i + 3 * n - 1, 4 * (i + 1) + 1] = -2
    A[4 * n - 2, 0] = 6 * x[0]
    A[4 * n - 1, 4 * (n - 1)] = 6 * x[n]
    A[4 * n - 2, 1] = 2
    A[4 * n - 1, 4 * (n - 1) + 1] = 2

    return np.dot(np.linalg.inv(A), b)


def interpolation(x_0, x, y):
    n = len(x)
    j = 0
    for i in range(n):
        if x[i] >= x_0:
            j = i - 1
            break
    C = cube_spline(x, y)
    return (
        C[4 * j] * x_0**3
        + C[4 * j + 1] * x_0**2
        + C[4 * j + 2] * x_0
        + C[4 * j + 3]
    )


x = np.array([0, 1, 2, 3, 4])
y = np.array([21, 24, 24, 18, 16])
x_0 = 3.5
print(interpolation(x_0, x, y))
