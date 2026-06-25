# Literature notes — the complexity space conventions

These notes record what the two foundational papers actually say about the
complexity space $(\mathcal{C}, d_\mathcal{C})$, and how the paper in this
repository relates to those conventions.

## Source files

- `Schellekens-1995-Smyth-completion-...pdf` — M. Schellekens, *The Smyth
  Completion: A Common Foundation for Denotational Semantics and Complexity
  Analysis*, Electron. Notes Theor. Comput. Sci. 1 (1995) 535–556.
- `Romaguera-Schellekens-1999-Quasi-metric-properties-...pdf` — S. Romaguera,
  M. Schellekens, *Quasi-metric properties of complexity spaces*, Topology
  Appl. 98 (1999) 311–322.

## What the literature actually defines

### Romaguera–Schellekens 1999 (p. 313)

> "the main object of our study is the complexity space $(C, d_C)$, where
>
> $$C = \left\{f:\omega\to(0,+\infty]\;\Big|\;\sum_{n=0}^\infty 2^{-n} \frac{1}{f(n)} < +\infty\right\}$$
>
> and $d_C$ is the quasi-metric on $C$ defined by
>
> $$d_C(f,g) = \sum_{n=0}^\infty 2^{-n}\left[\left(\frac{1}{g(n)} - \frac{1}{f(n)}\right) \vee 0\right]$$
>
> whenever $f, g \in C$. **Any subspace of $(C, d_C)$ is also called a
> complexity space** (cf. [12])."

(Emphasis added. Reference [12] in their paper is Schellekens 1995.)

Key points:

- The codomain is $(0, +\infty]$ — strictly positive, with the value $+\infty$
  permitted (the convention $1/+\infty = 0$ makes the sum well-defined).
- **There is no requirement $f(n) \ge 1$.** The single constraint is
  summability: $\sum 2^{-n}/f(n) < \infty$.
- The sum indexes from $n = 0$ (one off from the paper in this repo, which
  uses $n \ge 1$ — a cosmetic difference).
- The weighting function (relevant below) is
  $w_C(f) = \sum_{n=0}^\infty 2^{-n}/f(n)$.
- The "any subspace" clause matters: it means any $X \subseteq C$ — closed
  subspaces, $f \ge 1$ subspaces, $f \le M$ subspaces, finite-dimensional
  subspaces — all count as complexity spaces and inherit the structure.

### Schellekens 1995 (Section 5, p. 7–8)

> "we work on the general function space $(0, \infty]^{\mathbb{N}}$,
> containing the set of all possible complexity functions $C_P$ (recall our
> restriction: $C_P(n) \ne 0$)."
>
> "we work with a space $(X, d)$, where $X \subseteq (0, \infty]^{\mathbb{N}}$
> and where
>
> $$d(f, g) = \sum_{n \ge 0} \left\{\left(\frac{1}{g(n)} - \frac{1}{f(n)}\right)\frac{1}{2^n} \;\Big|\; f(n) > g(n)\right\}$$"

Schellekens 1995 is even more general: $X$ is *any* subset of
$(0, \infty]^{\mathbb{N}}$. The codomain again admits $+\infty$ but excludes
$0$ (running times are at least one step in his computational
interpretation, but represented by reciprocals — so the *reciprocal*, the
"efficiency," is the bounded quantity).

In Section 6 (Divide & Conquer), Schellekens does narrow to a specific
subset $\mathcal{C}_c|b$ to apply the Banach fixed-point theorem — but that
is a *choice of working subspace*, not the definition of complexity space.

## What this means for the paper in this repository

### My earlier fix is sound but unnecessarily restrictive

I previously narrowed the class to
$\mathcal{C} = \{f:\mathbb{N}\to[1,\infty) \;|\; \sum 2^{-n}/f(n) < \infty\}$.
This makes the bound $d_\mathcal{C}(f,g) \le 1$ true and the proof of
Theorem 3.2(iii) goes through verbatim.

### …but it has a new subtle bug

