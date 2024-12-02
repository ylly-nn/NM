def newton_interpolation(x, y, x0):
    n = len(x)

    # Создаем таблицу разделенных разностей
    divided_differences = [[0] * n for _ in range(n)]
    
    # Заполняем первую колонку таблицы значениями y
    for i in range(n):
        divided_differences[i][0] = y[i]
    
    # Вычисляем разделенные разности
    for j in range(1, n):
        for i in range(n - j):
            divided_differences[i][j] = (divided_differences[i + 1][j - 1] - divided_differences[i][j - 1]) / (x[i + j] - x[i])

    # Вычисляем значение интерполированной функции в точке x0
    result = divided_differences[0][0]
    term = 1.0
    for i in range(1, n):
        term *= (x0 - x[i - 1])
        result += divided_differences[0][i] * term

    return result

# Пример использования функции:
x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
y = [1.99, 2.03, 2.20, 2.39, 2.19, 2.61, 2.35, 2.60, 2.55, 2.49, 2.50, 2.52, 2.44, 2.35, 2.26, 2.19, 2.24, 2.34, 1.96, 2.19]

x0 = 0.1  # Точка, в которой мы хотим интерполировать
for i in range(39):
    result = newton_interpolation(x, y, x0)
    x0=round(x0,2)
    result=round(result,3)
    print(f"X = {x0}, Y = {result}")
    x0+=0.05
