# Disproving Kaplansky's Zero-Divisor Conjecture: A Geometric Counterexample in Characteristic Two

### 1. The Foundation: Group Algebras, Ring Elements, and Kaplansky's Conjectures

Let $K$ be a field and $G$ a group. The group algebra $K[G]$ is defined as the vector space over $K$ with basis $G$, equipped with multiplication extended bilinearly from the group operation. An arbitrary element $\alpha \in K[G]$ is a finite formal linear combination:
$$\alpha = \sum_{g \in G} k_g g$$
where $k_g \in K$ and $k_g = 0$ for all but finitely many $g \in G$. The addition of two elements is defined componentwise, and ring multiplication is given by:
$$\left( \sum_{g \in G} a_g g \right) \left( \sum_{h \in G} b_h h \right) = \sum_{g, h \in G} (a_g b_h) (gh) = \sum_{x \in G} \left( \sum_{g \in G} a_g b_{g^{-1}x} \right) x$$

Within the group algebra $K[G]$, key algebraic elements are classified as follows:
*   **Zero Divisors:** Nonzero elements $\alpha, \beta \in K[G] \setminus \{0\}$ such that $\alpha\beta = 0$.
*   **Nontrivial Units:** Invertible elements $\alpha \in K[G]$ (meaning $\alpha\beta = 1$ for some $\beta \in K[G]$) that are not trivial scalar multiples of group elements (i.e., $\alpha \neq k \cdot g$ for any $k \in K \setminus \{0\}$ and $g \in G$).
*   **Nontrivial Idempotents:** Nonzero elements $e \in K[G] \setminus \{0, 1\}$ satisfying $e^2 = e$.

#### Torsion as an Obstruction to Domain Structure
Torsion (the presence of nontrivial elements of finite order) in a group $G$ produces elementary zero divisors in $K[G]$. If $g \in G$ is an element of finite order $m > 1$ (so that $g^m = 1$ with $g \neq 1$), factoring $1 - g^m$ yields the identity:
$$(1 - g)(1 + g + g^2 + \dots + g^{m-1}) = 1 - g^m = 0$$
Because $m > 1$ and $g \neq 1$, both factors $1 - g$ and $1 + g + \dots + g^{m-1}$ are nonzero elements of $K[G]$, constituting an explicit pair of zero divisors.

In characteristic $2$, such as in the group algebra $\mathbb{F}_2[\mathbb{Z}/2]$ where $\mathbb{Z}/2 = \{1, g\}$ with $g^2 = 1$, addition and subtraction coincide ($-1 = 1$). The factorization simplifies cleanly:
$$(1 + g)(1 + g) = 1 + 2g + g^2 = 1 + 0 + 1 = 0$$
Here, the element $1 + g$ is a self-annihilating nonzero element ($\alpha^2 = 0$).

