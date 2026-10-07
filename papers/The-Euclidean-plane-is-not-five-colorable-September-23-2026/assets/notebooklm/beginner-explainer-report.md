# Explaining the Breakthrough: "The Euclidean plane is not five-colorable"

---

## Section 1: The Problem — Unit Distances, Graphs, and Plane Colorings

The **Hadwiger–Nelson problem** is one of the most famous and easily stated open questions in geometric combinatorics. Stated simply, it asks: *What is the minimum number of colors required to color every point in the two-dimensional Euclidean plane ($\mathbb{R}^2$) such that no two points located at a distance of exactly 1 unit from each other receive the same color?*

An assignment of colors fulfilling this condition is called a **proper $k$-coloring**, where $k$ represents the total number of distinct colors used. Formally, a function $c: \mathbb{R}^2 \to \{1, \dots, k\}$ is a proper $k$-coloring if $c(x) \neq c(y)$ whenever the Euclidean distance between points $x$ and $y$ satisfies $\|x - y\| = 1$. The minimum integer $k$ for which such a coloring exists is defined as the **chromatic number of the plane**, denoted by $\chi(\mathbb{R}^2)$.

```
   Point x (Color 1) ────────────── (Distance = 1) ────────────── Point y (Color 2)
                                (Color 1 ≠ Color 2)
```

To visualize this geometrically, one can view the Euclidean plane as an **infinite unit-distance graph**:
*   **Vertices:** Every individual point $x \in \mathbb{R}^2$ serves as a vertex.
*   **Edges:** An edge connects two vertices if and only if the Euclidean distance between them is exactly 1 unit.
*   **Edge Crossings:** When drawing finite subgraphs of this infinite graph on paper, edges are permitted to cross one another freely without forming a new vertex at their intersection point.

A critical aspect of the classical Hadwiger–Nelson problem is that **no regularity is assumed** for the color classes. A color class $A_i = c^{-1}(\{i\})$ is simply the set of all points assigned color $i$. These sets can be clean geometric shapes (like circles, polygons, or regular tiles), but they can also be arbitrarily wild, scattered, non-measurable sets that completely lack standard notions of length, area, or measure. It is precisely this freedom—allowing "wild" non-measurable sets—that makes proving lower bounds for $\chi(\mathbb{R}^2)$ exceptionally challenging.

> ### Key Concepts
> *   **Proper Coloring:** A function assigning one of $k$ labels to every point in a space such that no two points separated by a specific distance (here, 1 unit) receive the same label.
> *   **Unit-Distance Pair:** Any pair of points $x, y \in \mathbb{R}^2$ satisfying Euclidean distance $\|x - y\| = 1$. In the plane's infinite unit-distance graph, these pairs constitute the edges.
> *   **Chromatic Number $\chi(\mathbb{R}^2)$:** The minimum number of colors required to properly color the infinite unit-distance graph of the Euclidean plane.

---

## Section 2: Historical Background — From 1950 to Modern Obstructions

### Early Foundations (1950–1961)
The problem originated with **Edward Nelson** in 1950. Nelson proved a lower bound of 4 by constructing small finite unit-distance graphs that could not be colored with 3 colors. In the same year, **John Isbell** established an upper bound of 7 by creating an explicit hexagonal tiling of the plane. 

In 1961, **Hugo Hadwiger** published the formulation in a formal journal paper, asking for distance-avoiding coverings and confirming the bounds $4 \le \chi(\mathbb{R}^2) \le 7$.

#### Isbell's Hexagonal 7-Coloring
Isbell's upper bound construction partitions the plane using Voronoi hexagons derived from a triangular lattice. Each hexagon has a circumradius of $r = 2/5 = 0.4$. The centers of neighboring hexagons lie at a distance of $\sqrt{3}r$.

```
         /\          
        /  \          Voronoi Hexagon
       |    |         Circumradius r = 2/5
        \  /          Max interior distance = 2r = 0.8 < 1
         \/
```

