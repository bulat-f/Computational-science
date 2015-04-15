import math
from array import array
from integral import integral


class Erf:
    def __init__(self):
        self.derivative = lambda x: 2 / math.sqrt(math.pi) * math.exp(-x**2)

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

    def lagrange(self, nodes, values, x):
        Ln = 0
        for i in range(0, len(nodes)):
            F = 1
            for j in range(0, len(nodes)):
                if i != j:
                    F *= (x - nodes[j]) / (nodes[i] - nodes[j])
            Ln += values[i] * F
        return Ln

    def lagrange_for_derivative(self, nodes, values, x):
        Ln = 0
        n = len(nodes)
        xk_xi = 1
        lk = 0

        x_xi = 1
        for i in range(0, n):
            x_xi *= x - nodes[i]

        for k in range(0, n):
            for i in range(0, n):
                if i != k:
                    xk_xi *= nodes[k] - nodes[i]
            for j in range(0, n):
                if j != k:
                    lk += x_xi / ((x - nodes[k]) * (x - nodes[j]) * xk_xi)
            Ln += values[k] * lk
            lk = 0
            xk_xi = 1

        return Ln

    # methods: gauss, simpson, left_rectangle, center_rectangle, trapezoidal
    def integral(self, x, method = 'left_rectangle', eps = 1e-4):
        prev, current = integral(self.derivative, 0, x, 1, method), integral(self.derivative, 0, x, 2, method)
        tmp = current
        N = 2
        while abs(prev - current) > eps:
            N *= 2
            current = integral(self.derivative, 0, x, N, method)
            prev = tmp
            tmp = current
        return current


    # helper method for calc one node, after "overload" for scalar and list

    def quotient(self, x, n):
        return (-x * x * (2 * n + 1)) / ((n + 1) * (2 * n + 3))

if __name__ == '__main__':
    main()
