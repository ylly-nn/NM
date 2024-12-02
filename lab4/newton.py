import math

# Параметры задачи
n = 2
eps = 1e-4
max_iter = 1000  # максимальное количество итераций

# Определение функции системы уравнений
def func(x, i):
    if i == 1:
        return math.sin(x[1]) + 2 * x[0] - 2
    elif i == 2:
        return math.cos(x[0] - 1) + x[1] - 0.7

# Определение Якобиана
def jacobian(x, i, j):
    if i == 1:
        if j == 1:
            return 2  # частная производная по x в первом уравнении
        elif j == 2:
            return math.cos(x[1])  # частная производная по y в первом уравнении
    elif i == 2:
        if j == 1:
            return -math.sin(x[0] - 1)  # частная производная по x во втором уравнении
        elif j == 2:
            return 1  # частная производная по y во втором уравнении

# Вывод вектора значений
def print_vector(vector):
    output = "\n".join(f"x{idx + 1} = {val:.5f}" for idx, val in enumerate(vector))
    print(output)



# Решение системы линейных уравнений методом Гаусса
def solve_system(n, A, b):
    # Прямой ход метода Гаусса с выбором ведущего элемента
    for i in range(n):
        # Поиск максимального элемента для выбора ведущей строки
        max_elem = abs(A[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > max_elem:
                max_elem = abs(A[k][i])
                max_row = k
        
        # Если ведущий элемент слишком мал, система вырожденная
        if max_elem < 1e-21:
            raise ValueError("Matrix is singular or nearly singular.")
        
        # Обмен строк
        if max_row != i:
            A[i], A[max_row] = A[max_row], A[i]
            b[i], b[max_row] = b[max_row], b[i]

        # Нормализация строки
        pivot = A[i][i]
        A[i] = [a / pivot for a in A[i]]
        b[i] /= pivot

        # Обнуление элементов ниже главного
        for k in range(i + 1, n):
            factor = A[k][i]
            A[k] = [A[k][j] - factor * A[i][j] for j in range(n)]
            b[k] -= factor * b[i]

    # Обратный ход для получения решения
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))
    return x

# Основная программа
def newton_method():
    # Начальное приближение
    x = [0.0, 0.0]
    iter_count = 0

    while iter_count < max_iter:
        print_vector(x)
        print(f"Итерация № {iter_count}")
        print("=" * 20)

        # Построение Якобиана и вектора правой части
        A = [[jacobian(x, i + 1, j + 1) for j in range(n)] for i in range(n)]
        f = [-func(x, i + 1) for i in range(n)]

        # Решение системы линейных уравнений для нахождения dx
        dx = solve_system(n, A, f)

        # Нахождение максимального шага
        max_dx = max(abs(dx[i]) for i in range(n))

        # Обновление приближения
        x = [x[i] + dx[i] for i in range(n)]

        # Проверка условия остановки
        if max_dx < eps:
            break

        iter_count += 1

    if iter_count == max_iter:
        print("Метод Ньютона не сошелся за максимальное число итераций")
    else:
        print("Решение найдено:")
        print_vector(x)

# Запуск программы
newton_method()
