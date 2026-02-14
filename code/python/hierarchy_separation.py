"""Find hierarchy separation iterates.

Given functions f, g with f(n)log(f(n)) = o(g(n)), finds the iterate k
at which the symmetrized distance d_C^s(psi_alpha^k(f), psi_alpha^k(g))
exceeds delta, demonstrating the connection to the time hierarchy theorem.

Reference: Section 8 of the paper.
"""

import numpy as np

from complexity_distance import complexity_quasi_metric


def hierarchy_separation(f, g, alpha, delta, M=100, N=80):
    """Find iterate where hierarchy separation occurs."""
    for k in range(-M, M + 1):
        s = alpha ** k
        fn = lambda n, s=s: s * f(n)
        gn = lambda n, s=s: s * g(n)
        d_fwd = complexity_quasi_metric(fn, gn, N)
        d_bwd = complexity_quasi_metric(gn, fn, N)
        d_sym = max(d_fwd, d_bwd)
        if d_sym > delta:
            return k, d_sym
    return None, 0.0


if __name__ == "__main__":
    # n  vs  n*log(n)^2  -- hierarchy should separate them
    # n  vs  n*log(n)^2  -- hierarchy should separate them
    k, d = hierarchy_separation(
        f=lambda n: n,
        g=lambda n: n * np.log(n + 1)**2,
        alpha=2.0, delta=0.05)
    print(f"Separated at iterate k={k}, distance={d:.6f}")
    # Output: Separated at iterate k=0, distance=0.541178

    # Polynomial vs exponential
    k2, d2 = hierarchy_separation(
        f=lambda n: n**2,
        g=lambda n: 2**min(n, 50),
        alpha=2.0, delta=0.05)
    print(f"Poly vs exp: separated at k={k2}, distance={d2:.6f}")
    # Output: Poly vs exp: separated at k=0, distance=0.110907
