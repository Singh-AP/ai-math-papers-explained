# Matrix Multiplication in $O(n^{9/4+\epsilon})$ Time: A Developer's Guide to the 2.25 Exponent

## 1. The Problem: Matrix Multiplication and Algorithm Complexity

Matrix multiplication is one of the most fundamental operations in computer science, serving as the computational engine for computer graphics, machine learning, physical simulations, and graph algorithms. Given two $n \times n$ matrices $A$ and $B$, the goal is to compute their product $C = AB$.

### Schoolbook Algorithm
The straightforward algorithm taught in introductory software engineering courses computes each entry $c_{ij} = \sum_{k=1}^n a_{ik} b_{kj}$ using $n$ scalar multiplications and $n-1$ scalar additions. Because the product matrix contains $n^2$ entries, the algorithm requires $n^3$ scalar multiplications and $n^2(n-1)$ additions, establishing a baseline arithmetic time complexity of $O(n^3)$.

### Strassen's Breakthrough
In 1969, Volker Strassen made the shocking discovery that $2 \times 2$ matrix multiplication can be performed using only 7 scalar multiplications instead of the standard 8. By applying this reduction recursively to $n \times n$ matrices partitioned into $n/2 \times n/2$ submatrices, Strassen derived the divide-and-conquer recurrence relation:

$$T(n) = 7T(n/2) + O(n^2)$$

By the Master Theorem, this yields an exact arithmetic complexity of $O(n^{\log_2 7}) \approx O(n^{2.8073})$, proving that matrix multiplication can be executed faster than cubic time.

### Tensors, Legs, and Tensor Rank
To systematically optimize matrix multiplication beyond $2 \times 2$ blocks, computer scientists model bilinear operations using trilinear forms (tensors). The tensor encoding $n \times n$ matrix multiplication, denoted $T_n$, is defined as:

$$T_n = \sum_{i,j,k=1}^n x_{ij} y_{jk} z_{ki}$$

The three variable groups—$X = \{x_{ij}\}$, $Y = \{y_{jk}\}$, and $Z = \{z_{ki}\}$—are referred to as the **legs** of the tensor.

The **tensor rank** $R(A)$ of a tensor $A$ is the minimum integer $m$ such that $A$ can be expressed as a sum of $m$ rank-1 (simple) tensors. Tensor rank is monotone, subadditive under direct sums, and submultiplicative under tensor products. The exponent of exact tensor rank is defined as:

$$\nu = \inf_{n \ge 2} \frac{\log R(T_n)}{\log n}$$

> **Developer Perspective: What is Tensor Rank?**
> In practical software engineering terms, the tensor rank $R(A)$ represents the exact count of scalar multiplications required in a division-free, straight-line program executing the bilinear map $A$. Reducing tensor rank directly translates to reducing the instruction count of core scalar multiplication ops in the algorithm's inner loop.

### Definition of $\omega$ (Omega)
The exponent of matrix multiplication over the field of complex numbers $\mathbb{C}$, denoted by $\omega$, is defined as the infimum of all real numbers $\tau$ such that two $n \times n$ matrices can be multiplied using $O_\epsilon(n^{\tau+\epsilon})$ scalar arithmetic operations for any arbitrarily small $\epsilon > 0$:

$$\omega = \inf \{ \tau \in \mathbb{R} : \text{complexity is } O_\epsilon(n^{\tau+\epsilon}) \}$$

The parameter $\epsilon > 0$ represents an arbitrarily small theoretical "slack." The asymptotic notation $O_\epsilon(\cdot)$ explicitly denotes that while the matrix dimension $n$ approaches infinity, both the multiplicative scaling constants and the structural parameters of the underlying recursive algorithm may depend on the chosen $\epsilon$.

---

## 2. A Brief History of Matrix Multiplication Bounds

For over five decades, theoretical upper bounds on $\omega$ have advanced through a sequence of mathematical breakthroughs:

