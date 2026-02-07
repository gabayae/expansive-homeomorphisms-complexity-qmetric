"""Check expansive separation for the scaling transformation.

Given functions f, g and a scaling parameter alpha, checks whether
the orbits of f and g under psi_alpha separate beyond a threshold
delta within M iterates.

Reference: Section 4, Algorithm 2 of the paper.
"""

from complexity_distance import complexity_quasi_metric


def check_expansive_constant(f, g, alpha, delta, M=50, N=80):
    """Check whether orbits of f, g under psi_alpha
       separate beyond delta within M iterates."""
    for k in range(-M, M + 1):
        scale = alpha ** k
        fk = lambda n, s=scale: s * f(n)
        gk = lambda n, s=scale: s * g(n)
        d = complexity_quasi_metric(fk, gk, N)
        if d > delta:
            return True, k
    return False, None


if __name__ == "__main__":
    # alpha = 2: should be expansive
    # alpha = 2: should be expansive
    sep, n = check_expansive_constant(
        f=lambda n: n,
        g=lambda n: n + 0.5,
        alpha=2.0, delta=0.01
    )
    print(f"Separated: {sep}, at iterate n = {n}")
    # Output: Separated: True, at iterate n = -1

    # alpha = 1: should NOT be expansive
    sep1, n1 = check_expansive_constant(
        f=lambda n: n,
        g=lambda n: n + 0.5,
        alpha=1.0, delta=0.01
    )
    print(f"alpha=1 separated: {sep1}")
    # Output: alpha=1 separated: False
