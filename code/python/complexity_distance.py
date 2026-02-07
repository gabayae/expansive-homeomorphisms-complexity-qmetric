"""Compute the complexity quasi-metric d_C(f, g).

The complexity quasi-metric is defined as:
    d_C(f, g) = sum_{n=1}^{inf} 2^{-n} max{0, 1/g(n) - 1/f(n)}

This module provides a numerical approximation truncated at N terms.

Reference: Section 3 and Algorithm 1 of the paper.
"""

import numpy as np


def complexity_quasi_metric(f, g, N=100):
    """Compute d_C(f, g) truncated at N terms."""
    total = 0.0
    for n in range(1, N + 1):
        delta = 1.0 / g(n) - 1.0 / f(n)
        if delta > 0:
            total += 2**(-n) * delta
    return total


if __name__ == "__main__":
    # Example: f(n) = n,  g(n) = n^2
    f = lambda n: n
    g = lambda n: n**2

    print(f"d_C(f, g) = {complexity_quasi_metric(f, g):.8f}")
    print(f"d_C(g, f) = {complexity_quasi_metric(g, f):.8f}")
    # Output: d_C(f,g) = 0.00000000   (fast -> slow: free)
    #         d_C(g,f) = 0.11090665   (slow -> fast: costly)

    # Additional examples
    h = lambda n: np.log(n + 1)
    print(f"d_C(log, n)   = {complexity_quasi_metric(h, f):.8f}")
    print(f"d_C(n, log)   = {complexity_quasi_metric(f, h):.8f}")
    print(f"d_C(n, n^2)   = {complexity_quasi_metric(f, g):.8f}")
    print(f"d_C(n^2, 2^n) = {complexity_quasi_metric(g, lambda n: 2**min(n,50)):.8f}")
