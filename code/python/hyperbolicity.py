"""Verify exponential contraction along stable sets.

Checks that d_C(psi_alpha^n(f), psi_alpha^n(g)) = (1/alpha)^n * d_C(f,g)
by comparing actual and predicted distances.

Reference: Section 7 of the paper.
"""

from complexity_distance import complexity_quasi_metric


def verify_hyperbolicity(f, g, alpha, max_n=20, N=80):
    """Verify exponential contraction along stable set."""
    d0 = complexity_quasi_metric(f, g, N)
    print(f"d_C(f,g) = {d0:.6f}")
    lam = 1.0 / alpha
    for n in range(1, max_n + 1):
        s = alpha ** n
        fn = lambda m, s=s: s * f(m)
        gn = lambda m, s=s: s * g(m)
        dn = complexity_quasi_metric(fn, gn, N)
        predicted = lam**n * d0
        ratio = dn / predicted if predicted > 0 else float('inf')
        print(f"  n={n:2d}  actual={dn:.8f}  "
              f"predicted={predicted:.8f}  "
              f"ratio={ratio:.6f}")


if __name__ == "__main__":
    # Run verification
    verify_hyperbolicity(
        f=lambda n: n**2, g=lambda n: n, alpha=2.0)
    # Output:
    # d_C(f,g) = 0.110907
    #   n= 1  actual=0.05545333  predicted=0.05545333  ratio=1.000000
    #   n= 2  actual=0.02772666  predicted=0.02772666  ratio=1.000000
    #   ...  (ratio = 1.0 for all n, confirming exact contraction)
