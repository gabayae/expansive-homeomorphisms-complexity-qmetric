# Expansive Homeomorphisms on Complexity Quasi-Metric Spaces

This repository contains the paper and accompanying code for *Expansive homeomorphisms on complexity quasi-metric spaces* by Ya'e U. Gaba.

## TL;DR

We show that **scaling a function's running time** (multiplying by a constant $\alpha \neq 1$) is an **expansive homeomorphism** on the space of complexity functions. This single fact yields, via standard dynamical-systems machinery:

- **Stable sets = $d_\mathcal{C}$-neighbourhoods**: functions whose orbits stay close are exactly those within a quasi-metric ball.
- **Exact contraction rate**: forward iterates contract $d_\mathcal{C}$ by exactly $1/\alpha$ per step, backward iterates expand by exactly $\alpha$ — no approximation, no hidden constants.
- **Hierarchy theorem as orbit separation**: the classical time hierarchy theorem of Hartmanis–Stearns is recovered as a corollary of orbit separation under iteration.
- **No non-trivial compact invariant sets**: $\psi_\alpha$ is a strict contraction on the symmetrised space, so the standard topological-entropy machinery on compact invariant sets does not apply — a structural limitation of the framework rather than an entropy bound.

In short: **dynamical systems and computational complexity share the same underlying geometry**, and the complexity quasi-metric is the right space to see it.

## Abstract

The complexity quasi-metric, introduced by Schellekens, provides a topological framework where the asymmetric nature of computational comparisons finds precise mathematical expression. In this paper we develop the theory of expansive homeomorphisms on complexity quasi-metric spaces. Our central result establishes that the scaling transformation $\psi_\alpha(f) = \alpha f$ is expansive if and only if $\alpha \neq 1$, with an exact contraction rate of $1/\alpha$ per forward iterate. We characterise the stable and unstable sets explicitly, connect orbit separation to the Hartmanis–Stearns time hierarchy theorem, and show that no non-trivial compact invariant sets exist — clarifying the structural limit of the topological-entropy framework in this setting.

## Main results

| # | Result | Statement |
|---|--------|-----------|
| 1 | **Expansiveness characterisation** (Theorem `thm:main-scaling`) | The scaling map $\psi_\alpha(f)(n) = \alpha f(n)$ is expansive on $(\mathcal{C}, d_\mathcal{C})$ if and only if $\alpha \neq 1$. |
| 2 | **Stable sets** (Theorem `thm:stable-sets`) | The $\delta$-stable set of $f$ under $\psi_\alpha$ ($\alpha > 1$) coincides with the closed $d_\mathcal{C}$-ball $\{g : d_\mathcal{C}(f,g) \leq \delta\}$, and contains all functions pointwise dominated by $f$. |
| 3 | **Unstable sets** (Theorem `thm:unstable-sets`) | The $\delta$-unstable set of $f$ consists of all $g$ with $d_\mathcal{C}(g,f) \leq \delta$. |
| 4 | **Exact contraction rate** (Corollary `cor:exact-contraction`) | For all $\alpha > 0$ and $n \geq 0$: $d_\mathcal{C}(\psi_\alpha^n(f), \psi_\alpha^n(g)) = \alpha^{-n} \, d_\mathcal{C}(f,g)$, with optimal multiplicative constant $C = 1$. |
| 5 | **Hierarchy as orbit separation** (Theorem `thm:hierarchy`) | Any pair $f, g \in \mathcal{C}$ with $d_\mathcal{C}(g,f) > 0$ has $d_\mathcal{C}^s$-separated orbits under $\psi_\alpha$, $\alpha \neq 1$. The standard Hartmanis–Stearns condition $f(n)\log f(n) = o(g(n))$ is one sufficient (not necessary) source of such pairs. |
| 6 | **No non-trivial compact invariant sets** (Proposition `prop:no-compact-invariant`) | For $\alpha \neq 1$, every non-empty compact $\psi_\alpha$-invariant subset of $(\mathcal{C}, d_\mathcal{C}^s)$ has $d_\mathcal{C}^s$-diameter zero. |

### Dynamics–complexity dictionary

| Dynamical concept | Complexity interpretation |
|---|---|
| Quasi-metric $d_\mathcal{C}(f,g) = 0$ | $f$ is at least as fast as $g$ |
| Scaling map $\psi_\alpha$ | Uniform speed change by factor $\alpha$ |
| Expansiveness ($\alpha \neq 1$) | Orbits eventually separate |
| $\delta$-stable set | $d_\mathcal{C}$-ball of asymptotically slower-or-equal functions |
| Unstable set | $d_\mathcal{C}^t$-ball; pointwise-faster functions in particular |
| Exact contraction | $d_\mathcal{C}$ decays as $(1/\alpha)^n$ |
| Backward expansion | $d_\mathcal{C}$ grows as $\alpha^n$ |
| Orbit separation | Hierarchy gap (sufficient but not necessary) |
| No compact invariant sets | Standard entropy machinery does not apply |

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
├── expansive_homeo_complexity_qmetric.tex        # LaTeX source (repo build)
├── expansive_homeo_complexity_qmetric-arxiv.tex  # LaTeX source (arXiv build)
├── expansive_homeo_complexity_qmetric.pdf        # Compiled PDF (repo)
├── expansive_homeo_complexity_qmetric-arxiv.pdf  # Compiled PDF (arXiv)
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
