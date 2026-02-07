"""Orbit computation and visualisation under the scaling transformation.

Computes d_C(psi_alpha^k(f), g) for a range of iterates k and
optionally plots the orbit divergence.

Reference: Section 5 of the paper.
"""

import matplotlib.pyplot as plt

from complexity_distance import complexity_quasi_metric


def compute_orbit(f, alpha, k_range, g=None, N=80):
    """Compute d_C(psi_alpha^k(f), g) for each k.
    Measures how the distance from the orbit of f to a
    reference function g evolves under iteration."""
    if g is None:
        g = lambda n: n  # default reference
    distances = []
    for k in k_range:
        scale = alpha ** k
        fk = lambda n, s=scale: s * f(n)
        d = complexity_quasi_metric(fk, g, N)
        distances.append((k, d))
    return distances


if __name__ == "__main__":
    # Visualise orbit divergence
    orbit = compute_orbit(lambda n: n + 1, alpha=2.0,
                          k_range=range(-10, 11))
    ks = [p[0] for p in orbit]
    ds = [p[1] for p in orbit]
    plt.figure(figsize=(8, 5))
    plt.plot(ks, ds, 'b-o', markersize=4)
    plt.xlabel('iterate k')
    plt.ylabel('d_C(psi^k(f), g)')
    plt.title('Orbit divergence under scaling (alpha=2)')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('orbit_divergence.png', dpi=150)
    plt.show()