| Year | Researcher(s) | Bound on $\omega$ / Key Innovation |
| :--- | :--- | :--- |
| **1969** | Volker Strassen | $\omega \le \log_2 7 \approx 2.8073$; Recursive $2 \times 2$ matrix reduction using 7 multiplications. |
| **1979–1980** | Dario Bini | Introduced approximate bilinear algorithms (degenerations) and the interpolation lemma converting approximate bounds to exact asymptotic bounds. |
| **1981** | Arnold Schönhage | Proved the Asymptotic Sum Inequality, enabling exponent bounds from simultaneous independent matrix products. |
| **1986–1988** | Volker Strassen | Developed the Laser Method and the Asymptotic Spectrum of Tensors (tensor characters as spectral invariants). |
| **1990** | Don Coppersmith & Shmuel Winograd | Combined tensor powers with progression-free sets to extract independent matrix products ($\omega < 2.376$). |
| **2010** | Andrew Stothers | Higher-power analysis of the Coppersmith–Winograd tensor construction ($\omega < 2.3737$). |
| **2012–2013** | A. M. Davie & A. J. Stothers; Virginia Vassilevska Williams | Deeper higher-power tensor analyses breaking the $2.373$ threshold ($\omega < 2.37286$). |
| **2014** | François Le Gall | Formulated tensor-power laser method extraction as a convex optimization problem ($\omega < 2.372863$). |
| **2021–2024** | Josh Alman & Virginia Vassilevska Williams | Refined component extraction and analyzed recursive combination barriers ($\omega < 2.372859$). |
| **2023** | Ran Duan, Hongxun Wu, & Renfei Zhou | Introduced asymmetric hashing to bound combination losses across recursion levels. |
| **2024–2025** | Vassilevska Williams, Xu, Xu, & Zhou; Alman et al. | Exploited asymmetric tensor structures yields further reductions ($\omega < 2.37188$). |
| **2026** | E. Dupont et al. | Automated optimization of the combination-loss framework via AlphaEvolve ($\omega < 2.371177$). |
| **2026** | OpenAI Preprint | Combined explicit tensor degenerations with Strassen's spectral viewpoint ($\omega \le 9/4 = 2.25$). |

---

## 3. The Main Result

The paper achieves a major theoretical reduction in the exponent of matrix multiplication, establishing a new upper bound that significantly surpasses decades of incremental refinements:

> **Theorem 1.1.** *For every $\epsilon > 0$, two $n \times n$ complex matrices can be multiplied using $O_\epsilon(n^{9/4+\epsilon})$ arithmetic operations. In particular, $\omega \le 9/4$.*

### Key Technical Aspects:
1. **The 2.25 Barrier:** The value $9/4 = 2.25$ represents a drop from the long-standing $2.37$ regime that persisted through decades of laser-method variations.
2. **Ground Field:** The central proof of Theorem 1.1 is defined over the complex numbers $\mathbb{C}$.
3. **Superseding Companion Bounds:** As confirmed in the associated Lean 4 formalization scope document (`107.md`), the bound $\omega(\mathbb{C}) \le 9/4 = 2.25$ directly implies and supersedes the weaker $2.258$ headline bound established in the companion preprint *"Complex Matrix Multiplication Below 2.258 and Rectangular Bounds"*.

---

## 4. Why It Matters

* **Foundational Complexity:** Matrix multiplication is a foundational primitive in computational complexity theory. Reductions in $\omega$ immediately yield lower theoretical time complexities for a vast range of linear algebra algorithms, including matrix inversion, determinant calculation, LUP decomposition, and solving systems of linear equations.
* **Methodological Paradigm Shift:** For over thirty years, progress on $\omega$ relied almost exclusively on analyzing higher tensor powers of the Coppersmith–Winograd tensor with increasingly complex laser-method refinements. This paper demonstrates that combining explicit tensor degenerations with Strassen's original spectral viewpoint (analyzing numerical invariants on simpler algebraic structures like polynomial multiplication) bypasses the structural "combination-loss" barriers inherent to the laser method.
* **Conceptual Benchmark:** Lowering $\omega$ to $2.25$ moves theoretical matrix multiplication substantially closer to the absolute lower bound of $\omega = 2$ (the time required to read the $O(n^2)$ input entries).

