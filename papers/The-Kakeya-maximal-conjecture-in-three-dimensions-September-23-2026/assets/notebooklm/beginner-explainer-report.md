# Resolving the Four-Dimensional Kakeya Conjecture: A Calculus-Level Guide to the OpenAI Preprints

---

### 1. The Needle Problem and Besicovitch Sets

The Kakeya needle problem, first posed by Soichi Kakeya in 1917, asks a deceptively simple question in geometric measure theory: *What is the minimum Lebesgue measure (area) of a region in the Euclidean plane $\mathbb{R}^2$ within which a needle of length 1 can be continuously turned by $360^\circ$ (or $180^\circ$ to reverse its endpoints)?*

Kakeya intuitively expected that a symmetric convex figure, such as a deltoid or a circle, would prescribe a rigid non-zero lower bound on the required area. However, in 1919, Abram Besicovitch proved that no positive minimal area exists: a unit line segment can be continuously rotated inside a planar domain of **arbitrarily small Lebesgue measure** $\epsilon > 0$. By systematically splitting, translating, and overlapping triangular fragments, Besicovitch subsequently demonstrated that there exist sets of **zero Lebesgue measure** ($\lambda(K) = 0$) containing a unit line segment in every spatial direction. Such sets are formally termed *Kakeya sets* (or *Besicovitch sets*).

> **Key Conceptual Milestones**
>
> * **Kakeya Needle Problem (1917):** Posed the problem of identifying the minimal-area planar region required to continuously rotate a unit needle.
> * **Besicovitch Construction (1919):** Demonstrated that planar sets containing a unit line segment in every direction can have arbitrarily small—and ultimately zero—Lebesgue measure.
> * **Formal Definition of a Kakeya Set:** A subset $K \subset \mathbb{R}^n$ is a Kakeya set if for every unit vector $e \in S^{n-1}$, there exists an origin point $a_e \in \mathbb{R}^n$ such that the line segment $\{a_e + t e : 0 \le t \le 1\} \subset K$.
> * **Davies's Theorem (1971):** Roy Davies established that despite having zero Lebesgue measure, any Kakeya set $K \subset \mathbb{R}^2$ must be geometrically complex enough to have full Hausdorff dimension ($\dim_H K = 2$).

---

### 2. Measuring Geometric Complexity: Minkowski vs. Hausdorff Dimension

When a set $K \subset \mathbb{R}^n$ has Lebesgue measure zero ($\lambda_n(K) = 0$), standard integration cannot distinguish between a smooth lower-dimensional surface and a dense, highly chaotic fractal object. To quantify fine spatial complexity, geometric measure theory introduces fractal dimensions built on limiting operations ($\lim_{\delta \to 0^+}$).

#### Minkowski (Box-Counting) Dimension
For a bounded set $K \subset \mathbb{R}^n$, cover $K$ using a rigid, uniform grid of hypercubes or boxes of fixed side length $\delta > 0$. Let $N(\delta)$ denote the minimum number of such uniform $\delta$-boxes needed to overlap $K$ completely. The upper Minkowski (box-counting) dimension evaluates spatial complexity across a rigid scale $\delta$:

$$\dim_{\text{Minkowski}}(K) = \limsup_{\delta \to 0^+} \frac{\log N(\delta)}{-\log \delta}$$

#### Hausdorff Dimension
Hausdorff dimension provides a far more subtle geometric metric by relaxing the constraint of uniform box grids. Let $\{U_i\}$ be a countable cover of $K$ composed of arbitrary spatial sets of variable diameters $\operatorname{diam}(U_i) \le \delta$. For a dimension parameter $s \ge 0$, the $s$-dimensional Hausdorff content at resolution scale $\delta$ is defined by:

$$H^s_\delta(K) = \inf \left\{ \sum_{i} (\operatorname{diam} U_i)^s : K \subset \bigcup_{i} U_i, \, \operatorname{diam}(U_i) \le \delta \right\}$$

