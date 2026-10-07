# Technical Explainer: Exact Birch–Swinnerton-Dyer Formula from Low Selmer Corank

---

## 1. The Core Problem: From High-School Algebra to the BSD Conjecture

### Elliptic Curves & Rational Points
In high-school algebra, polynomial equations like $y^2 = x^3 + ax + b$ describe planar curves. When the coefficients $a$ and $b$ are rational numbers (and the cubic polynomial $x^3 + ax + b$ has non-zero discriminant, guaranteeing distinct roots), this equation defines an **elliptic curve** $E$ over the rational numbers $\mathbb{Q}$. When given in minimal form, this is called a global minimal Weierstrass equation.

While real solutions $(x,y) \in \mathbb{R}^2$ form a continuous curve, number theory focuses on **rational points**—solutions where both $x$ and $y$ are precise fractions or integers. Including an abstract "point at infinity" denoted by $\mathcal{O}$, the set of rational points $E(\mathbb{Q})$ possesses an algebraic structure: points can be added using a geometric chord-and-tangent construction. 

Under this addition law, $E(\mathbb{Q})$ forms an abelian group. The Mordell–Weil Theorem establishes that $E(\mathbb{Q})$ is finitely generated, decomposing into a finite torsion subgroup and a free algebraic part:
$$E(\mathbb{Q}) \cong E(\mathbb{Q})_{\text{tors}} \oplus \mathbb{Z}^{r(E)}$$
*   **Finite Torsion Subgroup $E(\mathbb{Q})_{\text{tors}}$:** The finite collection of rational points of finite order (points that loop back to the identity $\mathcal{O}$ under repeated group addition).
*   **Free Rank $r(E)$ (Mordell–Weil Rank):** The non-negative integer representing the exact number of independent rational points of infinite order required to generate all remaining rational points. Finding $r(E)$ purely algebraically is computationally difficult.

---

### Local Divisibility: $p$-adic Numbers and $p$-adic Valuations
To bridge high-school arithmetic and modern arithmetic geometry, we examine divisibility by prime numbers. For any prime $p$, the **$p$-adic valuation** $v_p(n)$ of a non-zero integer $n$ measures the exact power of $p$ dividing $n$. Extended to rational numbers $q = a/b$, the valuation is $v_p(a/b) = v_p(a) - v_p(b)$.

The $p$-adic valuation defines a notion of size—the $p$-adic absolute value $|q|_p = p^{-v_p(q)}$—where numbers divisible by high powers of $p$ are considered geometrically "small" or close to $0$. Completing $\mathbb{Q}$ under this metric yields the field of **$p$-adic numbers** $\mathbb{Q}_p$, whose ring of integers is $\mathbb{Z}_p = \{x \in \mathbb{Q}_p : v_p(x) \ge 0\}$. Studying an elliptic curve over $\mathbb{Q}_p$ allows mathematicians to analyze its behavior local to the prime $p$.

---

### The Analytic $L$-function
To inspect $E(\mathbb{Q})$ through analysis, mathematicians build the Hasse–Weil **$L$-function** $L(E,s)$ as an Euler product over all primes $\ell$:
$$L(E,s) = \prod_{\ell} L_\ell(E, s)^{-1}$$
where each local factor $L_\ell(E,s)^{-1}$ encodes the number of solutions to $y^2 \equiv x^3 + ax + b \pmod \ell$. Modularity guarantees that $L(E,s)$ extends analytically to the entire complex plane. The behavior of $L(E,s)$ at its central point $s=1$ defines the **analytic rank** $a(E)$:
$$a(E) = \text{ord}_{s=1} L(E,s)$$
which measures the order of vanishing (the number of vanishing Taylor derivatives) of $L(E,s)$ at $s=1$.

---

### The Full BSD Leading-Term Formula
The qualitative Birch–Swinnerton-Dyer (BSD) conjecture states that $r(E) = a(E)$. The quantitative BSD conjecture goes further, asserting a numerical equality between the first non-zero Taylor coefficient of $L(E,s)$ at $s=1$ and the arithmetic invariants of $E/\mathbb{Q}$:

