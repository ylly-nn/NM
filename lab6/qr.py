import numpy as np

def qr_decomposition(a):
    # Используем копию матрицы для работы
    aa = np.array(a, dtype=float)
    n = aa.shape[0]
    
    # Максимальное число итераций и порог для сходимости
    max_iterations = 1000
    tolerance = 1e-10
    
    for iteration in range(max_iterations):
        # QR-разложение
        q, r = np.linalg.qr(aa)
        aa = r @ q  # Пересчет матрицы
        
        # Проверка сходимости
        off_diagonal_sum = np.sum(np.abs(aa) - np.abs(np.diag(np.diag(aa))))
        if off_diagonal_sum < tolerance:
            break
    
    # Собственные значения - диагональные элементы финальной матрицы
    eigenvalues = np.diag(aa)
    return eigenvalues

# Задаем матрицу для тестирования
A = [
    [2, 2, -2],
    [2, 5, -4],
    [2, -4, 5]
]

# Вызываем функцию и выводим результат
eigenvalues = qr_decomposition(A)
print("Собственные значения:", eigenvalues)