The lattice of centers is mapped to a scaled copy of $\mathbb{Z} + \mathbb{Z}\omega$ (where $\omega = e^{2\pi i / 3}$). Scaling this lattice by $2 - \omega$ yields a similar sublattice of index 7, because $|2 - \omega|^2 = 7$. Coloring the hexagon centers according to their 7 lattice cosets, and assigning every point in the plane the color of its enclosing hexagon (with boundary points arbitrarily assigned to any incident hexagon), yields a valid coloring:
1.  **Maximum distance within a single hexagon:** $2r = 4/5 = 0.8 < 1$, guaranteeing that no two points inside the same hexagon are 1 unit apart.
2.  **Minimum distance between distinct same-color hexagons:** The centers of distinct same-color hexagons are at least $\sqrt{21}r$ apart. The distance between points in distinct same-color hexagons is therefore at least $(\sqrt{21} - 2)r \approx (4.582 - 2)(0.4) \approx 1.033 > 1$.

Thus, no two points of the same color are separated by 1 unit, establishing $\chi(\mathbb{R}^2) \le 7$.

#### The Moser Spindle
In 1961, **Leo Moser and William Moser** introduced a 7-vertex finite unit-distance graph now known as the **Moser Spindle**. It consists of two equilateral triangles of side length 1, sharing a common edge $AB$.

```
               T
              / \
             /   \
            A─────B
             \   /
              \ /
               0
               
  (Triangle 0AB and Triangle TAB share edge AB)
  (A rotated copy using vertex u forces 0 and uT to match)
```

In any proper 3-coloring of an equilateral triangle, all 3 vertices must have distinct colors. For two triangles $0AB$ and $TAB$ sharing edge $AB$, the vertices $0$ and $T$ are both forced to take the single remaining color not used on edge $AB$. Thus, $c(0) = c(T)$.

By adding a rotated copy of this structure using an algebraic rotation $u = (5 + i\sqrt{11})/6$ (where $|u| = 1$), the framework forces $c(0) = c(uT)$. However, the construction explicitly places $T$ and $uT$ at a distance of $|T - uT| = 1$. This forces $c(T) \neq c(uT)$, creating an inescapable contradiction:
$$c(0) = c(T) \quad \text{and} \quad c(0) = c(uT) \implies c(T) = c(uT) \quad \text{(Contradiction, since } |T - uT| = 1\text{)}$$
This 7-vertex graph proved that 3 colors are insufficient, establishing the classical lower bound of 4.

### The Compactness Bridge
A pivotal theoretical tool was supplied by **N.G. de Bruijn and Paul Erdős** (1951). They proved using the Axiom of Choice (ZFC) that an infinite graph is $k$-colorable if and only if **every finite subgraph** is $k$-colorable. 

This compactness theorem established a dual path for research:
*   **Constructive path:** Find an explicit finite unit-distance graph that requires $k+1$ colors.
*   **Non-constructive path:** Prove abstractly that no proper $k$-coloring of the infinite plane can exist, which implicitly guarantees the existence of a finite non-$k$-colorable subgraph without needing to display it explicitly.

### The Breakthrough to Five Colors (2018–2020)
After a 68-year stalemate at $4 \le \chi(\mathbb{R}^2) \le 7$, **Aubrey de Grey** (2018) constructed an explicit 1,581-vertex finite unit-distance graph that cannot be 4-colored, proving $\chi(\mathbb{R}^2) \ge 5$.

Subsequent efforts drastically reduced the size of this finite obstruction:
*   **Marijn Heule** (2018): Reduced the graph to 553 vertices using SAT solvers and unsatisfiable core extraction.
*   **Jaan Parts** (2020): Reduced the graph to 509 vertices and developed a human-verifiable proof.
*   **Geoffrey Exoo and Dan Ismailescu** (2020): Provided an alternative computer-assisted proof that $\chi(\mathbb{R}^2) \ge 5$.

