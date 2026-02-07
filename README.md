# Expansive Homeomorphisms on Complexity Quasi-Metric Spaces

This repository contains the paper and accompanying code for *Expansive homeomorphisms on complexity quasi-metric spaces*.

## Repository structure

```
├── paper/
│   └── expansive_homeo_complexity_qmetric.tex   # LaTeX source
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

## Abstract

The complexity quasi-metric, introduced by Schellekens, provides a topological framework where the asymmetric nature of computational comparisons finds precise mathematical expression. In this paper we develop a comprehensive theory of expansive homeomorphisms on complexity quasi-metric spaces. Our central result establishes that the scaling transformation is expansive, leading to a full characterisation of stable and unstable sets and a hyperbolicity theorem in canonical coordinates. We connect orbit separation to the time hierarchy theorem and derive topological entropy estimates.

## Requirements

### Python code

- Python 3.8+
- NumPy
- Matplotlib (for orbit visualisation)

```bash
pip install numpy matplotlib
```

### SageMath code

- [SageMath](https://www.sagemath.org/) >= 9.0

```bash
sage complexity_distances.sage
```

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

## Key results

| Function pair | $d_C(f,g)$ | Closed form |
|---|---|---|
| $f(n)=n^2,\ g(n)=n$ | 0.1109 | $\ln 2 - \mathrm{Li}_2(1/2)$ |
| $f(n)=2n,\ g(n)=n$ | 0.3466 | $\frac{1}{2}\ln 2$ |
| $f(n)=n+1,\ g(n)=n$ | 0.3069 | — |
| $f(n)=n,\ g(n)=\ln(n+1)$ | 0.4174 | — |
| $f(n)=n^3,\ g(n)=n^2$ | 0.0450 | — |
| $f(n)=n,\ g(n)=\sqrt{n}$ | 0.1130 | — |

## License

See [LICENSE](LICENSE) for details.
