import math
from array import array


class Erf:
    def taylor(self, x, eps=1e-6):
        a = x
        erf = x
        q = self.quotient(x, 0)
        n = 0
        while abs(a) > eps:
            a *= q
            erf += a
            n += 1
            q = self.quotient(x, n)
        return (2 / math.sqrt(math.pi)) * erf

    def arr_taylor(self, x, eps=1e-6):
        erf = []
        for i in range(0, len(x)):
            erf.append(self.taylor(x[i], eps))
        return erf

    def lagrange(self, nodes, values, x):
        Ln = 0
        for i in range(0, len(nodes)):
            F = 1
            for j in range(0, len(nodes)):
                if i != j:
                    F *= (x - nodes[j]) / (nodes[i] - nodes[j])
            Ln += values[i] * F
        return Ln

    def quotient(self, x, n):
        return (-x * x * (2 * n + 1)) / ((n + 1) * (2 * n + 3))

def create_nodes(a, b, n):
    nodes = []
    h = (b - a) / (n)
    for i in range(n + 1):
        nodes.append(a + i * h)
    return nodes

def main():
    f = Erf()
    nodes = create_nodes(0, 2, 10)
    values = f.arr_taylor(nodes)
    print(f.arr_taylor(nodes))

if __name__ == '__main__':
    main()
