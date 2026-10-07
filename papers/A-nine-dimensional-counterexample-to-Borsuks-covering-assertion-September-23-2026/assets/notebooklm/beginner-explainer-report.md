# Understanding the Nine-Dimensional Counterexample to Borsuk's Conjecture: A Beginner-Friendly Explainer

## 1. The Core Problem: Diameter and Covering Subsets

A **bounded set** is any collection of points in Euclidean space that can be fully enclosed within a sphere of finite radius. For any bounded set $Y$, its **diameter**, denoted $\text{diam}(Y)$, is defined as the least upper bound (or maximum distance) between any two points belonging to $Y$. This geometric quantity measures the maximal spread of the set across space.

In 1933, mathematician Karol Borsuk posed a fundamental question regarding how geometric sets can be partitioned into smaller pieces. **Borsuk's Question** asks whether every bounded set $Y \subset \mathbb{R}^d$ of positive diameter can be partitioned or covered by $d + 1$ subsets, where each subset has a strictly smaller diameter than $Y$. The quantity $b(Y)$ denotes the minimum number of strictly smaller-diameter subsets needed to cover $Y$, and Borsuk conjectured that $b(Y) \le d + 1$ for all bounded sets in $d$-dimensional space.

To understand why $d + 1$ subsets might be required, consider the geometry of a **regular simplex** in $d$-dimensional space $\mathbb{R}^d$. A regular simplex possesses $d + 1$ vertices that are all mutually equidistant from one another. To reduce the overall diameter of the set, no two vertices can share the same covering subset, forcing the use of at least $d + 1$ distinct subsets. Similarly, a smooth $d$-dimensional **ball** requires at least $d + 1$ subsets to reduce its diameter, a classic result proven by Borsuk for dimensions $d = 1, 2, 3$.

---

## 2. Historical Background: The Search for High-Dimensional Counterexamples

For decades, Borsuk's conjecture was believed to hold true across all dimensions. However, in 1993, Jeff Kahn and Gil Kalai disproved the conjecture in high dimensions using algebraic combinatorics. Their proof applied the Frankl-Wilson forbidden-intersection theorem to demonstrate that the required number of smaller-diameter subsets grows exponentially relative to the dimension.

Following Kahn and Kalai's breakthrough, researchers focused on reducing the minimum dimension $d$ required to construct a valid counterexample. Early reductions relied on discrete set constructions and distance graphs, which steadily lowered the dimension bound from 946 down to 560. Subsequent work leveraged spherical codes derived from lattice packings, followed by two-distance sets constructed from strongly regular graphs.

In 2026, a major breakthrough reduced the counterexample dimension down to 9. Unlike previous low-dimensional constructions that relied on large, finite point configurations, this approach constructs a compact continuous space of rank-one orthogonal projectors embedded in nine-dimensional Euclidean space. This transition from discrete point sets to smooth geometric manifolds resolved a long-standing boundary in geometric topology.

| Year / Milestone | Researcher(s) | Dimension Bound | Method / Approach Key |
| :--- | :--- | :--- | :--- |
| **1933** | Karol Borsuk | Holds for $d \le 3$ | Posed the partition question and proved $b(Y) \le d+1$ for $d \le 3$. |
| **1993** | Kahn and Kalai | High dimensions | Disproved conjecture using Frankl-Wilson forbidden-intersection theorem. |
| **Early Reductions** | Nilli | 946 | Combinatorial set constructions. |
| **Early Reductions** | Grey and Weissbach | 903 (announced) | Geometric and combinatorial boundary reductions. |
| **Early Reductions** | Raigorodskii | 561 | Distance graphs and discrete point sets. |
| **Early Reductions** | Weissbach | 560 | Combinatorial point configurations. |
| **Spherical Codes Era** | Hinrichs | 323 | Spherical codes derived from Leech lattice vectors. |
| **Spherical Codes Era** | Pikhurko | 321 | Optimized spherical codes and lattice packings (2002). |
| **Spherical Codes Era** | Hinrichs and Richter | 298 | Spherical codes and lattice configurations (2003). |
| **Strongly Regular Graphs** | Bondarenko | 65 | Two-distance sets derived from strongly regular graphs. |
| **Strongly Regular Graphs** | Jenrich and Brouwer | 64 | Graph-theoretic constructions and strongly regular graphs. |
| **Finite Configurations** | Grinsztajn | 63 | Explicit finite point configuration (2026). |
| **2026 Breakthrough** | OpenAI | 9 | Compact continuous manifold of projectors ($RP^3$ embedded in $\mathbb{R}^9$). |

