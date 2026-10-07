# Technical Explainer: Resolving the Hilbert–Smith Conjecture in Every Finite Dimension

---

### 1. The Problem, Historical Foundations, and the $p$-adic Reduction

#### Lie Groups and Hilbert's Fifth Problem
A **Lie group** is a topological group $G$ equipped with a smooth (or $C^\omega$) real manifold structure such that the group multiplication map $\mu: G \times G \to G$, $(g,h) \mapsto gh$, and the inversion map $\iota: G \to G$, $g \mapsto g^{-1}$, are smooth functions. 

Hilbert's Fifth Problem (1900) originally sought to determine to what extent differentiability assumptions could be eliminated from the foundation of continuous transformation groups. A major branch of this problem concerns groups that are themselves locally Euclidean. Gleason, Montgomery, Zippin (1952), and Yamabe (1953) resolved this formulation by demonstrating that any locally Euclidean topological group (and more generally, general locally compact groups via Yamabe's structure theory) is a Lie group.

The **Hilbert–Smith Conjecture** addresses the remaining, broader transformation-group formulation: whether a non-smooth, locally compact topological group acting continuously and faithfully on a connected topological manifold must necessarily be a Lie group.

#### Exact Hypotheses of Theorem 1.1
The central result of the paper is Theorem 1.1, stated verbatim below:

> **Theorem 1.1** (The Hilbert–Smith conjecture)**.** *Let $n \ge 1$. A locally compact second-countable Hausdorff group acting faithfully and jointly continuously on a connected Hausdorff second-countable topological $n$-manifold without boundary is a Lie group.*

To understand this hypothesis, each topological adjective carries precise topological and geometric meaning:
*   **Locally compact:** Every element has a compact neighborhood, providing the topological framework needed to analyze subgroups via Haar measure and structural limits.
*   **Second-countable:** The topology has a countable basis. For the manifold $M$, this ensures it can be embedded or analyzed via countable covers; for the group $G$, it prevents uncountably large continuous pathologies.
*   **Hausdorff:** Distinct points can be separated by disjoint open sets, ensuring unique limits.
*   **Faithful action:** The kernel of the action is trivial (the identity element is the only element fixing every point of the manifold). This does *not* require point stabilizers to be trivial.
*   **Joint continuity:** The evaluation map $G \times M \to M$, $(g, x) \mapsto g \cdot x$, is continuous in both variables simultaneously (equivalent to a continuous homomorphism $G \to \text{Homeo}(M)$ equipped with the compact-open topology).
*   **Topological $n$-manifold without boundary:** A space locally homeomorphic to $\mathbb{R}^n$. The result holds without assuming global orientability, compactness, or triangulability.

#### Small Subgroups and $p$-adic Integers ($\mathbb{Z}_p$)
A topological group has **no small subgroups** if there exists a neighborhood of the identity element that contains no non-trivial subgroups. Standard Lie groups possess this property due to the local diffeomorphism provided by the exponential map.

For a prime $p$, the additive group of **$p$-adic integers**, denoted by $\mathbb{Z}_p$, is defined as the inverse limit of finite cyclic groups:
$$\mathbb{Z}_p = \varprojlim_{k} \mathbb{Z}/p^k\mathbb{Z}$$
equipped with its profinite topology. The group $\mathbb{Z}_p$ is **not a Lie group** because:
1.  It is totally disconnected and infinite (topologically a compact Cantor set).
2.  It contains arbitrarily small open subgroups $p^k \mathbb{Z}_p$ for every $k \ge 1$, directly violating the "no small subgroups" property required of Lie groups.

#### Classical Reduction to $\mathbb{Z}_p$ and Newman's Theorem
Classical structure theory (Montgomery–Zippin, Yamabe, Lee) establishes that if a locally compact group $G$ acting faithfully on a connected topological manifold is *not* a Lie group, then $G$ must contain a closed subgroup isomorphic to $\mathbb{Z}_p$ for some prime $p$ that acts faithfully on the manifold. Resolving the Hilbert–Smith conjecture is therefore completely equivalent to ruling out faithful, jointly continuous actions of $\mathbb{Z}_p$ on connected manifolds.

To restrict $\mathbb{Z}_p$-actions locally, the proof relies on **Newman's Rigidity Theorem**:

> **Newman's Rigidity Theorem.** *A finite-order homeomorphism of a connected topological manifold that fixes a nonempty open set pointwise must be the identity homeomorphism.*