Taking the limit as the cover resolution vanishes yields the $s$-dimensional Hausdorff measure:

$$H^s(K) = \lim_{\delta \downarrow 0} H^s_\delta(K)$$

The exact critical threshold where $H^s(K)$ drops from $\infty$ to $0$ defines the Hausdorff dimension:

$$\dim_H K = \inf \{ s \ge 0 : H^s(K) = 0 \}$$

Crucially, Hausdorff dimension requires **no compactness, measurability, or structural regularity assumptions** on $K$ or its witnessing line family.

#### Concrete Worked Example: $S = \{0, 1, 1/2, 1/3, 1/4, \dots\} \subset \mathbb{R}$
Consider the countable set $S \subset \mathbb{R}$ consisting of the origin together with the harmonic sequence.

1. **Minkowski Dimension ($\dim_{\text{Minkowski}} S = 1/2$):**
   Cover $S$ using uniform grid intervals of fixed length $\delta > 0$:
   * For points $1/k \ge \sqrt{\delta}$ (corresponding to $k \le 1/\sqrt{\delta}$), the spatial gap between adjacent points exceeds $\delta$:
     $$\frac{1}{k} - \frac{1}{k+1} = \frac{1}{k(k+1)} \approx \frac{1}{k^2} \ge \delta$$
     These isolated points cannot share a single box and force a uniform cover count of $N_1(\delta) \approx \frac{1}{\sqrt{\delta}}$ distinct intervals.
   * The remaining tail of points residing in the cluster $[0, \sqrt{\delta}]$ accumulates around the origin $0$. Covering this continuous interval of length $\sqrt{\delta}$ requires $N_2(\delta) \approx \frac{\sqrt{\delta}}{\delta} = \frac{1}{\sqrt{\delta}}$ uniform intervals.
   * The total uniform box count scales as $N(\delta) = N_1(\delta) + N_2(\delta) \sim \delta^{-1/2}$. Evaluating the limit formula yields:
     $$\dim_{\text{Minkowski}}(S) = \lim_{\delta \to 0^+} \frac{\log (\delta^{-1/2})}{-\log \delta} = \frac{1}{2}$$

2. **Hausdorff Dimension ($\dim_H S = 0$):**
   Because Hausdorff covers permit variable diameters, fix $s > 0$ and an arbitrary small threshold $\epsilon > 0$. Select an interval $U_0 = [0, \epsilon_0]$ of diameter $\epsilon_0 = \min(\delta, \epsilon)$ to cover the accumulation point $0$. For each harmonic point $1/k$, assign a targeted interval $U_k$ centered at $1/k$ with variable diameter $\epsilon_k = \frac{\epsilon}{2^k}$. For sufficiently small $\epsilon$, every cover element satisfies $\operatorname{diam}(U_k) \le \delta$.
   Summing the $s$-dimensional diameters yields:
   $$H^s_\delta(S) \le \sum_{k=0}^\infty (\operatorname{diam} U_k)^s = \epsilon_0^s + \sum_{k=1}^\infty \left( \frac{\epsilon}{2^k} \right)^s = \epsilon_0^s + \epsilon^s \sum_{k=1}^\infty \frac{1}{2^{ks}}$$
   Taking the limit as $\epsilon \to 0^+$ causes this sum to vanish entirely for any $s > 0$. Consequently, $H^s(S) = 0$ for all $s > 0$, establishing that $\dim_H S = 0$. Uniform grid covers are forced to waste count elements over empty space near accumulation points, whereas variable Hausdorff covers compress isolated cluster points efficiently.

| Dimension Metric | Covering Geometry | Scale Constraint | Sensitivity to Accumulation Points |
| :--- | :--- | :--- | :--- |
| **Minkowski Dimension** | Rigid spatial grid ($N(\delta)$ boxes) | Uniform scale $\delta$ across all elements | High (artificially inflated by local point accumulation) |
| **Hausdorff Dimension** | Countable arbitrary sets $\{U_i\}$ | Variable scale $\operatorname{diam}(U_i) \le \delta$ | Low (captures fine spatial distribution without grid artifacts) |

