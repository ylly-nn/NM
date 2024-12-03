import numpy as np

# Определение системы дифференциальных уравнений
def derivatives(x, y1, y2):
    dy1 = np.e ** (y1 * y2)
    dy2 = x * y1 * y2
    return dy1, dy2

def f1(x, y1, y2):
    return np.e**(y1*y2)

def f2(x, y1, y2):
    return x*y1*y2

# Метод Рунге-Кутта 4-го порядка
def runge_kutta4(a, b, h, y1_init, y2_init):
    n = int((b - a) / h)
    x = np.zeros(n + 1)
    y1 = np.zeros(n + 1)
    y2 = np.zeros(n + 1)

    x[0] = a
    y1[0] = y1_init
    y2[0] = y2_init

    for i in range(n):
        k1_y1, k1_y2 = derivatives(x[i], y1[i], y2[i])
        k2_y1, k2_y2 = derivatives(x[i] + h / 2, y1[i] + h / 2 * k1_y1, y2[i] + h / 2 * k1_y2)
        k3_y1, k3_y2 = derivatives(x[i] + h / 2, y1[i] + h / 2 * k2_y1, y2[i] + h / 2 * k2_y2)
        k4_y1, k4_y2 = derivatives(x[i] + h, y1[i] + h * k3_y1, y2[i] + h * k3_y2)

        y1[i + 1] = y1[i] + h / 6 * (k1_y1 + 2 * k2_y1 + 2 * k3_y1 + k4_y1)
        y2[i + 1] = y2[i] + h / 6 * (k1_y2 + 2 * k2_y2 + 2 * k3_y2 + k4_y2)
        x[i + 1] = x[i] + h

    return x, y1, y2

# Метод Адамса 4-го порядка
def adams4(a, b, h, y1_init, y2_init):
    n = int((b - a) / h)
    x = np.zeros(n + 1)
    y1 = np.zeros(n + 1)
    y2 = np.zeros(n + 1)

    # Используем метод Рунге-Кутта для первых 4-х шагов
    x[:4], y1[:4], y2[:4] = runge_kutta4(a, a + 3 * h, h, y1_init, y2_init)

    for i in range(3, n):
        y1[i + 1] = y1[i] + h / 24 * (
            55 * f1(x[i], y1[i], y2[i])
            - 59 * f1(x[i - 1], y1[i - 1], y2[i - 1])
            + 37 * f1(x[i - 2], y1[i - 2], y2[i - 2])
            - 9 * f1(x[i - 3], y1[i - 3], y2[i - 3])
        )
        y2[i + 1] = y2[i] + h / 24 * (
            55 * f2(x[i], y1[i], y2[i])
            - 59 * f2(x[i - 1], y1[i - 1], y2[i - 1])
            + 37 * f2(x[i - 2], y1[i - 2], y2[i - 2])
            - 9 * f2(x[i - 3], y1[i - 3], y2[i - 3])
        )
        x[i + 1] = x[i] + h

    return x, y1, y2

# Основная функция
def main():
    a = 0.0       # начальная точка
    b = 5.0       # конечная точка
    h = 0.1       # шаг
    y1_init = 1.0  # начальное значение y1
    y2_init = 0.0 # начальное значение y2

    # метод Адамса
    x, y1, y2 = adams4(a, b, h, y1_init, y2_init)

    print("Метод Адамса")
    for i in range(len(x)):
        print(f"x={x[i]:4.1f}\ty1={y1[i]:10.5f}\ty2={y2[i]:10.5f}")

if __name__ == "__main__":
    main()