Newman's theorem provides local rigidity: no non-identity periodic transformation can collapse to the identity on any open region. Pardon utilized this theorem to prove that a faithful $\mathbb{Z}_p$-action on a manifold $M$ yields a faithful action of an open subgroup $G \cong \mathbb{Z}_p$ preserving orientation on an invariant, connected open subset $O \subset \mathbb{R}^n$ of a single coordinate chart.

---

### 2. Earlier Partial Results and Historical Predecessors

#### Low-Dimensional Manifestations
*   **Dimensions 1 and 2:** Classical results (Montgomery–Zippin, Pardon) established the conjecture for 1- and 2-manifolds using low-dimensional geometric topology.
*   **Dimension 3:** Solved by Pardon (2013). Pardon's local proof utilized incompressible surfaces within invariant open sets and analyzed the resulting action on surface mapping class groups, successfully handling arbitrary point stabilizers without replacing the topological action with a smooth one.

#### Regularity-Based Restrictions
Prior to this work, the Hilbert–Smith conjecture was established under various geometric regularity constraints on the homeomorphisms:
*   **Differentiable actions:** Excluded by Bochner–Montgomery (1946).
*   **Lipschitz actions:** Excluded on Riemannian manifolds by Repovš–Ščepin (1997) using invariant averaged metrics.
*   **Hölder actions:** Excluded on closed manifolds by Maleshich (1997) for Hölder exponent $\alpha > n/(n+2)$.
*   **Quasiconformal actions:** Excluded on Riemannian manifolds by Martin (1999).
*   **Uniformly quasisymmetric actions:** Excluded on compact metric cohomology manifolds by Mj (2012) under Ahlfors regularity and Hausdorff dimension hypotheses.

#### Cohomological Dimension and Symplectic Methods
*   **Dimension-Raising Theory:** Yang, Bredon–Raymond–Williams, and Raymond investigated obstructions via integral cohomological dimension. Continuous $\mathbb{Z}_p$-actions tend to raise the cohomological dimension of the orbit space ($n \to n+3$ with field coefficients vs. integral considerations), creating geometric incompatibilities under metric regularity assumptions.
*   **Floer-Theoretic Methods:** Shelukhin (2024) excluded continuous non-trivial $\mathbb{Z}_p$-actions lying in the $C^0$-closure of the Hamiltonian diffeomorphism group of closed symplectic manifolds with vanishing $\pi_2$ classes (with respect to both the symplectic class and first Chern class).

---

### 3. Main Results and Dynamical Consequences

#### Exact Statements of Main Theorems

> **Theorem 1.1** (The Hilbert–Smith conjecture)**.** *Let $n \ge 1$. A locally compact second-countable Hausdorff group acting faithfully and jointly continuously on a connected Hausdorff second-countable topological $n$-manifold without boundary is a Lie group.*

> **Theorem 1.2** ($p$-adic exclusion)**.** *Let $n \ge 1$ be an integer and $p$ a prime. Every jointly continuous action of $\mathbb{Z}_p$ on a connected Hausdorff second-countable topological $n$-manifold without boundary has nonzero kernel. Consequently the action factors through a finite quotient of $\mathbb{Z}_p$.*

#### Almost Periodic Homeomorphisms
For a manifold $M$, equip $\text{Homeo}(M)$ with the compact-open topology. A homeomorphism $f \in \text{Homeo}(M)$ is defined as **almost periodic** if the cyclic subgroup $\{f^j : j \in \mathbb{Z}\}$ has compact closure $K$ in $\text{Homeo}(M)$.

#### Proof of the Dynamical Consequence
Theorem 1.1 resolves a long-standing dynamical conjecture regarding almost periodic homeomorphisms:

1.  **Compact Group Action:** The closure $K = \overline{\{f^j : j \in \mathbb{Z}\}}$ is a compact abelian group acting faithfully and jointly continuously on $M$.
2.  **Second-Countability:** Evaluating elements of $K$ on a countable dense subset of $M$ embeds $K$ continuously into a countable product of copies of $M$. Because $M$ is second-countable, $K$ is second-countable.
3.  **Application of Theorem 1.1:** Since $K$ is a compact, second-countable, Hausdorff group acting faithfully and jointly continuously on $M$, Theorem 1.1 asserts that $K$ is a **compact abelian Lie group**.
4.  **Identity Component and Flow:** The identity component $K_0 \subseteq K$ is a torus of finite index. Therefore, some positive iterate $f^m \in K_0$ for an integer $m \ge 1$.
5.  **1-Parameter Subgroup:** The exponential map $\exp: \mathfrak{k}_0 \to K_0$ of a compact torus is surjective. Hence, $f^m$ lies on a 1-parameter subgroup, yielding a continuous homomorphism $\Phi: \mathbb{R} \to \text{Homeo}(M)$ such that $\Phi(1) = f^m$.

