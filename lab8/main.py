from Euler import euler_method
from Euler_cauchy import euler_cauchy_method
from Runge_kutt import runge_kutt
def print_results(x, y1, y2):
    print("=" * 50)
    for xi, y1i, y2i in zip(x, y1, y2):
        print(f"x={xi:4.1f}\ty1={y1i:10.5f}\ty2={y2i:10.5f}")
    print("=" * 50)

def main():
    a = 0.0
    b = 5.0
    h = 0.01
    y1_init = 1.0
    y2_init = 0.0

    while True:
        print("Выберите метод решения:")
        print("1. Метод Эйлера")
        print("2. Метод Эйлера-Коши")
        print("3. Метод Рунге-Кутта")
        print("0. Выход")
        choice = input("Ваш выбор: ")

        if choice == "1":
            print("Метод Эйлера")
            x, y1, y2 = euler_method(a, b, h, y1_init, y2_init)
            print_results(x, y1, y2)

        elif choice == "2":
            print("Метод Эйлера-Коши")
            x, y1, y2 = euler_cauchy_method(a, b, h, y1_init, y2_init)
            print_results(x, y1, y2)

        elif choice == "3":
            print("Метод Рунге-Кутта")
            x, y1, y2 = runge_kutt(a, b, h, y1_init, y2_init)
            print_results(x, y1, y2)

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
