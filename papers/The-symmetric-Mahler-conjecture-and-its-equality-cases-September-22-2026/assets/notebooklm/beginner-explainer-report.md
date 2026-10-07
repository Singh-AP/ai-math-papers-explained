# Solving the Symmetric Mahler Conjecture: A Geometric and Analytic Guide

---

### 1. The Problem: Convex Bodies, Symmetry, Polar Bodies, and Volume Product

In convex geometry and geometric functional analysis, the study of geometric invariants under linear transformations provides deep insights into the structural properties of space. Centered at the heart of this discipline is the **volume product** and the long-standing **Mahler Conjecture**.

* **Convex Body:** A **convex body** $K \subset \mathbb{R}^n$ is defined as a compact, convex subset of $n$-dimensional Euclidean space with a non-empty interior.
* **Origin-Symmetry:** A convex body $K$ is **origin-symmetric** if $K = -K$. For every origin-symmetric convex body, the origin $0 \in \mathbb{R}^n$ is an interior point.
* **Polar Body:** Given a convex body $K$, its **polar body** $K^\circ$ is defined by:
  $$K^\circ = \{y \in \mathbb{R}^n : \langle x, y \rangle \le 1 \text{ for all } x \in K\}$$
  By convex separation, taking the dual of the polar body yields the original body ($K^{\circ\circ} = K$), establishing a canonical duality between $K$ and $K^\circ$.

#### Concrete 2D Illustrative Examples
* **The Unit Square and Cross-Polytope:** Consider the two-dimensional hypercube (unit square) $K = [-1,1]^2$. Its polar dual $K^\circ$ is the cross-polytope (diamond) given by $K^\circ = \text{conv}(\pm e_1, \pm e_2) = \{y \in \mathbb{R}^2 : |y_1| + |y_2| \le 1\}$.
* **The Unit Disk:** The Euclidean unit disk $B_2^2 = \{x \in \mathbb{R}^2 : x_1^2 + x_2^2 \le 1\}$ is self-polar under the standard Euclidean inner product, satisfying $(B_2^2)^\circ = B_2^2$.

#### The Volume Product and Linear Invariance
The **volume product** (or Mahler volume) of a convex body $K \subset \mathbb{R}^n$ is defined as:
$$P(K) = |K||K^\circ|$$
where $|K|$ denotes the $n$-dimensional Lebesgue volume of $K$. 

A fundamental property of the volume product is its **linear invariance**. For any invertible linear transformation $T \in \text{GL}(n, \mathbb{R})$, the transformation rules for volume yield $|TK| = |\det T||K|$ and $(TK)^\circ = T^{-\text{T}} K^\circ$, which implies $|(TK)^\circ| = |\det T|^{-1}|K^\circ|$. Consequently, the reciprocal determinant factors cancel exactly:
$$P(TK) = |TK||(TK)^\circ| = |\det T| |K| \cdot |\det T|^{-1} |K^\circ| = |K||K^\circ| = P(K)$$

