# The Irrationality Exponent of $\pi$ is 2: A Comprehensive Explainer

---

### 1. The Question: Rational Approximation and the Irrationality Exponent

How well can real numbers be approximated by simple fractions? Any real number—even an irrational one—can be approximated by a rational fraction $p/q$, where $p$ is the integer numerator and $q$ is the positive integer denominator. 

For the famous circle constant $\pi \approx 3.141592653589793\dots$, familiar rational approximations include:
* $\frac{22}{7} \approx 3.142857$ (denominator $q = 7$)
* $\frac{355}{113} \approx 3.14159292$ (denominator $q = 113$)

Notice that $355/113$ is exceptionally close to $\pi$ ($|\pi - 355/113| \approx 0.000000267$), far closer than one would typically expect for a three-digit denominator. The quality of a rational approximation is measured by how small the error $|\pi - p/q|$ is relative to the size of the denominator $q$.

To see where these remarkably accurate fractions come from, we turn to **continued fractions**. Every real number $x$ can be represented as an infinitely nested sum of reciprocals. For $\pi$, the continued fraction expansion begins:

$$\pi = 3 + \cfrac{1}{7 + \cfrac{1}{15 + \cfrac{1}{1 + \cfrac{1}{292 + \cfrac{1}{1 + \dots}}}}}$$

Truncating this infinite expression at any step yields a fraction $p_j/q_j$ called a **convergent**:
* Truncating at $1/7$ gives $3 + 1/7 = \mathbf{22/7}$.
* Truncating right before the unusually large term $292$ gives $3 + \cfrac{1}{7 + \cfrac{1}{15 + \cfrac{1}{1}}} = \mathbf{355/113}$.

Because $292$ is so large, $355/113$ captures an extraordinarily precise snapshot of $\pi$ before the next reciprocal term can alter the value significantly.

> **Key Concept: Continued Fractions and Convergents**
> A continued fraction expresses a real number as a nested sequence of integer additions and reciprocals. Truncating this sequence at any step produces a fraction $p_j/q_j$ called a **convergent**. Convergents yield the mathematically "best" rational approximations for their denominator size.

To analyze how closely fractions can approximate an irrational number $x$ systematically, mathematicians rely on **Dirichlet's Approximation Theorem**. Derived using the pigeonhole principle, this fundamental theorem states that for *every* irrational number $x$, there exist infinitely many coprime fractions $p/q$ satisfying:

$$\left| x - \frac{p}{q} \right| < \frac{1}{q^2}$$

To classify real numbers by their "approximability," mathematicians define a precise numerical index called the **irrationality exponent** (or irrationality measure), denoted $\mu(x)$.

> **Definition: Irrationality Exponent $\mu(x)$**
> For an irrational real number $x$, its irrationality exponent $\mu(x)$ is defined as:
> $$\mu(x) = \sup \left\{ \nu > 0 : 0 < \left| x - \frac{p}{q} \right| < q^{-\nu} \text{ for infinitely many coprime } p, q \in \mathbb{Z}, q \ge 2 \right\}$$
> 
> *Intuition*: The exponent $\mu(x)$ sets a strict upper speed limit on how fast the approximation error $|x - p/q|$ can shrink as the denominator $q$ grows. A larger $\mu(x)$ means $x$ can be unusually well-approximated by fractions.

Because Dirichlet's theorem guarantees infinitely many approximations with an exponent of at least 2, every irrational number satisfies **$\mu(x) \ge 2$**. 

#### Algebraic vs. Transcendental Numbers
* **Algebraic Numbers**: These are roots of non-zero polynomials with integer coefficients (such as $\sqrt{2}$, which satisfies $x^2 - 2 = 0$). **Roth's Theorem** (a landmark 1955 result in number theory) proves that *every* irrational algebraic number has an irrationality exponent of exactly $\mu(x) = 2$.
* **Transcendental Numbers**: These numbers (such as $\pi$ and $e$) are not roots of any non-zero integer polynomial. Because Roth's theorem applies strictly to algebraic numbers, it **does not apply to $\pi$**. 