#### Kaplansky's Three Classical Conjectures
To isolate whether torsion is the *sole* algebraic obstruction to $K[G]$ being a domain, Irving Kaplansky (building on foundational questions posed in Graham Higman's 1940 doctoral thesis) formulated three conjectures for any field $K$ and any *torsion-free* group $G$:

1.  **The Unit Conjecture:** Every unit in $K[G]$ is trivial; that is, $\alpha \in K[G]^\times \implies \alpha = k \cdot g$ for some $k \in K \setminus \{0\}$ and $g \in G$.
2.  **The Zero-Divisor Conjecture:** $K[G]$ contains no nonzero zero divisors (i.e., $K[G]$ is an integral domain).
3.  **The Idempotent Conjecture:** The only idempotents in $K[G]$ are the trivial idempotents $0$ and $1$.

#### Geometric Approaches and Obstructions
Prior to recent developments, substantial effort was devoted to constructing zero divisors or nontrivial units geometrically via explicit combinatorial product structures on group algebras over $\mathbb{F}_2$:
*   **Mineyev's Origami Criteria:** Igor Mineyev developed geometric origami structures on group representations to generate nontrivial units and zero divisors through explicit geometric paper-folding analogies on 2-complexes.
*   **Garg–Mineyev Taiko Structures:** Manisha Garg and Igor Mineyev generalized these constructions into "taiko" product structures, analyzing support combinatorics to force pair cancellations in characteristic $2$.
*   **Shin's Global Girth Obstruction:** Henry Shin established a strict negative result demonstrating that orientable, no-fold "triple-girth" geometric routes cannot yield zero divisors whenever both support sizes are at least $2$. 

These structural obstructions underscored why traditional geometric cancellation schemes failed, motivating the probabilistic cone-picture machinery developed by OpenAI to circumvent fixed combinatorial constraints.

---

### 2. Logical Interrelations among the Conjectures

The logical implications among Kaplansky's three conjectures form a directed hierarchy. First, the presence of a nontrivial idempotent $e \in K[G] \setminus \{0, 1\}$ immediately yields a pair of nonzero zero divisors through the factorization:
$$e(1 - e) = e - e^2 = e - e = 0$$
Since $e \neq 0$ and $e \neq 1$, both $e$ and $1 - e$ are nonzero, so $\neg \text{Idempotent Conjecture} \implies \neg \text{Zero-Divisor Conjecture}$.

Second, classical ring-theoretic results established by Donald Passman demonstrate that if the Unit Conjecture holds for $K[G]$, then $K[G]$ contains no nonzero zero divisors. Taking contrapositives establishes the forward logical chain:

$$\begin{array}{ccccc}
\text{Unit Conjecture} & \implies & \text{Zero-Divisor Conjecture} & \implies & \text{Idempotent Conjecture} \\
& & \Downarrow & & \Downarrow \\
& & \text{No Zero Divisors} & \impliedby & \text{No Nontrivial Idempotents}
\end{array}$$

Reversing these implications from the bottom up demonstrates how counterexamples propagate:
```
Nontrivial Idempotent (e^2 = e, e ∉ {0,1})
                  │
                  ▼
          e(1 - e) = 0  ──>  Zero Divisor Exists  ──>  ¬ Zero-Divisor Conjecture
                                                             │
                                                             ▼
                                                    ¬ Unit Conjecture
```

#### Non-Reversibility and Gardam's Unit Counterexample
The logical chain cannot be reversed from units to zero divisors. In 2021, Giles Gardam disproved the Unit Conjecture over $\mathbb{F}_2$ (and subsequently over $\mathbb{C}$ in 2024) by constructing an explicit nontrivial unit in $\mathbb{F}_2[P]$. The group $P$ is the 3D crystallographic Hantzsche–Wendt group (also known as the Promislow group), defined by the presentation:
$$P = \langle a, b \mid b^{-1} a^2 b = a^{-2}, \; a^{-1} b^2 a = b^{-2} \rangle$$
Topologically, $P$ is the unique torsion-free 3-dimensional crystallographic group with finite abelianization, arising as a non-split extension:
$$1 \longrightarrow \mathbb{Z}^3 \longrightarrow P \longrightarrow \mathbb{Z}/2 \times \mathbb{Z}/2 \longrightarrow 1$$
Because $P$ is soluble (and thus elementary amenable) and satisfies the Farrell–Jones Conjecture, $K[P]$ is known to contain **no** zero divisors by the theorems of Kropholler, Linnell, and Moody. Gardam's unit $\alpha \in \mathbb{F}_2[P]$ (with $|\text{supp}(\alpha)| = 21$) satisfies $\alpha\beta = 1$ for an explicit inverse $\beta$, but this unit does not generate a zero divisor. Thus, the existence of nontrivial units in a group algebra does not force the existence of zero divisors.

---

### 3. Historical Context and Prior Status

Before the 2026 disproof, positive results established that Kaplansky's Zero-Divisor Conjecture held across wide families of torsion-free groups.

| Group Class / Algebraic Property | Status of Zero-Divisor & Unit Conjectures | Key Contributors & Historical Context |
| :--- | :--- | :--- |
| **Unique Product Property (UPP) & Left-Orderable Groups** | **Positive:** Every pair of finite subsets $A, B \subset G$ contains an element $ab \in AB$ with a unique factorization, forcing a unilinear term in algebra products. Guarantees no zero divisors and no nontrivial units. | Higman (1940), Rips & Segev (1987), Steenbock (2015), Mian & Siddique (2026) |
| **Elementary Amenable Groups** | **Positive:** Zero-divisor conjecture proven positive (even over general division-ring coefficients). | Kropholler, Linnell, & Moody (1988) |
| **3-Manifold & Compact Special Groups** | **Positive:** Division ring embeddings for group algebras of torsion-free virtually compact special groups and torsion-free compact 3-manifold groups. | Fisher & Sánchez-Peralta (2026) |
| **Groups Satisfying Atiyah Conjecture** | **Positive:** Over $\mathbb{C}$, the strong Atiyah Conjecture implies the Zero-Divisor Conjecture for covered group classes. | Linnell (1993), Lück (2002) |
| **Hantzsche–Wendt Group $P$** | **Unit Counterexample / Zero-Divisor Positive:** Contains nontrivial units in $\mathbb{F}_2[P]$ and $\mathbb{C}[P]$, but has **no zero divisors** ($K[P]$ is a domain). | Promislow (1988), Craven & Pappas (2013), Gardam (2021, 2024) |
| **Geometric Origami / Taiko Frameworks** | **Obstruction Criteria:** Mineyev's origami and Garg–Mineyev taiko conditions; Shin established global girth obstructions forbidding zero divisors under simple no-fold conditions. | Mineyev (2024), Garg & Mineyev (2025), Shin (2026) |

---

### 4. The Main Breakthrough: Theorem Statement and Scope

On September 23, 2026, OpenAI published a research preprint disproving Kaplansky's Zero-Divisor Conjecture.

> **Theorem 1.1** (OpenAI, 2026)  
> *There exist a finitely presented torsion-free group $G$ and nonzero elements $\alpha, \beta \in \mathbb{F}_2[G]$ such that $\alpha\beta = 0$. Moreover, $G$ admits a finite two-dimensional classifying space $X = K(G,1)$.*

#### Structural and Topological Scope
The constructed group $G$ is realized as the fundamental group $G = \pi_1(X)$ of a finite two-dimensional CW complex $X$. The complex $X$ is shown to be aspherical ($\pi_2(X) = 0$), which implies that its universal cover $\widetilde{X}$ is contractible. Consequently, $X$ is a finite $K(G,1)$ space, placing $G$ in the class of groups of cohomological dimension $cd(G) \le 2$. The existence of a finite-dimensional classifying space provides homological bounds that preclude finite-order elements, establishing that $G$ is strictly torsion-free.

---

### 5. Construction of the Group Algebra and the Cancellation Mechanism

The proof constructs $G$ and the factors $\alpha, \beta \in \mathbb{F}_2[G]$ using a combination of finite geometry over $\mathbb{F}_{128}$, prescribed parity cross-intersections, girth-conditioned random matchings, and an explicit simultaneous-step cancellation scheme.

```
       [ Finite Geometry: PG(2, F_128) + 3 Extras ]
                           │
                           ▼
           [ Prescribed Outgoing Label Sets ]
            |Sx ∩ Sy| is ODD for all (x,y)
                           │
                           ▼
     [ Random Matchings conditioned on Girth L ]
            Graphs Γ_A, Γ_B  ──> Rose F
                           │
                           ▼
        [ Abstract Coning of Graph Components ]
          Complex X = K(G,1), Group G = π_1(X)
                           │
                           ▼
     [ Factors α = Σ g_x ,  β = Σ h_y^(-1) in F_2[G] ]
                           │
                           ▼
  [ Simultaneous-Step Graph on A' x B' along label t ]
   • Step invariant: (g_x * t)(h_y * t)^(-1) = g_x * h_y^(-1)
   • Degree at (x,y) = |Sx ∩ Sy| (ODD)
   • Handshake Lemma => Component size is EVEN
   • Characteristic 2 => EVEN sum cancels to ZERO (1 + 1 = 0)
                           │
                           ▼
                    [ α * β = 0 ]
```

#### 5.1 Finite Geometry and Type Prescriptions
Fix the finite field parameters $q = 128$, $v = q^2 + q + 1 = 16513$, and $p = \frac{q+1}{v} = \frac{129}{16513}$. The finite projective plane $PG(2, \mathbb{F}_{128})$ contains $v = 16513$ points and $v$ lines. Each line contains $q + 1 = 129$ points, each point lies on 129 lines, any two distinct points lie on a unique common line, and any two distinct lines intersect at a unique point.

1.  **Alphabet Construction:** Define the signed alphabet $T$ consisting of the $v$ points of $PG(2, \mathbb{F}_{128})$ (*ordinary letters*) plus 3 *extra letters*. Pair the 3 extra letters with 3 distinct ordinary letters, and pair the remaining $v - 3 = 16510$ ordinary letters arbitrarily in pairs. This establishes a fixed-point-free involution $t \mapsto \bar{t}$ on $T$, where $|T| = 16516$. The corresponding rose $F = \bigvee_{i=1}^{8258} S^1$ has 8258 unoriented edges.
2.  **Vertex Sets and Empirical Proportions:** Take disjoint vertex sets $A$ and $B$, each of size $n$, where $n \to \infty$ through multiples of $2v^2$. For each vertex $x \in A$ and $y \in B$, assign outgoing label sets $S_x, S_y \subset T$:
    *   On both sides, the ordinary part of $S_x$ (or $S_y$) corresponds to a line in $PG(2, \mathbb{F}_{128})$, with all lines represented equally often.
    *   For $x \in A$, the extra part is chosen from the three 2-element subsets of extra letters with proportion $p/2$ each, and empty otherwise.
    *   For $y \in B$, the extra part consists of all 3 extra letters with proportion $p$, and empty otherwise.
    
    *Exact Empirical Proportions:* At $n = 2v^2$, each line class on $A$ contains exactly 129 vertices of each double-extra type and 32,639 vertices of the empty-extra type. On $B$, each line class contains 258 vertices of the triple-extra type and 32,768 vertices of the empty-extra type.

#### 5.2 The Parity Condition, Turn Weights, and Lyapunov Decay
Two ordinary line parts meet in either 1 point (distinct lines) or $q + 1 = 129$ points (identical line), both of which are odd integers. An extra part on $A$ (size 0 or 2) meets an extra part on $B$ (size 0 or 3) in either 0 or 2 letters, both of which are even integers. Combining ordinary and extra intersections yields the Parity Condition:
$$|S_x \cap S_y| \text{ is \textbf{odd} for every pair } (x, y) \in A \times B$$

To control path probabilities and prevent unwanted word coincidences, define turn weights derived from the incidence geometry. For a non-cancelling turn $(t, u)$, let $w(t, u)$ be the frequency of $u$ among vertices of $B$ containing $\bar{t}$ (with $w(t, \bar{t}) = 0$). For distinct $\bar{t}, u$, the transition weights are:
$$w(t, u) = \begin{cases} 
\frac{1}{q+1} = \frac{1}{129} & \text{if } (\bar{t}, u) \text{ is (ordinary, ordinary)} \\
p = \frac{129}{16513} & \text{if } (\bar{t}, u) \text{ is (ordinary, extra) or (extra, ordinary)} \\
1 & \text{if } (\bar{t}, u) \text{ is (extra, extra)}
\end{cases}$$

Define the turn matrix $M_{t,u} = w(t, u)^2$. To establish geometric decay, introduce the explicit test vector (Lyapunov function) $f: T \to \mathbb{R}^+$:
$$f(t) = \begin{cases} 5 & \text{if } \bar{t} \text{ is an extra letter} \\ 1 & \text{if } \bar{t} \text{ is an ordinary letter} \end{cases}$$

Evaluating the action of the turn matrix $M$ on $f$ yields:
*   If $\bar{t}$ is ordinary:
    $$(Mf)(t) \le \frac{q}{(q+1)^2} + 3p^2 + \frac{12}{(q+1)^2} = \frac{500731261911}{504183783481} < \frac{149}{150} f(t)$$
*   If $\bar{t}$ is extra:
    $$\frac{(Mf)(t)}{f(t)} \le \frac{2 + vp^2 + 12p^2}{5} = \frac{820350863}{1363395845} < \frac{149}{150}$$

Thus, $Mf \le \frac{149}{150} f$. For any word $W = t_1 t_2 \dots t_h \in T^h$, define its weight $P(W) = \prod_{i=1}^{h-1} w(t_i, t_{i+1})$. Because $\mathbf{1} \le f$ and $\sum_{t \in T} f(t) = 16528 < e^{10}$, summing the squared word weights over all words of length $h$ yields:
$$\sum_{W \in T^h} P(W)^2 = \mathbf{1}^T M^{h-1} \mathbf{1} \le 16528 \left(\frac{149}{150}\right)^{h-1} \le e^{-2\delta h}$$
where $\delta = \frac{1}{600}$ is an admissible exponential decay constant.

#### 5.3 Random Matchings and Complex Construction
For each inverse pair $t, \bar{t}$, choose a matching bijection between $A_t$ and $A_{\bar{t}}$, and between $B_t$ and $B_{\bar{t}}$, uniformly at random. Condition the uniform distribution of matchings on the requirement that the resulting disjoint union graph $\Gamma = \Gamma_A \sqcup \Gamma_B$ has girth at least $L = \lfloor c \log n \rfloor$, where $c = 1/100$. Switching transpositions show that the error incurred by adding $s$ conditional edge prescriptions is bounded by $r_n = O(d_*^{2L+2}) = o(n)$, where $d_* = q + 4 = 132$.

The 2-complex $X$ is formed by taking the rose $F = \bigvee_{i=1}^{8258} S^1$ and attaching abstract cones $K_\Lambda$ for each connected component $\Lambda$ of $\Gamma_A \sqcup \Gamma_B$ along their labelled immersive maps $\Lambda \to F$. The fundamental group of the resulting complex is $G = \pi_1(X)$. Coning kills the labels of all closed graph paths in $\Gamma$.

#### 5.4 Proposed Factors and the Cancellation Mechanism
Select predetermined root vertices $x_A \in A$ and $x_B \in B$. Let $A'$ and $B'$ be the full vertex sets of the connected components containing $x_A$ and $x_B$, respectively. For any $x \in A'$, let $g_x \in G$ be the label of a path from $x_A$ to $x$. For $y \in B'$, let $h_y \in G$ be the label of a path from $x_B$ to $y$. Define the elements in $\mathbb{F}_2[G]$:
$$\alpha = \sum_{x \in A'} g_x, \quad \beta = \sum_{y \in B'} h_y^{-1}$$

To compute the product $\alpha\beta = \sum_{x \in A', y \in B'} g_x h_y^{-1}$, construct a simultaneous-step graph on $A' \times B'$ where a directed edge $(x, y) \xrightarrow{t} (x', y')$ exists whenever $t \in S_x \cap S_y$.
1.  **Invariance Along Steps:** Along any simultaneous step $t$, the product element in $G$ is strictly invariant:
    $$(g_x t)(h_y t)^{-1} = g_x t t^{-1} h_y^{-1} = g_x h_y^{-1}$$
2.  **Odd Degrees:** The degree of any vertex $(x, y)$ in this simultaneous-step graph is precisely $|S_x \cap S_y|$, which is odd by the Parity Condition.
3.  **Handshake Lemma:** By the degree-sum formula, the sum of vertex degrees in any connected component equals twice the number of edges (an even integer). Because every vertex has an odd degree, the total number of vertices in every connected component must be **even**.
4.  **Coefficient Cancellation over $\mathbb{F}_2$:** All vertices in a given connected component yield the exact same group element $g_x h_y^{-1} \in G$. In characteristic 2, summing an even number of identical elements yields zero ($1 + 1 = 0$). Summing across all connected components yields $\alpha\beta = 0$.

---

### 6. The Two Geometric Safeguards

While the parity construction guarantees algebraic cancellation, two geometric safeguards are required to make the counterexample non-trivial: proving the factors are nonzero ($\alpha, \beta \neq 0$) and proving the group $G$ is torsion-free.

#### Safeguard 1: Root Separation (Nonzero Factors)
To ensure $\alpha \neq 0$ and $\beta \neq 0$, the identity element $e_G \in G$ must not be cancelled by non-root vertices within the factors.
*   **Requirement:** Any path label from the root $x_A$ to a distinct vertex $x \in A' \setminus \{x_A\}$ (or $x_B$ to $y \in B' \setminus \{x_B\}$) must be nontrivial in $G$ ($g_x \neq e_G$).
*   **Consequence:** The identity element $e_G$ appears with a coefficient of 1 in $\alpha$ (contributed solely by $x = x_A$) and in $\beta$ (contributed solely by $y = x_B$). Because $1 \neq 0$ in $\mathbb{F}_2$, both factors survive in the quotient ring: $\alpha \neq 0$ and $\beta \neq 0$.

