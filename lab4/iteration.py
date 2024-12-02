import numpy as np

# Константы
n = 2
eps = 1e-4
max_iter = 20

# Типы данных
a = np.zeros((n, n))
x = np.zeros(n)
f = np.zeros(n)
x0 = np.zeros(n)
print(x0)

# Вычисление нормы матрицы
def norma(a):
    """
    Вычисляет норму матрицы как квадратный корень из суммы квадратов всех элементов
    """
    res = np.sum(a**2)  # суммируем квадраты всех элементов матрицы
    return np.sqrt(res)

# Определение функций системы
def func(x, i):
    """
    Задает значения функций системы. Выбирает функцию по индексу i
    """
    if i == 0:
        return (2 - np.sin(x[1])) / 2  # значение первой функции: sin(y) + 2x = 2
    elif i == 1:
        return 0.7 - np.cos(x[0] - 1)  # значение второй функции: cos(x - 1) + y = 0.7

# Построение матрицы Якоби
def matr_jacobi(x, i, j):
    """
    Задает значение элемента матрицы Якоби по индексам строки и столбца i, j
    """
    if i == 0 and j == 0:
        return 2  # частная производная первой функции по x
    elif i == 0 and j == 1:
        return np.cos(x[1])  # частная производная первой функции по y
    elif i == 1 and j == 0:
        return np.sin(x[0] - 1)  # частная производная второй функции по x
    elif i == 1 and j == 1:
        return 1  # частная производная второй функции по y

# Вывод матрицы
def vivod_matr(mat):
    """
    Печатает матрицу с заданной точностью
    """
    for row in mat:
        print(" ".join(f"{elem:10.5f}" for elem in row))

# Вывод вектора
def vivod_vector(vector):
    """
    Печатает вектор с заданной точностью
    """
    for i, value in enumerate(vector):
        print(f"x{i+1} = {value:10.5f}")

# Начало основной программы
iter_count = 0  # счетчик итераций
x0 = np.array([0.0, 0.0])  # начальное приближение

while True:
    # Построение матрицы Якоби для текущего приближения
    for i in range(n):
        for j in range(n):
            a[i, j] = matr_jacobi(x0, i, j)
    
    # Вывод текущего приближения
    vivod_vector(x0)
    
    # Вычисление нормы матрицы Якоби
    print("Норма матрицы Якоби =", norma(a))
    
    # Вывод номера итерации
    print("Номер итерации -", iter_count)
    print("=================")
    
    # Нахождение нового приближения функции
    for i in range(n):
        x[i] = func(x0, i)
    
    # Проверка на сходимость
    max_diff = np.max(np.abs(x - x0))  # находим максимальное изменение
    
    # Обновляем значения для следующей итерации
    x0 = x.copy()
    iter_count += 1
    
    # Проверяем критерий остановки
    if max_diff < eps or iter_count >= max_iter:
        break

# Вывод результата
print("Решение найдено:")
vivod_vector(x0)
