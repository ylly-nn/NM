def Lagr(n, x, y, q):
    """
    Вычисляет значение интерполяционного полинома Лагранжа в точке q.

    :param n: Количество узлов интерполяции (целое число)
    :param x: Список абсцисс узлов (массив или список)
    :param y: Список ординат узлов (массив или список)
    :param q: Точка, в которой нужно вычислить значение интерполяционного полинома (число)
    :return: Значение интерполяционного полинома Лагранжа в точке q
    """
    L = 0
    for i in range(n):
        s = 1
        for j in range(n):
            if j != i:
                s *= (q - x[j]) / (x[i] - x[j])
        L += y[i] * s
    return L
# Пример данных
x=list()
x.append(0.1)
for i in range (1, 20):
    x.append(x[i-1]+0.1)
n = len(x)
for i in range(n):
    x[i]=round(x[i], 1)  

y = [1.99, 2.03, 2.20, 2.39, 2.19, 2.61, 2.35, 2.60, 2.55, 2.49, 2.50, 2.52, 2.44, 2.35, 2.26, 2.19, 2.24, 2.34, 1.96, 2.19]

q=0.05
# Вычисляем значение интерполяционного полинома в точке q
while q<2:
    q+=0.05
    q=round(q,2)
    result = Lagr(n, x, y, q)
    result = round(result, 3)
    print(f"X = {q}, Y={result}")