import math

def equidistant_nodes(a, b, n):
    nodes = []
    h = (b - a) / n
    for i in range(n+1):
        nodes.append(a + i * h)
    return nodes

def chebyshev_nodes(a, b, n):
    nodes = []
    for i in range(0, n):
        i += 1
        xi = (b - a) / 2 * math.cos((2 * i - 1) / (2 * n) * math.pi) + (b + a) / 2
        nodes.append(xi)
    return nodes

def method_for_array(arr, method):
    result = []
    for i in range(0, len(arr)):
        result.append(method(arr[i]))
    return result

if __name__ == '__main__':
    main()