---

## 5. The Proof Architecture

The proof of Theorem 1.1 follows a 6-step pipeline bridging spectral theory, tensor degeneration, discrete Fourier filtering, and polynomial multiplication profiles.

```
+-------------------------------------------------------------------+
| Step 1: Spectral Reduction via Tensor Characters                  |
| Bounding w reduces to character bounds: \lambda(T_m) = m^{3t}      |
+-------------------------------------------------------------------+
                                  |
                                  v
+-------------------------------------------------------------------+
| Step 2: Shared-Leg Separation & Entropy                           |
| Prop 3.1 & Cor 3.2: A^{\oplus 5M} --> \bigoplus (A_h \otimes B_X(M))|
+-------------------------------------------------------------------+
                                  |
                                  v
+-------------------------------------------------------------------+
| Step 3: Symmetrized Profile P(a,b) of Polynomial Multiplication   |
| Geometric mean across 6 permutations: P(a,b) <= (a + b - 1)^{1/t} |
+-------------------------------------------------------------------+
                                  |
                                  v
+-------------------------------------------------------------------+
| Step 4: Structural Inequalities (Lemmas 4.1 & 4.2)                |
| Discrete Concavity: 2P(a,b) >= P(a, b+1) + P(a, b-1)              |
| Shifted Tripling:  P(a, 3h + a - 1) >= 3P(a, h)                    |
+-------------------------------------------------------------------+
                                  |
                                  v
+-------------------------------------------------------------------+
| Step 5: Diagonal Growth and Exponent Squeeze                      |
| Lemma 5.1: P(a,a) >= a^{4/3} ==> a^{4/3} <= (2a-1)^{1/t}          |
| As a --> \infty, t <= 3/4 ==> 3t <= 9/4 ==> \nu <= 9/4            |
+-------------------------------------------------------------------+
                                  |
                                  v
+-------------------------------------------------------------------+
| Step 6: Strassen-Style Recursive Complexity                       |
| Exact rank decomposition gives S(N) <= r S(N/u) + C(N/u)^2         |
| Solves to O_\epsilon(n^{9/4 + \epsilon}) arithmetic operations    |
+-------------------------------------------------------------------+
```

> **Developer Perspective: What is Tensor Degeneration ($A \rightsquigarrow B$)?**
> Mathematically, $A \rightsquigarrow B$ means $B$ is an "approximate" algorithm that degenerates from $A$. In software engineering terms, think of degeneration as introducing a continuous perturbation parameter $\epsilon$ into variable weightings. Terms with positive powers of $\epsilon$ act as lower-order noise that vanish as $\epsilon \to 0$. Bini's interpolation technique guarantees that any approximate bilinear algorithm executing $B$ with error terms can be converted into an exact asymptotic algorithm without incurring an exponent penalty.

### Step 1: Spectral Reduction via Detecting Characters (Lemma 2.2 & Section 2.1)
Strassen's asymptotic spectrum characterizes tensor complexity using **tensor characters**: maps $\lambda: S \to \mathbb{R}_{\ge 0}$ from the tensor semiring to non-negative real numbers that are additive on direct sums ($\lambda(A \oplus B) = \lambda(A) + \lambda(B)$), multiplicative on tensor products ($\lambda(A \otimes B) = \lambda(A)\lambda(B)$), monotone under restriction ($\lambda(A) \ge \lambda(B)$ if $A \ge B$), and normalized such that $\lambda(1) = 1$.

* **Lemma 2.2 (Detecting Characters):** For integers $d \ge 2$ and $k < d^\nu$, there exists a tensor character $\lambda$ such that $\lambda(T_d) \ge k$. This reduces the global task of bounding $\nu$ (and $\omega$) to establishing upper bounds on character values for matrix multiplication.
* **Dot-Product Exponents:** Define oriented dot-product tensors as $B_X(m) = x \sum_{i=1}^m y_i z_i$ (and cyclic permutations $B_Y(m), B_Z(m)$). For any character $\lambda$, there exist real exponents $p_X, p_Y, p_Z \in [0, 1]$ such that:
  $$\lambda(B_X(m)) = m^{p_X}, \quad \lambda(B_Y(m)) = m^{p_Y}, \quad \lambda(B_Z(m)) = m^{p_Z}$$
