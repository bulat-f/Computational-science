import erf
import compare
import nodes

# helper methods
def write_tabs(a, digits, out):
    counter = 0
    rounding = '%.' + str(digits) + 'f'
    n = len(a)
    for x in a:
        counter += 1
        out.write('$' + rounding % x + '$' + ('&' if counter < n else '\\\\\n'))
    return

def tex_siquence(arr):
    return str(arr[0]) + ', ' + str(arr[1]) + '\\dots' + str(arr[len(arr) - 1])

# formulagte report files
def taylor(a, b, n):
    out = open('./tex/taylor.tex', 'w')
    f = erf.Erf()
    out.write('Протабулируем $erf(x)$ на отрезке [' + str(a) + ', ' + str(b) + '] на ' + str(n) + ' узлах с точностью $10^{-6}$, основываясь на ряде Тейлора:\\\\\n')
    out.write('\\begin{tabular}{' + 'c'*(n+1) + '}\n')
    taylor_nodes = nodes.equidistant_nodes(a, b, n)
    values = nodes.method_for_array(taylor_nodes, f.taylor)
    out.write('\hline\n')
    write_tabs(taylor_nodes, 2, out)
    out.write('\hline\n')
    write_tabs(values, 6, out)
    out.write('\\end{tabular}')

def lagrange(a, b):
    out = open('./tex/lagrange.tex', 'w')
    f = erf.Erf()
    nodes_count = []
    chebyshev = []
    equidistant = []
    for i in range(8):
        nodes_count.append(8 + 2*i)
    for count in nodes_count:
        chebyshev.append(compare.chebyshev_max_error(a, b, f.lagrange, f.taylor, count))
        equidistant.append(compare.equidistant_max_error(a, b, f.lagrange, f.taylor, count))
    out.write('Протабулируем $L_n(x)$ на отрезке [' + str(a) + ', ' + str(b) + '], где $n =' + tex_siquence(nodes_count) + '$ и вычилим погрешность в равностоящих $2n$ узлах\\\\\n')
    out.write('\\begin{tabular}{' + 'r|' + 'c'*len(nodes_count) + '}\n')
    out.write('\hline\n')
    out.write('Кол-во узлов&')
    write_tabs(nodes_count, 0, out)
    out.write('\hline\n')

    out.write('равн. узлы&')
    write_tabs(equidistant, 8, out)
    out.write('Чеб. узлы&')
    write_tabs(chebyshev, 8, out)
    out.write('\\end{tabular}')

def lagrange_for_derivative(a, b):
    out = open('./tex/lagrange_for_derivative.tex', 'w')
    f = erf.Erf()
    nodes_count = []
    chebyshev = []
    equidistant = []
    for i in range(8):
        nodes_count.append(8 + 2*i)
    for count in nodes_count:
        chebyshev.append(compare.chebyshev_max_error(a, b, f.lagrange_for_derivative, f.derivative, count))
        equidistant.append(compare.equidistant_max_error(a, b, f.lagrange_for_derivative, f.derivative, count))
    out.write('Протабулируем $L’_n(x)$ на отрезке [' + str(a) + ', ' + str(b) + '], где $n =' + tex_siquence(nodes_count) + '$ и вычилим погрешность в равностоящих $2n$ узлах\\\\\n')
    out.write('\\begin{tabular}{' + 'r|' + 'c'*len(nodes_count) + '}\n')
    out.write('\hline\n')
    out.write('Кол-во узлов&')
    write_tabs(nodes_count, 0, out)
    out.write('\hline\n')

    out.write('равн. узлы&')
    write_tabs(equidistant, 8, out)
    out.write('Чеб. узлы&')
    write_tabs(chebyshev, 8, out)
    out.write('\\end{tabular}')