---

## 3. The Nine-Dimensional Space of Projectors

The mathematical setting for the nine-dimensional counterexample is constructed within the space of real symmetric $4 \times 4$ matrices, denoted $\text{Sym}_4(\mathbb{R})$. A **symmetric matrix** is a square matrix that equals its transpose ($A = A^T$). This vector space is equipped with the **Frobenius inner product** $\langle A, B \rangle_F = \text{tr}(AB)$ and the induced **Frobenius norm** $\|A\|_F = \sqrt{\text{tr}(A^2)}$, where $\text{tr}(\cdot)$ denotes the matrix trace (the sum of diagonal entries). The full vector space $\text{Sym}_4(\mathbb{R})$ has dimension $N_4 = \frac{4(4+1)}{2} = 10$.

By restricting attention to symmetric matrices with trace equal to one, we obtain the affine hyperplane $\{A \in \text{Sym}_4(\mathbb{R}) : \text{tr } A = 1\}$. This hyperplane possesses Euclidean dimension $N_4 - 1 = 10 - 1 = 9$. Within this 9-dimensional Euclidean space, we define the set $X$ as the compact set of rank-one orthogonal projectors onto lines in $\mathbb{R}^4$:
$$X = \{uu^T : u \in \mathbb{R}^4, \|u\| = 1\}$$
Each matrix $P_x = uu^T$ acts as an orthogonal projection operator mapping $\mathbb{R}^4$ onto the line spanned by the unit vector $u$.

The distance between any two projectors $P_x = uu^T$ and $P_y = vv^T$ is determined by the inner product of their underlying unit vectors $u$ and $v$. According to Lemma 2.1 in the paper, the squared Frobenius distance expands as $\|P_x - P_y\|_F^2 = \text{tr}(P_x^2) + \text{tr}(P_y^2) - 2\text{tr}(P_x P_y) = 2 - 2\langle u, v \rangle^2$. Taking the square root yields the distance formula $\|P_x - P_y\|_F = \sqrt{2 - 2\langle u, v \rangle^2}$. Consequently, the maximum possible distance between any two points in $X$ is $\text{diam}(X) = \sqrt{2}$, which occurs if and only if the underlying lines are orthogonal ($\langle u, v \rangle = 0$).

To express points of $X$ explicitly in 9-dimensional Euclidean coordinates, Remark 2.2 provides an isometric mapping from any symmetric matrix $A = (a_{ij}) \in \text{Sym}_4(\mathbb{R})$ on the trace-one hyperplane directly into $\mathbb{R}^9$:
$$\left( \frac{a_{11}-a_{22}}{\sqrt{2}}, \frac{a_{11}+a_{22}-2a_{33}}{\sqrt{6}}, \frac{a_{11}+a_{22}+a_{33}-3a_{44}}{\sqrt{12}}, \sqrt{2}a_{12}, \sqrt{2}a_{13}, \sqrt{2}a_{14}, \sqrt{2}a_{23}, \sqrt{2}a_{24}, \sqrt{2}a_{34} \right)^T$$
The first three components utilize an orthonormal basis for trace-zero diagonal matrices. The remaining six components scale the off-diagonal entries by $\sqrt{2}$ to account for matrix symmetry under the Frobenius norm.

### Worked Example

