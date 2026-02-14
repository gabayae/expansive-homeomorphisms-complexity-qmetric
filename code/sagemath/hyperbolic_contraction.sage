# Hyperbolic contraction and backward expansion
#
# Verifies exponential contraction under forward iteration and
# exponential expansion under backward iteration of psi_alpha.
#
# Reference: Examples 7.7, 7.9, 7.10 of the paper.

var('n')

# --- Hyperbolic contraction: d_C(n^3, n^2) under psi_2 ---
# Base distance: d_C(n^3, n^2) = sum 2^(-n)*(n-1)/n^3
d0 = sum(2^(-n) * (n - 1) / n^3, n, 2, +Infinity)
print("=== Hyperbolic contraction (alpha=2) ===")
print(f"d_C(n^3, n^2) = {float(numerical_approx(d0)):.6f}")
for k in range(1, 5):
    dk = d0 / 2^k
    print(f"d_C(psi_2^{k}(n^3), psi_2^{k}(n^2))"
          f" = d0/{2^k} = {float(numerical_approx(dk)):.6f}")

# --- Backward expansion: d_C(n^2, n) under psi_3 ----------
d_base = sum(2^(-n) * (n - 1) / n^2, n, 2, +Infinity)
print("\n=== Backward expansion (alpha=3) ===")
for k in range(0, 5):
    dk = 3^k * d_base
    capped = min(float(numerical_approx(dk)), 1.0)
    print(f"d_C(psi_3^{{-{k}}}(n^2), psi_3^{{-{k}}}(n))"
          f" = {3^k}*d0 = {float(numerical_approx(dk)):.4f}"
          f"  (actual: {capped:.4f})")

# --- Numerical hyperbolicity: d_C(n^2, n) under psi_2 -----
print("\n=== Forward contraction (alpha=2) ===")
for k in range(0, 7):
    dk = d_base / 2^k
    print(f"  n={k}: d_C = d0/{2^k} = "
          f"{float(numerical_approx(dk)):.8f}")