---

### 4. Step-by-Step Architecture of the Proof

#### Step 4.1: Chart Reduction and Stabilization (Sections 5.1 & 5.2)

##### Proposition 5.1 (Invariant Chart Subset)
By Newman's theorem, there exists a point $x \in M$ whose open subgroups do not fix any neighborhood pointwise. Selecting an appropriate coordinate chart and taking a small open subgroup $G \cong \mathbb{Z}_p$ yields a connected, $G$-invariant open subset $O \subset \mathbb{R}^n$ on which $G$ acts faithfully and preserves orientation.

##### Stabilization
Fix an odd integer $d > n$ ($d \ge 3$). Define the stabilized open manifold:
$$W = O \times \mathbb{R}^{d-n} \subset \mathbb{R}^d$$
equipped with the product action ($G$ acts on $O$ and acts trivially on $\mathbb{R}^{d-n}$). $W$ is an oriented, connected open $d$-manifold. 

Let $W^+ = W \cup \{\infty\}$ be its one-point compactification (a compact metrizable $G$-space fixing $\infty$), and let $Y = W^+/G$ be its orbit space with orbit map $q: W^+ \to Y$ and basepoint $y_\infty = q(\infty)$.

##### Lemma 5.3 (Averaged Degree-One Test)
Let $c: S^d \to W^+$ be the continuous collapse map that maps $W$ identically and collapses $S^d \setminus W$ to $\infty$. To construct a continuous test map $a: Y \to S^d$ with $\deg(aqc) = 1$:
1. Select $z \in W$ and $r > 0$ such that $B(z, r) \subset W$. Define the local ball-pinching map $P_{z,r}: W^+ \to S^d$.
2. By uniform continuity on the compact space $G \times W^+$, choose a sufficiently small open subgroup $H \subset G$ ($H \cong \mathbb{Z}_p$) satisfying:
   $$\sup_{h \in H, w \in W^+} \|P_{z,r}(hw) - P_{z,r}(w)\| < \frac{1}{2}$$
3. Perform Haar integral averaging over $H$:
   $$A(w) = \int_H P_{z,r}(hw) \, d\mu_H(h)$$
4. Normalize $A(w)/\|A(w)\|$ to obtain an $H$-invariant map. Replace the acting group $G$ by this open subgroup $H \cong \mathbb{Z}_p$. The normalized map descends to $a: Y \to S^d$ such that $aq$ is homotopic to $P_{z,r}$, establishing:
   $$\deg(aqc) = 1$$

```
   S^d --------( c )--------> W^+ --------( q )--------> Y = W^+/G --------( a )--------> S^d
(Source)                  (Compactified)            (Orbit Space)                      (Target)
   |                            |                         |                               |
   +----------------------------+-- f_t = t ◦ q ◦ c ------+-------------------------------+
                                  (Compact-Source Test)
```

#### Step 4.2: Compact-Source Sheaf Categories and Witt Groups (Sections 2 & 3)

##### Category Construction
For a test space $X$, let $\mathcal{T}_0(X)$ be the thick subcategory of $D^b(\text{Sh}_{\mathbb{R}}(X))$ generated by proper direct images:
$$Rf_*\mathbb{R}_B, \quad f: B \to X \text{ continuous, } B \text{ a compact finite polyhedron}$$
Let $\mathcal{T}(X)$ be its closure under direct summands in $D^b(\text{Sh}_{\mathbb{R}}(X))$. The semialgebraic counterparts $\mathcal{P}_0(X)$ and $\mathcal{P}(X)$ restrict $B$ and $f$ to be semialgebraic. Objects in these categories may have infinite-dimensional stalks, but their topological origins ensure exact duality behavior.

##### Duality, Exactness Signs, and Witt Groups
Equip $\mathcal{T}(X)$ with the shifted Verdier duality functor:
$$D_{X,r} = [-r]D_X, \quad D_X A = R\mathcal{H}om(A, \omega_X)$$
In accordance with shifted duality conventions (Appendix A of the paper), the shifted duality exactness sign is $\delta_r = (-1)^r$. Symmetric forms of degree $r$ correspond to Koszul-symmetric pairings:
$$\beta: A \otimes A \longrightarrow \omega_X[-r], \quad \beta \circ \tau_{A,A} = \beta$$
whose adjoint map $\alpha: A \xrightarrow{\sim} D_{X,r} A$ is an isomorphism.

