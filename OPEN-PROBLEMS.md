# Open problems and directions for future work

These directions were originally drafted as the closing section of *Expansive
homeomorphisms on complexity quasi-metric spaces* by Yaé U. Gaba, then moved
here to keep the paper tighter. Each is a self-contained suggestion for
follow-up work; some are concrete and tractable, others are programmatic.

## Topological entropy on the non-compact space

Proposition `prop:no-compact-invariant` shows that for $\alpha \ne 1$ every
non-empty compact $\psi_\alpha$-invariant subset of $(\mathcal{C}, d_\mathcal{C}^s)$
has $d_\mathcal{C}^s$-diameter zero, so the standard Bowen entropy on such
subsets is necessarily zero. The dynamics of $\psi_\alpha$ on the full
non-compact space is non-trivial, however. **Open:** define a meaningful
entropy invariant for $\psi_\alpha$ on $(\mathcal{C}, d_\mathcal{C}^s)$ — for
example via volume-growth entropy, asymmetric Bowen entropy, or a
quasi-metric analogue of the variational principle equating topological and
measure-theoretic entropies.

## Non-linear scaling transformations

The map $\psi_\alpha(f)(n) = \alpha f(n)$ is linear in the function values.
**Open:** characterise expansiveness for non-linear analogues such as

- $\psi(f)(n) = f(n)^p$ for fixed $p > 0$ (power scaling);
- $\psi(f)(n) = f(f(n))$ (self-composition);
- $\psi(f)(n) = f(n) + h(n)$ for a fixed $h \in \mathcal{C}$ (additive shift —
  note that this fails to be a homeomorphism on $\mathcal{C}_{\ge 1}$, but
  may still be tractable on $\mathcal{C}$ as defined).

The Lipschitz identity of `lem:scaling-lip` is unlikely to survive these
generalizations, so qualitatively different techniques will be needed.

## Composition-based transformations and speed-up theorems

Instead of scaling outputs, one can scale inputs:

- $\phi(f)(n) = f(2n)$ (input doubling);
- $\phi(f)(n) = f(n^2)$ (input squaring);
- $\phi(f)(n) = f(\lceil n / 2 \rceil)$ (input halving).

These have a different algebraic structure and connect naturally to
speed-up theorems (Blum 1967). **Open:** are these expansive on
$(\mathcal{C}, d_\mathcal{C})$, and if so what is the expansive constant?
What is the relationship between the dynamical separation rate and the
Blum speed-up factor?

## Space complexity

The complexity quasi-metric $d_\mathcal{C}$ was designed with running-time
functions in mind. **Open:** adapt the framework to space (memory) complexity.
Specifically, given a space-complexity function $s: \mathbb{N} \to (0,\infty)$,
do the results of the paper transfer? The savings theorem (Savitch 1970) — that
$\mathrm{NSPACE}(s) \subseteq \mathrm{DSPACE}(s^2)$ — has no time analogue, so
the dynamics may be qualitatively different.

## Weighted complexity quasi-metrics

The choice of weight $2^{-n}$ in
$d_\mathcal{C}(f, g) = \sum_{n \ge 1} 2^{-n} \max\{0, 1/g(n) - 1/f(n)\}$
is conventional. Replacing $2^{-n}$ by a general summable positive sequence
$w_n$ yields a family of complexity quasi-metrics. Different weight sequences
emphasize different input sizes (e.g., $w_n = 1/n^2$ for an asymptotically
balanced weighting). **Open:** how do the expansiveness, hyperbolicity, and
stable-set results depend on the choice of weights? Is there a canonical
weight sequence determined by an optimality principle?

## Stronger hierarchy theorems

`thm:hierarchy` shows that any pair $f, g$ with $d_\mathcal{C}(g, f) > 0$ has
orbits eventually $d_\mathcal{C}^s$-separated under $\psi_\alpha$
($\alpha \ne 1$), and that the Hartmanis–Stearns time hierarchy condition
$f \log f = o(g)$ is one sufficient source of such pairs. **Open:** can the
dynamical orbit-separation criterion be used to obtain richer hierarchy-style
results — for example, an analogue of the non-deterministic time hierarchy
(Cook 1973), or the space hierarchy (Stearns–Hartmanis–Lewis 1965), within
the complexity quasi-metric framework?

## Shadowing and structural stability

In classical hyperbolic dynamics, expansive homeomorphisms with the shadowing
property are structurally stable: small perturbations of the map preserve the
qualitative orbit structure. **Open:** does $\psi_\alpha$ on
$(\mathcal{C}, d_\mathcal{C})$ possess the shadowing property? If so, this
would provide a robustness guarantee: dynamical conclusions about
$\psi_\alpha$ would transfer to nearby maps, supporting the framework as a
genuine tool for complexity analysis rather than an artefact of the specific
scaling map.

## Connections to domain theory

The complexity quasi-metric space has deep ties to domain theory
([Abramsky–Jung 1994]; [Scott 1982]) via the Smyth completion and the
weightability machinery used by Schellekens to introduce the space in the
first place. **Open:** translate the expansiveness, stable-set, and entropy
results of this paper into the language of (continuous) domains. Does
$\psi_\alpha$ have a natural denotational-semantic interpretation? Is there a
dynamical-systems analogue of the Plotkin–Smyth powerdomain that the
$\psi_\alpha$-orbit-closure operation realizes?

## A categorical view

The Olela-Otafudu–Matladi–Zweni (2024) framework treats $q$-expansive
homeomorphisms as morphisms in a suitable category of quasi-metric spaces.
**Open:** identify the category-theoretic universal property (if any) of the
complexity space $(\mathcal{C}, d_\mathcal{C})$ within the category of
weightable quasi-metric spaces. Is $(\mathcal{C}, d_\mathcal{C})$ a colimit
or limit of some natural diagram of computational objects?

---

## How to use this list

Most of these are independent of each other and can be attacked separately.
The most concrete (and probably the most tractable) is the family of
composition-based transformations: a single Lipschitz computation in the
spirit of `lem:scaling-lip`, performed for $\phi(f)(n) = f(2n)$ or
$\phi(f)(n) = f(n^2)$, would already produce a publishable note. The
shadowing question is conceptually the most ambitious — and the most likely
to yield surprises, given that the standard hyperbolic-dynamics setting
assumes compactness, which fails here.

If you start work on any of these, please open an issue on the companion
repository.
