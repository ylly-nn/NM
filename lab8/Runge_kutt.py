import math

def derivatives(x, y1, y2):
    e=math.e
    dy1 = e**(y1*y2)
    dy2 = x*y1*y2
    return dy1, dy2

def runge_kutt(a, b, h, y1_init, y2_init):
    n = int((b - a) / h)
    x = [0] * (n + 1)
    y1 = [0] * (n + 1)
    y2 = [0] * (n + 1)

    x[0] = a
    y1[0] = y1_init
    y2[0] = y2_init

    for i in range(n):
        k1_y1, k1_y2 = derivatives(x[i], y1[i], y2[i])
        k2_y1, k2_y2 = derivatives(x[i] + h / 2, y1[i] + h / 2 * k1_y1, y2[i] + h / 2 * k1_y2)
        k3_y1, k3_y2 = derivatives(x[i] + h / 2, y1[i] + h / 2 * k2_y1, y2[i] + h / 2 * k2_y2)
        k4_y1, k4_y2 = derivatives(x[i] + h, y1[i] + h * k3_y1, y2[i] + h * k3_y2)

        y1[i + 1] = y1[i] + h / 6 * (k1_y1 + 2 * k2_y1 + 2 * k3_y1 + k4_y1)
        y2[i + 1] = y2[i] + h / 6 * (k1_y2 + 2 * k2_y2 + 2 * k3_y2 + k4_y2)
        x[i + 1] = x[i] + h

    return x, y1, y2