The real Witt group $E_r(X) = W_r(\mathcal{T}(X))$ (and its semialgebraic analogue $F_r(X) = W_r(\mathcal{P}(X))$) is the Grothendieck group of non-singular symmetric forms modulo neutral forms containing triangular lagrangians.

##### Theorem 2.9 (Homotopy Invariance)
By modeling the interval $I = [0,1]$ and examining the boundary triangle $J \to H \to E \to J[1]$, the paper proves that a continuous homotopy $h: I \times X \to Y$ induces equal maps on Witt groups:
$$h_{0*} = h_{1*}: E_r(X) \longrightarrow E_r(Y)$$

#### Step 4.3: Fixed Sphere Lattice and Density Bounds (Sections 3 & 4)

##### Theorem 3.6 (Dense Doubling)
If $\mathcal{A} \subset \mathcal{C}$ is a dense subcategory inclusion with duality (i.e., every object in $\mathcal{C}$ is a summand of an object in $\mathcal{A}$), then the explicit double construction:
$$D(q) = q \perp q \perp H(x[1])$$
maps $W_r(\mathcal{C}) \to W_r(\mathcal{A})$ such that both composition maps equal multiplication by 2. This proves that the kernel and cokernel of $W_r(\mathcal{A}) \to W_r(\mathcal{C})$ are annihilated by 2.

##### Theorem 4.3 (Bounded Comparison)
Applying localization and five-lemma diagram chases across an open cover of $S^j$ by two pole complements ($U \cup V = S^j$) bounds the kernel and cokernel of the comparison map $F_r(S^j) \to E_r(S^j)$ by $2^{e_j}$, where $e_j$ depends *only* on the sphere dimension $j$.

##### Theorem 4.7 (Fixed Sphere Lattice)
For odd $d \ge 3$, the rationalized Witt group is 1-dimensional: $E_d(S^d) \otimes \mathbb{Q} = \mathbb{Q} u_d$, where $u_d$ is the orientation class. Furthermore, the image of $E_d(S^d)$ before rationalization is bounded within a fixed integral lattice:
$$\text{im}\left(E_d(S^d) \longrightarrow E_d(S^d)\otimes \mathbb{Q}\right) \subseteq L_d^{-1}\mathbb{Z}u_d$$
where $L_d = 2^{e_d}$ is an integer **fixed prior to selecting the prime $p$ or the quotient exponent $k$**.

#### Step 4.4: Character Classes and Involution Construction (Section 6.1 & 6.2)

##### Character Decompositions
Let $\Lambda = \bigcup_{j \ge 0} \mu_{p^j} \subset S^1$ be the character group of $p$-power roots of unity. The orbit sheaf $\mathcal{H} = q_*\mathbb{C}_{W^+}$ decomposes canonically into eigensheaves:
$$\mathcal{H} \cong \bigoplus_{\lambda \in \Lambda} \mathcal{H}_\lambda$$

##### Involution Classes and Localization
Given a finite partition $\Lambda = D_0 \sqcup \dots \sqcup D_{m-1}$, define self-adjoint projectors $e_i$ on $A_t|_{X \setminus \{b_t\}}$, where $A_t = R(tqc)_*\mathbb{C}_{S^d}$ and $b_t = t(y_\infty)$.

Using Proposition 4.9, localize away a contractible open neighborhood $U$ of $b_t$ to obtain an isomorphism:
$$\ell_U: E_d(X) \stackrel{\sim}{\longrightarrow} W_d(\mathcal{T}(X)/\mathcal{T}(U))$$

##### Proposition 6.4 (Sum Identity via Matrix Isometry)
The operators $2e_i - \text{id}$ are self-adjoint involutions. They define integral character classes $z_i(t) \in E_d(X)$ via:
$$\ell_U(z_i(t)) = [A_t, \alpha_t] + [A_t, \alpha_t(2e_i - \text{id})]$$
To establish the sum identity $\sum_{i=0}^{m-1} z_i(t) = 2[A_t, \alpha_t]$ without requiring quotient idempotents to split in $\mathcal{T}(X)/\mathcal{T}(U)$, the paper constructs an explicit matrix isometry $S$:
1. On $A^{\oplus m}$, set $Q = \text{diag}(2e_0 - \text{id}, \dots, 2e_{m-1} - \text{id})$ and $Q_0 = \text{diag}(\text{id}, -\text{id}, \dots, -\text{id})$.
2. Let $P_j$ be the permutation matrix interchanging the $0^{\text{th}}$ and $j^{\text{th}}$ copies (with $P_0 = \text{id}$), and let $E_j$ be the diagonal matrix having $e_j$ on every diagonal entry. Define:
   $$S = \sum_{j=0}^{m-1} E_j P_j$$