* Because the product $B_X(m) B_Y(m) B_Z(m)$ is isomorphic to $T_m$, evaluating character values yields:
  $$\lambda(T_m) = m^{p_X + p_Y + p_Z} = m^{3t}$$
  where $t = (p_X + p_Y + p_Z)/3 > 0$ represents the mean dot-product exponent parameter.

### Step 2: Shared-Leg Separation and Entropy (Prop 3.1 & Cor 3.2)
To extract independent direct sums from sub-blocks that share a leg, Proposition 3.1 constructs an explicit degeneration mechanism using discrete Fourier projection filters.

* **Proposition 3.1 (Finite Separation):** Let $A = \sum_{h=1}^M A_h$ where the blocks $A_h \in X \otimes Y_h \otimes Z_h$ share the first leg space $X$ but have pairwise disjoint coordinate spaces on $Y$ and $Z$. Then taking $L = 5M$ copies degenerates into $M$ fully independent direct-sum blocks, each augmented by an $M$-dimensional dot-product factor:
  $$A^{\oplus 5M} \rightsquigarrow \bigoplus_{h=1}^M \left( A_h \otimes B_X(M) \right)$$
* **Construction Mechanics:**
  1. Let $\zeta$ be a primitive $L$-th root of unity ($L = 5M$). Source copies are indexed by $r = 0, \dots, L-1$.
  2. Target variables $X_{a,g}, Y_{h,b,u}, Z_{h,c,v}$ receive phase substitutions:
     $$x_a^{(r)} \mapsto \sum_{g=1}^M \zeta^{2rg} X_{a,g}, \quad y_{h,b}^{(r)} \mapsto \sum_{u=1}^M \zeta^{r(u-h)} Y_{h,b,u}, \quad z_{h,c}^{(r)} \mapsto \frac{1}{L} \sum_{v=1}^M \zeta^{r(-v-h)} Z_{h,c,v}$$
  3. Summing over $r$ forms a discrete Fourier projection filter multiplying terms by $\frac{1}{L} \sum_{r=0}^{L-1} \zeta^{r[u-v+2(g-h)]}$, enforcing the modular constraint $u - v + 2(g - h) \equiv 0 \pmod L$. Because $|u - v + 2(g - h)| \le 3(M-1) < L$, this exact equality holds over the integers:
     $$u - v + 2(g - h) = 0 \implies v - u = 2(g - h)$$
  4. Assign variable weights $w(X_{a,g}) = g^2$, $w(Y_{h,b,u}) = hu - h^2$, and $w(Z_{h,c,v}) = -hv$. Total weight evaluates to:
     $$\text{Total Weight} = g^2 + hu - h^2 - hv = g^2 - h^2 - h(v - u) = g^2 - h^2 - 2h(g - h) = (g - h)^2 \ge 0$$
  5. Filtering for weight-zero terms forces $(g - h)^2 = 0 \implies g = h$, isolating $g=h$ and enforcing $u=v$. This isolates the direct-sum blocks while appending $B_X(M)$.
* **Corollary 3.2 (Shared-Leg Entropy Inequality):** Combining Proposition 3.1 with fixed-frequency word counting and Stirling's approximation yields, for any character $\lambda$ and probability vector $q = (q_1, \dots, q_s)$:
  $$\lambda(T) \ge e^{p_X H(q)} \prod_{i=1}^s \lambda(T_i)^{q_i}$$
  where $H(q) = -\sum_{i=1}^s q_i \log q_i$ is the natural Shannon entropy function.