While mathematicians long conjectured that $\mu(\pi) = 2$, proving it required an entirely different, highly sophisticated framework in multivariable interpolation and complex geometry.

---

### 2. Historical Context and the Search for $\mu(\pi)$

For over seven decades, mathematicians established a sequence of progressively smaller upper bounds for $\mu(\pi)$, gradually narrowing the gap toward the conjectured value of 2.

#### Refinement of Upper Bounds for $\mu(\pi)$

| Author(s) | Year | Upper Bound / Contribution | Method / Technique |
| :--- | :--- | :--- | :--- |
| **Mahler** | 1953 | $\mu(\pi) \le 42$ (eventually improved to 30) | Constructed polynomial-coefficient combinations of powers of logarithms; proved determinant nonvanishing. |
| **Mignotte** | 1974 | $\mu(\pi) \le 21$ ($\forall q \ge 2$), 20 eventually | Refined Mahler's polynomial-logarithm analytic construction. |
| **Chudnovsky** | 1982 | Asymptotic bounds improvement | Hermite–Padé approximations to exponential functions with precise asymptotic estimates. |
| **Hata** | 1993 | $\mu(\pi) \le 8.01604539\dots$ | Explicit complex integral constructions. |
| **Salikhov** | 2008, 2010 | $\mu(\pi) \le 7.606308\dots$ | Symmetric-integral method. |
| **Zeilberger & Zudilin** | 2020 | $\mu(\pi) \le 7.103205334137\dots$ | Parameter experiments combined with rigorous arithmetic and asymptotic analysis. |
| **Bai** | Sept 2026 (Preprint) | $\mu(\pi) < 7.101862832357$ | Two-exponent variation of the Zeilberger–Zudilin integral. |

#### Convergence Criteria and Related Work on the Flint–Hills Series

The **Flint–Hills series** is a famous infinite trigonometric series popularized by Clifford Pickover:

$$\sum_{n=1}^\infty \frac{1}{n^3 \sin^2 n}$$

Whether this series converges depends entirely on how close positive integers $n$ can get to integer multiples of $\pi$ (which makes $\sin n$ extremely close to $0$ and thus $1/\sin^2 n$ extremely large).
* **Alekseyev (2011)**: Proved that convergence of the Flint–Hills series *requires* $\mu(\pi) \le 5/2$.
* **Meiburg (2022)**: Proved that the strict condition **$\mu(\pi) < 5/2$** is *sufficient* to guarantee convergence.
* **Dan (2026) & López Zapata (2026)**: Investigated generalized series and continued-fraction criteria, leaving convergence undecided.
* **Mantzakouras & López Zapata (2025)**: Claimed convergence, but the paper was withdrawn in September 2026 because the proof failed to establish convergence or the required irrationality bound.
* **Carella (2022)**: Claimed $\mu(\pi) = 2$ and the stronger bounded-partial-quotient property. However, the displayed argument for the stronger assertion contains an explicit sign obstruction: defining $C = p_{n+1} - \pi q_{n+1} - 1/q_n$, the convergent estimate $|p_{n+1} - \pi q_{n+1}| < 1/q_{n+2} < 1/q_n$ gives $-2/q_n < C < 0$. This forces $\sin C < 0$ for large $n$, contradicting the positive lower bound assumed in Carella's display.

---

### 3. Core Results (Quoted Verbatim)

Below are the central mathematical statements established in the research paper, quoted verbatim from the source text, followed by plain-language breakdowns.

> **Theorem 1.1**
> *"The irrationality exponent of $\pi$ is 2. More precisely, for every real $\nu > 2$, there is an integer $Q(\nu)$ such that $|\pi - p/q| \ge q^{-\nu} (p \in \mathbb{Z}, q \in \mathbb{Z}, q \ge Q(\nu))$."*

* **Plain-Language Breakdown**: This completely settles the long-standing conjecture. It states that if you pick any exponent strictly greater than 2 (for instance, $\nu = 2.00001$), there are only finitely many fractions $p/q$ that can approximate $\pi$ closer than $1/q^\nu$. Beyond a threshold denominator $Q(\nu)$, every fraction fails to beat this bound.