To illustrate this geometry, consider two explicit unit vectors in $\mathbb{R}^4$:
$$u = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \quad v = \begin{pmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \\ 0 \\ 0 \end{pmatrix}$$
Their inner product is $\langle u, v \rangle = 1(1/\sqrt{2}) + 0 + 0 + 0 = 1/\sqrt{2}$. Constructing their rank-one projection matrices $P_u = uu^T$ and $P_v = vv^T$ gives:
$$P_u = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}, \quad P_v = \begin{pmatrix} 1/2 & 1/2 & 0 & 0 \\ 1/2 & 1/2 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$
Summing the squared entries of the matrix difference $P_u - P_v$ yields $\|P_u - P_v\|_F^2 = (1/2)^2 + (-1/2)^2 + (-1/2)^2 + (-1/2)^2 = 1$, giving a matrix distance of $\|P_u - P_v\|_F = 1$. Evaluating the analytical formula yields $\sqrt{2 - 2(1/\sqrt{2})^2} = \sqrt{2 - 1} = 1$, perfectly matching the matrix result.

We now map these matrices into 9-dimensional Euclidean coordinates $\mathbf{x}, \mathbf{y} \in \mathbb{R}^9$ using the explicit coordinate formula from Remark 2.2. Inserting the entries of $P_u$ into the formula produces $\mathbf{x} = (1/\sqrt{2}, 1/\sqrt{6}, 1/\sqrt{12}, 0, 0, 0, 0, 0, 0)^T$, while inserting the entries of $P_v$ yields $\mathbf{y} = (0, 1/\sqrt{6}, 1/\sqrt{12}, 1, 0, 0, 0, 0, 0)^T$. The standard Euclidean distance between these 9D vectors is:
$$\|\mathbf{x} - \mathbf{y}\|_2 = \sqrt{\left(\frac{1}{\sqrt{2}} - 0\right)^2 + \left(\frac{1}{\sqrt{6}} - \frac{1}{\sqrt{6}}\right)^2 + \left(\frac{1}{\sqrt{12}} - \frac{1}{\sqrt{12}}\right)^2 + (0 - 1)^2} = \sqrt{\frac{1}{2} + 1} = \sqrt{\frac{1}{2} + \frac{1}{2}} = 1$$
This explicit calculation bridges the space of symmetric matrices $\text{Sym}_4(\mathbb{R})$ and standard Euclidean space $\mathbb{R}^9$.

Consider a second case with unit vector $w = (0, 1, 0, 0)^T$, which is orthogonal to $u$ since $\langle u, w \rangle = 0$. The projection matrix is $P_w = ww^T = \text{diag}(0, 1, 0, 0)$. Calculating the Frobenius distance directly gives $\|P_u - P_w\|_F = \sqrt{(1-0)^2 + (0-1)^2} = \sqrt{2}$, confirming that orthogonal lines realize the maximum diameter $\sqrt{2}$.

---

## 4. Main Results: Exact Statements of Theorem 1.1 and Corollary 7.1

The paper establishes its primary mathematical breakthrough in Theorem 1.1, followed by an extension to arbitrary higher dimensions in Corollary 7.1. The **mod-two degree** of a continuous map between manifolds of equal dimension is defined as the parity (even or odd) of the number of preimages of a regular value.

> **Theorem 1.1.** *The compact set*
> $$X = \{uu^T : u \in \mathbb{R}^4, \|u\| = 1\} \subset \{A \in \text{Sym}_4(\mathbb{R}) : \text{tr } A = 1\},$$
> *with the Frobenius metric, has diameter $\sqrt{2}$ and cannot be covered by ten subsets of diameter strictly less than $\sqrt{2}$.*

> **Corollary 7.1.** *For every integer $d \ge 9$, there is a compact subset of $\mathbb{R}^d$ of diameter $\sqrt{2}$ that cannot be covered by $d+1$ subsets of strictly smaller diameter.*

The set $X$ acts as a 9-dimensional counterexample because it is the compact image of real projective three-space ($RP^3$). Because $X$ lies within a 9-dimensional space, Borsuk's conjecture asserts it can be covered by $9 + 1 = 10$ sets of smaller diameter; Theorem 1.1 proves 10 sets are impossible. Corollary 7.1 extends this obstruction to all $d > 9$ by placing a translated copy of $X$ into a 9D subspace and adjoining $s = d - 9$ orthogonal points whose pairwise inner products form a positive definite **Gram matrix** (a square matrix of pairwise inner products between a set of vectors).