### Step 3: Symmetrized Profile of Polynomial Multiplication (Section 4)
The polynomial multiplication tensor $C(a,b) = \sum_{i=0}^{a-1} \sum_{j=0}^{b-1} x_i y_j z_{i+j}$ represents multiplication of binary homogeneous forms of degrees $a-1$ and $b-1$. Its exact rank is:

$$R(C(a,b)) = a + b - 1$$

To eliminate directional bias across variable legs, define the **symmetrized profile** $P(a,b)$ as the geometric mean over all 6 leg permutations $\pi \in S_3$:

$$P(a,b) = \left( \prod_{\pi \in S_3} \lambda_\pi(C(a,b)) \right)^{1/(6t)}$$

where $\lambda_\pi(A) = \lambda(\pi(A))$ and $\sum_{\pi \in S_3} p_X^{(\pi)} = 2(p_X + p_Y + p_Z) = 6t$.

The profile $P(a,b)$ satisfies the baseline properties:
1. Symmetry: $P(a,b) = P(b,a) > 0$
2. Boundary evaluation: $P(1,b) = b$
3. Upper ceiling (via interpolation rank bound): $P(a,b) \le (a + b - 1)^{1/t}$

### Step 4: Structural Inequalities for $P(a,b)$ (Lemmas 4.1 & 4.2)

1. **Lemma 4.1 (Discrete Concavity):** For $a \ge 1, b \ge 2$:
   $$2P(a,b) \ge P(a, b+1) + P(a, b-1)$$
   * **Derivation & Algebra:** Tensoring $C(a,b)$ with $B_X(2)$ represents multiplication on doubled spaces. Applying the degree-one Clebsch–Gordan determinant exact sequence $0 \to D V_{e-1} \to V_e \otimes W_1 \to V_{e+1} \to 0$ (where $D = uw - vs$) decomposes the tensor into quotient and kernel spaces, degenerating into $C(a, b+1) \oplus C(a, b-1)$ sharing the $X$-leg.
   * Applying Corollary 3.2 for a specific permutation $\pi$ yields:
     $$\lambda_\pi(C(a,b) \otimes B_X(2)) = \lambda_\pi(B_X(2)) \lambda_\pi(C(a,b)) = 2^{p_X^{(\pi)}} \lambda_\pi(C(a,b)) \ge e^{p_X^{(\pi)} H(q)} \lambda_\pi(C(a,b+1))^{q_+} \lambda_\pi(C(a,b-1))^{q_-}$$
   * Taking the product over all six permutations $\pi \in S_3$, the product of the left-hand factors becomes:
     $$\prod_{\pi \in S_3} 2^{p_X^{(\pi)}} = 2^{\sum_{\pi \in S_3} p_X^{(\pi)}} = 2^{6t}$$
   * Taking the $(6t)^{-1}$ power of the product of both sides cleanly converts $2^{6t}$ into $2$, yielding:
     $$2 P(a,b) \ge e^{H(q)} P(a, b+1)^{q_+} P(a, b-1)^{q_-}$$
   * Optimizing over the probability vector $q = (q_+, q_-)$ via the weighted arithmetic-geometric mean inequality maximizes $e^{H(q)} A^{q_+} B^{q_-}$ at $A + B$, establishing discrete concavity.

2. **Lemma 4.2 (Shifted Tripling):** For all positive integers $a, h$:
   $$P(a, 3h + a - 1) \ge 3 P(a,h)$$
   * **Derivation:** Partitioning $Y$- and $Z$-indices into left, middle, and right sectors and assigning weight $+1$ to middle $Y$ and $-1$ to middle $Z$ yields a weight-zero degeneration into three matched sectors, each isomorphic to $C(a,h)$ (up to leg permutations and basis reversals).

