import math

def derivatives(x, y1, y2):
    e=math.e
    dy1 = e**(y1*y2)
    dy2 = x*y1*y2
    return dy1, dy2

def euler_cauchy_method(a, b, h, y1_init, y2_init):
    n = int((b - a) / h)
    x = [0] * (n + 1)
    y1 = [0] * (n + 1)
    y2 = [0] * (n + 1)

    x[0] = a
    y1[0] = y1_init
    y2[0] = y2_init

    for i in range(n):
        dy1, dy2 = derivatives(x[i], y1[i], y2[i])
        y1_pred = y1[i] + h * dy1
        y2_pred = y2[i] + h * dy2
        x_pred = x[i] + h

        dy1_pred, dy2_pred = derivatives(x_pred, y1_pred, y2_pred)
        y1[i + 1] = y1[i] + (h / 2) * (dy1 + dy1_pred)
        y2[i + 1] = y2[i] + (h / 2) * (dy2 + dy2_pred)
        x[i + 1] = x_pred

    return x, y1, y2
