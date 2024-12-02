import numpy as np

def gauss_solve(a, b):
    n = len(b)

    # Прямой ход
    for i in range(n):
        for j in range(i + 1, n):
            ratio = a[j][i] / a[i][i]
            for k in range(i, n):
                a[j][k] -= ratio * a[i][k]
            b[j] -= ratio * b[i]

    # Обратный ход
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= a[i][j] * x[j]
        x[i] /= a[i][i]

    return x

def least_squares(n, x, y, q):
    # Матрица коэффициентов
    a = np.zeros((3, 3))

    # Вектор правых частей
    b = np.zeros(3)

    # Вычисление элементов
    for i in range(n):
        a[0][0] += 1
        a[0][1] += x[i]
        a[0][2] += x[i] * x[i]
        a[1][0] += x[i]
        a[1][1] += x[i] * x[i]
        a[1][2] += x[i] * x[i] * x[i]
        a[2][0] += x[i] * x[i]
        a[2][1] += x[i] * x[i] * x[i]
        a[2][2] += x[i] * x[i] * x[i] * x[i]

        b[0] += y[i]
        b[1] += y[i] * x[i]
        b[2] += y[i] * x[i] * x[i]

    # Решение методом Гаусса
    coefficients = gauss_solve(a, b)

    c0, c1, c2 = coefficients[0], coefficients[1], coefficients[2]
    result = c0 + c1 * q + c2 * q * q
    return result, c0, c1, c2



x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
y = [1.99, 2.03, 2.20, 2.39, 2.19, 2.61, 2.35, 2.60, 2.55, 2.49, 2.50, 2.52, 2.44, 2.35, 2.26, 2.19, 2.24, 2.34, 1.96, 2.19]
q = 0.1
n = len(x)


for i in range(39):
    result, c0, c1, c2 = least_squares(n, x, y, q)
    q=round(q,2)
    result=round(result,3)
    print(f"X = {q}, Y = {result}")
    q+=0.05

print(f"Коэффициенты: c0={c0}\nc1={c1} \nc2={c2}")


