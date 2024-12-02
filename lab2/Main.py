import Seidel
import SeidelEx
import Jacoby
import numpy as np
import copy



# Пример использования
A = np.array([ [4.3000, 0.0217, 0.0270, 0.0324],
[0.0100, 3.4000, 0.0207, 0.0260],
[0.0037, 0.0090, 2.5000, 0.0197],
[-0.0027, 0.0027, 0.0080, 1.6000]], dtype=float)
B = np.array([2.6632, 2.7779, 2.5330, 1.9285], dtype=float)
print("1 - Метод Якоби")
print("2 - Метод Зейделя")
print("3 - Метод врехней релаксиции")
key=int(input("Введите число >>> "))
while key !=0:
    if key==1:
        vector=copy.deepcopy(B)
        X, step =Jacoby.Jacoby(A,vector)
        print ("Oригинальная матрица:")
        for row in A:
            print (row)
        print("")
        print ("Оригинальный вектор:")
        for row in B:
            print (row)
        print("")
        print ("Ответ:")
        for row in X:
            print (row)
        print("")
        print("Количество итераций:")
        print(step)
        input("Нажмите Enter для продолжения...")
        
    elif key==2:
        vector=copy.deepcopy(B)
        X, step =Seidel.seidel(A,vector)
        print ("Oригинальная матрица:")
        for row in A:
            print (row)
        print("")
        print ("Оригинальный вектор:")
        for row in B:
            print (row)
        print("")
        print ("Ответ:")
        for row in X:
            print (row)
        print("")
        print("Количество итераций:")
        print(step)
        input("Нажмите Enter для продолжения...")
    elif key==3:
        vector=copy.deepcopy(B)
        X, step =SeidelEx.SeidelEx(A,vector)
        print ("Oригинальная матрица:")
        for row in A:
            print (row)
        print("")
        print ("Оригинальный вектор:")
        for row in B:
            print (row)
        print("")
        print ("Ответ:")
        for row in X:
            print (row)
        print("")
        print("Количество итераций:")
        print(step)
        input("Нажмите Enter для продолжения...")
    print("1 - Метод Якоби")
    print("2 - Метод Зейделя")
    print("3 - Метод врехней релаксиции")
    key=int(input("Введите число >>> "))