### Measurable Colorings vs. Arbitrary Colorings
When color classes are restricted to Lebesgue-measurable sets, the problem behaves differently:
*   **K.J. Falconer** (1981) proved that the measurable chromatic number $\chi_m(\mathbb{R}^2) \ge 5$ using measure-theoretic density points and rotations.
*   **M.S. Payne** (2009) demonstrated that the unit-distance graph on $\mathbb{R}^2$ restricted to rational unit displacement vectors is 2-colorable for arbitrary sets, whereas any measurable coloring requires at least 5 colors. This proved that measurable colorings and unrestricted colorings are fundamentally distinct mathematical problems.
*   **Planar Maps and Regular Regions:** Woodall (1973) and Townsend (1981 announcement, 2005 full proof) proved a lower bound of 6 for planar-map colorings. **Sokolov and Voronov** (2025) proved a lower bound of 7 for polygonal colorings in a locally finite map framework using interface exclusion arguments.
*   **Recent Flawed Manuscripts:** A manuscript by Reed (May 14, 2026) claimed $\chi(\mathbb{R}^2) = 7$ using a circle-density argument. However, its proposed strict upper bound of $\pi/3$ on the angular measure of a unit-independent subset of the unit circle fails for the half-open arc $\{e^{it} : 0 \le t < \pi/3\}$, which has angular measure $\pi/3$ but contains no unit pair. Because Reed's formal theorem assumed this density bound as a hypothesis, it did not resolve the open problem.

### Timeline of Bounds on χ(R²)

| Year | Author(s) | Lower Bound | Upper Bound | Key Innovation |
| :--- | :--- | :---: | :---: | :--- |
| **1950** | E. Nelson / J. Isbell | 4 | 7 | Problem formulation; Nelson's 4-color bound; Isbell's 7-color hexagonal tiling. |
| **1951** | N.G. de Bruijn & P. Erdős | 4 | 7 | Graph Compactness Theorem bridging finite subgraphs and infinite graphs in ZFC. |
| **1961** | H. Hadwiger | 4 | 7 | First formal journal publication of the problem and its bounds. |
| **1961** | L. Moser & W. Moser | 4 | 7 | Construction of the 7-vertex Moser Spindle finite obstruction. |
| **1981** | K.J. Falconer | 5 (Measurable) | 7 | Density-point and rotation methods for Lebesgue-measurable colorings ($\chi_m \ge 5$). |
| **2005** | A.B. Townsend | 6 (Planar Maps) | 7 | Repaired planar-map region decomposition lower bound. |
| **2009** | M.S. Payne | 5 (Measurable) | 7 | Proved structural gap between rational-vector graph (2-colorable) and measurable graph ($\ge 5$). |
| **2018** | A. de Grey | 5 | 7 | First finite unit-distance graph requiring 5 colors (1,581 vertices). |
| **2018–2020**| M. Heule / J. Parts | 5 | 7 | SAT-based reduction to 553 vertices (Heule); reduction to 509 vertices and human proof (Parts). |
| **2025** | Sokolov & Voronov | 7 (Polygonal) | 7 | Lower bound of 7 for polygonal colorings in locally finite map frameworks. |
| **2026** | **OpenAI Paper** | **6** | **7** | **Proved $\chi(\mathbb{R}^2) \ge 6$ for arbitrary, unrestricted sets via Ergodic Transfer & Topo-Geometry.** |

---

## Section 3: Main Results of OpenAI (September 23, 2026)

On September 23, 2026, OpenAI published a theoretical breakthrough proving that 5 colors are strictly insufficient to color the Euclidean plane, working entirely within standard ZFC set theory.

> ### Theorem 1.1 (No Proper 5-Coloring)
> The Euclidean plane has no proper five-coloring, even when arbitrary (non-measurable) color classes are allowed. Consequently:
> $$6 \le \chi(\mathbb{R}^2) \le 7$$

To overcome the formidable barrier of non-measurable color classes, the authors introduced a measure-theoretic relaxation called a **Weak Measurable $k$-Coloring**.

