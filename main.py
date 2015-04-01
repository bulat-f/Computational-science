import erf

def create_nodes(a, b, n):
    nodes = []
    h = (b - a) / (n)
    for i in range(n + 1):
        nodes.append(a + i * h)
    return nodes

def main():
    f = erf.Erf()
    nodes = create_nodes(0, 2, 10)
    values = f.taylor(nodes)
    print(f.lagrange_for_derivative(nodes, values, 0.25))
    print(f.derivative(0.25))

if __name__ == '__main__':
    main()