$$\frac{L^{(r)}(E, 1)}{r!} = \frac{\Omega_E \cdot \text{Reg}_E \cdot \#\text{Sha}(E/\mathbb{Q}) \cdot \prod_{\ell \text{ finite}} c_\ell(E)}{\left(\#E(\mathbb{Q})_{\text{tors}}\right)^2}$$

Every factor in this formula represents a structural invariant of the curve:
*   **$\Omega_E$ (Real Period):** The geometric integral of the Néron differential $\omega_E$ over the real points $E(\mathbb{R})$, defined by $\Omega_E = \int_{E(\mathbb{R})} |\omega_E|$. This integral integrates over both connected components of $E(\mathbb{R})$ when two components are present.
*   **$\text{Reg}_E$ (Regulator):** The volume determinant of the canonical height pairing $B(P_i, P_j)$ computed on a basis $P_1, \dots, P_r$ of the free rational point group $E(\mathbb{Q})/E(\mathbb{Q})_{\text{tors}}$. For a rational point $P$ with $x(P) = a/b$ in lowest terms, its naïve logarithmic height is $h_x(P) = \log \max(|a|, b)$. The canonical height $H(P)$ strips away non-essential local factors via the limit:
    $$H(P) = \lim_{n \to \infty} 4^{-n} h_x([2^n]P)$$
    The associated bilinear canonical height pairing is:
    $$B(P,Q) = \frac{H(P+Q) - H(P) - H(Q)}{2}$$
    The regulator is $\text{Reg}_E = \det(B(P_i, P_j))$. If $r(E) = 0$, $\text{Reg}_E$ is defined to be $1$.
*   **$\#\text{Sha}(E/\mathbb{Q})$ (Order of the Tate–Shafarevich Group):** The cardinality of the Tate–Shafarevich group $\text{Sha}(E/\mathbb{Q}) = \ker\left( H^1(\mathbb{Q}, E) \to \prod_v H^1(\mathbb{Q}_v, E) \right)$. $\text{Sha}(E/\mathbb{Q})$ measures the failure of the Hasse local-global principle for curves of genus 1; it measures the obstruction when local solutions exist across all $p$-adic and real completions but fail to patch together into a global rational point.
*   **$c_\ell(E)$ (Local Tamagawa Numbers):** Finite local component indices $c_\ell(E) = [E(\mathbb{Q}_\ell) : E_0(\mathbb{Q}_\ell)]$, where $E_0(\mathbb{Q}_\ell)$ represents the subgroup of $\mathbb{Q}_\ell$-rational points reducing to non-singular (smooth) points on the special fiber modulo $\ell$.
*   **$\#E(\mathbb{Q})_{\text{tors}}$ (Order of Rational Torsion):** The exact cardinality of the finite rational torsion subgroup.

---

### Selmer Groups & Corank
Because $\text{Sha}(E/\mathbb{Q})$ is difficult to compute directly, number theorists enclose it inside **$p$-power Selmer groups** $\text{Sel}_{p^\infty}(E/\mathbb{Q})$. Defined via Galois cohomology using local Kummer images at every place, the Selmer group fits into the fundamental Kummer exact sequence:
$$0 \longrightarrow E(\mathbb{Q}) \otimes \mathbb{Q}_p/\mathbb{Z}_p \longrightarrow \text{Sel}_{p^\infty}(E/\mathbb{Q}) \longrightarrow \text{Sha}(E/\mathbb{Q})[p^\infty] \longrightarrow 0$$

The $p$-corank of the Selmer group, denoted $s_p(E) = \text{corank}_{\mathbb{Z}_p} \text{Sel}_{p^\infty}(E/\mathbb{Q})$, serves as an algebraic proxy combining the free rank $r(E)$ and the $p$-divisible part of $\text{Sha}(E/\mathbb{Q})$. Specifically, $s_p(E) = r(E) + \text{corank}_{\mathbb{Z}_p} \text{Sha}(E/\mathbb{Q})[p^\infty]$. When $\text{Sha}(E/\mathbb{Q})$ is finite, $s_p(E) = r(E)$ for all primes $p$.

---

## 2. Historical Context & What Was Previously Known

The path toward proving the Birch–Swinnerton-Dyer conjecture has advanced through several foundational breakthroughs, modularity extensions, and Iwasawa-theoretic refinements.

```
+-----------------------------------------------------------------------------------+
| HISTORICAL PROGRESSION TOWARD BSD                                                 |
+-----------------------------------------------------------------------------------+
|  1960s: BSD Experiments & Formalization [1, 29]                                   |
|  * Birch & Swinnerton-Dyer formulate numerical conjectures from computer experiments.|
|  * Tate formalizes BSD for abelian varieties; Cassels proves isogeny invariance [6]|
|                                                                                   |
|  1970s–1980s: Iwasawa Theory for CM Curves [25]                                    |
|  * Rubin proves Iwasawa Main Conjecture for CM elliptic curves over imaginary     |
|    quadratic fields, establishing rank 0/1 leading-term results for CM curves.   |
|                                                                                   |
|  1980s–1990s: Gross–Zagier, Kolyvagin & Modularity [4, 12, 17, 30, 32]             |
|  * Wiles, Taylor–Wiles, Breuil–Conrad–Diamond–Taylor prove modularity of E/Q.      |
|  * Gross–Zagier links L'(E/K,1) to Heegner point heights.                         |
|  * Kolyvagin uses Euler systems to prove r(E) = a(E) and #Sha < inf for a(E) in {0,1}.|
|                                                                                   |
|  2000s–2010s: p-Adic L-Functions & Galois Cohomology [5, 14, 15, 27]             |
|  * Kato applies p-adic zeta elements & reciprocity laws to link L-values to Cohomology.|
|  * Skinner–Urban & Jetchev–Skinner–Wan establish p-primary formulas under         |
|    residual, semistable, or ordinary reduction hypotheses.                        |
|  * Burungale–Flach prove full rank-0 BSD for CM elliptic curves over Q.           |
|                                                                                   |
|  THE GAP: All prior exact p-primary results required severe restrictions           |
|  (good reduction, semistability, residual irreducibility, or CM).                  |
+-----------------------------------------------------------------------------------+
```

### Chronological Milestones and Technical Hypotheses

*   **Foundations (1960s):**
    *   *Birch & Swinnerton-Dyer [1]:* Formulated conjectures based on computer counts of local points.
    *   *Tate [29]:* Formulated the qualitative rank prediction and quantitative leading-term formula in the context of abelian varieties.
    *   *Cassels [6]:* Proved the isogeny invariance of the BSD ratio $Q_E$, demonstrating that the combined quotient $Q_E / \#\text{Sha}(E/\mathbb{Q})$ is the natural arithmetic invariant preserved across $\mathbb{Q}$-isogenous curves.
*   **Modularity & Qualitative Equivalence (1980s–1990s):**
    *   *Wiles, Taylor–Wiles, Breuil–Conrad–Diamond–Taylor [4, 30, 32]:* Established the modularity of all elliptic curves over $\mathbb{Q}$, guaranteeing the analytic continuation and functional equation of $L(E,s)$.
    *   *Gross–Zagier [12] & Kolyvagin [17]:* Gross–Zagier identified $L'(E/K,1)$ with the canonical height of Heegner points. Kolyvagin developed Euler systems of Heegner points to prove that if $a(E) \in \{0, 1\}$, then $r(E) = a(E)$ and $\#\text{Sha}(E/\mathbb{Q}) < \infty$.
*   **Integral Refinements & Iwasawa Theory (1990s–2020s):**
    *   *Rubin [25]:* Proved the Iwasawa Main Conjecture for CM elliptic curves over imaginary quadratic fields, obtaining exact $p$-primary leading-term consequences.
    *   *Kato [15]:* Constructed modular-symbol $p$-adic zeta elements in Galois cohomology, establishing explicit reciprocity laws connecting $L$-values to $p$-adic cohomology.
    *   *Skinner–Urban [27]:* Proved ordinary rank-0 leading-term relations under specific residual Galois representation and ramification hypotheses.
    *   *Jetchev–Skinner–Wan [14]:* Established rank-1 $p$-primary formulas for semistable elliptic curves at good primes under residual irreducibility hypotheses.
    *   *Burungale–Flach [5]:* Proved the full rank-0 BSD formula for CM elliptic curves over $\mathbb{Q}$ via rational descent.

### The Historic Gap
While these breakthroughs established qualitative rank equality ($r(E) = a(E)$) and the finiteness of $\text{Sha}(E/\mathbb{Q})$, **prior exact $p$-primary formulas required restrictive local and residual hypotheses**—such as good reduction at $p$, semistability, residual Galois irreducibility, or complex multiplication. No general framework existed to evaluate the exact formula across all prime factors (including $p=2$ and bad reduction primes) without extra structural assumptions.

---

## 3. The Main Result: Theorem 1.1 and Paper Architecture

The principal result solves this longstanding problem by removing all conditional local and residual hypotheses.

### Statement of Theorem 1.1
> **Theorem 1.1.** *Let $E/\mathbb{Q}$ be an elliptic curve and let $q$ be any prime. If $s_q(E) \in \{0, 1\}$, then:*
> 1. $r(E) = a(E) = s_q(E)$
> 2. $\#\text{Sha}(E/\mathbb{Q}) < \infty$
> 3. *With $r = r(E)$ and standard normalizations, the exact BSD formula holds:*
> $$\frac{L^{(r)}(E, 1)}{r!} = \frac{\Omega_E \cdot \text{Reg}_E \cdot \#\text{Sha}(E/\mathbb{Q}) \cdot \prod_{\ell \text{ finite}} c_\ell(E)}{\left(\#E(\mathbb{Q})_{\text{tors}}\right)^2}$$
> *There are no additional hypotheses on reduction, rational torsion, isogenies, complex multiplication, or residual Galois representations.*

---

### The Three-Paper Division of Labor
The complete proof of Theorem 1.1 relies on a modular division of labor across three companion papers:

1.  **Paper 1: Unrestricted Converse Companion [23]:** Proves Theorem 2.1 (Unrestricted low-corank converse), demonstrating that if $s_q(E) \in \{0,1\}$ for *some* prime $q$, then $r(E) = a(E) = s_q(E)$ and $\#\text{Sha}(E/\mathbb{Q}) < \infty$.
2.  **Paper 2: Two-Primary Companion [24]:** Proves Theorem 2.2 (Two-primary formula), establishing that $Q_E \in \mathbb{Q}_{>0}$ and that the $2$-adic valuation satisfies $v_2(Q_E) = v_2(\#\text{Sha}(E/\mathbb{Q}))$.
3.  **Paper 3: Principal Paper (Oct 3, 2026):** Establishes the exact valuation of the leading-term formula at every odd prime $p > 2$ (Proposition 10.4 / Theorem 1.1), independently of the initial prime $q$ used in the low-corank hypothesis.

---

### Comparison & Architectural Mapping Table

| Paper Title / Source | Core Assertion Proven | Key Inputs / Method | Exact Section Attribution |
| :--- | :--- | :--- | :--- |
| **Converse Companion** ([23]) | $s_q(E) \in \{0,1\} \implies r(E)=a(E)=s_q(E)$ and $\#\text{Sha}(E/\mathbb{Q}) < \infty$. | Rationalized Galois cohomology, Euler systems, and low-corank converse. | Section 2.1, Theorem 2.1 |
| **Two-Primary Companion** ([24]) | $Q_E \in \mathbb{Q}_{>0}$ and $v_2(Q_E) = v_2(\#\text{Sha}(E/\mathbb{Q}))$. | 2-primary Kummer lattices, 2-adic Iwasawa theory, 2-adic line/square switches. | Section 2.1, Theorem 2.2 |
| **Principal Paper** (OpenAI, Oct 3, 2026) | $v_p(Q_E) = v_p(\#\text{Sha}(E/\mathbb{Q}))$ for all odd primes $p > 2$. | Integral Siegel classes, residual concentration, pair comparisons over $K$, theta congruences, central volume specialization. | Sections 1.1–10.2, Theorem 1.1 |

---

## 4. Significance and Applications

Theorem 1.1 represents a milestone in number theory with direct consequences:

*   **Unconditional Full BSD:** It settles the exact Birch–Swinnerton-Dyer formula unconditionally for all elliptic curves over $\mathbb{Q}$ of analytic or Selmer corank 0 or 1.
*   **Exact Size of Sha:** It provides an exact, finite determination of $\#\text{Sha}(E/\mathbb{Q})$, establishing its precise prime-power factorization across all odd and even primes without exceptional sets.
*   **Density-One Quadratic Twist Families:** By incorporating Smith's results on Selmer group distributions [28] alongside analytic twist densities [22] (Theorem 2.5), the theorem shows that 100% (density 1) of quadratic twists $E_d$ of any fixed elliptic curve $A/\mathbb{Q}$ satisfy $a(E_d) \in \{0, 1\}$. Consequently, **the exact BSD formula holds for almost all quadratic twists of every elliptic curve over $\mathbb{Q}$**.
*   **Sums of Two Rational Cubes:** Applying the unrestricted converse companion [23] solves the classical Diophantine problem $x^3 + y^3 = n$ for primes $p \equiv 4, 7, 8 \pmod 9$, unconditionally establishing rank and finiteness bounds without conditional hypotheses.

---

## 5. Step-by-Step Proof Architecture (The Principal Paper)

The principal paper computes $v_p(Q_E) = v_p(\#\text{Sha}(E/\mathbb{Q}))$ for an arbitrary odd prime $p > 2$ through seven steps.

```
+-----------------------------------------------------------------------------------+
| PROOF FLOW CHART (PRINCIPAL PAPER)                                                 |
+-----------------------------------------------------------------------------------+
| STEP 1: Define Discrepancy Metric X_p(E) = v_p(Q_E) - v_p(#Sha(E/Q))             |
|        (BSD holds at p if and only if X_p(E) = 0)                                 |
|                                 |                                                 |
|                                 v                                                 |
| STEP 2: Single-Curve Inequality                                                   |
|        Transfer Kato classes to Iwasawa ring R = Z_p[[t, u_1,..., u_k]]           |
|        Prove X_p(E) >= 0 for non-CM curves via de Rham/height calibrations        |
|        [Prop 5.11, Prop 5.7]                                                      |
|                                 |                                                 |
|                                 v                                                 |
| STEP 3: Auxiliary Imaginary Quadratic Field K & Heegner Points                     |
|        Construct K = Q(sqrt(D)) splitting p & bad primes with a(E_D) = 1 - a(E)   |
|        Define Manin constant c_E via phi* w_E = c_E f(q) dq/q                    |
|        [Lemma 2.6, Theorem 2.7]                                                   |
|                                 |                                                 |
|                                 v                                                 |
| STEP 4: Full-Index Discrepancy Identity                                           |
|        Establish Gross-Zagier restriction-of-scalars sum:                        |
|        X_p(E) + X_p(E_D) = 2(n_P + tau_g) - 2 v_p(c_E) - 2 sum v_p(c_l) - v_p(#Sha) |
|        [Prop 2.8]                                                                 |
|                                 |                                                 |
|                                 v                                                 |
| STEP 5: Pair Comparison & Theta Implications                                      |
|        Construct quotients U_w = B_w / L_w in Frac(R).                            |
|        - Sub-step 5a: Vertical p-primitivity via Chai-Hida rigidity -> U_w in R   |
|        - Sub-step 5b: Horizontal divisor removal via theta congruences            |
|                        -> U_w in R^x (Integral Unit) [Sec 6-9]                    |
|                                 |                                                 |
|                                 v                                                 |
| STEP 6: Central Value Specialization                                              |
|        Specialize U_w in R^x at origin (0, 0) -> X_p(E) + X_p(E_D) = 0           |
|        [Cor 10.2]                                                                 |
|                                 |                                                 |
|                                 v                                                 |
| STEP 7: Resolution for Non-CM and CM Cases                                        |
|        Non-CM: X_p(E) >= 0 and X_p(E_D) >= 0 with sum = 0  =>  X_p(E) = 0         |
|        CM: Combine rank-0 CM formula [5] with sum identity => X_p(E) = 0          |
|        [Lemma 10.3, Prop 10.4]                                                    |
+-----------------------------------------------------------------------------------+
```

### Step 1: The Discrepancy Metric $X_p(E)$
Define the arithmetic quotient $Q_E$ and its $p$-adic arithmetic discrepancy $X_p(E)$ by:
$$Q_E = \frac{L^{(r)}(E,1) \cdot \left(\#E(\mathbb{Q})_{\text{tors}}\right)^2}{r! \cdot \Omega_E \cdot \text{Reg}_E \cdot \prod_\ell c_\ell(E)}, \quad X_p(E) = v_p(Q_E) - v_p\left(\#\text{Sha}(E/\mathbb{Q})\right)$$
where $v_p(p) = 1$. The exact BSD formula holds at the prime $p$ if and only if $X_p(E) = 0$.

---

### Step 2: Single-Curve Inequality $X_p(E) \ge 0$
To establish the lower bound $X_p(E) \ge 0$ for non-CM curves of analytic rank $a(E) \in \{0, 1\}$:
1.  **Iwasawa Diagram Transfer:** Kato’s Euler system of Siegel and modular symbol classes is transferred into finite free models of Galois cochain diagrams over the ring $R = \mathbb{Z}_p[[t, u_1, \dots, u_k]]$, where $t$ is a cyclotomic variable and $u_i$ are tame variables attached to auxiliary primes.
2.  **Central Calibration:**
    *   *Rank 0:* The central coordinate of the normalized determinant is calibrated against modular symbols using explicit $p$-adic de Rham/dual-exponential maps (Section 5.1).
    *   *Rank 1:* An exact $p$-adic tame height pairing and biextension comparison (Section 5.5, Proposition 5.7) connects the derivative class to the canonical point height:
        $$\frac{\log_\omega z^\circ}{\left(\log_\omega P\right)^2} = \pm d_0 \frac{L'(E,1)}{\Omega_0 H(P)}$$
3.  **Result (Proposition 5.11):** The determinant coordinate $U \in R$ specializes at the origin to $v_p(U(0)) = X_p(E)$. Since $U \in R$ is integral, $v_p(U(0)) \ge 0$, establishing $X_p(E) \ge 0$ (Section 1.4 & Section 5).

---

### Step 3: Auxiliary Imaginary Quadratic Field $K$ & Heegner Points
To create an exact duality pairing, an auxiliary imaginary quadratic field $K = \mathbb{Q}(\sqrt{D})$ is constructed using Lemma 2.6:
*   Choose coprime negative odd fundamental discriminants $D, D' < -4$ satisfying the Jacobi symbol condition $\left(\frac{D}{|D'|}\right) = 1$ such that $p$ and all bad reduction primes split in $K$.
*   The analytic ranks satisfy $a(E_D) = 1 - a(E)$, ensuring that $L(E/K, s)$ has a simple zero at $s=1$.
*   Using the modular parametrization $\phi: X_0(N) \to E$, define the **Manin constant** $c_E \in \mathbb{Q}^\times$ via the pullback of the minimal differential:
    $$\phi^* \omega_E = c_E f(q) \frac{dq}{q}$$
*   Define the Heegner point $P_K = \phi_* P_X \in E(K)$ via the Heegner divisor on $X_0(N)$ (Section 2.3).

---

### Step 4: Full-Index Discrepancy Identity
By restriction of scalars ($A = \text{Res}_{K/\mathbb{Q}} E_K \sim E \times E_D$), Gross–Zagier normalization (Theorem 2.7) yields the real arithmetic identity (Proposition 2.8):

$$\frac{Q_E}{\#\text{Sha}(E/\mathbb{Q})} \cdot \frac{Q_{E_D}}{\#\text{Sha}(E_D/\mathbb{Q})} = \frac{[E(K) : \mathbb{Z}P_K]^2}{c_E^2 \cdot \prod_\ell c_\ell(E)^2 \cdot \#\text{Sha}(E/K)}$$

Taking the $p$-adic valuation $v_p$ converts this real product into an additive discrepancy sum (Equation 2.6):
$$X_p(E) + X_p(E_D) = 2(n_P + \tau_g) - 2v_p(c_E) - 2\sum_\ell v_p(c_\ell(E)) - v_p\left(\#\text{Sha}(E/K)\right)$$
where $n_P = v_p\left([E(K)/E(K)_{\text{tors}} : \mathbb{Z}P_K]\right)$ and $\tau_g = v_p\left(\#E(K)_{\text{tors}}\right)$.

> **Geometric Interpretation:** This equation translates a global real product of analytic $L$-values, periods, and canonical heights into an exact additive ledger of $p$-adic error terms. It balances the combined arithmetic discrepancy $X_p(E) + X_p(E_D)$ against the $p$-adic index of the Heegner point lattice $n_P$, local Tamagawa correction factors $c_\ell(E)$, the Manin scaling factor $c_E$, and global Tate–Shafarevich obstruction classes over $K$.

---

### Step 5: Pair Comparison & Theta Implications
Over $K$, the prime $p$ splits as $p\mathcal{O}_K = w\bar{w}$.
1.  **Analytic and Determinant Series:** Construct two determinant series $L_w, L_{\bar{w}} \in R$ by imposing strict local conditions at $w$ and full conditions at $\bar{w}$. Construct companion analytic CM series $B_w, B_{\bar{w}} \in R$ from bounded CM measures (Section 6).
2.  **Sub-step 5a: Vertical $p$-Primitivity via Chai–Hida Rigidity:**
    *   Form the quotient $U_w = B_w / L_w \in \text{Frac}(R)$. Using high-character Weierstrass division (Lemma 3.9), $L_w \mid B_w$ integrally, establishing $U_w \in R$.
    *   Linear independence on ordinary modular curves combined with Chai–Hida rigidity and monodromy on ordinary modular towers (Proposition 6.5) proves $p \nmid B_w$, showing $U_w$ has no factor of $p$ (Corollary 6.9).
3.  **Sub-step 5b: Horizontal Divisor Elimination via Theta Congruences:**
    *   Evaluate at characteristic-zero points $z_0$ where an undepleted CM period vanishes (Lemma 7.2).
    *   A theta-to-cusp comparison produces non-zero classes satisfying strict local conditions.
    *   Adding tame variables forces any simultaneous strict jumps to have codimension at least two (Section 9).
    *   Because a divisor has codimension one, no quotient divisors remain, proving **$U_w \in R^\times$ (an integral unit)**.

---

### Step 6: Center Specialization
Specialize the integral unit $U_w \in R^\times$ at the origin $(t, \mathbf{u}) = (0, \mathbf{0})$. Because $U_w$ is an integral unit, its central valuation is zero:
$$v_p(U_w(0)) = 0 \implies X_p(E) + X_p(E_D) = 0$$
(Section 10, Corollary 10.2).

---

### Step 7: Resolution for Both Non-CM and CM Cases
The proof concludes by analyzing $X_p(E) + X_p(E_D) = 0$ (Lemma 10.3 & Proposition 10.4):
*   **Non-CM Case:** Combining the single-curve inequalities $X_p(E) \ge 0$ and $X_p(E_D) \ge 0$ with the sum identity $X_p(E) + X_p(E_D) = 0$ forces $X_p(E) = 0$.
*   **CM Case:** The rank-0 CM formula of Burungale–Flach [5] establishes $X_p(E_{\text{CM, rank 0}}) = 0$ independently. Substituting this into $X_p(E) + X_p(E_D) = 0$ forces $X_p(E) = 0$ for the rank-1 CM component as well.

In all cases, $X_p(E) = 0$, establishing $v_p(Q_E) = v_p(\#\text{Sha}(E/\mathbb{Q}))$ for every odd prime $p$.

---

## 6. Key Intellectual Contributors and Methodological Inputs

| Researcher / Group | Core Mathematical Contribution | Role in Proof / Section Attribution |
| :--- | :--- | :--- |
| **A. Wiles, R. Taylor, et al.** | Modularity theorem for elliptic curves over $\mathbb{Q}$. | Provides analytic continuation and functional equation of $L(E,s)$ (Section 1.2). |
| **B. Gross, W. Zagier, V. Kolyvagin** | Height formulas, Heegner point constructions, and Euler systems for rank 0 and 1. | Proves qualitative equivalence $r(E)=a(E)$ and finiteness of $\text{Sha}$ for analytic ranks 0/1 (Section 1.2, 2.3). |
| **K. Kato** | Modular symbols, $p$-adic zeta elements, explicit reciprocity laws in Galois cohomology. | Supplies integral Siegel classes and dual-exponential calibrations (Section 1.2, 5.1). |
| **K. Rubin** | Iwasawa Main Conjecture for imaginary quadratic fields. | Foundations for CM Iwasawa theory and CM Euler systems (Section 1.2). |
| **C. Skinner, E. Urban, D. Jetchev, X. Wan** | $p$-Adic $L$-functions and Iwasawa main conjectures for rank 0/1 curves under local conditions. | Provides Iwasawa-theoretic framework and local division inputs (Section 1.2). |
| **A. Burungale, M. Flach** | Full rank-0 BSD formula for CM elliptic curves over $\mathbb{Q}$ via rational descent. | Supplies the rank-0 CM baseline valuation in the final step (Section 1.2, 10.2). |
| **C. Smith** | Distribution of Selmer groups in quadratic twist families. | Used to guarantee density-one non-vanishing in twist families (Section 1.2, 2.2). |
| **J.-P. Serre, F. Bogomolov** | Galois image principles and $p$-adic open image theorems for non-CM curves. | Ensures non-vanishing of Galois evaluations on deep $SL_2(\mathbb{Z}_p)$ subgroups (Section 1.2, 4.1, 5.1, 6.3). |
| **C.-L. Chai, H. Hida** | Rigidity, canonical coordinates, and monodromy on ordinary modular towers. | Proves vertical analytic primitivity ($p \nmid B_w$) via tame-stalk independence (Section 1.2, 6.3). |
| **J. Cassels, J. Milne** | Isogeny invariance of BSD ratio and restriction-of-scalars volume identities. | Validates discrepancy invariance under isogenies and global restriction of scalars (Section 1.2, 2.1). |
| **OpenAI Paper Authors (2026)** | Synthesis of low-corank converse, 2-primary valuations, residual concentration, theta congruences, and central specialization. | Primary synthesis establishing the unconditional odd-primary formula (Principal Paper, Oct 3, 2026). |

---

## 7. Scope, Boundaries, and Limitations

> ### IMPORTANT METACONTEXTUAL LIMITATIONS & SCOPE BOUNDARIES
>
> 1. **Analytic Rank $\ge 2$ Unproven:** The results apply **strictly** to elliptic curves of analytic or Selmer corank 0 or 1. Elliptic curves of higher rank ($a(E) \ge 2$) remain outside the scope of Theorem 1.1 and remain unproven.
> 2. **Base Field Limitation:** The proof is constructed **strictly over the rational numbers $\mathbb{Q}$**. Extensions to general number fields (such as totally real or imaginary quadratic fields) are not established.
> 3. **Unverified Preprint Dependencies:** The main theorem relies on three companion preprints ([22], [23], [24]). The absolute unconditional validity of Theorem 1.1 requires the correctness of these underlying preprints.
> 4. **AI-Produced Preprint & Verification Status:** This document summarizes an AI-generated technical paper dated October 3, 2026. While mathematically rigorous in its structural logic, it has not yet undergone computer-verified formalization (e.g., Lean 4 interactive theorem prover verification).

---

## 8. Accessible Glossary of Core Mathematical Concepts

| Mathematical Term | Definition & High-School Level Analogy |
| :--- | :--- |
| **Elliptic Curve** | A smooth geometric curve defined by $y^2 = x^3 + ax + b$. *Analogy:* Unlike a line or circle, it has a unique "addition" rule where drawing a straight line through two points on the curve intersects it at a third rational point. |
| **Rational Point** | A point $(x,y)$ on the curve where both coordinates are exact fractions or integers. *Analogy:* Grid intersections on a sheet of graph paper that fall exactly on the curve. |
| **Mordell–Weil Rank ($r$)** | The number of independent rational points of infinite order needed to generate all rational points on the curve. *Analogy:* The number of fundamental directions required to map out all non-repeating rational solutions. |
| **$p$-adic Valuation ($v_p$)** | An arithmetic function measuring the exact power of a prime $p$ dividing a rational number $q$. *Analogy:* A metric measuring divisibility, where numbers divisible by large powers of $p$ are considered $p$-adically "small" or close to $0$. |
| **$L$-function $L(E,s)$** | A complex function combining point counts modulo every prime number $\ell$ into a single analytical tool. *Analogy:* A financial "index" that aggregates localized point counts across all primes into one global smooth function. |
| **Analytic Rank ($a$)** | The order of vanishing (number of zero derivatives) of $L(E,s)$ at $s=1$. *Analogy:* The degree of a zero root in a polynomial, measuring how "flat" $L(E,s)$ is at its central point. |
| **Tate–Shafarevich Group ($\text{Sha}$)** | A group measuring the obstruction to finding rational solutions when local $p$-adic solutions exist everywhere. *Analogy:* A diagnostic error code that registers when localized regional solutions fail to patch together into a single global solution. |
| **Selmer Group & Corank ($s_q$)** | An algebraic group bounding rational points and $\text{Sha}$ classes modulo powers of a prime $q$. *Analogy:* An upper-bound computational envelope surrounding both rational points and local-global errors. |
| **Real Period ($\Omega_E$)** | The geometric length/area traced by the real points of the curve under integration. *Analogy:* The physical perimeter or loop length of the curve when drawn on standard real graph paper. |
| **Regulator ($\text{Reg}_E$)** | A matrix determinant measuring the geometric spacing and canonical height complexity of independent rational points. *Analogy:* A measurement of the "volume" spanned by the fundamental solution generators. |
| **Tamagawa Number ($c_\ell$)** | A small local integer $[E(\mathbb{Q}_\ell) : E_0(\mathbb{Q}_\ell)]$ measuring singular geometric reduction at a prime $\ell$. *Analogy:* A local correction factor for sharp corners or self-intersections that occur when viewing the curve modulo $\ell$. |
| **Manin Constant ($c_E$)** | A non-zero rational scaling factor $c_E \in \mathbb{Q}^\times$ linking the differential of the modular parametrization $\phi^* \omega_E$ to the newform $f(q)\frac{dq}{q}$. *Analogy:* A global conversion ratio between modular coordinates and minimal geometric coordinates. |
| **Heegner Point** | A special complex-multiplication point on a modular curve coming from an auxiliary imaginary quadratic field $K$. *Analogy:* A landmark point constructed using complex geometry that aligns with the curve's modular symmetry. |