### Definition 1.2: Weak Measurable $k$-Coloring
Let $k$ be a positive integer, $S^1 \subset \mathbb{R}^2$ be the unit circle, and $\sigma$ be its normalized arc-length measure ($d\sigma = d\theta / 2\pi$). A Lebesgue measurable function $c: \mathbb{R}^2 \to \{1, \dots, k\}$ with color classes $A_i = c^{-1}(\{i\})$ is a **weak measurable $k$-coloring** if, for every radius $R > 0$:
$$\sum_{i=1}^k \int_{B(0,R)} \int_{S^1} \mathbf{1}_{A_i}(x) \mathbf{1}_{A_i}(x + u) \, d\sigma(u) \, dx = 0$$

*Plain-English Meaning:* A weak measurable coloring allows "bad" monochromatic unit pairs to exist, provided that the set of such pairs has measure zero across spatial positions $x$ and circle directions $u \in S^1$. Modifying the coloring on any spatial Lebesgue null set does not alter this condition at all.

> ### Theorem 1.3 (Transfer of Colorability)
> For every positive integer $k$, in ZFC:
> $$\text{A proper } k\text{-coloring of } \mathbb{R}^2 \text{ exists} \iff \text{A weak measurable } k\text{-coloring of } \mathbb{R}^2 \text{ exists}$$

This bridge establishes that if one can rule out weak measurable $k$-colorings, one simultaneously rules out all arbitrary, non-measurable proper $k$-colorings.

> ### Theorem 1.4 (Impossibility of Weak Measurable 5-Coloration)
> There is no weak measurable five-coloring of the Euclidean plane.

Together, Theorem 1.3 and Theorem 1.4 directly imply Theorem 1.1: an arbitrary 5-coloring would generate a weak measurable 5-coloring (Theorem 1.3), which cannot exist (Theorem 1.4).

### Corollary 1.5: Positive Monochromatic Pair Proportion
As a probabilistic consequence, any 5-coloring of the plane must produce a guaranteed positive minimum proportion $\delta > 0$ of monochromatic unit pairs:
1.  **Existential Constant:** $\delta = 1/m$, where $m = |E(H)|$ is the edge count of a finite unit-distance graph $H$ that is not 5-colorable (guaranteed to exist by de Bruijn–Erdős compactness).
2.  **Invariant-Mean Badness:** For any normalized, left-invariant measure $\mu$ on the isometry group $E(2)$, the badness satisfies:
    $$p_\mu^5(c) := \mu\left(\{T \in E(2) : c(T^{-1}0) = c(T^{-1}1)\}\right) \ge \delta$$
3.  **Needle Frequencies:** For any Lebesgue-measurable 5-coloring with two linearly independent periods, or for general measurable 5-colorings under square-table limits as $R \to \infty$, the probability that a randomly dropped unit needle has monochromatic endpoints is at least $\delta$:
    $$\mathbb{P}(c(A) = c(A+U)) \ge \delta$$

---

## Section 4: Why It Matters — Significance of the Breakthrough

1.  **Resolving a 76-Year-Old Open Question:**
    By proving $\chi(\mathbb{R}^2) \ge 6$, this paper eliminates 5 as a possible chromatic number for the plane, narrowing the open possibilities for $\chi(\mathbb{R}^2)$ to just two integers: **6 or 7**.
2.  **Unifying Measure Theory and Arbitrary Set Theory:**
    Historically, combinatorialists focused on finite subgraphs (de Grey, Heule, Parts) while analysts studied measurable colorings (Falconer, Payne). The **Transfer Theorem (Theorem 1.3)** rigorously unifies these parallel tracks. It establishes that wild, non-measurable colorings contain no secret structural advantages over measurable ones when it comes to avoiding unit-distance constraints.
3.  **Methodological Innovation:**
    The proof creates an unprecedented bridge across distant subfields of mathematics, seamlessly combining:
    *   **Ergodic Theory & Structure Theory:** Furstenberg–Zimmer compact extensions and Følner group averaging over countable isometry groups.
    *   **Harmonic Analysis & Spectral Rigidity:** Unitary representations and rigidity theorems for wild character laws on compact dual groups.
    *   **Geometric Topology:** Planar cover obstructions using the Brouwer fixed-point theorem and continua extraction.
    *   **Geometric Combinatorics:** Interface exclusions and rational geometric placements of small graph obstructions (Moser Spindle).

