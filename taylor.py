import math


class erf:
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

    def quotient(self, x, n):
        return (-x * x * (2 * n + 1)) / ((n + 1) * (2 * n + 3))


def main():
    f = erf()
    print(f.taylor(0.8))

if __name__ == '__main__':
    main()
