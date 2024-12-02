import numpy as np

def SeidelEx(a, b,w=1.0, eps=0.01):
    n=len(b)
    x0 = np.zeros(n)
    x = np.zeros(n)
    step = 0
    
    # Начальное приближение
    for i in range(n):
        x0[i] = b[i] / a[i, i]
    
    while True:
        step += 1
        # Вычисляем новое приближение
        for i in range(n):
            x[i] = w * b[i] / a[i, i] + (1 - w) * x0[i]
            for j in range(i):
                x[i] -= w * a[i, j] * x[j] / a[i, i]
            for j in range(i + 1, n):
                x[i] -= w * a[i, j] * x0[j] / a[i, i]
        
        # Оценка ошибки
        e = max(abs(x[i] - x0[i]) for i in range(n))
        
        # Обновляем x0 для следующей итерации
        x0 = np.copy(x)
        
        if e <= eps:
            break
    
    return x, step




