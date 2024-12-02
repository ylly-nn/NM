import Gauss
import Cholesky

print("1 - Метод Гаусса")
print("2 - Метод Холецкого")
print("0 - Выход")
key=int(input("Введите число >>> "))
while key !=0:
    if key==1:
        Gauss.Gauss()
        input("Нажмите Enter для продолжения...")
    elif key==2:
        Cholesky.Cholesky()
        input("Нажмите Enter для продолжения...")
    print("1 - Метод Гаусса")
    print("2 - Метод Холецкого")
    print("0 - Выход")
    key=int(input("Введите число >>> "))

