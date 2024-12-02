import copy
import numpy as np



def Cholesky():
    size=3

    matrixOriginal=np.array([
        [1.54, 1.70, 1.62],
        [3.69, 3.73, 3.59],
        [2.45, 2.43, 2.25]
    ])

    matrix=copy.deepcopy(matrixOriginal)
    vectorOriginal=np.array([
        -1.97,
        -3.74,
        -2.26
    ])


    vector=copy.deepcopy(vectorOriginal)

    X=np.array([0.0, 0.0, 0.0])

    Y=np.array([0.0, 0.0, 0.0])

    chek=[
        [0.0],
        [0.0],
        [0.0]
    ]
    determinant = np.linalg.det(matrix)
    if determinant>0:

        L=np.zeros_like(matrix)


        matrixTransposed=matrix.T

        print("Оригинальная матрица: ")
        print(matrix)

        print("Оригинальный вектор")
        for row in vector:
            print(row)

        
        #умножение матриц
        matrix=np.dot(matrixTransposed,matrix)
        vector=np.dot(matrixTransposed, vector)



        for i in range(size):
            for j in range(i + 1):
                sum_k = sum(L[i][k] * L[j][k] for k in range(j))
                    
                if i == j:  #Диагональ 
                    L[i][j] = np.sqrt(matrix[i][i] - sum_k)
                else:  #Остальное
                    L[i][j] = (matrix[i][j] - sum_k) / L[j][j]
            
        

        
        #Ly=b; поиск Y
        Y[0]=vector[0]/L[0][0]
        for n in range(1,size):
            for i in range(n):
                sum_LY = 0
                for i in range(n):
                    sum_LY += L[n][i] * Y[i]
                Y[n] = (vector[n] - sum_LY) / L[n][n]

        L_Transpose=L.T
        X[size-1]=Y[size-1]/L_Transpose[size-1][size-1]
        for n in range(size-2, -1,-1):
            for i in range(size-1, n,-1):
                X[n]=X[n]+L_Transpose[n][i]*X[i]
            X[n]=(Y[n]-X[n])/L_Transpose[n][n]
        print("X:")
        for row in X:
            print(round(row,3))

        for i in range(size):
            for j in range(size):
                chek[i][0]+=matrixOriginal[i][j]*X[j]
            chek[i][0]=round(chek[i][0],3)
            chek[i].append(vectorOriginal[i])




                
        print("Проверка")
        for row in chek:
            print(row)




                

    else:
        print("Матрица не положительно определённая")    