> **Corollary 1.2**
> *"The classical Flint–Hills series converges."*

* **Plain-Language Breakdown**: Because the paper proves $\mu(\pi) = 2$, and $2 < 5/2$, Meiburg's sufficient condition ($\mu(\pi) < 5/2$) is fully satisfied. Therefore, the long-unsettled Flint–Hills series does not blow up to infinity; its infinite sum converges to a finite numerical value.

> **Corollary 5.2**
> *"For fixed real numbers $a, b > 0$, the series $\sum_{n=1}^\infty \frac{1}{n^a |\sin n|^b}$ with angles in radians converges if and only if $a > \max\{1, b\}$."*

* **Plain-Language Breakdown**: This provides a complete classification for a broad family of trigonometric series. For example, if $b = 2$ (as in the Flint–Hills series), the series converges if and only if $a > \max\{1, 2\} = 2$. Since $a = 3 > 2$ in the classical Flint–Hills series, convergence is rigorously confirmed.

---

### 4. Why This Result Matters

* **Resolves Waldschmidt's Open Problem**: The result definitively proves a core problem in Diophantine approximation recorded by Michel Waldschmidt, establishing that $\pi$ has the expected irrationality exponent of 2.
* **Definitively Solves the Flint–Hills Convergence Problem**: By establishing $\mu(\pi) = 2$, the proof satisfies Meiburg's strict condition $\mu(\pi) < 5/2$, resolving the convergence problem popularized by Pickover.
* **Clarifies Boundaries of Stronger Unproved Claims**: Proving $\mu(\pi) = 2$ means $|\pi - p/q| < q^{-\nu}$ has only finitely many solutions for any $\nu > 2$. However, it is essential to distinguish this from even stronger mathematical claims:
  * It does **not** establish a uniform positive lower bound of the form $c/q^2$ for all $q$.
  * It does **not** prove that $\pi$ has bounded continued-fraction partial quotients (which would mean the terms in its continued fraction never exceed a fixed integer ceiling).
  These stronger properties remain unresolved.

---

### 5. Step-by-Step Walkthrough of the Proof

> **Proof Strategy Overview**
> The proof operates via proof by contradiction using an interpolation-determinant framework:
> 1. **Hypothesis**: Assume $\mu(\pi) > 2$, which permits an infinite sequence of unusually accurate rational fractions $p_i/q_i$.
> 2. **Matrix Construction**: Build a giant square matrix $\Delta_H$ whose entries are evaluations of polynomials and their derivatives (jets) at centers derived from these rational approximations.
> 3. **Dual Determinant Estimates**: Calculate the determinant of $\Delta_H$ using two independent, competing methods:
>    * **Arithmetic Lower Bound**: Scale matrix entries to Gaussian integers $\mathbb{Z}[i]$. Because the matrix is non-singular and entries are integers, its determinant modulus cannot drop below a fixed floor ($|\Delta_H| \ge 1$).
>    * **Analytic Upper Bound**: Translate evaluation rows to exact complex logarithmic periods $2\pi \mathbf{i} j$. Grouping rows that test the same entire functions forces massive term cancellations ("collision savings") or high approximation-error factors, forcing the determinant to shrink exponentially toward $0$ as degree $H \to \infty$.
> 4. **Contradiction**: Tune parameters so that the analytic ceiling falls strictly below the arithmetic floor, proving that $\mu(\pi)$ cannot exceed 2.

