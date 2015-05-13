import erf
import report

def main():
    f = erf.Erf()
    report.taylor(0, 2, 10)
    report.lagrange(0, 2)
    report.derivative(0, 2)
    report.integral(0, 2)
    report.inverse(0, 0.95)


if __name__ == '__main__':
    main()
