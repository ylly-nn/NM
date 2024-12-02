import numpy as np

def Jacoby(a: np.ndarray, b: np.ndarray):
    n = a.shape[0]
    eps=0.01
    # Инициализация вектора предыдущего решения x0
    x0 = np.zeros(n)
    # Инициализация текущего вектора решения x
    x = np.zeros(n)
    
    # Счётчик шагов
    step = 0
    
    # Начальное предположение для x0
    for i in range(n):
        x0[i] = b[i] / a[i, i]

    while True:
        for i in range(n):
             # Вычисляем x[i] на основе предыдущих оценок
            x[i] = b[i] / a[i, i]
            for j in range(i):
                x[i] -= a[i, j] * x0[j] / a[i, i]
            for j in range(i + 1, n):
                x[i] -= a[i, j] * x0[j] / a[i, i]

         # Вычисляем ошибку
        e = np.max(np.abs(x - x0))
        
        # Обновляем предыдущее решение
        x0 = np.copy(x)
        step += 1
        
        # Завершаем цикл, если ошибка в пределах допустимого диапазона
        if e <= eps:
            break
    
    # Обновляем b с найденным решением
    b[:] = x0
    return b, step


  

 