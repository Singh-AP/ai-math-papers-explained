# Nonamenability of Thompson's Group $F$: A Technical Explainer

---

## 1. Introduction and Foundations

### 1.1 Invariant Means and Group Amenability
In the classical analytical framework established by von Neumann and Day, a discrete group $G$ is defined as **amenable** if the space of its bounded real-valued functions $\ell^\infty(G; \mathbb{R})$ admits a positive normalized left-invariant mean. Formally, a linear functional $M: \ell^\infty(G; \mathbb{R}) \to \mathbb{R}$ is a positive normalized left-invariant mean if it satisfies the following three foundational axioms:

1. **Normalization:**
   $$M(1) = 1$$
   where $1$ denotes the constant function identically equal to $1$ on $G$.

2. **Positivity:**
   $$M(\varphi) \ge 0 \quad \text{whenever } \varphi \in \ell^\infty(G; \mathbb{R}) \text{ and } \varphi(g) \ge 0 \text{ for all } g \in G$$

3. **Left-Invariance:**
   $$M(g \mapsto \varphi(hg)) = M(\varphi) \quad \text{for all } h \in G \text{ and all } \varphi \in \ell^\infty(G; \mathbb{R})$$

### 1.2 The Følner Criterion
The analytical existence of an invariant mean can be reformulated combinatorially via the Følner criterion. Amenability of a discrete group $G$ implies that for every finite subset $S \subset G$ and every tolerance parameter $\varepsilon > 0$, there exists a nonempty finite subset $A \subset G$ that satisfies the relative boundary inequality:

$$\frac{|hA \triangle A|}{|A|} < \varepsilon \quad \text{for all } h \in S \tag{1.1}$$

where $hA \triangle A$ denotes the symmetric difference between the translated set $hA = \{ha : a \in A\}$ and $A$. Modern left-translation formulations bound the sum of these translation ratios; taking a smaller tolerance parameter ensures that amenability requires the existence of finite sets whose relative boundaries under any fixed finite family of translations are simultaneously small.

### 1.3 Definition and Structure of Thompson's Group $F$
Thompson's group $F$ (introduced by Richard Thompson in 1965) is defined as the group of orientation-preserving (increasing) piecewise-linear homeomorphisms of the closed unit interval $[0, 1]$ satisfying three structural conditions:
* Finitely many linear pieces;
* Breakpoints occurring strictly at dyadic rational numbers (i.e., numbers of the form $k / 2^r$ for non-negative integers $r$ and $0 \le k \le 2^r$);
* Slopes on linear segments restricted to integral powers of 2 ($2^\mathbb{Z} = \{2^q : q \in \mathbb{Z}\}$).

Throughout this document, $F$ is regarded as a discrete group under the composition/multiplication convention:

$$hg = h \circ g$$

where $g$ is applied first, followed by $h$.

---

## 2. Historical Context, Structural Properties, and Prior Work

### 2.1 Subgroup Structure and Topological Finiteness
Deciding the amenability of Thompson's group $F$ has historically stood as a central open problem in geometric group theory. The difficulty stems directly from the fact that $F$ avoids all the classical, standard obstructions to amenability while simultaneously escaping the basic constructions that generate amenable groups:

* **Absence of Nonabelian Free Subgroups (Brin–Squier, 1985):** $F$ contains no nonabelian free subgroup $F_2$. Nonabelian free subgroups provide the classical Tits-alternative paradox used to establish nonamenability (e.g., in the Banach–Tarski paradox). Their complete absence in $F$ ruled out the most direct geometric obstruction.
* **Non-Elementary Amenability (Cannon–Floyd–Parry, 1996):** $F$ is not elementary amenable. That is, $F$ lies strictly outside the smallest class of groups containing all finite and abelian groups that is closed under taking subgroups, quotients, extensions, and directed unions. Escaping this inductive hierarchy left the status of $F$ entirely ambiguous.
* **Topological Finiteness $FP_\infty$ (Brown–Geoghegan, 1984):** $F$ possesses high topological finiteness properties, admitting an infinite-dimensional torsion-free classifying space with finitely many cells in each dimension. Homologically, $F$ behaves like a finite-dimensional object, ruling out simple infinite-dimensional topological obstructions.