---

### 3. Tubes, Shadings, and the Kakeya Maximal Function

To translate spatial segment overlaps into functional analysis, geometric measure theory models thin neighborhoods around line segments as cylindrical tubes and formulates spatial density averages via maximal operators.

#### Cylindrical Tubes and the Maximal Operator
Let $a \in \mathbb{R}^n$ represent a spatial origin, and let $e \in S^{n-1}$ be a direction vector on the unit sphere. A **$\delta$-tube** $T_\delta(a, e) \subset \mathbb{R}^n$ is a cylinder of length $1$ and transverse radius $\delta > 0$ centered at $a$ along the axis $e$:

$$T_\delta(a, e) = \{ x \in \mathbb{R}^n : |(x - a) \cdot e| \le 1/2, \, |(x - a) - ((x - a) \cdot e) e| \le \delta \}$$

*Annotated Variables:*
* $a \in \mathbb{R}^n$: Spatial offset vector fixing the tube center.
* $e \in S^{n-1}$: Unit vector defining the longitudinal direction axis of the cylinder.
* $\delta > 0$: Transverse radius specifying the narrow spatial thickness of the tube.
* $(x - a) \cdot e$: Longitudinal coordinate projecting $x$ along the primary direction vector $e$.
* $(x - a) - ((x - a) \cdot e) e$: Transverse vector component orthogonal to the directional axis $e$.

The **Kakeya maximal operator** $K_\delta f(e)$ measures the maximum average concentration of a locally integrable density function $f \in L^1_{\text{loc}}(\mathbb{R}^n)$ across any $\delta$-tube oriented in direction $e$:

$$K_\delta f(e) = \sup_{a \in \mathbb{R}^n} \frac{1}{|T_\delta(a,e)|} \int_{T_\delta(a,e)} |f(x)| \, dx$$

*Annotated Variables:*
* $e \in S^{n-1}$: Direction vector on the unit sphere indexing the operator.
* $a \in \mathbb{R}^n$: Translation vector maximizing the directional integral over $\mathbb{R}^n$.
* $|T_\delta(a,e)|$: $n$-dimensional Lebesgue volume of the cylinder $T_\delta(a,e)$, proportional to $\delta^{n-1}$.
* $f(x)$: Non-negative spatial test function (shading density) evaluated across $x \in \mathbb{R}^n$.

#### The Kakeya Maximal Conjecture
The **Kakeya Maximal Conjecture** asserts that for every dimension $n \ge 2$ and every $\epsilon > 0$, there exists a constant $C_{\epsilon, n} > 0$ such that:

$$\|K_\delta f\|_{L^n(S^{n-1})} \le C_{\epsilon, n} \delta^{-\epsilon} \|f\|_{L^n(\mathbb{R}^n)}$$

for all $f \in L^n(\mathbb{R}^n)$ and all scales $0 < \delta < 1$.

*Annotated Variables:*
* $\|K_\delta f\|_{L^n(S^{n-1})}$: $L^n$-norm of the maximal operator integrated over all directions $e \in S^{n-1}$.
* $\|f\|_{L^n(\mathbb{R}^n)}$: $L^n$-norm of the spatial density function $f$ over the domain $\mathbb{R}^n$.
* $C_{\epsilon, n}$: Constant independent of the scale $\delta$ and the shading function $f$.
* $\delta^{-\epsilon}$: Arbitrarily small power-law loss factor capturing multi-scale overlap interactions.

#### Bridging Functional Bounds to Fractal Dimensions
The maximal function bound directly forces lower geometric dimension bounds. Let $K \subset \mathbb{R}^n$ be a Kakeya set, and let $E_\delta = \bigcup_{e \in S^{n-1}} T_\delta(a_e, e)$ be the spatial $\delta$-neighborhood covering its witnessing unit line segments. Test the maximal operator inequality against the characteristic shading function $f = \mathbf{1}_{E_\delta}$:

1. The $L^n$-norm of $f$ evaluates directly to the spatial volume of the neighborhood:
   $$\|f\|_{L^n(\mathbb{R}^n)} = \left( \int_{\mathbb{R}^n} (\mathbf{1}_{E_\delta}(x))^n \, dx \right)^{1/n} = |E_\delta|^{1/n}$$
2. Because each tube $T_\delta(a_e, e)$ is entirely contained within $E_\delta$, the local average inside $T_\delta(a_e, e)$ is identically 1 for every direction $e \in S^{n-1}$:
   $$K_\delta f(e) = \frac{1}{|T_\delta(a_e,e)|} \int_{T_\delta(a_e,e)} 1 \, dx = 1 \implies \|K_\delta f\|_{L^n(S^{n-1})} = \left( \int_{S^{n-1}} 1^n \, de \right)^{1/n} = |S^{n-1}|^{1/n} \sim 1$$

Substituting these identities into the $L^n$ maximal bound yields:

$$1 \le C_{\epsilon, n} \delta^{-\epsilon} |E_\delta|^{1/n} \implies |E_\delta| \ge C_{\epsilon, n}^{-n} \delta^{n\epsilon}$$

As the resolution vanishes ($\delta \to 0^+$), this spatial volume growth constraint forces the covering box count to scale as $N(\delta) \ge c_\epsilon \delta^{-n + n\epsilon}$, establishing that any Kakeya set $K \subset \mathbb{R}^n$ must satisfy both:

$$\dim_{\text{Minkowski}}(K) = n \quad \text{and} \quad \dim_H(K) = n$$

---

### 4. The Principal Paper: The $L^3(\mathbb{R}^3)$ Maximal Bound Uniform in Shading

The principal 3D preprint by OpenAI resolves the analytic formulation of the Kakeya problem in three dimensions by establishing a density-uniform maximal operator bound.

> **Theorem (3D Density-Uniform Kakeya Maximal Bound)**
>
> *For every $\epsilon > 0$, there exists a constant $C_\epsilon < \infty$ such that for all $0 < \delta < 1$ and all $f \in L^3(\mathbb{R}^3)$, the 3D Kakeya maximal operator satisfies:*
>
> $$\|K_\delta f\|_{L^3(S^2)} \le C_\epsilon \delta^{-\epsilon} \|f\|_{L^3(\mathbb{R}^3)}$$
>
> *uniformly in the shading density of $f$.*

> **Why Set Estimates $\neq$ Maximal Function Estimates**
>
> Prior breakthroughs by Wang and Zahl established that 3D Kakeya sets have full Hausdorff dimension 3. However, set-based dimension proofs relied on specific structural assumptions—such as uniform dense-shading conditions, sticky tube families, or power-law bounds $\lambda^{K(\epsilon)}$ on characteristic functions $\mathbf{1}_E$.
>
> In contrast, the $L^3(\mathbb{R}^3)$ Kakeya maximal operator bound must hold for arbitrary, highly irregular test functions $f \in L^3(\mathbb{R}^3)$ containing wild density fluctuations across space. Translating set-based incidence estimates into an $L^3$ operator bound requires controlling multiscale density variations uniformly across all level-set thresholds, preventing high-density spatial hotspots from blowing up global $L^3$ integrability.

---

### 5. Proof Mechanics of the Principal 3D Paper

The principal paper establishes the density-uniform $L^3(\mathbb{R}^3)$ bound through a six-step analytical workflow that combines multiscale geometry, profile constructions, and frame-pinning entropy arguments.