### Step 5: Diagonal Growth and Exponent Squeeze (Lemma 5.1 & End of Proof)
* **Lemma 5.1 (Diagonal Growth):** By discrete concavity, increments $\Delta_{a,h} = P(a, h+1) - P(a,h)$ are nonincreasing in $h$. Combining shifted tripling with $h = a$ and defining $D_a = P(a,a)$ and $H_a = \frac{2D_a}{3a-1}$ yields:
  $$2D_a \le P(a, 4a-1) - D_a = \sum_{h=a}^{4a-2} \Delta_{a,h} \le (3a-1)\Delta_{a,a} \implies \Delta_{a,a} \ge H_a$$
  Symmetry and concavity give $D_a - D_{a-1} = \Delta_{a-1,a-1} + \Delta_{a,a-1} \ge H_{a-1} + H_a$. Rearranging and iterating from $H_1 = 1$:
  $$H_a \ge \prod_{m=1}^{a-1} \left( 1 + \frac{1}{3m} \right) \implies H_a^3 \ge \prod_{m=1}^{a-1} \left( 1 + \frac{1}{3m} \right)^3 \ge \prod_{m=1}^{a-1} \left( 1 + \frac{1}{m} \right) = a \implies H_a \ge a^{1/3}$$
  Because $D_a = P(a,a) = \frac{3a-1}{2} H_a$, and noting that $\frac{3a-1}{2} \ge a$ for all $a \ge 1$:
  $$P(a,a) = \frac{3a-1}{2} H_a \ge a \cdot a^{1/3} = a^{4/3}$$
* **Squeezing $t$:** Comparing lower diagonal growth $P(a,a) \ge a^{4/3}$ with upper ceiling $P(a,a) \le (2a-1)^{1/t}$:
  $$a^{4/3} \le (2a-1)^{1/t}$$
  Taking $a \to \infty$ forces $t \le 3/4$.
* **Consequence for Exponents:** Since $3t \le 9/4$, character values satisfy $\lambda(T_d) \le d^{9/4}$. Choosing $k_d = \lceil d^\nu \rceil - 1 < d^\nu$, Lemma 2.2 supplies a character with $\lambda(T_d) \ge k_d$, forcing $d^\nu \le d^{9/4} + 1$. Taking $d \to \infty$ proves:
  $$\nu \le \frac{9}{4} = 2.25$$

### Step 6: Strassen-Style Recursion
Converting $\nu \le 9/4$ into an arithmetic complexity algorithm uses recursive composition. Fixing $\epsilon > 0$ and $0 < \delta < \epsilon$, there exists a block dimension $u \ge 2$ with an exact rank decomposition of $T_u$ of length $r < u^{9/4+\delta}$. Applying this algorithm recursively to matrices of size $N = u^k$ yields:

$$S(N) \le r S(N/u) + C_{u,r}(N/u)^2$$

Solving this recurrence gives $S(N) = O(N^{\log_u r}) = O(N^{9/4+\delta}) = O_\epsilon(N^{9/4+\epsilon})$. Matrix dimensions $n$ not equal to a power of $u$ are padded to the nearest power of $u$, completing the proof of Theorem 1.1.

---

## 6. Intellectual Lineage: Key Contributors

This breakthrough synthesizes foundational concepts developed by theoretical computer scientists and mathematicians over six decades:

| Contributor | Key Theoretical Contribution(s) Utilized |
| :--- | :--- |
| **Volker Strassen** | Recursive divide-and-conquer for matrix multiplication (1969); Laser Method, Asymptotic Spectrum of Tensors, and character framework (1986–1988). |
| **Dario Bini** | Tensor degenerations (approximate bilinear algorithms) and the Interpolation Lemma (Lemma 2.3) converting degenerations to exact asymptotic bounds. |
| **Arnold Schönhage** | Asymptotic Sum Inequality (1981) for simultaneous independent matrix computations. |
| **Don Coppersmith & Shmuel Winograd** | High-tensor-power extraction techniques and progression-free sets (1990). |
| **François Le Gall** | Convex optimization framework for analyzing tensor powers (2014). |
| **Alfred Tychonoff** | Schauder–Tychonoff Fixed Point Theorem (1935), used in Appendix A to guarantee the existence of detecting characters. |

---

## 7. Limitations and Open Questions