The class $\{f : f(n) \ge 1\}$ is *not* $\psi_\alpha$-invariant for
$\alpha < 1$. Concretely, take $f \equiv 1 \in \mathcal{C}$ and
$\psi_{1/2}(f)(n) = 1/2 < 1$, so $\psi_{1/2}(f) \notin \mathcal{C}$.
But the Main Theorem (Theorem 5.3, `thm:main-scaling`) claims
$\psi_\alpha$ is expansive for *every* $\alpha \ne 1$, including
$\alpha < 1$. The $\alpha < 1$ case of the proof becomes vacuous if
$\psi_\alpha$ isn't even a self-map.

### The cleaner fix (faithful to Schellekens)

Use the full Schellekens class without the lower bound:

$$\mathcal{C} = \left\{f:\mathbb{N}\to(0,\infty) \;\Big|\; \sum_{n=1}^\infty 2^{-n}/f(n) < \infty\right\}$$

(Real-valued positive functions with summability — we drop the $+\infty$
value to keep the paper notation light; this corresponds to a subspace of
Romaguera–Schellekens' class, which is fine by the "any subspace" clause.)

Properties:

- $\mathcal{C}$ is $\psi_\alpha$-invariant for all $\alpha > 0$:
  $\sum 2^{-n}/(\alpha f(n)) = (1/\alpha)\sum 2^{-n}/f(n) < \infty$.
- $\psi_\alpha$ is a bijection with inverse $\psi_{1/\alpha}$, both
  preserving the class.
- $d_\mathcal{C}(f,g)$ is finite for every $f, g \in \mathcal{C}$ because
  $d_\mathcal{C}(f, g) \le \sum 2^{-n}/g(n) = w_\mathcal{C}(g) < \infty$.

### The correct upper bound is $g$-dependent

Replace the universal claim $d_\mathcal{C}(f, g) \le 1$ by the actual bound

$$d_\mathcal{C}(f, g) \le \sum_{n=1}^\infty 2^{-n}/g(n) = w_\mathcal{C}(g)$$

where $w_\mathcal{C}$ is the Romaguera–Schellekens weighting function. As a
special case: if $g(n) \ge 1$ for all $n$, then $w_\mathcal{C}(g) \le 1$,
recovering $d_\mathcal{C}(f, g) \le 1$ on the subspace
$\mathcal{C}_{\ge 1} = \{f \in \mathcal{C} : f(n) \ge 1 \;\forall n\}$.
That subspace is itself a complexity space in the Romaguera–Schellekens
sense, so the specialization is principled.

### The original counter-example is back in scope

Example 3.10 (`ex:counter-bounded`) originally used $f(n) = 1/n$, $g(n) = 1$,
giving $d_\mathcal{C}(g, f) = \sum_{n=2}^\infty 2^{-n}(n - 1) = 1$. With the
broader class, $f(n) = 1/n$ is back in: $\sum 2^{-n} n = 2 < \infty$, so
$f \in \mathcal{C}$. And the example now saturates the $g$-dependent bound
$w_\mathcal{C}(g) = \sum 2^{-n} = 1$ at $g \equiv 1$. The earlier rewrite
(to constant-function family) was a workaround for the over-restrictive
class; the original is more natural and can be restored.

## Recommended fix to the paper

1. Restore the broader class definition
   $\mathcal{C} = \{f:\mathbb{N}\to(0,\infty) : \sum 2^{-n}/f(n) < \infty\}$
   in Section 3.
2. Replace the Remark (currently "Why $f(n) \ge 1$") with one citing
   Romaguera–Schellekens' "any subspace is also a complexity space" clause
   and noting that the bound $\le 1$ specializes to $\mathcal{C}_{\ge 1}$.
3. Restate Theorem 3.2(iii) as: $d_\mathcal{C}(f, g) \le w_\mathcal{C}(g)
   = \sum 2^{-n}/g(n)$, with the corollary that
   $d_\mathcal{C}(f, g) \le 1$ when $g(n) \ge 1$.
4. Restore the original Example 3.10 ($f = 1/n$, $g = 1$, giving
   $d_\mathcal{C}(g, f) = 1 = w_\mathcal{C}(g)$).
5. Verify that the rest of the paper (which only uses Lemma 4.2 and the
   $d_\mathcal{C}$-finiteness) doesn't depend on the universal $\le 1$ bound.
   Spot-check: `prop:no-compact-invariant` uses Banach contraction on
   $d_\mathcal{C}^s$, which is valid in the broader class.
6. No other downstream changes needed.
