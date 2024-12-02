import numpy as np

def matrix_determinant(matrix):
    """Вычисление определителя матрицы"""
    return np.linalg.det(matrix)

def characteristic_polynomial(matrix):
    """Метод Леверрье для нахождения характеристического многочлена"""
    n = matrix.shape[0]
    trace_powers = [np.trace(np.linalg.matrix_power(matrix, k)) for k in range(1, n+1)]
    coefficients = [1]
    
    for i in range(n):
        sum_terms = sum(coefficients[j] * trace_powers[i-j-1] for j in range(i))
        coefficients.append(-(trace_powers[i] + sum_terms) / (i + 1))
    
    return coefficients

def leverrier(matrix):
    """Метод Леверрье для нахождения собственных значений"""
    coefficients = characteristic_polynomial(matrix)
    roots = np.roots(coefficients)
    return roots

def fadeev(matrix):
    """Метод Фадеева для нахождения характеристического многочлена и собственных значений"""
    n = matrix.shape[0]
    p = np.zeros(n + 1)
    b = np.eye(n)
    
    for k in range(n):
        trace = np.trace(np.dot(matrix, b))
        p[k+1] = -trace / (k + 1)
        b = np.dot(matrix, b + p[k+1] * np.eye(n))
    
    p[0] = 1
    eigenvalues = np.roots(p)
    return eigenvalues

def krylov(matrix):
    """Метод Крылова для нахождения собственных значений"""
    n = matrix.shape[0]
    b = np.random.rand(n)
    krylov_matrix = np.zeros((n, n))
    
    for i in range(n):
        krylov_matrix[:, i] = b
        b = np.dot(matrix, b)
    
    try:
        _, eigenvalues = np.linalg.qr(krylov_matrix)
    except np.linalg.LinAlgError:
        raise ValueError("Невозможно построить Крыловскую матрицу.")
    
    return np.diag(eigenvalues)

def eigenvectors(matrix, eigenvalues):
    """Находим собственные вектора для заданных собственных значений"""
    vectors = []
    for eig in eigenvalues:
        identity = np.eye(matrix.shape[0])
        eig_matrix = matrix - eig * identity
        _, _, vh = np.linalg.svd(eig_matrix)
        vectors.append(vh[-1, :])
    return np.array(vectors).T

def main():
    matrix = np.array([
        [4, 1, -2],
        [1, 3, 1],
        [0, 1, 2]
    ])

    print("Метод Леверрье:")
    leverrier_values = leverrier(matrix)
    print("Собственные значения:", leverrier_values)
    print("Собственные вектора:\n", eigenvectors(matrix, leverrier_values))

    print("\nМетод Фадеева:")
    fadeev_values = fadeev(matrix)
    print("Собственные значения:", fadeev_values)
    print("Собственные вектора:\n", eigenvectors(matrix, fadeev_values))

    print("\nМетод Крылова:")
    krylov_values = krylov(matrix)
    print("Собственные значения:", krylov_values)
    print("Собственные вектора:\n", eigenvectors(matrix, krylov_values))

if __name__ == "__main__":
    main()