```
                      +-----------------------------------+
                      | Assume μ(π) > 2 for Contradiction |
                      +-----------------+-----------------+
                                        |
                                        v
                      +-----------------------------------+
                      | 1. Fix Dimension m, Weights W, V, |
                      |    and Thresholds (Independent)   |
                      +-----------------+-----------------+
                                        |
                                        v
                      +-----------------------------------+
                      | 2. Select Rational Approximations |
                      |    pi/qi & Almost-Periods c_ji    |
                      +-----------------+-----------------+
                                        |
                                        v
                      +-----------------------------------+
                      | 3. Construct Matrix Δ_H           |
                      |    (Separated-Weight Theorem 2.1) |
                      +--------+-----------------+--------+
                               |                 |
            PARALLEL EVALUATION|                 |PARALLEL EVALUATION
                               v                 v
     +---------------------------+     +---------------------------+
     | 4. Arithmetic Lower Bound |     | 5. Analytic Upper Bound   |
     |    (Lemma 3.1)            |     |    (Prop 3.4)            |
     |    Clear Denominators in  |     |    Translate to Exact     |
     |    Z[i] ==> |Δ_H| >= 1    |     |    Periods ==> Group      |
     |    log|Δ_H|/M_H >=        |     |    Cancellations & Error  |
     |    -(1 - b_bar) - E_ar    |     |    Factors Shrink |Δ_H|   |
     +------------+--------------+     +------------+--------------+
                  |                                 |
                  +----------------+----------------+
                                   |
                                   v
                      +-----------------------------------+
                      | 6. Parameter Tuning (Lemma 4.1)   |
                      |    Choose Large m ==> Upper Bound |
                      |    Falls Strictly Below Lower     |
                      |    Bound (Direct Contradiction)   |
                      +-----------------+-----------------+
                                        |
                                        v
                      +-----------------------------------+
                      | CONCLUSION: μ(π) = 2 Exactly      |
                      +-----------------------------------+
```

#### Step 1: Order of Parameters and Constants
To prevent circular logic, the sequence of parameter choices is strictly fixed:
1. Dimension $m$, coordinate weights, and interpolation thresholds are chosen first.
2. A finite number of rational approximations $p_i/q_i$ (and corresponding center coordinates $c_{ji}$) satisfying these thresholds are chosen second.
3. Only **after** dimension, weights, and centers are fixed does the polynomial degree $H$ tend to infinity ($H \to \infty$).

#### Step 2: Logarithmic Almost-Periods
Finitely many exceptionally close rational approximations $p_i/q_i$ are selected. Scaled rational quantities $r_i = \frac{2 i p_i}{q_i}$ (where $i \in \{1, \dots, m\}$ denotes the coordinate axis index) and center coordinates $c_{ji} = j r_i = \frac{2 i j p_i}{q_i}$ are formed. These serve as "almost-periods" approximating the exact complex logarithmic period components $2\mathbf{i} j \pi$ (where $\mathbf{i} = \sqrt{-1}$).

#### Step 3: Interpolation Matrix Dimension Count
Polynomial monomials $P(Y, X) = Y^h X^\alpha$ form the columns of an interpolation matrix $\Delta_H$, while derivative packets (jets) evaluated at centers $a_j = (1, c_{j1}, \dots, c_{jm})$ form the rows. The parameter constraints ($K\theta^m < 1$ and $K w_0 v_0 / \theta^m < 1$) ensure that the space of polynomial monomial columns strictly outnumbers the prescribed Taylor evaluation conditions (rows).

#### Step 4: Separated-Weight Interpolation (Theorem 2.1)
Although monomials outnumber evaluation conditions, establishing that the evaluation matrix has full row rank at these specialized centers requires deep algebraic geometry:

> **Intuitive Metaphor: Vector Fields and Logarithmic Residues**
> * **Vector Fields**: The proof introduces differential operators $D_0 = Y \partial_Y + \sum \partial_{X_i}$ and $D_i = \partial_{X_i}$. Think of $D_0$ as tracking rates of change directly *along* a logarithmic curve, while $D_i$ tracks transverse (*sideways*) departures from the curve.
> * **Logarithmic Residues**: If derivative evaluations were to vanish along an algebraic curve component $Z$, calculus forces the differential relation $dX_i = dY/Y$. If $Y$ is a nonconstant rational function with a zero or pole, $dY/Y$ behaves like $1/x$, producing a non-zero loop integral (residue) around the origin. However, $X_i$ is a polynomial coordinate whose derivative $dX_i$ has zero residue everywhere. The only way their rates of change can match everywhere without contradiction is if both $Y$ and $X_i$ are constant functions.

This curve inequality enforces positivity on an ordinary blow-up schema, proving full row rank and yielding a non-zero square minor determinant $\Delta_H$.

