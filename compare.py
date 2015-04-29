import nodes

def chebyshev_errors(a, b, approximate_func, true_func, n):
    interpolation_nodes = nodes.chebyshev_nodes(a, b, n + 1)
    interpolation_values = nodes.method_for_array(interpolation_nodes, true_func)
    points = nodes.equidistant_nodes(a, b, n * 2)
    approximate = lambda x : approximate_func(interpolation_nodes, interpolation_values, x)
    approx_values = nodes.method_for_array(points, approximate)
    true_values = nodes.method_for_array(points, true_func)
    approx_error = []
    for i in range(2 * n):
        approx_error.append(abs(approx_values[i] - true_values[i]))
    return approx_error

def equidistant_errors(a, b, approximate_func, true_func, n):
    interpolation_nodes = nodes.equidistant_nodes(a, b, n)
    interpolation_values = nodes.method_for_array(interpolation_nodes, true_func)
    points = nodes.equidistant_nodes(a, b, n * 2)
    approximate = lambda x : approximate_func(interpolation_nodes, interpolation_values, x)
    approx_values = nodes.method_for_array(points, approximate)
    true_values = nodes.method_for_array(points, true_func)
    approx_error = []
    for i in range(2 * n):
        approx_error.append(abs(approx_values[i] - true_values[i]))
    return approx_error

def chebyshev_max_error(a, b, approximate_func, true_func, n):
    return max(chebyshev_errors(a, b, approximate_func, true_func, n))

def equidistant_max_error(a, b, approximate_func, true_func, n):
    return max(equidistant_errors(a, b, approximate_func, true_func, n))

if __name__ == '__main__':
    main()
