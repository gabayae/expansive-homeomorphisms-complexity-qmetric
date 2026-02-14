"""Stable and unstable set membership tests.

Determines whether candidate functions belong to the delta-stable or
unstable set of a given function f under the scaling transformation.

Reference: Section 6 and Algorithm 3 of the paper.
"""

from complexity_distance import complexity_quasi_metric


def stable_set(f, candidates, alpha, delta, M=40, N=80):
    """Return functions in the delta-stable set of f."""
    members = []
    for g in candidates:
        in_set = True
        for n in range(M + 1):
            s = alpha ** n
            fn = lambda m, s=s: s * f(m)
            gn = lambda m, s=s: s * g(m)
            if complexity_quasi_metric(fn, gn, N) > delta:
                in_set = False
                break
        if in_set:
            members.append(g)
    return members


def unstable_set(f, candidates, alpha, delta, M=40, N=80):
    """Return functions in the unstable set of f
       (using conjugate quasi-metric).
       By Theorem 5.2, g is in the unstable set iff
       d_C(g, f) = 0, i.e. g(n) <= f(n) for all n.
       We check numerically that d_C(g, f) < tolerance."""
    members = []
    tol = 1e-12
    for g in candidates:
        if complexity_quasi_metric(g, f, N) < tol:
            members.append(g)
    return members


if __name__ == "__main__":
    # Test: g(n) = n^2 should be in S(f, delta) for f(n) = n
    f = lambda n: n
    candidates = [
        lambda n: n**2,     # slower -> in stable set
        lambda n: n**0.5,   # faster -> NOT in stable set
        lambda n: n + 10,   # slightly slower -> in stable set
    ]
    result = stable_set(f, candidates, alpha=2.0, delta=0.2)
    print(f"Members in stable set: {len(result)}")
    # Output: Members in stable set: 2  (n^2 and n+10; sqrt(n) rejected)
