# Expansive Homeomorphisms on Complexity Quasi-Metric Spaces

This repository contains the paper and accompanying code for *Expansive homeomorphisms on complexity quasi-metric spaces* by Ya'e U. Gaba.

## TL;DR

We show that **scaling a function's running time** (multiplying by a constant $\alpha \neq 1$) is an **expansive homeomorphism** on the space of complexity functions. This single fact yields, via standard dynamical-systems machinery:

- **Stable sets = complexity classes**: functions whose orbits stay close are exactly those with comparable asymptotic growth.
- **Exact hyperbolicity**: distances contract by $1/\alpha$ per forward iterate and expand by $\alpha$ per backward iterate — no approximation, no hidden constants.
- **Hierarchy theorem as orbit separation**: the classical time hierarchy theorem of Hartmanis–Stearns corresponds to orbits being pulled apart under iteration.
- **Entropy dichotomy**: topological entropy is either zero (finite invariant sets) or at least $\log\alpha$ (infinite ones).

In short: **dynamical systems and computational complexity share the same underlying geometry**, and the complexity quasi-metric is the right space to see it.

## Abstract

The complexity quasi-metric, introduced by Schellekens, provides a topological framework where the asymmetric nature of computational comparisons finds precise mathematical expression. In this paper we develop a comprehensive theory of expansive homeomorphisms on complexity quasi-metric spaces. Our central result establishes that the scaling transformation is expansive, leading to a full characterisation of stable and unstable sets and a hyperbolicity theorem in canonical coordinates. We connect orbit separation to the time hierarchy theorem and derive topological entropy estimates.

## Main results

| # | Result | Statement |
|---|--------|-----------|
| 1 | **Expansiveness characterisation** (Theorem 5.8) | The scaling map $\psi_\alpha(f)(n) = \alpha f(n)$ is expansive on $(\mathcal{C}, d_\mathcal{C})$ if and only if $\alpha \neq 1$. |
| 2 | **Stable sets = complexity classes** (Theorem 6.3) | The $\delta$-stable sets of $\psi_\alpha$ coincide with $d_\mathcal{C}$-neighbourhoods and contain all functions that are asymptotically at least as slow. |
| 3 | **Unstable sets** (Theorem 6.7) | The $\delta$-unstable set of $f$ consists of all functions pointwise bounded above by $f$. |
| 4 | **Hyperbolicity** (Theorem 7.3) | Forward iterates contract distances exactly: $d_\mathcal{C}(\psi_\alpha^n(f), \psi_\alpha^n(g)) = \alpha^{-n} \, d_\mathcal{C}(f,g)$, with optimal constant $C = 1$. |
| 5 | **Hierarchy as orbit separation** (Theorem 8.1) | If $f(n)\log f(n) = o(g(n))$, then the symmetrised orbits eventually separate — recovering the time hierarchy theorem dynamically. |
| 6 | **Entropy dichotomy** (Corollary 9.5) | Topological entropy of $\psi_\alpha$ restricted to a compact invariant set is $0$ if the set is finite, and $\geq \log\alpha$ otherwise. |

### Dynamics–complexity dictionary

| Dynamical concept | Complexity interpretation |
|---|---|
| Quasi-metric $d_\mathcal{C}(f,g) = 0$ | $f$ is at least as fast as $g$ |
| Scaling map $\psi_\alpha$ | Uniform speed change by factor $\alpha$ |
| Expansiveness ($\alpha \neq 1$) | Orbits eventually separate |
| $\delta$-stable set | Complexity class neighbourhood |
| Unstable set | All pointwise-faster functions |
| Hyperbolic contraction | $d_\mathcal{C}$ decays as $(1/\alpha)^n$ |
| Backward expansion | $d_\mathcal{C}$ grows as $\alpha^n$ |
| Orbit separation | Time hierarchy gap |
| Topological entropy $\geq \log\alpha$ | Dynamical complexity bound |

## Computed complexity distances

| Function pair | $d_\mathcal{C}(f,g)$ | Closed form |
|---|---|---|
| $f(n)=n^2,\ g(n)=n$ | 0.1109 | $\ln 2 - \mathrm{Li}_2(1/2)$ |
| $f(n)=2n,\ g(n)=n$ | 0.3466 | $\frac{1}{2}\ln 2$ |
| $f(n)=n+1,\ g(n)=n$ | 0.3069 | — |
| $f(n)=n,\ g(n)=\ln(n+1)$ | 0.4174 | — |
| $f(n)=n^3,\ g(n)=n^2$ | 0.0450 | — |
| $f(n)=n,\ g(n)=\sqrt{n}$ | 0.1130 | — |

## Repository structure

```
├── paper/
│   └── expansive_homeo_complexity_qmetric.tex   # LaTeX source + compiled PDF
├── code/
│   ├── python/                    # Python numerical implementations
│   │   ├── quasi_metric.py        # Standard quasi-metric (Section 2)
│   │   ├── complexity_distance.py # Complexity quasi-metric d_C (Section 3)
│   │   ├── expansiveness_check.py # Expansive separation check (Section 4)
│   │   ├── orbit_computation.py   # Orbit computation & plots (Section 5)
│   │   ├── stable_set.py          # Stable/unstable set membership (Section 6)
│   │   ├── hyperbolicity.py       # Exponential contraction (Section 7)
│   │   ├── hierarchy_separation.py# Hierarchy separation iterate (Section 8)
│   │   └── entropy_estimate.py    # Topological entropy estimate (Section 9)
│   └── sagemath/                  # SageMath symbolic verifications
│       ├── complexity_distances.sage   # Exact d_C values (Examples 3.3–3.7)
│       ├── partial_sums.sage           # Convergence analysis (Example 5.5)
│       ├── hyperbolic_contraction.sage # Contraction & expansion (Examples 7.7–7.10)
│       ├── separation_iterates.sage    # Separation & hierarchy (Examples 5.14, 8.3)
│       └── incomparable_functions.sage # Both directions positive (Example 3.7)
├── README.md
├── .gitignore
└── LICENSE
```

## Requirements

### Python

- Python 3.8+
- NumPy
- Matplotlib (for orbit visualisation)

```bash
pip install numpy matplotlib
```

### SageMath

- [SageMath](https://www.sagemath.org/) >= 9.0

## Running the code

### Python

Each Python script can be run standalone:

```bash
cd code/python
python complexity_distance.py
python expansiveness_check.py
python orbit_computation.py
```

The `complexity_distance.py` module is imported by other scripts, so run from the `code/python/` directory.

### SageMath

Each `.sage` file can be run directly with SageMath:

```bash
cd code/sagemath
sage complexity_distances.sage
sage partial_sums.sage
sage hyperbolic_contraction.sage
sage separation_iterates.sage
sage incomparable_functions.sage
```

## License

See [LICENSE](LICENSE) for details.
