import copy
import numpy as np

def Gauss():
    size=3
    matrixOriginal =[
        [1.54, 1.70, 1.62],
        [3.69, 3.73, 3.59],
        [2.45, 2.43, 2.25]
    ]

    vector=[
        -1.97,
        -3.74,
        -2.26
    ]

    x=[
        0,
        0,
        0
    ]


    Gvector=copy.deepcopy(vector)
    Gmatrix=copy.deepcopy(matrixOriginal)
    for i in range(size):
        Gmatrix[i].append(vector[i])




    for n in range(1,size): 
        for i in range(n,size):
            for j in range(size,n-2,-1):
                Gmatrix[n-1][j]=Gmatrix[n-1][j]/Gmatrix[n-1][n-1] 
                Gvector[n-1]=vector[n-1]/Gmatrix[n-1][n-1] 
                Gmatrix[i][j]=Gmatrix[n-1][j]*-1*Gmatrix[i][n-1]+Gmatrix[i][j]

                

    for i in range(size):
        Gvector[i]=Gmatrix[i][size]

    x[size-1]=Gvector[size-1]/Gmatrix[size-1][size-1]
    for n in range(size-2, -1,-1):
        for i in range(size-1, n,-1):
            x[n]=x[n]+Gmatrix[n][i]*x[i]
        x[n]=(Gvector[n]-x[n])/Gmatrix[n][n]
        
    
        
    for i in  range(0,size):
        x[i]=round(x[i],3)   

    print ("Оригинальная матрица:")
    for row in matrixOriginal:
        print(row)

    print("")
    
    print("Вектор:")
    for row in vector:
        print(row)

    print("")    

    print("x:")
    for row in x:
        print(row)

    print("")

    chek=[
        [0],
        [0],
        [0]
    ]
    for i in range(size):
        chek[i].append(vector[i])
    for i in range(size):
        for j in range(size):
            chek[i][0]+=matrixOriginal[i][j]*x[j]
        chek[i][0]=round(chek[i][0],3)




    print("Проверка:")
    for row in chek:
        print(row)