3. Using the algebraic identities $e_i e_j = \delta_{ij} e_i$, $\sum e_i = \text{id}$, and $e_i^\dagger = e_i$, one verifies directly that $S^2 = \text{id}$, $S^\dagger = S$, and:
   $$S^\dagger Q_0 S = \sum_{j=0}^{m-1} E_j P_j Q_0 P_j = Q$$
This proves that $S$ is an explicit matrix isometry between the sum of twisted forms and $(A, \alpha) \perp (A, -\alpha)^{\perp (m-1)}$, which yields:
$$\sum_{i=0}^{m-1} z_i(t) = 2[A_t, \alpha_t]$$

#### Step 4.5: Finite Quotient Sheets and Serre's Odd-Sphere Argument (Sections 5.3 & 6.4)

##### Lemma 5.6 (Finite Quotient Sheets)
Setting $m = p^k$, faithfulness yields a nonempty open region $V \subset Y \setminus \{y_\infty\}$ over which the map $W/(p^k G) \to W/G$ decomposes into $m$ disjoint trivial sheets. A locally constant multiplier map $\beta: q^{-1}(V) \to S^1$ satisfies $\beta(gw) = \zeta^{\bar{g}}\beta(w)$, where $\zeta = \exp(2\pi i / p^k)$.

##### Proposition 6.7 (Concentrated Equality)
If a test map $h: Y \to S^d$ is constant outside $V$, multiplication by $\beta$ induces a sheaf isometry that cyclically permutes the character parts $D_i = \zeta^i D_0$. Consequently, all character classes associated with $h$ are strictly equal:
$$z_0(h) = z_1(h) = \dots = z_{m-1}(h)$$

##### Serre's Odd-Sphere Argument (Lemma 5.5 & Proposition 5.8)
To deform the test map $a$ into a map constant outside $V$, the paper utilizes Serre's odd-sphere mapping telescope:
$$\mathbb{S} = \text{Tel}\left(S^d \xrightarrow{D_2} S^d \xrightarrow{D_3} S^d \xrightarrow{D_4} \dots\right)$$
1. The infinite mapping telescope $\mathbb{S}$ constructs an Eilenberg–MacLane space $K(\mathbb{Q}, d)$.
2. Serre's finiteness theorem establishes that for odd $d \ge 3$, all higher homotopy groups $\pi_j(S^d)$ ($j > d$) are finite torsion. Postcomposition with a degree-$2q$ map kills elements of order $q$.
3. Thus, a finite composite map $D_s = D_m \circ \dots \circ D_2$ of degree $s > 0$ maps into $K(\mathbb{Q}, d)$, killing the higher obstruction classes and deforming $D_s a$ into a map $h$ that is constant outside $V$.

```
     aq: W^+ ---> Y ---> S^d  (Averaged Test, deg = 1)
               |
               v [Serre Mapping Telescope D_s = D_m ◦ ... ◦ D_2]
               |
     h: W^+ ---> Y ---> S^d  (Concentrated Map, constant outside V, deg = s)
               |
               +---> Cyclic Sheet Permutation via β
               |
               v
     z_0(h) = z_1(h) = ... = z_{m-1}(h)  (Equal Character Classes)
```

#### Step 4.6: The Final Contradiction (Theorem 6.8)

##### Differentiating Rational vs. Integral Algebra
1.  Pushing the classes along $D_s$ and using homotopy invariance gives:
    $$D_{s*} z_i(a) = z_i(D_s a) = z_i(h) = z_j(h) = D_{s*} z_j(a)$$
2.  By Proposition 4.8, $D_{s*}$ acts on $E_d(S^d) \otimes \mathbb{Q} = \mathbb{Q} u_d$ as multiplication by the scalar $s > 0$.
3.  Canceling the non-zero rational scalar $s$ proves that the rational images are equal:
    $$z_0(a) = z_1(a) = \dots = z_{m-1}(a) \in E_d(S^d) \otimes \mathbb{Q}$$
