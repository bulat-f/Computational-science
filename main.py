import erf

def create_nodes(a, b, n):
    nodes = []
    h = (b - a) / (n)
    for i in range(n + 1):
        nodes.append(a + i * h)
    return nodes

def method_for_array(arr, method):
    result = []
    for i in range(0, len(arr)):
        result.append(method(arr[i]))
    return result

def main():
    f = erf.Erf()
    nodes = create_nodes(0, 2, 10)
    values = method_for_array(nodes, f.taylor)
    print(f.lagrange(nodes, values, 0.25))
    print(f.taylor(0.25))

if __name__ == '__main__':
    main()