---

## 5. Step-by-Step Overview of the Counterexample Proof

### 1. From Diameter Cover to Admissible Map (Lemma 2.4)
Assume for contradiction that $X$ can be covered by 10 sets of diameter strictly less than $\sqrt{2}$. These covering sets can be inflated into slightly larger open sets $U_1, \dots, U_{10}$ while preserving the strictly smaller diameter condition. Pulling these open sets back to real projective space $RP^3$ and applying a smooth partition of unity yields a smooth map $f: RP^3 \to \Delta^9$ defined by coordinate functions $f_1, \dots, f_{10}$.

This map is **admissible**: each coordinate $f_i$ is nonnegative, the coordinates sum to one, and orthogonal lines $x \perp y$ produce disjoint sets of positive coordinate labels ($S(x) \cap S(y) = \emptyset$). The positive coordinate sets form a finite simplicial complex called the **support complex** $K$ on the label set $\{1, \dots, 10\}$. This combinatorial complex records all non-zero coordinate labels assigned by the map.

### 2. Symmetric Matrix Extension & Spheres (Section 3)
To establish topological constraints on $K$, the map $f$ is extended first to positive semidefinite matrices and then to all symmetric matrices. We define the degree-two homogeneous function $H: V \to \mathbb{R}^m$ by $H(v) = \|v\|^2 f([v])$ for non-zero $v$, with $H(0) = 0$. For any positive semidefinite operator $Q$, its extension $E_V(Q)$ is computed via the explicit integration formula over the unit sphere $S(V)$:
$$E_V(Q) = k \int_{S(V)} H(Q^{1/2} u) \, d\mu_V(u)$$
where $\mu_V$ is the rotation-invariant probability measure on $S(V)$.

Any general symmetric matrix $A$ can be uniquely decomposed into its positive and negative parts $A = A^+ - A^-$, whose ranges are orthogonal subspaces. Defining the matrix map $F(A) = E_V(A^+) - E_V(A^-)$ yields a continuous odd map ($F(-A) = -F(A)$) on symmetric matrices. This map satisfies the key trace identities $\|F(A)\|_1 = \text{tr } |A|$ and $\sum_{i} F(A)_i = \text{tr } A$. Normalizing matrices by their trace norm converts $F$ into a continuous odd map $F: \Sigma(V) \to \Sigma_m$ between norm spheres.

### 3. Label Count & Facet Cycle at Equality (Proposition 4.1 & Theorem 4.3)
By the Borsuk-Ulam theorem, a continuous odd map between spheres $S^n \to S^d$ requires $n \le d$. For 4-dimensional vector space $V = \mathbb{R}^4$ ($k=4$), the space of symmetric matrices has dimension $N_4 = \frac{4(4+1)}{2} = 10$. The trace-norm domain sphere has dimension $N_4 - 1 = 9$, forcing the target sphere to have at least $m \ge 10$ labels. At the threshold equality case $m = 10$, the extended map $F$ has a mod-two degree equal to 1.

Because the mod-two degree is odd, every maximal support face (**facet**) of the support complex $K$ must contain exactly $k = 4$ labels, forming tetrahedra. Furthermore, examining local preimage counts demonstrates that the sum of all tetrahedral facets forms a simplicial cycle over $\mathbb{F}_2$. As a consequence, every triangular face (3-label face) in $K$ must belong to a positive even number of tetrahedra.

### 4. Rigid Triangle Systems on Six Labels (Lemmas 5.2 & 5.3)
Restricting an admissible map to an $RP^2$ subspace requires 6 remaining labels and generates a **six-label triangle system**. In this system, every pair of elements belongs to exactly two triangles, and each vertex link graph forms a simple cycle of length 5.