> **Logical Workflow of the 3D Proof**
>
> **Step 1: Line Representation & Marking**
> Index weighted lines with marked time bins across spatial-time mesh grids.
> $\downarrow$
> **Step 2: Critical Exponent & Extremality**
> Define critical exponent $h(p,z)$; establish extremal configurations.
> $\downarrow$
> **Step 3: Local Analytical Tools**
> Apply multilinear Kakeya bounds and planar Furstenberg/planebrush estimates.
> $\downarrow$
> **Step 4: Canonical Profile Construction**
> Parameterize relative density evolution via profile $F(s) = \beta(s - \tau)_+$.
> $\downarrow$
> **Step 5: Coordinate Frame & Pinning**
> Erect frame $(X,Y,U,V)$; enforce product-slope pinning under entropy demand.
> $\downarrow$
> **Step 6: The Final Contradiction**
> Force $h(p,0) = 0$, eliminating non-zero horizon parameters and proving the $L^3$ bound.

#### Detailed Mathematical Steps:

1. **Step 1: Line Representation & Marking:** Parameterize line traces as $x(t) = y_0 + tV$. Spatial-time mesh cells are marked across resolution scales $N_0 \to \infty$ using discrete time bins $J_i$ of length $\rho = D^{-1}$.
2. **Step 2: Critical Exponent & Extremality:** Define an extremal exponent $h(p,z)$ measuring the minimal time-localization cost required to sustain an incidence mass density $p$ and spatial alignment $z$. Extremal configurations isolate configurations where density losses per unit depth approach theoretical upper limits.
3. **Step 3: Local Analytical Tools:** Local spatial incidence mass is bounded using determinant multilinear Kakeya estimates (to control linearly independent direction families) combined with planar Furstenberg / planebrush estimates (to bound concentration along 2D planar structures). *(Note: The 3D weighted full-time plank bound is reserved as a primary spatial input for the 4D reduction).*
4. **Step 4: Canonical Profile Construction:** Local density evolution across normalized depth scales $s$ is reduced to canonical piecewise linear profiles $F(s) = \beta(s - \tau)_+$, tracking logarithmic incidence mass ratios across depth transitions.
5. **Step 5: Coordinate Frame & Pinning:** Erect a four-coordinate frame $(X,Y,U,V)$ along line trajectories. Evaluating two distinct coordinate frames on a single line under an entropy demand forces a product-slope pinning estimate, strictly bounding velocity discrepancies.
6. **Step 6: The Final Contradiction:** The product-slope pinning constraints prevent line configurations from sustaining positive time-localization costs, forcing $h(p,0) = 0$. This eliminates non-zero horizon parameters and establishes the density-uniform $L^3(\mathbb{R}^3)$ bound.

---

### 6. The Companion Paper: $\dim_H(K) = 4$ for Kakeya Sets in $\mathbb{R}^4$

The companion preprint resolves the long-standing four-dimensional Hausdorff Kakeya conjecture for arbitrary sets.

> **Theorem 1.1 (Four-Dimensional Hausdorff Kakeya Theorem)**
>
> *Let $K \subset \mathbb{R}^4$. Suppose that for every unit vector $e \in S^3$, there exists a point $a_e \in \mathbb{R}^4$ such that $\{a_e + te : 0 \le t \le 1\} \subset K$. Then:*
>
> $$\dim_H K = 4$$
>
> *No compactness, measurability, or structural regularity assumption is imposed on $K$ or its witnessing line family.*

#### Setup and Cap Class Reduction
Assume for contradiction that $\dim_H K < 4$. The proof converts a hypothetical Hausdorff deficit $\sigma > 0$ into an exact weighted line problem:

1. **Cap Class $\mathcal{C}(d)$ Parameters:** A Hausdorff deficit $\sigma > 0$ forces the existence of a weighted line problem belonging to cap class $\mathcal{C}(d)$ with exponent $d < 1$. The profile density exponent satisfies $f(L) - f(r) \le d(L - r)$ for depths $0 \le r \le L$. Furthermore, for parameters $S, \eta > 0$ and angular depth $0 < u \le \eta L$, the joint terminal-angular observation density obeys the typical cap ceiling:
   $$\rho_{\text{joint}} \le n(L) N_0^{-Su + o(1)}$$
