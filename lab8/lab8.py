import math

# Функция для вычисления производных dy1/dx и dy2/dx
def derivatives(x, y1, y2):
    dy1 = math.cos(x + y2)
    dy2 = math.sin(x - y2)
    return dy1, dy2

# Метод Эйлера
def euler_method(a, b, h, y1_init, y2_init):
    # Количество шагов
    n = int((b - a) / h)

    # Массивы для хранения значений x, y1 и y2 на каждом шаге
    x = [0] * (n + 1)
    y1 = [0] * (n + 1)
    y2 = [0] * (n + 1)

    # Начальные условия
    x[0] = a
    y1[0] = y1_init
    y2[0] = y2_init

    # Основной цикл метода Эйлера
    for i in range(n):
        # Вычисляем производные
        dy1, dy2 = derivatives(x[i], y1[i], y2[i])

        # Вычисляем значения на следующем шаге
        y1[i + 1] = y1[i] + h * dy1
        y2[i + 1] = y2[i] + h * dy2
        x[i + 1] = x[i] + h

    return x, y1, y2

# Метод Эйлера-Коши
def euler_cauchy_method(a, b, h, y1_init, y2_init):
    # Количество шагов
    n = int((b - a) / h)

    # Массивы для хранения значений x, y1 и y2 на каждом шаге
    x = [0] * (n + 1)
    y1 = [0] * (n + 1)
    y2 = [0] * (n + 1)

    # Начальные условия
    x[0] = a
    y1[0] = y1_init
    y2[0] = y2_init

    # Основной цикл метода Эйлера-Коши
    for i in range(n):
        # Вычисляем производные в начальной точке
        dy1, dy2 = derivatives(x[i], y1[i], y2[i])

        # Предсказание (метод Эйлера)
        y1_pred = y1[i] + h * dy1
        y2_pred = y2[i] + h * dy2
        x_pred = x[i] + h

        # Вычисляем производные в предсказанной точке
        dy1_pred, dy2_pred = derivatives(x_pred, y1_pred, y2_pred)

        # Корректировка
        y1[i + 1] = y1[i] + (h / 2) * (dy1 + dy1_pred)
        y2[i + 1] = y2[i] + (h / 2) * (dy2 + dy2_pred)
        x[i + 1] = x_pred

    return x, y1, y2

# Метод Рунге-Кутта 4-го порядка
def runge_kutta_4(a, b, h, y1_init, y2_init):
    # Количество шагов
    n = int((b - a) / h)

    # Массивы для хранения значений x, y1 и y2 на каждом шаге
    x = [0] * (n + 1)
    y1 = [0] * (n + 1)
    y2 = [0] * (n + 1)

    # Начальные условия
    x[0] = a
    y1[0] = y1_init
    y2[0] = y2_init

    # Основной цикл метода Рунге-Кутта
    for i in range(n):
        k1_y1, k1_y2 = derivatives(x[i], y1[i], y2[i])
        k2_y1, k2_y2 = derivatives(x[i] + h / 2, y1[i] + h / 2 * k1_y1, y2[i] + h / 2 * k1_y2)
        k3_y1, k3_y2 = derivatives(x[i] + h / 2, y1[i] + h / 2 * k2_y1, y2[i] + h / 2 * k2_y2)
        k4_y1, k4_y2 = derivatives(x[i] + h, y1[i] + h * k3_y1, y2[i] + h * k3_y2)

        # Обновляем значения y1 и y2
        y1[i + 1] = y1[i] + h / 6 * (k1_y1 + 2 * k2_y1 + 2 * k3_y1 + k4_y1)
        y2[i + 1] = y2[i] + h / 6 * (k1_y2 + 2 * k2_y2 + 2 * k3_y2 + k4_y2)
        x[i + 1] = x[i] + h

    return x, y1, y2

# Основная программа
def main():
    a = 0.0       # начальная точка
    b = 4.0       # конечная точка
    h = 0.1       # шаг
    y1_init = 0.7 # начальное значение y1
    y2_init = -0.5 # начальное значение y2

    # Метод Эйлера
    x, y1, y2 = euler_method(a, b, h, y1_init, y2_init)
    print("Решение методом Эйлера")
    print("=" * 50)
    for xi, y1i, y2i in zip(x, y1, y2):
        print(f"x={xi:4.1f}\ty1={y1i:10.5f}\ty2={y2i:10.5f}")
    print("=" * 50)

    # Метод Эйлера-Коши
    print("Метод Эйлера-Коши")
    print("=" * 50)
    x, y1, y2 = euler_cauchy_method(a, b, h, y1_init, y2_init)
    for xi, y1i, y2i in zip(x, y1, y2):
        print(f"x={xi:4.1f}\ty1={y1i:10.5f}\ty2={y2i:10.5f}")
    print("=" * 50)

    # Метод Рунге-Кутта
    print("Метод Рунге-Кутта")
    print("=" * 50)
    x, y1, y2 = runge_kutta_4(a, b, h, y1_init, y2_init)
    for xi, y1i, y2i in zip(x, y1, y2):
        print(f"x={xi:4.1f}\ty1={y1i:10.5f}\ty2={y2i:10.5f}")
    print("=" * 50)

if __name__ == "__main__":
    main()