* **$\omega = 2$ Remains Open:** Although establishing $\omega \le 2.25$ represents a breakthrough, it does not achieve the theoretical lower bound of $\omega = 2$.
* **Non-Constructive Existence Proof:** The proof establishes the asymptotic bound $\omega \le 9/4$ non-constructively. It does not provide explicit low-rank tensor decompositions for practical, finite matrix sizes encountered in software engineering.
* **Arithmetic vs. Bit Complexity:** The arithmetic model counts pure scalar operations (additions, subtractions, multiplications) over $\mathbb{C}$. It ignores bit-level precision, floating-point rounding errors, memory bandwidth limitations, and CPU cache hierarchies.
* **Field Restriction and General Field Bounds:** Theorem 1.1 is proven over the complex numbers $\mathbb{C}$. However, as detailed in the companion formalization paper *"Staggered extraction for exact matrix multiplication over every field"* and confirmed in `107.md`, there exists a separate unconditional bound of $\omega(F) < 2.371054886006746$ for every general field $F$ (including finite fields and fields of positive characteristic).
* **Preprint & Lean Formalization Scope:** The main paper is an unreviewed 2026 preprint. The accompanying Lean formalization scope document (`107.md`) confirms machine-checked proofs for:
  - Square exponent bound: $\omega(\mathbb{C}) \le 9/4 = 2.25$
  - Dual exponent bound: $\alpha > 0.465$ (where $\alpha$ is the supremum of rectangular aspect ratios $k$ attainable with exponent 2, i.e., multiplying $n \times n^k$ by $n^k \times n$ matrices in $O(n^{2+\epsilon})$ operations)
  - Rectangular exponent bound: $\omega(\mathbb{C}; 1, 0.709, 1) < 2.092$
  - Unconditional field bound: $\omega(F) < 2.371054886006746$

---

## 8. Glossary of Key Terms and Notation

| Term / Symbol | Definition / Context |
| :--- | :--- |
| **$\omega$ (Omega)** | The exponent of matrix multiplication; the infimum of $\tau$ such that $n \times n$ matrices can be multiplied in $O_\epsilon(n^{\tau+\epsilon})$ scalar arithmetic operations. |
| **$\nu$ (Nu)** | The exponent of exact tensor rank for matrix multiplication ($R(T_n) \ge n^\nu$). |
| **$T_n$** | The trilinear form (tensor) encoding $n \times n$ matrix multiplication: $\sum_{i,j,k=1}^n x_{ij} y_{jk} z_{ki}$. |
| **$R(A)$** | Tensor rank; the minimum number of scalar multiplications needed to execute bilinear map $A$. |
| **Legs ($X, Y, Z$)** | The three variable groups of a trilinear form / tensor. |
| **$\lambda$** | Tensor character; a normalized, additive, multiplicative, restriction-monotone map $S \to \mathbb{R}_{\ge 0}$. |
| **$B_X(m), B_Y(m), B_Z(m)$** | Oriented $m$-dimensional dot-product tensors (e.g., $B_X(m) = x \sum_{i=1}^m y_i z_i$). |
| **$p_X, p_Y, p_Z$** | Dot-product character exponents, where $\lambda(B_X(m)) = m^{p_X}$. |
| **$t$** | Mean dot-product exponent parameter: $t = (p_X + p_Y + p_Z)/3 > 0$. |
| **$C(a,b)$** | Polynomial multiplication tensor for binary homogeneous forms of degrees $a-1$ and $b-1$. |
| **$P(a,b)$** | Symmetrized character profile of polynomial multiplication across all 6 leg permutations in $S_3$. |
| **$A \rightsquigarrow B$** | Tensor degeneration; $A$ degenerates to $B$ via variable weighting and taking minimum weight terms. |
| **$H(q)$** | Natural Shannon entropy function: $H(q) = -\sum q_i \log q_i$. |
| **Dual Exponent ($\alpha$)** | The supremum of rectangular aspect ratios $k$ such that $n \times n^k$ and $n^k \times n$ matrices can be multiplied in $O(n^{2+\epsilon})$ time ($\alpha > 0.465$). |