---

## Section 5: The Proof — Step-by-Step Mathematical Architecture

### High-Level Proof Pipeline

```
┌─────────────────────────────────────────────────────────────────────────┐
│                      Arbitrary Proper 5-Coloring                        │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼  (Step 1: Følner Averaging & Spectral Rigidity)
┌─────────────────────────────────────────────────────────────────────────┐
│              Invariant Probability Measure ν on Dual Group D             │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼  (Theorem 2.3: Haar Rigidity of Wild Characters)
┌─────────────────────────────────────────────────────────────────────────┐
│                      Weak Measurable 5-Coloring Field                   │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼  (Step 2: Smooth Transport & 60° Exclusions)
┌─────────────────────────────────────────────────────────────────────────┐
│             Circle Palettes P_x(e) of Size ≤ 2 Almost Everywhere        │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼  (Step 3: Transition Graphs & Local Finiteness)
┌─────────────────────────────────────────────────────────────────────────┐
│             Closed Locally Finite Locus L of Cyclic Centers             │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼  (Step 4: Brouwer Fixed-Point Cover Obstruction)
┌─────────────────────────────────────────────────────────────────────────┐
│              Common Exclusion Continua K_j Straddling Distance 1         │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼  (Step 5: Geometric Cycle Exhaustions)
┌─────────────────────────┬─────────────────────────┬─────────────────────────┐
│     Length 5 Cycle      │     Length 4 Cycle      │     Length 3 Cycle      │
│ Incompatible 6-step     │ Antipodal split rays &  │ Open 3-label polynomial │
│ angular words           │ parity rule violation   │ region containing Moser │
└───────────┬─────────────┴────────────┬────────────┴────────────┬────────────┘
            │                          │                         │
            └──────────────────────────┼─────────────────────────┘
                                       │
                                       ▼
                            ┌─────────────────────┐
                            │    CONTRADICTION    │
                            │ (No 5-Coloring)     │
                            └─────────────────────┘
```

---

### Step 1: The Transfer (Arbitrary Labels to Measurable Fields)

The goal of Step 1 is to prove **Theorem 1.3** by bridging wild non-measurable colorings and structured measurable fields.

#### High-School Intuition & Mathematical Machinery
*   **The Algebraic Plane:** To perform fair probabilistic sampling, mathematicians restrict the plane to points whose coordinates are real algebraic numbers: $F = \overline{\mathbb{Q}} \cap \mathbb{R}$ and $E = F(i) \subset \mathbb{C}$. Because $E$ is a countable algebraic field, its rotation group $K = \{u \in E : |u| = 1\}$ is amenable. This allows us to take **Følner averages**—think of this as taking fair, uniform probabilistic averages over larger and larger geometric regions of translations and rotations.
*   **Character Groups ($D$) and Harmonics:** The space of all additive characters on $E$ forms a compact group $D = \hat{E}_{\text{disc}}$. Think of characters like fundamental frequency waves or pure musical tones in sound analysis. Ordinary continuous waves form a subspace $C = j(\mathbb{R}^2) \subset D$. "Wild" characters off $C$ represent erratic, non-continuous noise.
*   **Theorem 2.3 (Rigidity of Wild Character Laws):** Any $K$-invariant probability measure $\nu$ on $D$ that places no mass on the continuous subspace $C$ (a "wild" law) must be the uniform **Haar measure** $m_D$. This means wild erratic noise averages out to absolute zero correlation under every nonzero algebraic translation.
*   **Conditional Expectation & Sample Extraction:** Projecting label indicators onto the continuous factor $H_c = L^2(F_c)$ acts as a conditional expectation. This operation preserves nonnegativity and keeps coordinate sums equal to 1 ($\sum p_i = 1$). Extracting joint measurable fields across spatial coordinates yields a **weak measurable $k$-coloring**.
*   **Converse Passage:** Conversely, if a weak measurable coloring exists, **Lemma 4.3** proves that density-one points (points where a single color overwhelmingly dominates a tiny surrounding neighborhood) contain no unit-distance pairs. De Bruijn–Erdős graph compactness then constructs a proper coloring of the entire plane.