#### Baseline Values and Extremal Bounds
* **2D Square / Diamond:** $|K| = 4$, $|K^\circ| = 2 \implies P(K) = 8 = \frac{4^2}{2!}$.
* **2D Disk:** $|B_2^2| = \pi$, $|(B_2^2)^\circ| = \pi \implies P(B_2^2) = \pi^2 \approx 9.8696$.
* **2D Non-symmetric Triangle (Reference):** For a non-symmetric triangle $T \subset \mathbb{R}^2$ centered at its centroid, the volume product equals $\frac{27}{2} = 13.5$ (or $9$ when normalized differently in non-centroid formulations).
* **Upper Bound (Blaschke–Santaló Inequality):** The Blaschke–Santaló inequality states that among all origin-symmetric convex bodies in $\mathbb{R}^n$, the volume product $P(K)$ is maximized *if and only if* $K$ is an ellipsoid (an invertible linear image of the Euclidean unit ball).
* **Lower Bound (Mahler's Symmetric Conjecture):** Kurt Mahler conjectured that $P(K)$ is minimized among origin-symmetric convex bodies by the hypercube $[-1,1]^n$ and its dual cross-polytope, establishing the lower bound:
  $$P(K) \ge \frac{4^n}{n!}$$

#### Hanner Polytopes and Linear Hanner Bodies
The minimizers of the symmetric volume product are not unique; they form a rich recursive family known as **Hanner polytopes**:
1. **Base Case:** A one-dimensional centered nondegenerate interval $H = [-a, a]$ ($a > 0$) is a 1D Hanner polytope.
2. **Recursive Construction:** Given Hanner polytopes $H_1 \subset \mathbb{R}^k$ and $H_2 \subset \mathbb{R}^l$, higher-dimensional Hanner polytopes in $\mathbb{R}^{k+l}$ are formed via:
   * **Cartesian Product ($\ell_\infty$-sum):** $H_1 \oplus_\infty H_2 = H_1 \times H_2$
   * **Convex Hull Join ($\ell_1$-sum):** $H_1 \oplus_1 H_2 = \text{conv}\left((H_1 \times \{0\}) \cup (\{0\} \times H_2)\right)$

A **linear Hanner body** is any convex body $K \subset \mathbb{R}^n$ obtained as an invertible linear image $K = T(H)$ of a Hanner polytope $H$.

---

### 2. Historical Context & Prior Progress

#### Origins
Kurt Mahler introduced the volume product problem in 1938–1939 in connection with the geometry of numbers and transference theorems in lattice theory. He proved the sharp lower bound in two dimensions, showing that $P(K) \ge 8$ for all symmetric planar bodies.

#### Low Dimensions & Special Structural Classes
* **Two Dimensions:** Mahler (1938) established the planar lower bound. Reisner (1986) subsequently characterized all planar equality cases as parallelograms.
* **Three Dimensions:** Iriyeh and Shibata (2020) proved the 3D symmetric conjecture. Fradelizi et al. (2022) provided a simplified proof utilizing equipartition techniques alongside stability results. Chen, Li, Xi, and Xu (2026) introduced an alternative proof via shadow-flow deformations.
* **Unconditional Bodies:** Saint-Raymond (1981) proved the sharp inequality for unconditional convex bodies (bodies invariant under coordinate sign changes). Meyer and Reisner (1986, 1987) identified the equality cases within this class as Hanner polytopes.
* **Zonoids:** Reisner (1985, 1986) established the sharp inequality for zonoids (Hausdorff limits of Minkowski sums of line segments), demonstrating that equality requires $K$ to be a parallelotope. Gordon, Meyer, and Reisner (1988) supplied a direct geometric proof.
* **Local Minimality:** Nazarov, Petrov, Ryabogin, and Zvavitch (2010) proved that the unit hypercube is a strict local minimizer of the volume product in Banach–Mazur distance. Kim (2014) extended local minimality to all Hanner polytopes. Kim and Zvavitch (2015) established local stability in the neighborhood of unconditional bodies.

#### Analytic and Asymptotic Precedents
* **Reverse Blaschke–Santaló Exponential Bounds:** Bourgain and Milman (1987) established the existence of an absolute constant $c > 0$ such that $P(K) \ge c^n \frac{4^n}{n!}$. Kuperberg (2008) provided explicit, stronger exponential bounds using topological Gauss linking integrals.
* **Complex-Analytic & Extremal Frameworks:** Nazarov (2012) employed Hörmander’s $\bar{\partial}$-theorem and Bergman kernel techniques to give an analytic proof of the reverse Blaschke–Santaló inequality. Berndtsson (2021) recast Kuperberg’s proof using complex integral formulas. The search for the conformal mapping $F(z)$ employed in the present resolution was motivated by the symmetric-convex extremal-function framework of Lundin (1985) and Baran, while $F(z)$ itself represents a complex rotation of Renan Gross's (2019) conformal Skorokhod embedding for uniform boundary distributions. Analytical mass estimates on $F(z)$ draw upon Demailly’s (1993) foundational theory of generalized Lelong numbers.
* **Symplectic Approaches:** Karasev (2021) proved the sharp inequality for hyperplane sections and projections of $\ell_p$ balls ($1 \le p \le \infty$) and Hanner polytopes using symplectic volume estimates.

#### Foundations in Normed Space Theory
* **Olof Hanner (1956):** Formulated recursive space constructions and studied ball intersection properties.
* **Åsvald Lima (1978):** Introduced the norm-additive decomposition criterion connecting metric medians to intersection properties of balls in Banach spaces.
* **Allan B. Hansen & Åsvald Lima (1981):** Provided the complete isometric classification theorem for finite-dimensional Banach spaces possessing the 3.2 ball intersection property.

---

### 3. Main Results: Theorem and Functional Corollaries

> **Theorem 1.1 (Symmetric Mahler Theorem)**  
> *For every integer $n \ge 1$ and every origin-symmetric convex body $K \subset \mathbb{R}^n$,*
> $$|K||K^\circ| \ge \frac{4^n}{n!}$$
> *Equality holds if and only if $K$ is a linear Hanner body.*

> **Corollary 1.2 (Even Functional Mahler Inequality)**  
> *For every integer $n \ge 1$ and every even proper lower-semicontinuous convex function $\phi: \mathbb{R}^n \to \mathbb{R} \cup \{+\infty\}$ such that $0 < \int_{\mathbb{R}^n} e^{-\phi(x)} dx < \infty$,*
> $$\left(\int_{\mathbb{R}^n} e^{-\phi(x)} dx\right) \left(\int_{\mathbb{R}^n} e^{-\phi^*(y)} dy\right) \ge 4^n$$
> *where $\phi^*(y) = \sup_{x \in \mathbb{R}^n} \{\langle x, y \rangle - \phi(x)\}$ is the Fenchel–Legendre transform.*

> **Corollary 1.3 (Symmetric Entropy–Transport Inequality)**  
> *For every integer $n \ge 1$, let $\eta_i(dx) = e^{-V_i(x)} dx$ ($i=1,2$) be full-dimensional origin-symmetric log-concave probability measures with proper lower-semicontinuous convex potentials $V_i$ whose densities are essentially continuous. Then their moment measures $\nu_i = (\nabla V_i)_\# \eta_i$ have finite first moments, the relative entropies $H(\eta_i) = -\int V_i d\eta_i$ are finite, and:*
> $$H(\eta_1) + H(\eta_2) \le -n \log(4e^2) + T(\nu_1, \nu_2)$$
> *where $T(\nu_1, \nu_2) = \inf_{f \in \mathcal{F}} \{\int f d\nu_1 + \int f^* d\nu_2\}$ is the optimal transport cost.*

---

### 4. Significance and Impact

* **Resolution of an 88-Year Benchmark:** Completely settles Kurt Mahler's 1938 conjecture for origin-symmetric convex bodies in arbitrary dimensions.
* **Unification of Diverse Mathematical Fields:** Synthesizes techniques across convex analysis, complex analysis (conformal mappings, higher-dimensional Lelong numbers, and Stokes' theorem), and Banach space geometry.
* **Bridge to Functional Inequalities & Transport Theory:** Translates classical geometric volume bounds into precise, dimension-sharp functional inequalities for log-concave functions and optimal transport estimates for moment measures.

---

### 5. Step-by-Step Proof of the Symmetric Mahler Conjecture

#### 5.1 Slab Polytopes & Dual Framing
Consider a bounded polytope $A \subset \mathbb{R}^d$ generated by $m$ nonzero, pairwise nonproportional row vectors $b_1, \dots, b_m$ spanning $(\mathbb{R}^d)^*$:
$$A = \{X \in \mathbb{R}^d : |b_i \cdot X| \le 1, \, 1 \le i \le m\}$$
By bipolarity, its polar dual $C = A^\circ$ is the convex hull of the row vectors and their antipodes:
$$A^\circ = \text{conv}\{\pm b_1, \dots, \pm b_m\}$$

#### 5.2 The Conformal Lens Map & Boundary Law (Lemma 3.1)
Define the complex series mapping on the unit disk $\mathbb{D} = \{z \in \mathbb{C} : |z| < 1\}$:
$$F(z) = \frac{8}{\pi^2} \sum_{j=0}^\infty \frac{(-1)^j z^{2j+1}}{(2j+1)^2}$$
The map $F(z)$ acts as a probability-preserving transducer: it transforms standard angular uniform measure on the complex boundary $\partial \mathbb{D}$ into uniform linear Lebesgue measure along the imaginary axis $[-1,1]$, perfectly matching the height parameterization of slab polytopes.

The mapping $F$ is a biholomorphism from $\mathbb{D}$ onto a bounded convex domain $D \subset \mathbb{C}$ (the planar lens), bounded by $D = \{v + it : |t| \le 1, |v| \le \lambda(t)\}$. The horizontal half-width function $\lambda(t)$ satisfies:
$$\lambda'(t) = -\frac{2}{\pi} \text{arctanh}\left(\sin \frac{\pi t}{2}\right), \quad \lambda''(t) = -\sec \frac{\pi t}{2} < 0$$

**Key Boundary Law:** If $\Theta$ is a uniform random angle on $[0, 2\pi)$, then the boundary image $F(e^{i\Theta})$ obeys the exact probability law:
$$F(e^{i\Theta}) \stackrel{\text{law}}{=} \epsilon \lambda(T) + iT$$
where $T$ is uniformly distributed on $[-1,1]$ and $\epsilon \in \{-1, 1\}$ is an independent uniform sign.

```
(a) Unit Disk Boundary                      (b) Conformal Lens Boundary D
       e^{i\Theta}                                  \epsilon\lambda(T) + iT
         * * *                                            +1 (t=1)
     *           *                                       /  \
    *      \       *               F                    /    \
   *        \       *          --------->              |  \lambda(t_0) |
  *          \ \theta_0 *                              |   <---->    | t_0
   *          *        *                                \           /
     *               *                                   \         /
         * * *                                            -1 (t=-1)
```

#### 5.3 Feasible Basis Probabilities & Holomorphic Mass Bound (Lemmas 4.1 & 5.1)
Let $\mathcal{B}$ denote the collection of all $d$-element subsets $I \subset \{1, \dots, m\}$ corresponding to linearly independent row sets $B_I = (b_i)_{i \in I}$. 
1. For independent uniform angles $\theta_i$, solve $b_i Z = F(e^{i\theta_i})$ ($i \in I$) for the complex vector $Z_I(\theta) \in \mathbb{C}^d$.
2. Define $P_I$ as the probability that $Z_I(\theta)$ satisfies all remaining row constraints:
   $$P_I = \mathbb{P}\left\{b_j Z_I(\theta) \in \overline{D} \text{ for all } 1 \le j \le m\right\}$$
3. **Holomorphic Mass Lemma & Radial Rescaling (Lemma 4.1 & 5.1):** Apply Stokes' theorem to the form $(dd^c \tau)^d$ for high powers $k$ of the inverse map $g = F^{-1}$, where $\tau_k = \sum_{j=1}^m |g(b_j z)|^{2k}$. This yields a mass bound scaling as $(k\pi)^d / d!$:
   $$M_{I,k} := \int_{\{\tau_k < 1\}} \left| \det \frac{\partial(h_i^k)_{i \in I}}{\partial(z_1, \dots, z_d)} \right|^2 dV_{2d}(z)$$
   To evaluate this as $k \to \infty$, make the explicit radial substitution $u_i = \rho_i^{1/k} e^{i \theta_i}$ ($i \in I$), where $u_i = h_i(z) = g(b_i z)$. The Jacobian transformation identity $k^2 |u_i|^{2k-2} dV_2(u_i) = k \rho_i d\rho_i d\theta_i$ introduces a factor of $k^d \prod_{i \in I} \rho_i d\rho_i d\theta_i$. This $k^d$ factor identically cancels the $k^d$ growth rate in $M_{I,k}$:
   $$\limsup_{k \to \infty} \frac{M_{I,k}}{k^d} \le \frac{\pi^d}{d!} P_I$$
   Summing over all independent bases $I \in \mathcal{B}$ establishes the fundamental analytic bound:
   $$S = \sum_{I \in \mathcal{B}} P_I \ge 1$$

#### 5.4 The Real Simplex Identity & Upper Bound (Proposition 6.1)
Using the uniform distribution of the imaginary coordinate $T = b_i \cdot X$, the complex probability sum $S$ transforms exactly into a real integral over unions of feasible simplices $\Sigma_X \subset A^\circ$:
$$1 \le S = \frac{d!}{4^d} \int_A |\Sigma_X| dX \le \frac{d!}{4^d} |A||A^\circ|$$
where $\Sigma_X = \bigcup_{(I,\epsilon) \text{ feasible at } X} \text{conv}\left(0, \{\epsilon_i b_i\}_{i \in I}\right)$.

This proves the fundamental inequalities:
$$|A||A^\circ| \ge \frac{4^d}{d!}$$
$$\int_A \left(|A^\circ| - |\Sigma_X|\right) dX = |A||A^\circ| - \frac{4^d}{d!} S \le |A||A^\circ| - \frac{4^d}{d!}$$

#### 5.5 Cube Sanity Check & Missing Volume Breakdown
For the $d$-dimensional hypercube $A = [-1,1]^d$, the polar $A^\circ$ is the cross-polytope $\text{conv}(\pm e_1, \dots, \pm e_d)$. There is a single basis $I = \{1, \dots, d\}$, and for every $X \in \text{int}(A)$, all $2^d$ sign choices are feasible. The $2^d d!$ feasible simplices perfectly tile $A^\circ$ without overlap, yielding $S = 1$ and zero missing volume $|\Sigma_X| = |A^\circ|$, confirming $|A||A^\circ| = \frac{4^d}{d!}$.

Conversely, missing volume $|A^\circ \setminus \Sigma_X| > 0$ arises whenever redundant row constraints are present. Consider the 2D planar setup with rows $b_1 = (1, 0)$, $b_2 = (1/2, \sqrt{3}/2)$, and $b_3 = b_2 - b_1 = (-1/2, \sqrt{3}/2)$, forming a polar regular hexagon $C = \text{conv}\{\pm b_1, \pm b_2, \pm b_3\}$. At the point $X = 0.9(1, 1/\sqrt{3})$, we have $b_1 \cdot X = b_2 \cdot X = 0.9$ and $b_3 \cdot X = 0$. Writing $a = \lambda(0.9)$, the lens width satisfies $2a < \lambda(0)$, rendering the third strip $|b_3 \cdot Y| \le \lambda(0)$ strictly redundant in $L_X$. As a result, the four feasible vertex witnesses $Y_{\epsilon_1 \epsilon_2}$ defined by $b_1 Y = \epsilon_1 a$ and $b_2 Y = \epsilon_2 a$ generate only the sub-diamond $\Sigma_X = \text{conv}\{\pm b_1, \pm b_2\}$. The remaining two triangular caps of $C$ adjacent to $\pm b_3$ are omitted, leaving a missing volume $|C \setminus \Sigma_X| = \sqrt{3}/2 > 0$ (one third of the total polar area $|C| = 3\sqrt{3}/2$).

```
(a) Feasible Witnesses in L_X                   (b) Feasible Simplices in C = A^\circ
         b_2 Y = a                                             b_3          b_2
      Y_{-+} +---------+ Y_{++}                                 *----------*
            /         /                                        / \  ++    / \
           /   L_X   /                                        /   \      /   \
          /         /  b_1 Y = a                       -b_1  *-----\0---/----*  b_1
  Y_{--} +---------+ Y_{+-}                                   \     \  +-/   /
   max |b_3 Y| = 2a < \lambda(0)                               \  -- \  /   /
                                                                *----------*
  a = \lambda(0.9)                                            -b_2         -b_3
                                                      \Sigma_X = conv{\pm b_1, \pm b_2}
                                                      |C \ \Sigma_X| = \sqrt{3}/2
```

#### 5.6 Approximation of General Convex Bodies
For an arbitrary origin-symmetric convex body $K \subset \mathbb{R}^n$, choose a sequence of inner polytopes $Q_j \subset K^\circ$ constructed from fine nets converging to $K^\circ$ in Hausdorff distance. Setting $A_j = Q_j^\circ$, the polar inclusions $(1-\delta_j) K \subset A_j^\circ \subset K$ yield $|A_j| \to |K|$ and $|Q_j| \to |K^\circ|$. Applying the polytope inequality to $A_j$ and taking $j \to \infty$ proves:
$$|K||K^\circ| \ge \frac{4^n}{n!}$$

#### 5.7 Equality Classification & Dimension Lifting
To classify equality cases, lift $K \subset \mathbb{R}^n$ to dimension $d = n+1$ by constructing:
$$B = K \oplus_1 [-1,1] \subset \mathbb{R}^{n+1}, \quad C = B^\circ = K^\circ \times [-1,1]$$

1. **Volume Ratio Calculation:** The volume of the lifted body $B$ and its polar $C$ satisfy exact multiplicative relationships:
   $$|B| = |K| \int_{-1}^1 (1 - |s|)^n ds = \frac{2|K|}{n+1}, \quad |C| = 2|K^\circ|$$
   Multiplying these volumes yields:
   $$|B||C| = \frac{4}{n+1} |K||K^\circ| = \frac{4^{n+1}}{(n+1)!} \iff |K||K^\circ| = \frac{4^n}{n!}$$
2. **Vanishing Missing Volume:** If $P(K) = \frac{4^n}{n!}$, then $P(B) = \frac{4^{n+1}}{(n+1)!}$, and the integrated missing volume $\int_B (|C| - |\Sigma_X|) dX$ vanishes identically.
3. **Common Feasibility Witness:** For every $X \in \text{int}(B)$ and direction $\xi = (q, a)$, Proposition 7.1 constructs a common witness vector $Y \in \mathbb{R}^{n+1}$ minimizing the lens representation cost.
4. **Endpoint Asymptotics & Support Function Inequality:** Evaluating representation costs as $X_\delta = (\delta u, 1-\delta) \in \text{int}(B)$ approaches the apex $(0, 1)$ utilizes the lens width asymptotic (Lemma 3.2: $\lambda(1-\eta) = \frac{2}{\pi}\eta \log(1/\eta) + O(\eta)$). For $b \in Q$ and $\sigma \in \{-1, 1\}$, evaluating $\lambda(\langle (b, \sigma), X_\delta \rangle) = \lambda(1 - \delta(1 - \sigma \langle b, u \rangle))$ yields:
   $$\langle x+y, u \rangle \le h_{D_0}(u) + s - p \quad \text{for all } u \in K$$
   where $D_0 = \{r_+ - r_- : r_+ + r_- = x - y, \|r_+\| \le A_+, \|r_-\| \le A_-\}$, $p = \|x-y\|$, $s = \|x\| + \|y\|$, and $c = (s-p)/2$.
5. **Convex Separation to Metric Medians:** Applying convex separation to the support function bound proves $x+y \in D_0 + (s-p)Q$. Constructing $m = x - r_+ = y + r_-$ shows that every triple of points $x_0, x_1, x_2 \in (\mathbb{R}^n, p_{K^\circ})$ possesses a **metric median** $m \in \mathbb{R}^n$ satisfying:
   $$\|x_i - x_j\|_{p_{K^\circ}} = \|x_i - m\|_{p_{K^\circ}} + \|m - x_j\|_{p_{K^\circ}} \quad (0 \le i < j \le 2)$$
6. **Ball Intersection Property & Final Structure:** By Lemma 8.2, the existence of metric medians implies that $(\mathbb{R}^n, p_{K^\circ})$ has the **3.2 ball intersection property** (any three pairwise-intersecting closed balls share a common point). Applying the **Hansen–Lima Theorem (Theorem 8.3)** proves that $(\mathbb{R}^n, p_{K^\circ})$ is linearly isometric to a combination of $\ell_1$ and $\ell_\infty$ sums of $\mathbb{R}$. Consequently, $K^\circ$ (and thus $K$) is a linear Hanner body.

---

### 6. Key Contributors & Figures

| Mathematician | Conceptual Contribution |
| :--- | :--- |
| **Kurt Mahler** | Formulated the volume product problem and conjecture (1938–1939). |
| **Olof Hanner** | Recursively defined Hanner polytopes and Hanner spaces (1956). |
| **Åsvald Lima & Allan B. Hansen** | Established the norm-additive decomposition criterion (1978), the 3.2 ball intersection property, and the structure classification of finite-dimensional Banach spaces (1981). |
| **Shlomo Reisner** | Characterized volume product minimizers and equality cases for zonoids, 2D parallelograms, and unconditional bodies (1985–1987). |
| **Jean Bourgain & Vitali Milman** | Established the reverse Blaschke–Santaló exponential lower bounds ($c^n \frac{4^n}{n!}$) (1987). |
| **Greg Kuperberg** | Proved explicit exponential bounds using topological Gauss linking integrals (2008). |
| **Fedor Nazarov** | Introduced complex-analytic Hörmander $\bar{\partial}$-methods (2012) and strict local minimality of the cube (2010). |
| **Hiroshi Iriyeh & Masataka Shibata** | Resolved the 3D symmetric Mahler conjecture (2020). |
| **Matthieu Fradelizi et al. / Shibing Chen et al.** | Developed equipartition proofs, stability results, and shadow-flow deformations (2022, 2026). |

---

### 7. Scope, Limits, Formalization Status, and Caveats

* **Unreviewed Preprint Status:** The proof presented in the underlying text is sourced from AI-generated OpenAI preprints dated 22 September 2026. These manuscripts represent newly released results that have not undergone formal academic peer review.
* **Separation from the Nonsymmetric Companion Paper:** The symmetric Mahler conjecture proved here relies fundamentally on origin-symmetry ($K = -K$). The general nonsymmetric Mahler conjecture (minimizing $|K||(K-z)^\circ|$ with lower bound $\frac{(n+1)^{n+1}}{(n!)^2}$ achieved uniquely by simplices) is resolved in a separate companion paper using a completely distinct methodology.
* **Lean Formalization Scope (`openai/math` repository):**
  * **Symmetric Inequality & Equality:** Fully formalized in `MahlerConjecture.lean` ($\ge \frac{4^n}{n!}$) and `SymmetricMahlerEquality.lean` (linear Hanner characterization).
  * **General Nonsymmetric & Symplectic Scope:** `GeneralMahler.lean` formalizes the general nonsymmetric bound. `SymmetricPolar.lean` formalizes the symplectic capacity / Gromov width of $\text{int } K \times \text{int } K^\circ$ for origin-symmetric bodies $K \subset \mathbb{R}^n$ ($n \ge 2$), proving it equals $4$ (with ball capacity normalized as $\pi r^2$) and establishing that every ball of capacity $0 < c < 4$ embeds symplectically into it (an embedding at capacity exactly 4 is not asserted).
  * **Not Formalized:** The functional extensions (Corollary 1.2 and Corollary 1.3) fall outside the Lean formalization scope.
  * **Catalog Status:** The Lean formalization catalog review status for these entries is marked as `'unchecked'`.

---

### 8. Technical Glossary

* **Convex Body:** A compact, convex subset $K \subset \mathbb{R}^n$ with a non-empty interior.
* **Polar Body ($K^\circ$):** The dual convex body defined by $K^\circ = \{y \in \mathbb{R}^n : \langle x, y \rangle \le 1 \text{ for all } x \in K\}$.
* **Volume Product ($P(K)$):** The linear invariant product $P(K) = |K||K^\circ|$, where $|\cdot|$ denotes $n$-dimensional Lebesgue volume.
* **Hanner Polytope:** A convex polytope constructed recursively from 1D centered intervals using Cartesian products ($\ell_\infty$-sums) and convex hull joins ($\ell_1$-sums).
* **Linear Hanner Body:** Any convex body formed as an invertible linear image $T(H)$ of a Hanner polytope $H$.
* **Planar Lens ($D$):** The bounded convex complex domain image of the unit disk under $F(z) = \frac{8}{\pi^2}\sum_{j=0}^\infty \frac{(-1)^j z^{2j+1}}{(2j+1)^2}$, possessing a uniform boundary imaginary coordinate distribution.
* **Metric Median:** A point $m$ in a normed space satisfying $\|x_i - x_j\| = \|x_i - m\| + \|m - x_j\|$ for all pairs in a triple $(x_0, x_1, x_2)$.
* **3.2 Intersection Property:** The geometric property of a normed space wherein any three pairwise-intersecting closed balls share at least one common point.
* **Fenchel–Legendre Transform:** The convex conjugate function defined by $\phi^*(y) = \sup_{x \in \mathbb{R}^n} \{\langle x, y \rangle - \phi(x)\}$.