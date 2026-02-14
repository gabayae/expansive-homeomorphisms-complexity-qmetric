# Separation iterates and hierarchy distances
#
# Computes the separation iterate k_min for various function pairs,
# verifies the hierarchy distance, and checks stable set membership.
#
# Reference: Examples 5.14, 5.15, 6.6, 8.3 of the paper.

var('n')

# --- Separation iterate: d_C(n^2, n), alpha=2, delta=0.5 --
d_quad = sum(2^(-n) * (n - 1) / n^2, n, 2, +Infinity)
delta = 0.5
alpha = 2
k_min = ceil(log(delta / d_quad) / log(alpha))
print("=== Separation iterate (n^2 vs n) ===")
print(f"d = {float(numerical_approx(d_quad)):.6f}")
print(f"k_min = ceil(log_{alpha}({delta}/d))"
      f" = ceil({float(log(delta/d_quad)/log(alpha)):.4f})"
      f" = {k_min}")
print(f"Check: 2^{k_min} * d ="
      f" {float(numerical_approx(2^k_min * d_quad)):.6f}"
      f" > {delta}")
print(f"       2^{k_min-1} * d ="
      f" {float(numerical_approx(2^(k_min-1) * d_quad)):.6f}"
      f" < {delta}")

# --- Slow separation: d_C(n+1, n), alpha=1.01, delta=0.5 --
d_shift = sum(2^(-n) / (n * (n + 1)), n, 1, +Infinity)
alpha_slow = 1.01
k_slow = ceil(log(delta / d_shift) / log(alpha_slow))
print(f"\n=== Slow separation (n+1 vs n) ===")
print(f"d = {float(numerical_approx(d_shift)):.6f}")
print(f"k_min = ceil(log_{{1.01}}({delta}/d))"
      f" = {k_slow}")

# --- Hierarchy: d_C^s(n, n*log^2(n+1)) --------------------
# d_C(f, g) where f(n)=n, g(n)=n*log^2(n+1)
# Since g(1) = log^2(2) ~ 0.48 < 1 = f(1), both directions > 0
d_fg = sum(2^(-n) * max_symbolic(0,
    1/(n*log(n+1)^2) - 1/n), n, 1, 100)
d_gf = sum(2^(-n) * max_symbolic(0,
    1/n - 1/(n*log(n+1)^2)), n, 1, 100)
print(f"\n=== Hierarchy: n vs n*log^2(n+1) ===")
print(f"d_C(f, g) ~ {float(numerical_approx(d_fg)):.6f}")
print(f"d_C(g, f) ~ {float(numerical_approx(d_gf)):.6f}")
print(f"d_C^s     ~ {float(max(numerical_approx(d_fg), numerical_approx(d_gf))):.6f}")

# --- Stable set: d_C(n, sqrt(n)) --------------------------
d_sqrt = sum(2^(-n) * (1/sqrt(n) - 1/n), n, 2, +Infinity)
print(f"\n=== Stable set: d_C(n, sqrt(n)) ===")
print(f"d_C(n, sqrt(n)) ~ "
      f"{float(numerical_approx(d_sqrt)):.6f}")
print(f"  > 0.1 (delta)?  {bool(numerical_approx(d_sqrt) > 0.1)}")
print(f"  > 0.05?         {bool(numerical_approx(d_sqrt) > 0.05)}")
print(f"  < 0.2?          {bool(numerical_approx(d_sqrt) < 0.2)}")
