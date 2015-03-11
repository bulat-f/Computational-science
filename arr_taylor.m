function erf_arr = arr_taylor(x, eps = 1e-6)
    for k = 1:length(x)
        erf_arr(k) = taylor(x(k), eps);
    end
end
