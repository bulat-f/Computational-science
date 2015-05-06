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
    write_tabs(values, 6, out)
    out.write('\\end{tabular}')
