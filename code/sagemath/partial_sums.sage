# Partial sums and convergence analysis
#
# Displays partial sums of the d_C series to illustrate convergence,
# and verifies the scaling property d_C(alpha*f, alpha*g) = (1/alpha)*d_C(f,g).
#
# Reference: Examples 3.3, 3.4, 5.5 of the paper.

var('n')

def dc_partial_sums(expr, start, num_terms=10):
    """Display partial sums of a d_C series."""
    cumul = 0
    for k in range(start, start + num_terms):
        term_val = numerical_approx(expr.subs(n=k))
        cumul += term_val
        print(f"  S_{k:2d} = {float(cumul):.8f}"
              f"  (term = {float(term_val):.8f})")
    total = numerical_approx(
        sum(expr, n, start, +Infinity))
    print(f"  S_inf = {float(total):.10f}")
    return total

# d_C(n^2, n): each term is 2^(-n)*(n-1)/n^2
print("=== d_C(n^2, n): partial sums ===")
dc_partial_sums(2^(-n) * (n-1)/n^2, start=2, num_terms=8)

# d_C(2n, n): each term is 2^(-n)/(2n)
print("\n=== d_C(2n, n): partial sums ===")
dc_partial_sums(2^(-n) / (2*n), start=1, num_terms=8)

# d_C(n+1, n): each term is 2^(-n)/(n(n+1))
print("\n=== d_C(n+1, n): partial sums ===")
dc_partial_sums(2^(-n) / (n*(n+1)), start=1, num_terms=8)

# Verify scaling property: d_C(alpha*f, alpha*g) = (1/alpha)*d_C(f,g)
alpha = 3
s_orig  = sum(2^(-n) * (n-1)/n^2, n, 2, +Infinity)
s_scale = sum(2^(-n) * (1/(alpha*n) - 1/(alpha*n^2)),
              n, 2, +Infinity)
print(f"\nScaling check (alpha={alpha}):")
print(f"  d_C(n^2, n)        = {float(numerical_approx(s_orig)):.8f}")
print(f"  d_C(3n^2, 3n)      = {float(numerical_approx(s_scale)):.8f}")
print(f"  (1/3)*d_C(n^2, n)  = {float(numerical_approx(s_orig/3)):.8f}")