#### Step 5: Arithmetic Lower Bound (Lemma 3.1)
To bound $|\Delta_H|$ from below, entries are cleared of rational denominators. Using the denominator clearing factor:

$$D_H = \prod_{i=1}^m L_i^{\lfloor H/w_i \rfloor}$$

where $L_i = \text{lcm}(1, \dots, T_i - 1)$ and $\lfloor H/w_i \rfloor$ is the coordinate exponent, the matrix $\Delta_H$ is mapped into a matrix over the Gaussian integers $\mathbb{Z}[\mathbf{i}]$. Because any non-zero Gaussian integer has a modulus of at least 1, the scaled determinant cannot collapse below 1:

$$\frac{\log |\Delta_H|}{M_H} \ge -(1 - \bar{b}) - E_{ar}$$

where the explicit arithmetic error term is defined by:

$$E_{ar} = \frac{\Lambda F_0 m}{v_0} + \Lambda \sum_{i=1}^m \frac{1}{w_i} + \frac{\theta}{w_*}$$

with $\Lambda = 4 \log 2$, $F_0$ representing the tail cutoff parameter, and $w_* = \min_{i>0} w_i$.

#### Step 6: Analytic Upper Bound (Lemmas 3.2–3.3 & Prop 3.4)
To derive an upper bound, each row is translated to exact logarithmic periods $j\omega = 2\pi \mathbf{i} j$ and expanded in transverse variables $u_i$. Rows test Taylor coefficients of entire functions $f_{a,P}(z) = [u^a] P(e^z, z+u_1, \dots, z+u_m)$.

The proof analyzes two alternative cases for row multi-indices $a$:
* **Case A (Low Transverse Weight $w_a \le AH$)**: Multiple rows test Taylor expansions of the *same* entire functions. When $n_a$ different rows test the same function, expanding the determinant in power series causes identical lower-degree Taylor terms to cancel out completely across rows. The first non-vanishing term must come from higher derivative degrees $0, 1, 2, \dots, n_a - 1$. Summing these forced higher powers produces an exponent sum:
  $$\sum_{k=0}^{n_a - 1} k = \frac{n_a(n_a - 1)}{2} \approx \frac{n_a^2}{2}$$
  This linear algebra mechanism (Laurent 2000) drives a strong exponential decay factor $\exp(-c \sum n_a^2)$ on the determinant's size.
* **Case B (High Transverse Weight $w_a > AH$)**: Rows with large transverse indices instead supply high powers of the tiny rational approximation errors $|\pi - p_i/q_i|$.

#### Step 7: Parameter Tuning (Lemma 4.1)
Lemma 4.1 proves that the geometric inequalities $\nu(A - \theta) > 1 - \theta$ and $A^2 < \theta$ hold simultaneously if and only if $\nu > 2$. 

Setting parameters as functions of dimension $m$:
$$K = \lfloor C^m \rfloor, \quad w_0 = B^{-m}, \quad v_0 = 2K\theta^m w_0$$

causes the collision saving growth factor:

$$L = \frac{\eta^2 (B/A)^m}{2(m+1)}$$

to grow exponentially toward $\infty$ as $m \to \infty$ (since $B > A$), while all dimension-dependent error terms ($E_{ar} + E_{an}$) shrink toward zero. Choosing a sufficiently large dimension $m$ forces the analytic upper bound strictly below the arithmetic lower bound—a direct contradiction. Thus, no exponent $\nu > 2$ can permit infinitely many rational approximations, proving $\mu(\pi) = 2$.

#### Step 8: Dyadic Spacing Argument (Section 5)
To prove Corollary 1.2, Lemma 5.1 divides integers $q$ into dyadic blocks $[K, 2K)$. Because $\mu(\pi) < 5/2$, points $q\pi$ on the circle $\mathbb{R}/\mathbb{Z}$ maintain a minimal separation $d = c(2K)^{1-\nu}$. Summing the minimal distances $d, 2d, 3d, \dots$ over dyadic blocks proves that $\sum q^{-3} \|q\pi\|^{-2} < \infty$. Grouping integers $n$ by their nearest multiple $q\pi$ establishes the convergence of the Flint–Hills series and yields the general criterion $a > \max\{1, b\}$.

