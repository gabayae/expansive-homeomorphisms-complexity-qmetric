"""Standard quasi-metric computations.

Implements the standard quasi-metric u(x,y) = max(0, y-x) on the reals,
its conjugate u^t(x,y) = max(0, x-y), and the symmetrized version
u^s(x,y) = |x-y|.

Reference: Section 2 of the paper.
"""

import numpy as np


def standard_quasi_metric(x, y):
    """u(x,y) = max(0, y - x)."""
    return max(0.0, y - x)


def conjugate_quasi_metric(x, y):
    """u^t(x,y) = u(y,x) = max(0, x - y)."""
    return max(0.0, x - y)


def symmetrized_quasi_metric(x, y):
    """u^s(x,y) = max(u(x,y), u(y,x)) = |x - y|."""
    return abs(x - y)


if __name__ == "__main__":
    # Examples
    print(standard_quasi_metric(2, 7))      # Output: 5.0
    print(standard_quasi_metric(7, 2))      # Output: 0.0
    print(symmetrized_quasi_metric(2, 7))   # Output: 5.0
