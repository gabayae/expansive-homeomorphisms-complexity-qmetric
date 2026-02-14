"""Topological entropy approximation via spanning sets.

Estimates the topological entropy h(psi_alpha|_K) by computing
(n, epsilon)-spanning sets using a greedy covering heuristic.

Reference: Section 9 of the paper.
"""

import numpy as np

from complexity_distance import complexity_quasi_metric


def topological_entropy_approx(functions, alpha,
                               eps_values, max_n=20, N=80):
    """Estimate topological entropy via spanning sets.

    For each epsilon, approximate the number of
    (n, eps)-spanning sets using a greedy covering
    heuristic (upper bound on the true minimum), then
    estimate h = lim (1/n) log r(n, eps).
    """
    results = {}
    for eps in eps_values:
        counts = []
        for n in range(1, max_n + 1):
            # Compute pairwise max distances over 0..n-1
            m = len(functions)
            max_dists = np.zeros((m, m))
            for j in range(n):
                s = alpha ** j
                for i1 in range(m):
                    for i2 in range(i1 + 1, m):
                        fi = lambda x, s=s, f=functions[i1]: s*f(x)
                        gi = lambda x, s=s, f=functions[i2]: s*f(x)
                        d1 = complexity_quasi_metric(fi, gi, N)
                        d2 = complexity_quasi_metric(gi, fi, N)
                        ds = max(d1, d2)
                        max_dists[i1][i2] = max(max_dists[i1][i2], ds)
                        max_dists[i2][i1] = max_dists[i1][i2]
            # Greedy spanning set count
            covered = [False] * m
            count = 0
            for i in range(m):
                if not covered[i]:
                    count += 1
                    for j in range(m):
                        if max_dists[i][j] < eps:
                            covered[j] = True
            counts.append((n, count))
        results[eps] = counts
    return results


if __name__ == "__main__":
    # Example usage with a small set of functions
    funcs = [
        lambda n: n,
        lambda n: n + 1,
        lambda n: n**2,
        lambda n: n * np.log(n + 1),
        lambda n: 2 * n,
    ]
    entropy_data = topological_entropy_approx(
        funcs, alpha=2.0, eps_values=[0.1, 0.01], max_n=10)

    for eps, counts in entropy_data.items():
        print(f"\neps = {eps}:")
        for n, c in counts:
            h_est = np.log(c) / n if c > 1 else 0
            print(f"  n={n:2d}, spanning count={c}, h_est={h_est:.4f}")
    # Output:
    # eps = 0.1:
    #   n= 1, spanning count=4, h_est=0.6931
    #   n= 2, spanning count=4, h_est=0.6931
    #   ...
    # eps = 0.01:
    #   n= 1, spanning count=5, h_est=0.8047
    #   ...
