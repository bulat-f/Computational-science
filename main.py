import erf
import report

def main():
    f = erf.Erf()
    report.taylor(0, 2, 10)
    report.lagrange(0, 2)
    report.lagrange_for_derivative(0, 2)


if __name__ == '__main__':
    main()
