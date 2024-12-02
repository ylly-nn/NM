import numpy as np

def seidel(a: np.ndarray, b: np.ndarray):
    max_iterations: int = 1000
    eps=0.01
    n = len(b)
    x0 = np.zeros_like(b)  # Начальное приближение
    x = np.zeros_like(b)
    
    for step in range(max_iterations):
        for i in range(n):
            # Считаем новое значение x[i]
            x[i] = b[i] / a[i, i]
            for j in range(i):
                x[i] -= a[i, j] * x[j] / a[i, i]
            for j in range(i + 1, n):
                x[i] -= a[i, j] * x0[j] / a[i, i]

        # Вычисляем максимальное отклонение
        e = np.max(np.abs(x - x0))
        
        # Обновляем x0 для следующей итерации
        x0 = x.copy()
        
        # Проверка условия остановки
        if e <= eps:
            break

    return x0, step