These triangle systems obey strict combinatorial rules. Complementary triples force opposite matching structures across vertex links, and no transposition of two labels can preserve the triangle system. These rigid properties allow local topological features to be propagated globally.

### 5. Combinatorial Obstruction & Final Contradiction (Lemmas 6.1–6.4 & Theorem 6.5)
In the 10-label support complex on $RP^3$, taking the 6-label complement of any tetrahedral facet $S$ forces a six-label triangle system on those 6 labels. Combining these local systems across adjacent tetrahedra establishes that every triangle in $K$ belongs to *exactly* two tetrahedra (Lemma 6.2). Furthermore, Lemma 6.3 proves that edge link components are restricted to short cycles of length 3 or 4.

Lemma 6.4 defines partner blocks $B_y = p^{-1}(y) \cup \{y\}$ among labels, where $p(v)$ is the unique partner label outside $S$ such that $(S \setminus \{v\}) \cup \{p(v)\}$ forms a tetrahedron. The only valid configuration divides 7 labels into $t=3$ blocks of sizes 3, 2, and 2, leaving a set $R$ of 3 remaining labels ($|R| = 3$). The complement of $S$ consists of $R$ plus one omitted element from each of the three blocks.

Selecting two labels $r, s \in R$ and an omitted label $q_2$ from a size-two block $B_2$ forms a triangle $\{r, s, q_2\}$. Every tetrahedron containing $\{r, s, q_2\}$ must contain at least two elements from some block. Because $r$ and $s$ belong to no block, the fourth vertex of any such tetrahedron must be the second element of the size-two block $B_2$.

Consequently, the triangle $\{r, s, q_2\}$ can belong to at most *one* tetrahedron. This directly contradicts Lemma 6.2, which dictates that every triangle in $K$ must belong to *exactly two* tetrahedra. This contradiction completes the proof of Theorem 6.5, establishing that no 10-label admissible map can exist on $RP^3$.

---

## 6. Significance: Why Dimension 9 Matters

The discovery of a 9-dimensional counterexample represents a dramatic breakthrough in distance geometry and geometric topology. It reduces the lowest known dimension in which Borsuk's conjecture fails from 63 (established by Grinsztajn) down to 9.

Beyond the magnitude of the dimension reduction, this result introduces a fundamental conceptual shift in counterexample construction. Previous low-dimensional counterexamples (such as those by Bondarenko, Jenrich-Brouwer, and Grinsztajn) relied on finite point configurations derived from strongly regular graphs. In contrast, this proof utilizes a smooth, compact geometric manifold: real projective three-space ($RP^3$) embedded as rank-one orthogonal projectors in 9D space.

---

## 7. Open Questions in Geometry

Despite resolving the conjecture for dimension 9, several key questions in geometric topology remain unresolved:

*   **Dimensions 4 through 8:** The validity of Borsuk's conjecture remains completely unknown for dimensions $d \in \{4, 5, 6, 7, 8\}$. (The conjecture is known to hold for $d \le 3$).
*   **Exact Value of $b(X)$:** For the 9-dimensional projector set $X$, the proof demonstrates that 10 smaller-diameter sets are insufficient, establishing $b(X) \ge 11$. However, the exact minimum number of smaller-diameter sets needed to cover $X$ remains uncalculated.

---

## 8. Computer-Assisted Formal Verification

To guarantee absolute mathematical correctness, the core counterexample proof has been machine-checked and formally verified using the Lean theorem prover. **Formal verification** uses interactive computer proof assistants to check every logical step against foundational mathematical axioms.

The formal proof is hosted in the open-source repository `openai/math` under the primary formalization target `OAI.BorsukNine.main_theorem` (located in `BorsukNine.lean`). The repository's scope file (`156.md`) documents that the formalization machine-checks the exact geometric setup: verifying that the compact set of rank-one orthogonal projectors in $\mathbb{R}^4$ equipped with the Frobenius metric lies in a 9D affine space of trace-one symmetric matrices, has diameter $\sqrt{2}$, and cannot be covered by 10 sets of smaller diameter.