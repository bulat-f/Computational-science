import math

def integral(func, a, b, N, method_name):
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(method_name)
    sum = 0
    h = (b - a) / N
    for i in range(0, N):
        sum += method(func, a + i*h, a + (i + 1)*h)
    return sum

def left_rectangle(func, a, b):
    return func(a) * (b - a)

def center_rectangle(func, a, b):
    return func((a + b)/2) * (b - a)

def gauss(func, a, b):
    return 0.5 * (func((a + b)/2 - (b - a)/(2 * math.sqrt(3))) + func((a + b)/2 - (b - a)/(2 * math.sqrt(3)))) * (b - a)

def simpson(func, a, b):
    return (b - a) * (func(a) + 4 * func((a + b) / 2) + func(b)) / 6

def trapezoidal(func, a, b):
    print('trapezoidal')
    return 0.5 * (func(a) + func(b)) * (b - a)