---

### Step 2: Angular Palettes and 60-Degree Exclusion

Given a weak measurable 5-coloring, define the **circle trace family** $W_x$ at center $x$. 
*   *Analogy:* Imagine taking a microscopic zoom-in limit of color distributions on unit circles surrounding $x$.
*   The **maximal palette** $P_x(e) \subset \{1, \dots, 5\}$ collects all colors having positive weight at direction $e \in S^1$ in these circle traces.

```
                         R (Rotate by π/3 = 60°)
                             \       /
                              \     /
                               \   /
                                \ /
                                 x  (Center)
                                 
                 P_x(f) ∩ P_x(Rf) = ∅  (Disjoint Palettes)
```

*   **Proposition 5.6 (Palette Size Bound):** At every fixed center $x$, $1 \le |P_x(e)| \le 2$ for almost every direction $e \in S^1$. (Almost every direction on the circle sees at most 2 colors!).
*   **Sixty-Degree Exclusion (Corollary 5.4):** $P_x(f) \cap P_x(R f) = \emptyset$ for almost every direction $f \in S^1$, where $R$ rotates directions by $\pi/3$ ($60^\circ$).
*   **Lemma 5.5 (Separation of Binary Centers):** A center $x$ is *binary* for a pair $\{i_+, i_-\}$ if $P_x(e) \cap \{i_+, i_-\} \neq \emptyset$ almost everywhere. Any two distinct binary centers for the same label pair must be separated by at least an absolute minimum distance $\delta_* > 0$.

---

### Step 3: Transition Graphs and Cyclic Centers

Define the **transition area** $D_{ij}(B, h) = |\{q \in B : (c(q), c(q+h)) \in \{(i,j), (j,i)\}\}|$.

The **transition graph** $\Gamma_x$ is the simple graph on $\{1, \dots, 5\}$ where edge $ij \in \Gamma_x$ if and only if $\limsup_{h \to 0} \frac{D_{ij}(B(x,r), h)}{|h|} > 0$ for all $r > 0$.

*   **Lemma 6.2:** If $ij \in \Gamma_x$, there exists a circle trace $b_{ij} \in W_x$ avoiding both $i$ and $j$ ($b_{ij, i} = b_{ij, j} = 0$). Consequently, $P_x(e) \not\subset \{i, j\}$ almost everywhere.
*   **Theorem 6.5 (Local Finiteness):** The locus of cyclic centers:
    $$L = \{x \in \mathbb{R}^2 : \Gamma_x \text{ contains a cycle}\}$$
    is closed and locally finite (it has finite intersection with any compact subset of $\mathbb{R}^2$).

---

### Step 4: Topological Obstructions and Exclusion Continua

To analyze irregular color boundaries, color indicators are smoothed via disk averages $p_i^\epsilon(q)$, then thresholded to construct normalized probability vectors $q_i^\epsilon(z)$. Outside small core disks surrounding the finite set $L$, these vectors map into the **1-skeleton of the 5-simplex**—which is simply the **complete graph $K_5$** (five vertices with all pairs connected by edges).

```
                      Square Q (Side 10)
     ┌──────────────────────────────────────────────────┐
     │   ● Bn,x1 (Core Disk)                            │
     │                 \                                │
     │                  \ gn (Loop)                     │
     │                   ▼                              │
     │                 (K_5 Complete Graph)             │
     │                                                  │
     │                                 ● Bn,x2          │
     └──────────────────────────────────────────────────┘
```

*   **Brouwer Fixed-Point Cover Obstruction (Lemma 7.5 & 7.6):** 
    *   *Analogy:* Think of stretching a continuous rumpled rubber sheet over a frame with holes. If you try to cover a large square of side 10 with small overlapping patches without covering the holes, the sheet is forced to stretch and loop around at least one hole.
    *   Formally, the Brouwer fixed-point theorem forces the continuous map $g_n$ on the boundary loop of at least one core disk $B_{n,x}$ to be **non-null homotopic** in $K_5$.