#### Safeguard 2: Torsion-Freeness via Asphericity
To guarantee $G$ is torsion-free, the complex $X$ is proven to be aspherical:
$$\pi_2(X) = 0$$
*   **Homological Contractibility:** Because $X$ is 2-dimensional and $\pi_2(X) = 0$, its universal cover $\widetilde{X}$ has vanishing homology in all positive dimensions ($H_1(\widetilde{X}) = 0$, $H_2(\widetilde{X}) = 0$, and $H_k(\widetilde{X}) = 0$ for $k \ge 3$). Because $\widetilde{X}$ is simply connected, Whitehead's theorem implies $\widetilde{X}$ is contractible, making $X$ a finite 2D classifying space $K(G,1)$.
*   **Resolution Obstruction to Torsion:** The augmented cellular chain complex of $\widetilde{X}$ provides a finite length-2 free $\mathbb{Z}G$-resolution of $\mathbb{Z}$:
    $$0 \longrightarrow C_2(\widetilde{X}) \longrightarrow C_1(\widetilde{X}) \longrightarrow C_0(\widetilde{X}) \longrightarrow \mathbb{Z} \longrightarrow 0$$
    If $G$ contained a finite-order element $g$ of prime order $\ell$, restricting this resolution to the cyclic subgroup $H = \langle g \rangle \cong \mathbb{Z}/\ell$ would yield a finite length-2 free $\mathbb{Z}H$-resolution of $\mathbb{Z}$. Computing group cohomology with $\mathbb{F}_\ell$ coefficients via this restricted resolution forces $H^k(H; \mathbb{F}_\ell) = 0$ for all $k > 2$. However, cyclic groups have periodic cohomology $H^k(H; \mathbb{F}_\ell) \cong \mathbb{F}_\ell$ for all $k \ge 0$. This contradiction establishes that $G$ cannot contain finite-order elements.