2. **Formal Horizon $H(E) > 0$:** A *chart* is a collection of line segments in a moving box over time interval $q = N_0^{-h+o(1)}$ maintaining a small quadratic test $P(t,y,w) \le K_0 a_r$. A chart is *true* if its incidence mass divided by interval length meets the spatial density floor up to subpower factors. The **horizon $H(E)$** is formally defined as the infimum of time costs $h \ge 0$ over true terminal systems of substantial coverage ($N_0^{-o(1)}$ incidence mass) in the weighted problem $E$:
   $$H(E) = \inf \{ h \ge 0 : \text{true terminal system at cost } h \text{ has coverage } N_0^{-o(1)} \} > 0$$
3. **3D Weighted Plank Input:** Spatial boxes are supplied with sufficient incidence mass using the 3D weighted full-time plank estimate (Lemma 2.15 / OpenAI [24, Lemma 2.3]), enabling quadratic polynomial local fits.
4. **Chart Framework & Critical Paths:** Nested true charts form linear critical paths governed by time rate $k > 0$ and an optimized narrowness parameter $\ell$.

#### The Three Narrowness Regimes ($\ell$)

The narrowness parameter $\ell$ evaluates how much thinner the minor spatial axis becomes relative to the primary time scale ($q^2/J_c \sim N_0^{-\ell}$). The analytical proof branches into three distinct geometric regimes based on $\ell$:

| Regime | Spatial Geometry | Mathematical Obstruction | Dynamic Resolution Mechanism |
| :--- | :--- | :--- | :--- |
| **$\ell = 0$<br>(Isotropic)** | Isotropic spatial width; broad direction separation across all axes. | Directions concentrate near an exceptional degree-two conic surface, obstructing degree-two polynomial fits. | Construct an algebraic polynomial potential; isolate surviving cubic and quartic terms; encode these terms into a quadratic correction to chart tests, restoring degree-two tests (Proposition 6.8). |
| **$0 < \ell < \infty$<br>(Finite Positive)** | Highly anisotropic; line segments lie in thin planar sheets. | Rigidity forces trajectories into the horizontal model $Y' = -Z + tv$. | Apply affine scalar sheet projections; execute a 3-leg switch at critical rate $2k=1$ (filling 3D base volume); execute a scalar projection bootstrap when $2k \neq 1$. |
| **$\ell = \infty$<br>(Unbounded)** | Extreme narrowness; spatial projection collapses along minor axis. | Normalization introduces large density exponent shifts. | Perform full-time localization across nested true chart labels; project onto scalar models to force time cost $h \to 0$, contradicting $H(E) > 0$. |

#### Dynamic Intuition of the Three Regimes

* **Isotropic Regime ($\ell = 0$):** When direction vectors remain broadly separated, line intersections can concentrate near an exceptional conic section. Standard quadratic chart tests fail because higher-degree algebraic components survive. By interpolating the physical field and enforcing approximate conservativity across switched trajectories, the proof constructs a scalar potential. Surviving cubic and quartic potential terms are re-encoded into the hidden spatial coordinate as quadratic chart corrections, successfully restoring admissible degree-two polynomial tests.
* **Finite Positive Narrowness ($0 < \ell < \infty$):** When spatial width is anisotropic, non-commuting direction vectors force trajectory interactions into the horizontal differential model $Y' = -Z + tv$. The non-abelian geometry forces scalar sheets (analytic branches of algebraic equations) to be affine. At the critical time rate $2k = 1$, a 3-leg trajectory switch sweeps out enough 3D volume to construct an improved chart. Away from this rate ($2k \neq 1$), repeated scalar projections improve trajectory parameters across the entire normalized time interval, returning the system to wide projected intervals.
* **Unbounded Narrowness ($\ell = \infty$):** When narrowness diverges, nested chart labels localize trajectory traces over the entire normalized time interval. Although spatial normalization shifts individual density exponents, these exponent shifts cancel exactly in relative ratio calculations. Projecting onto a scalar model yields chart assignments whose time cost vanishes ($h \to 0$), directly contradicting $H(E) > 0$.

