# Expansive homeomorphisms on complexity quasi-metric spaces

Paper and reproducibility code for the manuscript of the same title by
[Yaé U. Gaba](mailto:yaeulrich.gaba@gmail.com).

> **Compiled paper:** [`expansive_homeo_complexity_qmetric.pdf`](expansive_homeo_complexity_qmetric.pdf) — 26 pages
> **arXiv build:** [`expansive_homeo_complexity_qmetric-arxiv.pdf`](expansive_homeo_complexity_qmetric-arxiv.pdf)
> **Open problems / future directions:** [`OPEN-PROBLEMS.md`](OPEN-PROBLEMS.md)
> **Source PDFs of cited foundational papers:** [`references/`](references/)

---

## What is in the paper

The paper studies the dynamics of the *scaling transformation*
$\psi_\alpha(f)(n) = \alpha f(n)$ on the complexity quasi-metric space
$(\mathcal{C}, d_\mathcal{C})$ introduced by Schellekens (1995) and developed
further by Romaguera and Schellekens (1999). The framework treats running-time
profiles as points and equips them with an asymmetric distance reflecting the
asymmetry of computational comparisons ("$f$ is at most as fast as $g$" is not
the same statement as "$g$ is at most as slow as $f$").

The central result is that $\psi_\alpha$ is an expansive homeomorphism in the
sense of [Olela-Otafudu–Matladi–Zweni (2024)](https://polipapers.upv.es/index.php/AGT/article/view/19855)
exactly when $\alpha \neq 1$, with an exact contraction rate of $1/\alpha$ per
forward iterate (constant $C = 1$). The paper derives the consequent
characterisations of stable and unstable sets, a dynamical reading of the
Hartmanis–Stearns time hierarchy, and a structural negative result for
topological entropy: no non-trivial compact $\psi_\alpha$-invariant subset
exists in the symmetrised space, so the standard Bowen entropy machinery does
not apply.

## Repository layout

```
expansive_homeo_complexity_qmetric.tex        LaTeX source (repo build)
expansive_homeo_complexity_qmetric-arxiv.tex  LaTeX source (arXiv build)
expansive_homeo_complexity_qmetric.pdf        Compiled PDF (repo build)
expansive_homeo_complexity_qmetric-arxiv.pdf  Compiled PDF (arXiv build)
OPEN-PROBLEMS.md                              Future-work catalogue
README.md                                     This file

code/
  python/    Numerical implementations (NumPy, Matplotlib)
  sagemath/  Symbolic verifications (SageMath ≥ 9.0)

references/
  Schellekens-1995-Smyth-completion-...pdf
  Romaguera-Schellekens-1999-Quasi-metric-properties-...pdf
  NOTES.md   Literature conventions adopted in the paper
```

## Reproducing the computations

Every numerical claim and worked example in the paper is backed by a
runnable script. The headline cross-checks:

```bash
# Lipschitz identity (Lemma 4.2) and backward expansion (Example 6.4):
sage code/sagemath/hyperbolic_contraction.sage

# d_C and d_C^t on representative pairs (Section 3 examples):
sage code/sagemath/complexity_distances.sage

# Orbit-separation iterate count (Section 5):
python code/python/expansiveness_check.py
```

Each script is self-contained and prints its output to stdout; no input data
is required.

## Citation

```bibtex
@unpublished{gaba2026expansive,
  author = {Ya{\'e} U. Gaba},
  title  = {Expansive homeomorphisms on complexity quasi-metric spaces},
  year   = {2026},
  note   = {Manuscript.
            \url{https://github.com/gabayae/expansive-homeomorphisms-complexity-qmetric}},
}
```

The arXiv identifier and DOI will be added here once available.

## License

A formal license file will be added shortly. In the meantime, the LaTeX
sources and code in this repository are released for non-commercial
scholarly use; the paper text will be governed by the publishing journal's
terms once accepted.