```
       [ Minimization over Boundary Lengths ]
                          │
                          ▼
            [ Minimal Cone Pictures on S^2 ]
                          │
                          ▼
         [ Band Surgery on Coincident Edges ]
     Splicing/contracting overlapping occurrences
                          │
                          ▼
         [ Reduced Spherical Arrangements ]
                          │
                          ▼
        [ Lipton-Tarjan Planar Separation ]
     Decomposes arrangements into bounded clusters
                          │
                          ▼
      [ Squared-Word Decay & Bounded Pattern ]
    Probability -> 0 via Σ P(W)^2 <= e^(-2δh)
                          │
                          ▼
     [ No Reduced Spherical Arrangements Exist ]
                          │
                          ▼
        [ π_2(X) = 0  &  Root Labels Nontrivial ]
```

#### Minimal Cone Pictures and Band Surgery
Both safeguards are proved simultaneously by establishing that $\Gamma$ admits no *reduced spherical arrangements*. Any hypothetical failure of root separation or asphericity yields a spherical or disk cone picture. Select a picture of minimal total boundary length. If two paired edge occurrences traverse the same underlying undirected graph edge $e$, perform band surgery along the mapping band:

| Incident Disks | Old Lifted Paths | Spliced / Contracted New Paths | Boundary Length Change |
| :--- | :--- | :--- | :--- |
| **Two Inner Disks** | $e a, \; e^{-1} b$ | $a b$ | $|S'| = |S| - 2$ |
| **Exterior & Inner Disk** | $a e c \; (x \to y), \; e^{-1} b$ | $a b c \; (x \to y)$ | $|S'| = |S| - 2$ |
| **One Inner Disk Twice** | $e a e^{-1} b$ | $a, \; b$ (Splits into two disks) | $|S'| = |S| - 2$ |
| **Exterior Disk Twice** | $a e b e^{-1} c \; (x \to y)$ | $a c \; (x \to y)$ | $|S'| = |S| - 2$ |

