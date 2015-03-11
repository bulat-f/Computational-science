function erf = taylor(x, eps = 1.0e-6)
    erf = a = x;
    n = 1;
    do
        q = quotient(x, n);
        if abs(q) > eps
            a *= q;
            erf += a;
            n++;
        end
    until abs(q) < eps;
    erf *= 2 / sqrt(pi);
end

function q = quotient(x, n)
    q = (-(x^2) * (2*n + 1)) / ((n + 1) * (2*n + 3));
end