4.  Crucially, canceling $s$ as a scalar does *not* alter the underlying integral classes $z_i(a)$, which remain elements of the fixed integral lattice $L_d^{-1}\mathbb{Z}u_d$.

##### Derivation of the Constant $4u_d$ and Numerical Contradiction
The evaluation of the sum $\sum_{i=0}^{m-1} z_i(a) = 4u_d$ follows a precise two-step arithmetic breakdown:
1.  **Factor of 2 from Real Rank:** The complex coefficient sheaf $\mathbb{C}_{S^d}$ is a two-dimensional real vector space (the real plane $\mathbb{R}^2$ with coefficient pairing $B(z,w) = \text{Re}(z\bar{w})$). Pushing this two-dimensional real coefficient pairing gives:
    $$[A_a, \alpha_a] = 2(aqc)_* u_d = 2u_d$$
2.  **Factor of 2 from Involution Identity:** The sum identity for character classes established in Proposition 6.4 contributes the second factor of 2:
    $$\sum_{i=0}^{m-1} z_i(a) = 2[A_a, \alpha_a] = 2 \times (2u_d) = 4u_d$$

Because all $m = p^k$ rational images are equal and sum to $4u_d$, each individual class must equal:
$$z_i(a) = \frac{4}{p^k} u_d$$

##### Conclusion
Membership in the fixed sphere lattice requires:
$$\frac{4}{p^k} u_d \in L_d^{-1}\mathbb{Z}u_d \implies p^k \le 4L_d$$
Because $L_d = 2^{e_d}$ was fixed by the sphere dimension $d$ *before* choosing $k$ or $p$, choosing $k$ sufficiently large such that $p^k > 4L_d$ yields a direct numerical contradiction ($0 < \frac{4L_d}{p^k} < 1$).

Thus, no continuous action of $\mathbb{Z}_p$ on a topological manifold can be faithful. Theorem 1.2 is established, and Theorem 1.1 follows immediately.

---

### 5. Scope, Context, and Current Status

*   **Authoring Context:** The analyzed preprint titled *"The Hilbert–Smith conjecture in every finite dimension"* is an AI-generated manuscript produced by OpenAI, dated September 23, 2026.
*   **Formalization Status:** As of the document date, the proof has not been formalized in interactive theorem provers such as Lean.
*   **Scope Boundaries:** The proof applies universally to all finite-dimensional topological manifolds without boundary of dimension $n \ge 1$. It makes no restrictions on compactness, global orientability, or triangulability, handles arbitrary point stabilizers, and requires no boundary conditions.

---

### 6. Mathematical Glossary

| Technical Term | Grounded Mathematical Definition |
| :--- | :--- |
| **Faithful Action** | An action of a group $G$ on a space $M$ where the kernel is trivial (only the identity element fixes every point). |
| **Joint Continuity** | Continuity of the evaluation map $G \times M \to M$ simultaneously in both variables. |
| **$p$-adic Integers ($\mathbb{Z}_p$)** | The additive topological group defined by the inverse limit $\varprojlim_{k} \mathbb{Z}/p^k\mathbb{Z}$ equipped with the profinite topology. |
| **Compact-Source Sheaf Category $\mathcal{T}(X)$** | The thick subcategory of $D^b(\text{Sh}_{\mathbb{R}}(X))$ generated under sums, shifts, cones, and summands by proper direct images $Rf_*\mathbb{R}_B$ from compact finite polyhedra $B$. |
| **Verdier Duality ($D_X$)** | The derived functor $R\mathcal{H}om(-, \omega_X)$ providing internal duality for sheaves on locally compact spaces. |
| **Triangular Witt Group ($W_r$)** | The Grothendieck group of non-singular symmetric forms for shifted duality $D_{X,r} = [-r]D_X$ (exactness sign $\delta_r = (-1)^r$), modulo neutral forms with triangular lagrangians. |
| **Dense Subcategory Inclusion** | A full subcategory inclusion $\mathcal{A} \subset \mathcal{C}$ where every object in $\mathcal{C}$ is a direct summand of an object in $\mathcal{A}$. |
| **Character Class ($z_i$)** | The integral Witt class in $E_d(X)$ associated with a character partition $D_i \subset \Lambda$ via self-adjoint involutions $2e_i - \text{id}$. |
| **Serre Odd-Sphere Map ($D_s$)** | A positive degree map $S^d \to S^d$ obtained from finite stages of Serre's $K(\mathbb{Q},d)$ mapping telescope that kills higher finite torsion homotopy groups. |