# Exact complexity distances via SageMath
#
# Evaluates the infinite series defining d_C(f,g) symbolically,
# producing closed-form expressions and high-precision numerical values.
#
# Reference: Examples 3.3, 3.4, 3.7, 4.4 of the paper.

var('n')

# --- d_C(n^2, n) -------------------------------------------
# sum_{n=2}^{inf} 2^(-n) * (n-1)/n^2
s1 = sum(2^(-n) * (n - 1) / n^2, n, 2, +Infinity)
print("d_C(n^2, n)  =", s1)
print("             =", s1.simplify_full())
print("             ~", numerical_approx(s1, digits=10))
# Output: -1/2*dilog(1/2) + 1/2*log(2)
#         = ln(2) - Li_2(1/2) ~ 0.1109066541

# --- d_C(2n, n) --------------------------------------------
# sum_{n=1}^{inf} 2^(-n) * 1/(2n)
s2 = sum(2^(-n) / (2*n), n, 1, +Infinity)
print("\nd_C(2n, n)   =", s2.simplify_full())
print("             ~", numerical_approx(s2, digits=10))
# Output: 1/2*log(2) ~ 0.3465735903

# --- d_C(n+1, n) -------------------------------------------
# sum_{n=1}^{inf} 2^(-n) * 1/(n*(n+1))
s3 = sum(2^(-n) / (n * (n + 1)), n, 1, +Infinity)
print("\nd_C(n+1, n)  =", s3.simplify_full())
print("             ~", numerical_approx(s3, digits=10))
# Output: ~ 0.3068528194

# --- d_C(n, ln(n+1)) ---------------------------------------
# sum_{n=1}^{inf} 2^(-n) * max(0, 1/ln(n+1) - 1/n)
# (all terms positive since ln(n+1) < n for n >= 1)
s4 = sum(2^(-n) * (1/log(n + 1) - 1/n), n, 1, +Infinity)
print("\nd_C(n, ln(n+1)) ~", numerical_approx(s4, digits=10))
# Output: ~ 0.4174050156

# --- d_C(n^3, n^2) -----------------------------------------
# sum_{n=2}^{inf} 2^(-n) * (n-1)/n^3
s5 = sum(2^(-n) * (n - 1) / n^3, n, 2, +Infinity)
print("\nd_C(n^3, n^2) =", s5.simplify_full())
print("              ~", numerical_approx(s5, digits=10))
# Output: ~ 0.04502733

# --- d_C(n, sqrt(n)) ---------------------------------------
# sum_{n=2}^{inf} 2^(-n) * (1/sqrt(n) - 1/n)
s6 = sum(2^(-n) * (1/sqrt(n) - 1/n), n, 2, +Infinity)
print("\nd_C(n, sqrt(n)) ~", numerical_approx(s6, digits=10))
# Output: ~ 0.1129795387
