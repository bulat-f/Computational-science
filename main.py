import erf
import compare

def main():
    f = erf.Erf()
    print(compare.chebyshev_max_error(0, 2, f.lagrange, f.taylor, 10))
    print(compare.equidistant_max_error(0, 2, f.lagrange, f.taylor, 10))

if __name__ == '__main__':
    main()