### 2.2 Finite Approximations, Trees, and Operator Algebras
Prior to the full resolution of the problem, a substantial body of literature constrained the structural behavior of $F$ through finite approximations, trees, and operator algebras:

* **Combinatorial and Ramsey Bounds (Moore, 2013):** Moore established tower lower bounds on the growth of Følner set sizes in $F$ and introduced a characterization of amenability for $F$ based on a scalar convex Ramsey property for finite rooted ordered binary trees.
* **Density and Diagram-Defined Classes (Guba, 2025, 2026):** Guba derived Cayley subgraph density bounds and restricted the existence of right-invariant means by partitioning elements into seven diagram-defined classes.
* **Operator Algebraic Connections (Haagerup–Olesen, 2017):** Haagerup and Olesen proved that if the reduced group $C^*$-algebra of Thompson's group $T$ were simple, then Thompson's group $F$ would necessarily be nonamenable.

### 2.3 Published Claims and Resolutions
Literature on Thompson's group $F$ contains a rich history of conjectures, claimed proofs, and mathematical corrections:

| Year | Author(s) | Claim / Result Summary |
| :--- | :--- | :--- |
| **1979** | Geoghegan | Conjectured that Thompson's group $F$ is nonamenable (recorded in Cannon–Floyd–Parry, 1996). |
| **2009 / 2011** | Shavgulidze / Moore | Shavgulidze published a manuscript claiming amenability for $F$; Moore (2011) identified critical errors in the proof. |
| **2012** | Moore | Withdrew a separate manuscript claiming amenability after Akhmedov identified an error in Lemma 4.13 of that text. *(Note: This withdrawal concerned a separate manuscript and did not invalidate Moore's 2013 published Ramsey characterization or fast Følner growth results).* |
| **2021** | Akhmedov | Claimed nonamenability of $F$ via a height-function criterion. |

---

## 3. Main Theorem and Quantitative Boundary Bound

### 3.1 Statement of Main Theorem

#### Theorem 1.1
> Thompson's group $F$ is not amenable.

This result confirms Geoghegan's 1979 conjecture and completely resolves the long-standing amenability problem for $F$.

### 3.2 Quantitative Følner Lower Bound

The nonamenability of $F$ is established by showing that a fixed, explicit finite set of group elements imposes a positive uniform lower bound on the relative boundary of *any* nonempty finite set $A \subset F$.

#### Proposition 2.3
> For the explicitly constructed finite set of transports $S \subset F$, every nonempty finite subset $A \subset F$ satisfies:
> 
> $$\max_{h \in S} \frac{|hA \triangle A|}{|A|} \ge \frac{\delta^2/L^2 - 4/D}{4(1 - 1/D)} > 0$$
> 
> where $L, \delta > 0$ are the Lipschitz and displacement constants of a map on a Hilbert unit ball, and $D \ge 2$ is a fixed integer satisfying $D > 4L^2 / \delta^2$.

Because this lower bound is strictly positive and depends only on universal geometric constants ($L, \delta, D$) and not on $A$, it directly contradicts the Følner criterion (Equation 1.1), thereby establishing Theorem 1.1.

---

## 4. Step-by-Step Proof of Nonamenability

### 4.1 The Benyamini–Sternfeld Displacement Map (Lemma 1.2)
The proof constructs a contradiction by mapping finite group averages onto an infinite-dimensional Hilbert space where fixed points are ruled out by topological geometry.

#### Lemma 1.2 (Benyamini–Sternfeld Phenomenon)
> In a real Hilbert space $H$ with closed unit ball $B = \{x \in H : \|x\| \le 1\}$, there exists a Lipschitz map $f: B \to B$ with Lipschitz constant $L > 0$ and displacement constant $\delta > 0$ such that:
> 
> $$\|f(x) - x\| \ge \delta \quad \text{for all } x \in B$$

This map prevents the existence of approximate fixed points for finite-average translation actions.

### 4.2 Dyadic Partitions, Normalized Restrictions, and Mesh Convergence
To analyze functions on $F$, elements are evaluated via their actions on dyadic intervals and partitions:

1. **Basic Dyadic Interval:** An interval of the form $I = [k 2^{-r}, (k+1)2^{-r}] \subseteq [0, 1]$, where $r \in \mathbb{N} \cup \{0\}$ and $0 \le k < 2^r$. Its associated orientation-preserving affine scaling map is $s_I: [0, 1] \to I$, defined by $s_I(x) = k 2^{-r} + x 2^{-r}$. We write $I \cdot J = s_I(J)$.
2. **Basic Partition:** A finite partition $T$ of $[0, 1]$ into basic dyadic intervals. A partition $T$ *respects* an interval $I$ if $I$ is a union of cells of $T$.
3. **Normalized Restriction:** If $T$ respects $I$, its normalized restriction $T_I$ is defined as:
   $$T_I = \{s_I^{-1}(K) : K \in T, K \subseteq I\}$$
   The composition of affine charts satisfies $s_{I \cdot J} = s_I \circ s_J$. Consequently, if $T$ respects both $I$ and $I \cdot J$, then $T_I$ respects $J$ and:
   $$(T_I)_J = T_{I \cdot J}$$

#### Lemma 2.1
> For each $g \in F$, the image partitions $g T(n)$ (where $T(n)$ is the uniform partition into $2^n$ cells) are basic partitions for all sufficiently large $n$, and their mesh size (maximum length of a cell) tends to zero as $n \to \infty$. 
> Furthermore, given any finite set $K \subset F$ and finite family of basic intervals $\mathcal{J}$, there exists an integer $n_0$ such that $g T(n)$ is basic and respects every interval $J \in \mathcal{J}$ for all $g \in K$ and all $n \ge n_0$.

### 4.3 Affine Transport and Exact Covariance
For basic intervals $I, J$, write $I < J$ if $\max I < \min J$ (requiring a positive gap). An interval is *internal* if its endpoints lie strictly within the open interval $(0, 1)$.

#### Lemma 2.2
> If $I < J$ and $I' < J'$ are two pairs of internal separated basic intervals, there exists an element $h \in F$ whose restrictions carry $I$ affinely onto $I'$ and $J$ affinely onto $J'$.

If $h \in F$ carries $I$ affinely onto $I'$, then $h \circ s_I = s_{I'}$. Thus, if $g T(n)$ and $(hg) T(n)$ respect $I$ and $I'$ respectively, exact covariance holds:

$$((hg) T(n))_{I'} = (g T(n))_I$$

Let $D \ge 2$ be an integer chosen to satisfy $D > 4L^2 / \delta^2$. Fix $D$ strictly separated internal basic intervals $I_1 < I_2 < \dots < I_D$ (parents), and place an affine copy of these intervals inside each parent $I_i$, producing $D^2$ descendant intervals $I_i \cdot I_j$. Define the finite collection of internal basic intervals:

$$\mathcal{I} = \{I_i : 1 \le i \le D\} \cup \{I_i \cdot I_j : 1 \le i, j \le D\}$$

**Generation of the Transport Set $S$:** For *every* ordered strictly separated pair $I < J$ in the finite family $\mathcal{I}$, an element $h_{I,J} \in F$ is selected using Lemma 2.2 to carry $(I, J)$ affinely onto the single reference pair $(I_1, I_2)$. The finite set $S \subset F$ is defined as the collection of all such transport elements $h_{I,J}$. Crucially, $S$ is constructed *before* and *independently of* any finite target set $A \subset F$ to be tested.

### 4.4 Recursive Coloring and Vector Identities
Every basic partition $T$ is assigned a Hilbert color $p(T) \in B$ via induction on its number of cells:

$$p(T) = \begin{cases} 
f\left(\frac{1}{D}\sum_{j=1}^D p(T_{I_j})\right), & \text{if } T \text{ respects every parent } I_j \\ 
0, & \text{otherwise} 
\end{cases}$$

This induction is well-founded because each parent $I_j$ is internal, meaning any proper restriction $T_{I_j}$ contains strictly fewer cells than $T$.

A pair $(n, g)$ is called *admissible* if $g T(n)$ is basic and respects every interval in $\mathcal{I}$. For $g \in F$, parent colors $X_i(g)$ and descendant colors $Y_{ij}(g)$ are defined by:

$$X_i(g) = X_{I_i}(g) = p((g T(n))_{I_i}), \quad Y_{ij}(g) = X_{I_i \cdot I_j}(g) = p((g T(n))_{I_i \cdot I_j})$$

When $(n, g)$ is admissible, the recursion rules and equality $(T_{I_i})_{I_j} = T_{I_i \cdot I_j}$ yield the exact vector identity:

$$X_i(g) = f(z_i(g)) \quad \text{where } z_i(g) = \frac{1}{D}\sum_{j=1}^D X_{I_i \cdot I_j}(g)$$

Define the parent mean vector as:

$$m(g) = \frac{1}{D}\sum_{k=1}^D X_k(g)$$

### 4.5 Correlation Comparisons and Variance Bounds
Fix a nonempty finite set $A \subset F$. Choose a level $n$ large enough so that $(n, g)$ is admissible for all $g \in A \cup SA$ (where $SA = \bigcup_{h \in S} hA$). 

Let $\eta = \max_{h \in S} \frac{|hA \triangle A|}{|A|}$ be the maximal relative boundary ratio over $S$, and let $E_A \psi = \frac{1}{|A|}\sum_{g \in A} \psi(g)$ denote the average over $A$. Define the central correlation parameter:

$$\alpha = E_A \langle X_{I_1}, X_{I_2} \rangle$$

For any strictly separated pair $I, J \in \mathcal{I}$, applying the transport element $h_{I,J} \in S$ and cancellation over $h_{I,J} A \cap A$ yields:

$$\left| E_A \langle X_I, X_J \rangle - \alpha \right| \le \eta$$

When computing inner products across the grid of descendants and parents $\langle X_{I_i \cdot I_j}, X_{I_k} \rangle$:
* **Off-Diagonal / Separated Pairs:** $D(D-1)$ pairs consist of strictly separated intervals. Their averaged inner products lie within $\eta$ of $\alpha$.
* **Diagonal / Nested Pairs:** $D$ pairs involve a descendant nested inside or meeting its own parent. By Cauchy–Schwarz and unit-ball bounds ($\|x\| \le 1$), these inner products are bounded below by $-1$.

```
                  Parents (k = 1 ... D)
             I_1      ...      I_i      ...      I_D
          +--------+--------+--------+--------+--------+
   I_i·I_1| Separ. | ...    | Nested | ...    | Separ. |
Desc-     |  pair  |        |  pair  |        |  pair  |
 endants  +--------+--------+--------+--------+--------+
(j=1..D)  |  ...   | ...    |  ...   | ...    |  ...   |
          +--------+--------+--------+--------+--------+
   I_i·I_D| Separ. | ...    | Nested | ...    | Separ. |
          +--------+--------+--------+--------+--------+
```
*Figure 1: Schematic matrix of inner products $\langle X_{I_i \cdot I_j}, X_{I_k} \rangle$. Off-diagonal terms ($D(D-1)$ terms) correspond to separated pairs with average within $\eta$ of $\alpha$. Column $i$ contains the $D$ nested pairs, bounded below by $-1$.*

Expanding $E_A \|m\|^2$, $E_A \|z_i\|^2$, and $E_A \langle z_i, m \rangle$:

$$E_A \|m\|^2 \le \left(1 - \frac{1}{D}\right)(\alpha + \eta) + \frac{1}{D}$$

$$E_A \|z_i\|^2 \le \left(1 - \frac{1}{D}\right)(\alpha + \eta) + \frac{1}{D}$$

$$E_A \langle z_i, m \rangle \ge \left(1 - \frac{1}{D}\right)(\alpha - \eta) - \frac{1}{D}$$

To see the exact linear algebra mechanism behind the variance bound, compute $E_A \|z_i - m\|^2 = E_A \|z_i\|^2 + E_A \|m\|^2 - 2 E_A \langle z_i, m \rangle$. Substituting the bounds above, the leading linear terms containing the central correlation parameter $\alpha$ combine as:

$$\left(1 - \frac{1}{D}\right)\alpha + \left(1 - \frac{1}{D}\right)\alpha - 2\left(1 - \frac{1}{D}\right)\alpha = 0$$

Because these terms cancel out exactly regardless of the sign or magnitude of $\alpha$, the variance bound is completely independent of the actual geometric correlations of the colors. Gathering the remaining terms involving $\eta$ and $1/D$ yields the universal variance bound:

$$E_A \|z_i - m\|^2 \le \frac{4}{D} + 4\left(1 - \frac{1}{D}\right)\eta \quad (1 \le i \le D) \tag{2.16}$$

### 4.6 Convexity, Displacement Contradiction, and Final Proof
For every $g \in A$, applying the displacement lower bound ($\|f(x) - x\| \ge \delta$), convexity of the squared norm, and $L$-Lipschitz continuity yields:

$$\delta^2 \le \|m(g) - f(m(g))\|^2 = \left\| \frac{1}{D}\sum_{i=1}^D (f(z_i(g)) - f(m(g))) \right\|^2 \le \frac{L^2}{D} \sum_{i=1}^D \|z_i(g) - m(g)\|^2 \tag{2.12}$$

Averaging Equation 2.12 over $A$ and applying the variance bound (Equation 2.16):

$$\delta^2 \le \frac{L^2}{D} \sum_{i=1}^D E_A \|z_i - m\|^2 \le L^2 \left( \frac{4}{D} + 4\left(1 - \frac{1}{D}\right)\eta \right)$$

Rearranging this inequality for $\eta$ gives:

$$\eta \ge \frac{\delta^2/L^2 - 4/D}{4(1 - 1/D)}$$

Because $D$ was chosen such that $D > 4L^2 / \delta^2$, this lower bound is strictly positive, independent of $A$, and directly contradicts the Følner criterion (Equation 1.1). Thus, $F$ cannot be amenable. $\blacksquare$

---

## 5. Explicit Construction of the Displacement Map

### 5.1 The Hilbert Space Setting and Separated Curve
To ensure self-contained rigor, Lemma 1.2 is explicitly constructed on the real Hilbert space $H = L^2([0, 1]; \mathbb{R}^2)$ with closed unit ball $B = \{x \in H : \|x\| \le 1\}$.

Define functions $a(t)$ and $\theta(t)$ on $\mathbb{R}$:

$$a(t) = \begin{cases} 
t/8, & t \le 2 \\ 
5/16 - (3-t)^2/16, & 2 < t < 3 \\ 
5/16, & t \ge 3 
\end{cases}, \quad 
\theta(t) = \begin{cases} 
0, & t \le 1 \\ 
(t-1)^2/2, & 1 < t < 2 \\ 
t - 3/2, & t \ge 2 
\end{cases}$$

For $w \in [0, 1]$, set $v(t)(w) = (\cos(\theta(t)w), \sin(\theta(t)w))$ and define the parametrized curve $\gamma(t) = a(t) v(t)$.

#### Lemma A.2
> The curve $\gamma$ is injective, has a bounded derivative with speed $c = \inf_{t \in \mathbb{R}} \|\gamma'(t)\| = 1/8$, and unit tangent $u(t) = \gamma'(t)/\|\gamma'(t)\|$ satisfying $\langle u(t), v(t) \rangle \ge 0$.
> Furthermore, $\gamma$ satisfies uniform separation:
> 
> $$\sigma(d) = \inf_{|t-s| \ge d} \|\gamma(t) - \gamma(s)\| > 0 \quad \text{for all } d > 0$$
> 
> Consequently, there exists a tube radius $0 < \rho < 1/32$ such that every element $x$ in the tubular neighborhood $U = \{x \in H : \text{dist}(x, \gamma(\mathbb{R})) < \rho\}$ has a unique nearest point $\gamma(t(x))$ with residual $e(x) = x - \gamma(t(x)) \perp u(t(x))$.

### 5.2 Tubular Neighborhoods and Nonvanishing Map $G$

#### Lemma A.3
> There exists a family of orthogonal operators $R_t: H \to H$, operator-norm Lipschitz in $t$, such that $R_t u(t) = v(t)$ and $R_t = \text{Id}$ for all $t \le 1$.

*Proof Construction:* Suppressing $t$, let $\kappa = \langle u, v \rangle \ge 0$. Define the operator $A$ and rotation $R_t$ by:

$$A h = v \langle u, h \rangle - u \langle v, h \rangle, \quad R_t = \text{Id} + A + \frac{A^2}{1 + \kappa}$$

The operator $A$ is skew-adjoint on $\text{span}\{u, v\}$ and vanishes identically on its orthogonal complement. Thus $R_t$ is orthogonal, operator-norm Lipschitz, and maps $u(t)$ directly to $v(t)$.

**Cutoff Functions and Map Definition:** Define $b(t) = \min\{a(t), -1/8\}$ and $q(t) = b(t) - a(t)$. This simplifies to:

$$q(t) = -\max\left\{a(t) + \frac{1}{8}, 0\right\}$$

Notice that $q(t)$ vanishes identically for $t \le -1$ (where $a(t) \le -1/8$), guaranteeing that $G(x) = x$ smoothly along the unbounded negative tail of the curve.

Let $\beta, \chi: [0, \infty) \to [0, 1]$ be continuous piecewise-linear cutoffs satisfying:
* $\beta(r) = 1$ for $r \le \rho/4$, dropping linearly to $0$ at $r = \rho/2$.
* $\chi(r) = 1$ for $r \le \rho/2$, dropping linearly to $0$ at $r = \rho$.

Define $G: B \to H$ by $G(x) = x$ outside $U$, and for $x \in B \cap U$:

$$G(x) = x + \beta(r)q(t)v(t) + \chi(r)(R_t - \text{Id})e \quad \text{where } r = \|e(x)\|$$

The map $G$ satisfies three key properties:
1. $G$ is globally Lipschitz on $B$.
2. $G$ is bounded away from zero: $\|G(x)\| \ge \rho/4 > 0$ for all $x \in B$.
3. $G(x) = x$ whenever $\|x\| \ge 1/2$.

### 5.3 Normalization and the $\delta = 1/2$ Bound
Define the normalized map $f: B \to B$ by:

$$f(x) = -\frac{G(x)}{\|G(x)\|}$$

Since normalization on vectors of norm at least $\rho/4$ is Lipschitz with constant $8/\rho$, $f$ is globally Lipschitz on $B$, and $\|f(x)\| = 1$ for all $x \in B$. 

If $\|x\| < 1/2$, then $\|f(x) - x\| \ge 1 - \|x\| > 1/2$. If $\|x\| \ge 1/2$, then $G(x) = x$, giving $\|f(x) - x\| = 1 + \|x\| \ge 3/2$. Thus:

$$\|f(x) - x\| \ge \frac{1}{2} \quad \text{for all } x \in B$$

establishing Lemma 1.2 with exact parameters $\delta = 1/2$ and $L < \infty$.

---

## 6. Companion Results and Consequences

The established nonamenability of Thompson's group $F$ allows direct application of companion results in representation theory and percolation theory.

### 6.1 Uniformly Bounded Representations

#### Corollary 3.1
> For every $\varepsilon > 0$, there exists a separable complex Hilbert space $H$ and a group representation $\pi: F \to GL(H)$ satisfying:
> 
> $$\sup_{g \in F} \|\pi(g)\| \le 1 + \varepsilon$$
> 
> but no bounded invertible operator $S$ on $H$ exists such that $S \pi(g) S^{-1}$ is unitary for all $g \in F$.

*Proof:* Follows by combining Theorem 1.1 with the companion unitarizability theorem for discrete countable nonamenable groups (OpenAI preprint, Sep 23, 2026).

### 6.2 Bernoulli Bond Percolation on Cayley Graphs

#### Corollary 3.2
> Let $S \subset F \setminus \{\text{id}\}$ be any finite symmetric generating set, and let $G_S$ be the associated Cayley graph. In Bernoulli bond percolation on $G_S$:
> 
> 1. The critical connection kernel operator norm satisfies:
>    $$\|T_{p_c}\|_{2 \to 2} < \infty \quad \text{and} \quad p_c < p_{2 \to 2} \le p_u$$
> 2. For each fixed $p \in (p_c, p_u)$, there are almost surely infinitely many infinite open clusters.
> 3. There exist deterministic thresholds $p_c < p_1 < p_2 < 1$ such that in the standard uniform coupling, there are almost surely infinitely many infinite open clusters simultaneously for all $p \in [p_1, p_2]$.

*Proof:* Follows by combining Theorem 1.1 with the companion nonuniqueness percolation result on nonamenable graphs (OpenAI preprint, Sep 24, 2026).

---

## 7. Formal Verification Status

### 7.1 Scope of the Lean Formalization
The nonamenability of Thompson's group $F$ has been formally verified using the Lean interactive theorem prover.

* **Repository Location:** `openai/math` repository (`lean/docs/248.md`).
* **Verified Result:** The formal proof rules out the existence of a positive normalized left-invariant mean on bounded real functions for the standard group of dyadic piecewise-linear homeomorphisms of $[0, 1]$.
* **Comparator File:** Formalized in `ThompsonNonamenability.lean`.
* **Explicit Scope:** The Lean formalization rules out the invariant mean directly without computing explicit numerical boundary constants or fixing a prescribed generating set.

---

## 8. Mathematical Glossary

| Term | Technical Definition |
| :--- | :--- |
| **Amenable Group** | A discrete group $G$ whose bounded real functions $\ell^\infty(G; \mathbb{R})$ admit a positive, normalized, left-invariant linear functional (mean). |
| **Følner Criterion** | A combinatorial characterization of group amenability requiring the existence of finite sets with arbitrarily small relative boundary ratios under translation. |
| **Thompson's Group $F$** | The group of increasing piecewise-linear homeomorphisms of $[0, 1]$ with finitely many linear pieces, dyadic rational breakpoints, and slopes in $2^\mathbb{Z}$. |
| **Basic Dyadic Interval** | An interval of the form $[k 2^{-r}, (k+1) 2^{-r}] \subseteq [0, 1]$ for non-negative integers $r$ and $0 \le k < 2^r$. |
| **Basic Partition** | A finite partition of $[0, 1]$ composed entirely of basic dyadic intervals. |
| **Normalized Restriction** | The partition $T_I = \{s_I^{-1}(K) : K \in T, K \subseteq I\}$ obtained by restricting a partition $T$ to a subinterval $I$ and stretching it affinely back to $[0, 1]$. |
| **Benyamini–Sternfeld Map** | A Lipschitz map $f: B \to B$ on the unit ball of an infinite-dimensional space satisfying a uniform displacement bound $\|f(x) - x\| \ge \delta > 0$. |
| **Elementary Amenable Group** | Member of the smallest class of groups containing all finite and abelian groups that is closed under subgroups, quotients, extensions, and directed unions. |
| **Unitarizable Representation** | A group representation $\pi: G \to GL(H)$ that can be conjugated to a unitary representation via a single bounded invertible operator $S$. |
| **Percolation Thresholds ($p_c, p_u, p_{2 \to 2}$)** | $p_c$: Phase transition threshold for cluster emergence; $p_u$: Threshold for uniqueness of the infinite cluster; $p_{2 \to 2}$: Threshold bound for operator norm boundedness of $T_p$. |