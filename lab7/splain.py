import numpy as np

def progon(a, b, c, d, n):
    # Метод прогонки для решения системы линейных уравнений
    for i in range(1, n):
        m = a[i] / b[i-1]
        b[i] = b[i] - m * c[i-1]
        d[i] = d[i] - m * d[i-1]
    
    x = np.zeros(n)
    x[n-1] = d[n-1] / b[n-1]
    
    for i in range(n-2, -1, -1):
        x[i] = (d[i] - c[i] * x[i+1]) / b[i]
    
    return x

def spline(n, x, y, xx):
    # Инициализация массивов для коэффициентов
    a = np.zeros(n)
    b = np.zeros(n)
    c = np.zeros(n)
    d = np.zeros(n)
    z = np.zeros(n)
    
    # Первоначальные коэффициенты для граничных условий
    a[0] = 0
    b[0] = -2
    c[0] = 1
    d[0] = 3 * (y[1] - y[0]) / (x[1] - x[0])

    # Вычисление коэффициентов для системы
    for j in range(1, n-1):
        hj = x[j+1] - x[j]
        hj1 = x[j] - x[j-1]
        am = hj1 / (hj1 + hj)
        al = 1 - am
        a[j] = al
        b[j] = -2
        c[j] = am
        d[j] = 3 * (am * (y[j+1] - y[j]) / hj + al * (y[j] - y[j-1]) / hj1)

    a[n-1] = 1
    b[n-1] = -2
    c[n-1] = 0
    d[n-1] = 3 * (y[n-1] - y[n-2]) / (x[n-1] - x[n-2])

    # Решение системы методом прогонки
    z = progon(a, b, c, d, n)

    # Если xx совпадает с последним значением x, то возвращаем y[n-1]
    if xx == x[n-1]:
        return y[n-1]

    # Вычисление значения сплайна в точке xx
    for j in range(1, n):
        if x[j] > xx:
            hj = x[j] - x[j-1]
            t = (xx - x[j-1]) / hj
            t1 = 1 - t
            t2 = t * t
            t12 = t1 * t1
            s = y[j-1] * t12 * (1 + 2 * t) + y[j] * t2 * (3 - 2 * t) + z[j-1] * hj * t * t12 - z[j] * hj * t2 * t1
            return s

# Пример использования функции:
x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
y = [1.99, 2.03, 2.20, 2.39, 2.19, 2.61, 2.35, 2.60, 2.55, 2.49, 2.50, 2.52, 2.44, 2.35, 2.26, 2.19, 2.24, 2.34, 1.96, 2.19]

n = len(x)
xx = 0.1
for i in range(39):

    result = spline(n, x, y, xx)
    xx=round(xx,2)
    result=round(result,3)
    print(f"X = {xx}, Y = {result}")
    xx+=0.05