*   **Midpoint Extraction & Continua (Lemma 7.7 & Prop 7.1):** A non-null loop contains a simple reduced cycle of length $\ell \in \{3, 4, 5\}$. For each edge midpoint $m_j$ in this cycle, connected components crossing the surrounding annulus yield compact connected sets $K_j \subset B(x, \rho)$ meeting $x$ and $\partial B(x, \rho)$. The open **straddling region**:
    $$\Delta(K_j) = \{z \in \mathbb{R}^2 : \min_{q \in K_j} |z - q| < 1 < \max_{q \in K_j} |z - q|\}$$
    excludes both endpoint colors of edge $j$: $H_{i_j} \cap \Delta(K_j) = \emptyset$ and $H_{i_{j+1}} \cap \Delta(K_j) = \emptyset$.

---

### Step 5: The Geometric Cycle Contradictions

The proof concludes by systematically proving that cycle lengths 5, 4, and 3 are all geometrically impossible.

#### 1. Exclusion of 5-Cycles (Proposition 8.2)
A 5-cycle forces the outer allowed palette sets to consist of two runs of edge signs of lengths 2 and 3. On a 6-position rotation orbit under $R$, palette choices require steps $\varepsilon_j \in \{1, -1\}$ in diagonal indices. Antipodal positions force 3-step sums to equal $\pm 2 \pmod 5$, requiring all 6 steps to have identical signs. However, 6 equal steps cannot close modulo 5, creating an immediate contradiction.

#### 2. Exclusion of 4-Cycles (Proposition 8.5)
A 4-cycle on labels $\{0, 1, 2, 3\}$ with outsider $X$ forces rays to organize into two distinct antipodal pairs of split lines. Modulo antipodes, directions divide into two open arcs where forced diagonals take values $U = \{0, 2\}$ and $V = \{1, 3\}$, with one arc having length $\le \pi/2$. However, adjacent cross-word restrictions force the effective $X$-position parity $h(t)$ to be locally constant, implying $h(t)$ is globally constant on $S^1$. This contradicts the fact that rotation by $\pi/3$ shifts words by one position and reverses parity.

#### 3. Exclusion of 3-Cycles (Proposition 8.10) & The Moser Punchline
For a 3-cycle of triangle labels with two outsiders $X, Y$, Lemma 8.7 proves that the essential boundary of the outsider state divides the circle into 6 alternating sectors of angle $\pi/3$.

In polar coordinates $z = \xi + i\upsilon$, $l = \xi^2 + \upsilon^2$, **Lemma 8.8** defines an open polynomial region:
$$P := \upsilon^2(3\xi^2 - \upsilon^2)^2 < P' := l^3(1 - l/4)(l - 1)^2 \quad (0 < l < 4)$$
*   **Crucial Property 1:** Lemma 8.8 proves that any point $x + z$ in this region is restricted to using **at most 3 colors** (the triangle labels $i_0, i_1, i_2$) almost everywhere.
*   **Crucial Property 2:** The authors place the 7-vertex **Moser Spindle graph** $G = \{0, A, B, T, uA, uB, uT\}$ inside this region via the rigid transform:
    $$z_g = \frac{35 + 12i}{37} \left( g + \frac{-290 + 149i}{250} \right), \quad g \in G$$

```
                                  z_uT
                                  /  \
                                 /    \
                           z_uA /      \ z_T
                             \ /        \ /
                              *──────────*
                             / z_A    z_B \
                            /              \
                           /                \
                          z_0───────────────z_uB
                          
             (All 7 vertices of the Moser Spindle fit strictly 
              inside the open 3-label polynomial region P < P')
```

**Lemma 8.9** provides an exact rational arithmetic verification certifying that all 7 transformed vertices $z_g$ satisfy $P < P'$ and $0 < |z_g|^2 < 4$ strictly. 

