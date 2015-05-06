import erf
import report

def main():
    f = erf.Erf()
    report.taylor(0, 2, 10)
    print(f.taylor(1.25))
    print(f.inverse(0.922900105827684))
    # print(compare.chebyshev_max_error(0, 2, f.lagrange, f.taylor, 10))
    # print(compare.equidistant_max_error(0, 2, f.lagrange, f.taylor, 10))

if __name__ == '__main__':
    main()