---

### 7. Downstream Geometric Consequences

Section 11 of the companion paper combines $\dim_H K = 4$ with known transfer principles (Keleti–Máthé, Gao et al., Nadjimzadah) to establish major results across geometric measure theory:

* **Packing and Minkowski Dimensions in $\mathbb{R}^4$:** Every Kakeya set $K \subset \mathbb{R}^4$ satisfies full packing dimension $\dim_{\text{packing}} K = 4$. Furthermore, any bounded Kakeya set in $\mathbb{R}^4$ has full upper Minkowski dimension $\dim_{\text{Minkowski}} K = 4$.
* **Projections to Higher Dimensions ($n \ge 4$):** By orthogonally projecting higher-dimensional Kakeya sets onto four-dimensional subspaces, it follows that any Kakeya set $K \subset \mathbb{R}^n$ ($n \ge 4$) satisfies $\dim_H K \ge 4$.
* **Direction Subsets and Line Extensions:** If $E \subset S^3$ is a direction set of Hausdorff dimension $\dim_H E = d \le 3$, any set $K \subset \mathbb{R}^4$ containing unit line segments oriented in every direction of $E$ satisfies $\dim_H K \ge 1 + d$. Additionally, extending unit line segments in $K$ to infinite straight lines preserves $\dim_H = 4$.
* **Nikodym Sets on 4D Constant-Curvature Manifolds ($S^4, \mathbb{H}^4, \mathbb{R}^4$):** A Nikodym set $N \subset M$ on a 4D constant-curvature manifold $M$ is a set where for every $x \in M$, there exists a geodesic segment through $x$ intersecting $N$ in a set whose complement relative to the segment has zero 1D measure. Every Nikodym set on $S^4, \mathbb{H}^4,$ or $\mathbb{R}^4$ has full Hausdorff dimension 4.
* **Curved Kakeya Phase Extensions:** For sets generated by unit segments along smooth curves governed by a fixed translation-invariant phase, the Hausdorff dimension in $\mathbb{R}^4$ is strictly 4.
* **3D Quadratic Space Curve Consequences:** Yields optimal lower bounds for 3D sets containing unit line segments sweeping along families of quadratic space curves.

---

### 8. Current Limits, Open Questions, and Meta-Context

| Established Results | Remaining Open Frontiers |
| :--- | :--- |
| **4D Hausdorff Kakeya Conjecture:** Proved ($\dim_H K = 4$ for any $K \subset \mathbb{R}^4$). | **4D Kakeya Maximal Conjecture:** Open (The $L^4(S^3)$ maximal bound $\|K_\delta f\|_{L^4} \le C_\epsilon \delta^{-\epsilon} \|f\|_{L^4}$ remains unproven). |
| **3D Kakeya Maximal Conjecture:** Proved ($\|K_\delta f\|_{L^3(S^2)} \le C_\epsilon \delta^{-\epsilon} \|f\|_{L^3(\mathbb{R}^3)}$ holds uniformly in density). | **Dimensions $n \ge 5$:** Open (Both the Hausdorff dimension conjecture $\dim_H K = n$ and $L^n$ maximal conjecture remain open for $n \ge 5$). |
| **Unconditional Set Hypothesis:** Proved without compactness,0-measurability, or regularity assumptions. | **Formal Verification Status:** Proofs currently rely on deep, highly complex human/AI analytic arguments spanning hundreds of pages and lack formal machine verification (e.g., Lean). |
| **Preprint Publication Context:** Preprints released by OpenAI on September 24, 2026. | **Peer-Review Status:** Unreviewed preprints currently undergoing rigorous evaluation by the global scientific community. |