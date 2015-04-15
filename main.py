import erf

def create_nodes(a, b, n):
    nodes = []
    h = (b - a) / (n)
    for i in range(n + 1):
        nodes.append(a + i * h)
    return nodes

def main():
    f = erf.Erf()
    # nodes = create_nodes(0, 2, 10)
    # values = f.taylor(nodes)
    print(f.integral(0.8, 'simpson'))
    print(f.taylor(0.8))

if __name__ == '__main__':
    main()