#### The Grand Punchline:
1.  Lemma 8.8 forces the open polynomial region $P < P'$ to be **at most 3-colorable**.
2.  Lemma 8.9 verifies that all 7 vertices of the Moser Spindle fit strictly inside this region.
3.  Placing the 7-vertex Moser Spindle inside a 3-color region forces the Moser Spindle to be properly 3-colored.
4.  **Contradiction:** The Moser Spindle is mathematically proven (Moser & Moser, 1961) to have chromatic number 4 (it **cannot** be 3-colored).

This inescapable contradiction proves **Theorem 1.4**, establishing that the Euclidean plane cannot be 5-colored.

---

## Section 6: Key Contributors and People Behind the Ideas

*   **Edward Nelson & John Isbell (1950):** Formulated the problem. Nelson established the lower bound of 4; Isbell established the upper bound of 7 via a Voronoi hexagonal tiling of index 7.
*   **N.G. de Bruijn & Paul Erdős (1951):** Proved the De Bruijn–Erdős Compactness Theorem in ZFC, showing that $k$-colorability of an infinite graph is equivalent to $k$-colorability of all its finite subgraphs.
*   **Hugo Hadwiger (1961):** Published the formal paper defining the problem and its initial $4 \le \chi(\mathbb{R}^2) \le 7$ bounds.
*   **Leo Moser & William Moser (1961):** Constructed the 7-vertex Moser Spindle, providing the standard finite geometric obstruction to 3-colorings.
*   **K.J. Falconer (1981) & M.S. Payne (2009):** Developed density-point and rotation techniques for Lebesgue-measurable colorings ($\chi_m \ge 5$) and demonstrated the foundational gap between rational-vector subgraphs and measurable colorings.
*   **A.B. Townsend (1981/2005) & Sokolov–Voronov (2025):** Established map and region decomposition lower bounds (Townsend: 6 for planar maps; Sokolov & Voronov: 7 for polygonal maps using interface exclusions).
*   **Aubrey de Grey (2018):** Broke the 68-year lower-bound stalemate by constructing a 1,581-vertex finite unit-distance graph requiring 5 colors.
*   **Marijn Heule & Jaan Parts (2018–2020):** Reduced the 5-chromatic finite graph to 553 vertices (Heule) and 509 vertices / human proof (Parts).
*   **OpenAI Authors (September 23, 2026):** Proved the Ergodic Transfer Theorem (Theorem 1.3) and eliminated 5-colorings of the plane (Theorem 1.1 & 1.4), proving $6 \le \chi(\mathbb{R}^2) \le 7$.

---

## Section 7: Limitations, Context, and Open Questions

1.  **Chromatic Number Remains Unresolved ($6$ vs $7$):**
    While the paper proves $\chi(\mathbb{R}^2) \ge 6$, it does **not** determine whether $\chi(\mathbb{R}^2) = 6$ or $\chi(\mathbb{R}^2) = 7$. Closing this final gap remains an outstanding open challenge in mathematics.
2.  **Non-Constructive Finite Lower Bound:**
    The transfer mechanism relies on non-constructive ZFC compactness (the Axiom of Choice in the de Bruijn–Erdős theorem). Consequently, while the proof guarantees that a finite 6-chromatic unit-distance graph exists, it **does not construct an explicit finite graph** requiring 6 colors.
3.  **Preprint Status & Formal Verification:**
    The paper is a theoretical computer science and mathematical preprint published by OpenAI on September 23, 2026. Notably, formal proof scripts written in **Lean 4** exist for certifying the baseline 5-color lower bound and 7-color upper bound statements of the Hadwiger–Nelson problem, providing computer-verified grounding for the classical foundation.

> ### Current Status of the Hadwiger–Nelson Problem
> *   **Lower Bound:** **6** (Proven by OpenAI, Sept 23, 2026)
> *   **Upper Bound:** **7** (Isbell / Hadwiger, 1950/1961 Hexagonal Tiling)
> *   **Remaining Open Question:** Is $\chi(\mathbb{R}^2)$ equal to 6 or 7?
> *   **Explicit Subgraph Challenge:** Constructing an explicit, finite 6-chromatic unit-distance graph (analogous to de Grey's 1,581-vertex graph for 5 colors).