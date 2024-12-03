import numpy as np

class CubicSpline:
    def __init__(self, x, y):
        self.x = np.array(x)
        self.y = np.array(y)
        self.n = len(x) - 1
        self.a = np.array(y[:-1])
        self.b, self.c, self.d = self._build_spline()
    
    def _build_spline(self):
        h = np.diff(self.x)
        alpha = [0] + [3 * (self.y[i + 1] - self.y[i]) / h[i] - 3 * (self.y[i] - self.y[i - 1]) / h[i - 1] for i in range(1, self.n)]

        l = np.zeros(self.n + 1)
        mu = np.zeros(self.n + 1)
        z = np.zeros(self.n + 1)
        l[0] = 1

        for i in range(1, self.n):
            l[i] = 2 * (self.x[i + 1] - self.x[i - 1]) - h[i - 1] * mu[i - 1]
            mu[i] = h[i] / l[i]
            z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]
        
        l[self.n] = 1

        c = np.zeros(self.n + 1)
        b = np.zeros(self.n)
        d = np.zeros(self.n)

        for j in range(self.n - 1, -1, -1):
            c[j] = z[j] - mu[j] * c[j + 1]
            b[j] = (self.y[j + 1] - self.y[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
            d[j] = (c[j + 1] - c[j]) / (3 * h[j])

        return b, c[:-1], d
    
    def _find_segment(self, x0):
        for i in range(self.n):
            if self.x[i] <= x0 <= self.x[i + 1]:
                return i
        raise ValueError("x0 is outside the interpolation range.")
    
    def first_derivative(self, x0):
        i = self._find_segment(x0)
        dx = x0 - self.x[i]
        return self.b[i] + 2 * self.c[i] * dx + 3 * self.d[i] * dx**2
    
    def second_derivative(self, x0):
        i = self._find_segment(x0)
        dx = x0 - self.x[i]
        return 2 * self.c[i] + 6 * self.d[i] * dx


if __name__ == "__main__":
    a = float(input("Введите границу a: "))
    b = float(input("Введите границу b: "))
    n = int(input("Введите количество точек n: "))

    if n < 2:
        print("Количество точек должно быть не менее 2")
        exit()

    x0 = float(input("Введите точку для вычисления производных (x0): "))
    
    if not (a <= x0 <= b):
        print("x0 должна быть внутри интервала [a, b]")
        exit()

    x = np.linspace(a, b, n)
    y = np.sin(x)*np.exp(-1*x*x)  # задание функции

    spline = CubicSpline(x, y)

    first = spline.first_derivative(x0)
    second = spline.second_derivative(x0)

    print(f"Первая производная в точке x0 = {x0:.2f}: {first:.3f}")
    print(f"Вторая производная в точке x0 = {x0:.2f}: {second:.3f}")