---

### 6. Key Mathematicians and Intellectual Foundations

The proof synthesizes key techniques developed by prominent mathematicians in Diophantine approximation and algebraic geometry:

| Mathematician | Role / Concept Used in Proof |
| :--- | :--- |
| **Dirichlet** | Pigeonhole principle establishing the foundational lower bound $\mu(x) \ge 2$ for all irrationals. |
| **Roth** | Multi-variable method employing successively separated approximation denominators. |
| **Laurent** | Interpolation-determinant method and elimination of repeated Taylor degrees in exponential polynomials. |
| **Philippon** | Zero-estimate and derivative-ideal methods in commutative algebraic groups. |
| **Farhi** | Separated multidegrees used in the context of Roth's lemma. |
| **Demailly** | Asymptotic jet generation and the connection between curvewise positivity and Seshadri constants. |
| **Lazarsfeld** | Positivity in algebraic geometry, line bundles, and ample/nef divisor arguments on blow-ups. |

---

### 7. Limitations and Scope Boundaries

While this work solves a fundamental problem, the source text explicitly outlines several scope boundaries and limitations:

* **Ineffectivity**: The proof is non-effective. Theorem 1.1 proves the existence of the threshold integer $Q(\nu)$, but the argument does **not** supply a numerical algorithm to calculate $Q(\nu)$ for a given $\nu$.
* **Bounded Partial Quotients Unproved**: Proving $\mu(\pi) = 2$ is strictly weaker than establishing a uniform lower bound of the form $c/q^2$ or proving that $\pi$ has bounded continued-fraction partial quotients. These stronger properties remain unproved.
* **No Explicit Sum Value**: The paper proves definitively that the Flint–Hills series converges, but it does **not** compute an explicit numerical value for the sum.
* **Lean Formalization Scope**: Based on the official Lean formalization documentation (`017.md`), the machine-checked formalization in `PiExponent.lean` strictly covers Theorem 1.1 (the statement that for every $\nu > 2$, $|\pi - p/q| \ge q^{-\nu}$ for all $q \ge Q(\nu)$, as well as the supremum characterization). The trigonometric series convergence corollary (Corollary 1.2) is explicitly outside the scope of the formalized Lean code.
* **Preprint Status**: The document is an AI-generated preprint published by OpenAI on September 24, 2026.

---

### 8. Glossary

* **Irrationality Exponent ($\mu$)**: A metric measuring how closely an irrational number can be approximated by rational fractions.
* **Convergent**: A rational fraction $p_j/q_j$ generated by truncating a continued fraction expansion; it represents an optimal rational approximation for its denominator size.
* **Transcendental Number**: A real number that is not the root of any non-zero polynomial with rational coefficients (e.g., $\pi$).
* **Gaussian Integer ($\mathbb{Z}[\mathbf{i}]$)**: A complex number of the form $a + b\mathbf{i}$, where $a$ and $b$ are integers and $\mathbf{i} = \sqrt{-1}$.
* **Minor (Matrix)**: The determinant of a square submatrix formed by selecting specific rows and columns from a larger matrix.
* **Jet**: A finite packet containing the Taylor expansion coefficients of a function up to a given order at a specific point.
* **Dyadic Spacing**: A proof technique that divides numbers or intervals into dyadic blocks $[K, 2K)$ (powers of two) to establish upper bounds on sums.
* **Blow-Up (Algebraic Geometry)**: A geometric transformation that takes a single point where curves intersect or self-collide and replaces it with a "horizon" (projective space) of all incoming directions, separating tangled lines so their contact angles can be analyzed cleanly.
* **Nef / Ample Divisors**: Criteria measuring geometric positivity for line bundles. An *ample divisor* acts like a positive curvature metric that allows embedding a shape into projective space without collapsing dimensions; a *nef (numerically effective) divisor* is a limit of ample divisors that has non-negative intersections with all algebraic curves.