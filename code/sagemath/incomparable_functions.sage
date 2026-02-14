# Incomparable functions: both directions positive
#
# Computes d_C in both directions for f(n) = n + (-1)^{n+1} and g(n) = n,
# demonstrating that neither f <= g nor g <= f pointwise.
#
# Reference: Example 3.7 of the paper.

var('n')

# f(n) = n + (-1)^(n+1),  g(n) = n
# d_C(f, g): only odd-index terms contribute
s_fg = sum(2^(-n) / (n * (n + 1)), n, 1, +Infinity,
           algorithm='mathematica_free')  # odd n only
# Manual computation via separate odd/even sums:
d_fg = sum(2^(-(2*n-1)) / ((2*n-1) * (2*n)),
           n, 1, +Infinity)
d_gf = sum(2^(-(2*n)) / ((2*n) * (2*n - 1)),
           n, 1, +Infinity)

print("d_C(f, g) ~", numerical_approx(d_fg, digits=8))
print("d_C(g, f) ~", numerical_approx(d_gf, digits=8))
print("d_C^s     ~", numerical_approx(max(d_fg, d_gf), digits=8))
# Output: d_C(f,g) ~ 0.26162407
#         d_C(g,f) ~ 0.13081204
#         d_C^s    ~ 0.26162407