In every case, band surgery contracts the common edge $e$, strictly decreasing total boundary length ($|S'| = |S| - 2$) while preserving the topological failure. This minimality contradiction proves that every reduced spherical arrangement must satisfy the reduction condition (paired occurrences traverse distinct underlying graph edges).

#### Parameter Dependency Chain and Quantifier Ordering
To exclude reduced spherical arrangements without incurring a fatal union bound over arbitrary arrangement sizes, parameters must be fixed in a precise, strict dependency chain:

$$\underbrace{\text{types}, c, \delta}_{\text{Finite Geometry \& Decay}} \longrightarrow \underbrace{\varepsilon, d}_{\text{Decay \& Diameter}} \longrightarrow \underbrace{D}_{\text{Closure Cost}} \longrightarrow \underbrace{U}_{\text{Segment Length}} \longrightarrow \underbrace{\eta}_{\text{Separation Ratio}} \longrightarrow \underbrace{K}_{\text{Cluster Size}} \longrightarrow \underbrace{C, I}_{\text{Pattern Bounds}} \longrightarrow \underbrace{n}_{\text{Sampling Size}}$$

*Critical Architecture Point:* The tolerance $\varepsilon > 0$ for unpaired occurrences is fixed **before** $K, C, I$. Consequently, a single bounded pattern class detects every spherical arrangement regardless of how many paths or total length it contains, avoiding a union bound over arrangement sizes.

#### Planar Separation and Bounded Pattern Estimate
1.  **Lipton–Tarjan Planar Separation:** A planar arrangement with $m$ path pieces is localized by deleting at most $C_{\text{sep}} m / \sqrt{K}$ vertices, where $C_{\text{sep}} = \frac{2\sqrt{2}}{1 - \sqrt{2/3}}$. Setting $K = \max\{1, \lceil (C_{\text{sep}}/\eta)^2 \rceil\}$ guarantees that remaining component clusters have at most $K$ pieces.
2.  **Bounded-Pattern Estimate:** For a cluster of total length $H$ with $L \le H \le CL$, at most $I$ interval pairs, and $b \le \varepsilon H$ unpaired positions, multiplicity stages and squared-word decay establish that the expectation bound satisfies:
    $$\prod_{j=1}^{m^*} B_j \le e^{-\delta H / 4}$$
    Taking $M = \max\{1, \lceil 2(C + K) \rceil\}$, at least one stage $j$ satisfies $B_j \le e^{-\delta H / (4M)}$. Applying the union bound across all $\exp(o(L))$ enlarged patterns yields a realization probability of $\exp(o(L) - \delta L / (4M)) \to 0$ as $n \to \infty$. Thus, no reduced spherical arrangements exist, completing the proof of both safeguards.

---

### 7. Scope, Status, and Formalization

#### Result Scope and Limitations
*   **Field Characteristic:** The explicit construction and cancellation mechanism apply specifically to characteristic 2 ($\mathbb{F}_2$), fundamentally relying on $1 + 1 = 0$ over even-degree graph components.
*   **Non-Constructive Existence:** The proof is probabilistic; it establishes that valid graph matchings exist with high probability for sufficiently large $n$, rather than generating a small explicit matrix representation or simple word presentation for $G$.
*   **Graph Scale:** The required graph sizes $n$ are astronomically large due to the parameter chain ($q = 128$, girth $L = \lfloor c \log n \rfloor$, separator bounds $K, U, D$).

#### Publication Context and Machine Verification
*   **Preprint Reference:** The result was published as an AI-generated research preprint by OpenAI on September 23, 2026, titled *"A Torsion-Free Group Algebra with Zero Divisors"*.
*   **Lean 4 Formalization:** The proof has been machine-checked in the Lean 4 proof assistant. The formal repository `openai/math` contains the scope documentation (`196.md`) and formal statement challenge file (`TorsionFreeZeroDivisors.lean`). The machine-verified formalization confirms that a finitely presented torsion-free group algebra over $\mathbb{F}_2$ contains nonzero zero divisors and admits a finite two-dimensional classifying space $K(G, 1)$.