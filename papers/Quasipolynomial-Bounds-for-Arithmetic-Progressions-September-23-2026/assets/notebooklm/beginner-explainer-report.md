# Beginner Explainer: Quasipolynomial Bounds for Arithmetic Progressions

---

## 1. The Core Problem: Arithmetic Progressions and Erdős's Conjecture

Extremal set theory and additive combinatorics investigate how dense a set of integers must be to guarantee the presence of specific arithmetic patterns. A fundamental pattern is a **$k$-term arithmetic progression** ($k$-term AP), defined as a sequence of $k$ integers of the form:
$$a, \, a+d, \, a+2d, \, \dots, \, a+(k-1)d \quad (d > 0)$$
where $a \in \mathbb{Z}$ is the starting term and $d \in \mathbb{Z}^+$ is the common difference. An arithmetic progression is termed **nonconstant** when its common difference $d$ is strictly positive ($d > 0$).

For a fixed integer $k \ge 3$ and scale $N \ge 1$, the central object of study is the **extremal density bound $r_k(N)$**, defined as the maximum size of a subset $A \subseteq \{1, \dots, N\} = [N]$ that contains no nonconstant $k$-term arithmetic progression:
$$r_k(N) := \max \left\{ |A| : A \subseteq \{1, \dots, N\}, \, A \text{ contains no nonconstant } k\text{-term AP} \right\}$$

### Szemerédi's Theorem and Erdős's Conjecture
In 1975, Endre Szemerédi established that any subset of positive integers with positive upper density contains arbitrarily long arithmetic progressions. Qualitatively, this asserts that $r_k(N) = o(N)$ for every fixed length $k \ge 3$.

In Problem 4.33.6, Paul Erdős formulated a much deeper conjecture addressing sparse integer sets:

> **Erdős's Reciprocal-Sum Conjecture:** Any set of positive integers $A \subseteq \mathbb{N}$ whose reciprocal sum diverges,
> $$\sum_{a \in A} \frac{1}{a} = \infty$$
> contains nonconstant arithmetic progressions of every finite length $k$.

> **Callout: Density Bounds vs. Reciprocal Sum Divergence**
> * **Qualitative Density Bounds ($r_k(N) = o(N)$):** Guarantee that a set containing a fixed positive fraction $\alpha = |A|/N > 0$ of an interval $[N]$ contains a $k$-term AP. However, integer sets can be extremely sparse on average—having asymptotic density zero—while still possessing a divergent reciprocal sum (e.g., sequences growing slightly faster than linear scales). Consequently, qualitative density bounds like $r_k(N) = o(N)$ are **strictly insufficient** to resolve Erdős's conjecture.
> * **Dyadic Summability Threshold ($\sum_{m \ge 1} \frac{r_k(2^m)}{2^m} < \infty$):** Resolving the Erdős conjecture requires a quantitative upper bound on $r_k(N)$ that decays fast enough so that block reciprocal sums over dyadic intervals $[2^m, 2^{m+1})$ form a convergent infinite series whenever $A$ is $k$-AP-free.

---

## 2. Proof of Corollary 1.2 via Dyadic Decomposition

Corollary 1.2 demonstrates that Erdős's Reciprocal-Sum Conjecture is a quantitative consequence of the main density bound established for $r_k(N)$.

### Step-by-Step Derivation

1. **Dyadic Interval Partition:** Partition the positive integers $\mathbb{N}$ into disjoint dyadic intervals $[2^m, 2^{m+1})$ for integers $m \ge 0$.
2. **Interval Translation:** Translation identifies each interval $[2^m, 2^{m+1}) \cap \mathbb{Z}$ with an integer interval of length $2^m$.
3. **Block Cardinality Bound:** If $A \subseteq \mathbb{N}$ contains no nonconstant $k$-term arithmetic progression, its restriction to any dyadic interval satisfies:
   $$\left| A \cap [2^m, 2^{m+1}) \right| \le r_k(2^m)$$
4. **Step-by-Step Block Reciprocal Sum Inequality:** For every element $a \in [2^m, 2^{m+1})$, we have $1/a \le 2^{-m}$. Applying the main upper bound $r_k(2^m) \le C_k 2^m \exp\left(-c_k (m \log 2)^{\epsilon_k}\right)$ yields the explicit chain of inequalities:
   $$\sum_{a \in A \cap [2^m, 2^{m+1})} \frac{1}{a} \le 2^{-m} \left| A \cap [2^m, 2^{m+1}) \right| \le \frac{r_k(2^m)}{2^m} \le C_k \exp\left( -c_k (m \log 2)^{\epsilon_k} \right)$$
5. **Total Reciprocal Sum:** Summing over all dyadic blocks $m \ge 0$:
   $$\sum_{a \in A} \frac{1}{a} = \sum_{a \in A \cap [1, 2)} \frac{1}{a} + \sum_{m=1}^{\infty} \sum_{a \in A \cap [2^m, 2^{m+1})} \frac{1}{a} \le 1 + C_k \sum_{m=1}^{\infty} \exp\left( -c_k (m \log 2)^{\epsilon_k} \right)$$

### Convergence Mechanism

* **Stretched-Exponential Exponent Dominance:** Consider the sequence $e^{-d m^\epsilon}$ for positive constants $d, \epsilon > 0$. Taking the natural logarithm of the comparison $e^{-d m^\epsilon} \le m^{-2}$ yields the requirement $d m^\epsilon \ge 2 \log m$, or equivalently $\frac{m^\epsilon}{\log m} \ge \frac{2}{d}$.
* **Asymptotic Bound:** Because $\frac{m^\epsilon}{\log m} \to \infty$ as $m \to \infty$, the power term $d m^\epsilon$ eventually dominates $2 \log m$ for all sufficiently large $m$.
* **Comparison Test:** Consequently, the individual terms satisfy $\exp\left(-d m^\epsilon\right) \le m^{-2}$ for all sufficiently large $m$.
* **Conclusion & Dyadic Summability:** Since the $p$-series $\sum_{m=1}^\infty m^{-2} = \frac{\pi^2}{6} < \infty$ converges, the infinite series $\sum_{m=1}^\infty \exp\left( -c_k (m \log 2)^{\epsilon_k} \right)$ converges to a finite constant. Thus, if $A$ contains no nonconstant $k$-term AP, its reciprocal sum $\sum_{a \in A} 1/a$ must be finite. By contraposition, any set $A \subseteq \mathbb{N}$ with $\sum_{a \in A} 1/a = \infty$ must contain nonconstant $k$-term arithmetic progressions for every $k \ge 3$.

---

## 3. Historical Context and Evolution of Density Bounds

The problem of estimating $r_k(N)$ has driven key developments in analytic number theory, ergodic theory, and additive combinatorics over nearly nine decades.

### Evolution for $k = 3$ Progression Lengths
Erdős and Turán inaugurated the quantitative study of arithmetic progressions in 1936, conjecturing that $r_3(N) = o(N)$. Klaus Roth established the three-term case in 1953 using linear Fourier analysis, obtaining $r_3(N) \ll N / \log \log N$ via density increments on subprogressions. In the late 1980s and 1990s, Heath-Brown and Szemerédi broke the double-logarithm barrier, improving the bound to $r_3(N) \ll N / (\log N)^c$ for a small constant $c > 0$.

Jean Bourgain introduced the density-increment method on regular Bohr sets (local harmonic structures in $\mathbb{T}^d$), sharpening the bound to $r_3(N) \ll N (\log \log N / \log N)^{1/2}$. Further structural breakthroughs by Sanders ($r_3(N) \ll N / (\log N)^{1-o(1)}$) and Bloom brought the bound close to $N / \log N$. In 2020, Thomas Bloom and Olof Sisask applied Schoen–Sisask almost-periodicity to establish $r_3(N) \ll N / (\log N)^{1+c}$. Crucially, because $1+c > 1$, this bound crossed the dyadic summability threshold $\sum r_3(2^m)/2^m < \infty$, fully resolving Erdős's Reciprocal-Sum Conjecture for three-term progressions.

In 2023, Zander Kelley and Raghu Meka achieved a major breakthrough by establishing a quasipolynomial bound $r_3(N) \ll N \exp(-c(\log N)^{1/12})$. Their method introduced dependent random choice sifting to control loss during density increments on Bohr sets. Bloom and Sisask refined this technology to improve the exponent to $1/9$, and Raghavan subsequently pushed the exponent to $r_3(N) \le N \exp(-(\log N)^{1/6-o(1)})$. On the lower-bound side, Felix Behrend (1946) constructed a $3$-AP-free set by mapping spheres in high-dimensional integer lattices, showing $r_3(N) \ge N \exp(-C \sqrt{\log N})$. Behrend's lower bound proves that a fixed power saving of the form $r_3(N) \le N^{1-\delta}$ (for $\delta > 0$) is mathematically impossible even for $k=3$.

### Evolution for General $k \ge 4$ Progression Lengths
For progressions of length $k \ge 4$, linear Fourier analysis fails because progression counts depend on higher-degree polynomial phases. In 2001, Timothy Gowers introduced the $U^d$ uniformity norms and higher-order Fourier analysis, establishing $r_k(N) \ll_k N / (\log \log N)^{c_k}$. Green and Tao sharpened the four-term bound to $r_4(N) \ll N / (\log N)^c$ in 2017. 

Recently, Leng, Sah, and Sawhney proved $r_k(N) \ll_k N \exp(-(\log \log N)^{c_k})$ for general $k \ge 5$ by combining a quasipolynomial inverse theorem for uniformity norms with density increments. However, because their saving decays as a power of $\log \log N$, the corresponding series $\sum_{m \ge 1} \exp(-c_k (\log m)^{c_k})$ diverges. Thus, their bound fell short of the dyadic summability required to settle Erdős's conjecture for $k \ge 4$.

The present work establishes a quasipolynomial bound in $\log N$ for all fixed $k \ge 3$, providing the required dyadic summability to settle the full Erdős conjecture.

### Historical Comparison of Density Bounds

| Author(s) | Progression Length ($k$) | Quantitative Density Bound $r_k(N)$ | Dyadic Summable? ($\sum \frac{r_k(2^m)}{2^m} < \infty$) |
| :--- | :--- | :--- | :--- |
| **Erdős & Turán (1936)** | $k=3$ | Conjectured $r_3(N) = o(N)$ | N/A |
| **Roth (1953)** | $k=3$ | $\ll N / \log \log N$ | **No** |
| **Heath-Brown (1987) / Szemerédi (1990)** | $k=3$ | $\ll N / (\log N)^c$ | **No** |
| **Bourgain (1999, 2008)** | $k=3$ | $\ll N (\log \log N / \log N)^{1/2}$ | **No** |
| **Sanders (2011)** | $k=3$ | $\ll N / (\log N)^{1-o(1)}$ | **No** |
| **Bloom (2016)** | $k=3$ | $\ll N (\log \log \log N)^2 / \log N$ | **No** |
| **Bloom & Sisask (2020)** | $k=3$ | $\ll N / (\log N)^{1+c}$ | **Yes** (Settles $k=3$ Erdős conjecture) |
| **Kelley & Meka (2023)** | $k=3$ | $\ll N \exp\left(-c (\log N)^{1/12}\right)$ | **Yes** |
| **Raghavan (2024)** | $k=3$ | $\le N \exp\left(-(\log N)^{1/6-o(1)}\right)$ | **Yes** |
| **Behrend (1946) [Lower Bound]** | $k=3$ | $\ge N \exp\left(-C \sqrt{\log N}\right)$ | N/A (Rules out $N^{1-\delta}$ bound) |
| **Gowers (2001)** | General $k \ge 4$ | $\ll_k N / (\log \log N)^{c_k}$ | **No** |
| **Green & Tao (2017)** | $k=4$ | $\ll N / (\log N)^c$ | **No** |
| **Leng, Sah & Sawhney (2024)** | General $k \ge 5$ | $\ll_k N \exp\left(-(\log \log N)^{c_k}\right)$ | **No** (Fails dyadic summability) |
| **OpenAI (2026) [This Work]** | General $k \ge 3$ | $\le C_k N \exp\left(-c_k (\log N)^{\epsilon_k}\right)$ | **Yes** (Settles full Erdős conjecture) |

---

## 4. Main Results: Theorem 1.1, Coloring Thresholds, and Weighted Extensions

### Quantitative Density Bounds (Theorem 1.1)

The main quantitative result is established in two mathematically equivalent formulations:

1. **Stretched-Exponential Density Upper Bound:**
   \begin{equation}
   r_k(N) \le C_k N \exp\left( -c_k (\log N)^{\epsilon_k} \right)
   \end{equation}
   for positive constants $C_k, c_k, \epsilon_k > 0$ depending only on the progression length $k$.

2. **Density Threshold Form:**
   An $\alpha$-dense subset $A \subseteq [N]$ (where $\alpha = |A|/N > 0$) contains a nonconstant $k$-term arithmetic progression whenever the interval scale $N$ satisfies:
   \begin{equation}
   \log N \ge A_k \left( 2 + \log(1/\alpha) \right)^{A_k}
   \end{equation}
   for a constant $A_k \ge 1$. This threshold is **quasipolynomial** in $1/\alpha$, meaning the logarithm of the required scale $N$ grows as a fixed power of $2 + \log(1/\alpha)$.

### Van der Waerden Coloring Thresholds
Let $W_r(k)$ denote the Van der Waerden number: the minimum integer $N$ such that every $r$-coloring of $\{1, \dots, N\}$ contains a monochromatic nonconstant $k$-term arithmetic progression. Because the largest color class in an $r$-coloring has density $\alpha \ge 1/r$, Theorem 1.1 yields an upper bound on $W_r(k)$:
\begin{equation}
W_r(k) \le \left\lceil \exp\left( A_k (2 + \log r)^{A_k} \right) \right\rceil \quad (r \ge 1)
\end{equation}
This is accompanied by the complementary lower bound established in the companion work:
\begin{equation}
W_r(k) > \exp\left( \frac{(\log r)^2}{64 \log 2} \right) \quad (r \ge 256, \, k \ge 3)
\end{equation}
Together, equations (3) and (4) demonstrate that for any fixed progression length $k \ge 3$, the growth of $W_r(k)$ as a function of the number of colors $r$ is superpolynomial but at most quasipolynomial.

### Weighted Consequences and Dense Subsets of the Primes
Section 11 extends Theorem 1.1 to weighted arithmetic progressions and prime subsets:

* **Weighted Divergence Criterion:** Any integer set $A \subseteq \mathbb{N}$ satisfying the weighted divergence condition:
  $$\sum_{a \in A} \frac{(\log(2+a))^B}{a} = \infty$$
  for any fixed exponent $B \ge 0$ contains nonconstant $k$-term arithmetic progressions for every finite length $k$.
* **Uniform Harmonic Tails:** The quantitative density bound provides uniform tail estimates and harmonic control over progression-free integer sets.
* **Green–Tao Theorem Recovery:** The density estimates recover the Green–Tao theorem: every subset of the prime numbers $\mathbb{P}$ with positive relative upper density contains infinitely many arithmetic progressions of every finite length.

---

## 5. Proof Architecture and Triangular Polynomial Iteration

To execute a density-increment strategy without destroying structural constraints introduced in earlier rounds, the proof constructs and iterates on **triangular polynomial cells**.

### Structural Geometry of Cells
A cell is defined on a rectangular integer box using:
* A spatial variable $u$ assigned **weight 1**.
* Integer coordinate blocks $b_h \in \mathbb{Z}^{d_h}$ assigned **weight $h$**, indexed across $1 \le h \le D$. Here $s = k-2$ represents the number of **active layers** (where testing degrees equal or exceed block weights), while $D = D_k \ge s$ denotes the total maximum weight dimension of the cell.
* Polynomial mapping vectors $C_h(u, b_{<h}) \in \mathbb{R}^{d_h}$ of weighted degree $\le h$, center vectors $l_h$, and residual widths $0 < w_h \le 1/32$.

The **logarithmic precision** at weight $h$ is defined as $Q_h = \log(2/w_h)$.

### Density Certificate
A **density certificate** at threshold $a > 0$ for a progression-free function $f: [N] \to [0, 1]$ is defined by the expectation inequality:
$$\mathbb{E}[f B^-] > a \, \mathbb{E}[B^+]$$
where $B^-$ and $B^+$ are indicator functions satisfying:
$$\begin{aligned}
B^- \text{ indicator constraint:} \quad &\|b_h - C_h(u, b_{<h}) - l_h\|_\infty \le w_h \quad (1 \le h \le D) \\
B^+ \text{ padded indicator constraint:} \quad &\|b_h - C_h(u, b_{<h}) - l_h\|_\infty \le (1 + \gamma) w_h \quad (1 \le h \le D)
\end{aligned}$$

### Precision and Dimension Recurrences

> **Theorem 2.1 (Triangular Increment):** When a density certificate holds on a cell, a structured density increment can be extracted on a sub-slice at an elevated threshold $(1 + \eta)a$. The dimension increments and logarithmic precision losses satisfy descending recurrences:
> $$\begin{aligned}
> d_i' - d_i &\le d_0 + P_i(p, d_{i+1}, \dots, d_D) \\
> Q_i' - Q_i &\le P_i'(p, \text{dimension forecasts}, Q_{i+1}, \dots, Q_D)
> \end{aligned}$$

* **Precision Independence Rule:** The relative precision loss $Q_i' - Q_i$ depends **exclusively** on higher-weight precisions $(Q_{i+1}, \dots, Q_D)$ and dimension data. It is completely independent of the current-layer precision $Q_i$ and lower precisions $Q_{<i}$. This prevents logarithmic precision losses from compounding exponentially across iteration rounds.
* **Lemma 2.2 (Dimension-Independent Fresh Rank):** The number of fresh absolute slots added by the analytic increment is bounded by $d_0 = (2+p)^C$, which depends on the logarithmic density parameter $p = \log(1/a)$ but is **strictly independent** of the ambient box dimension $n$.

### The 6-Stage Operational Pipeline

1. **Prepare (Section 4):** Execute rank cuts via Proposition 4.1. If a defining polynomial $C_h$ fails a formal matrix rank test, extract a linear relation and cut the ambient value space $W_h \mapsto W_h \cap \ker \lambda$. This eliminates low-rank relations while preserving box density certificates.
2. **Descend (Sections 3 & 6):** Sample constrained affine paths $\psi(t) = x + V t$ along the stopped tree of the cell to transfer density certificates down to terminal boxes (Proposition 6.2).
3. **Absolute Increment (Lemma 2.2):** On terminal boxes, combine higher-order inverse theory, shift comparison, and relative lifting to obtain an absolute patch with $d_0 = (2+p)^C$ fresh coordinate slots and a positive score gain at target $(1 + \xi)a$.
4. **Return (Sections 7 & 8):** Carry the score backwards through passive layers ($j > s$) and active layers ($j \le s$). Use comparison measures $\mathbb{K}$, niltest approximations, and selected affine plane flags to preserve the exact defining polynomial equations while returning the score.
5. **Extract (Section 9):** Reconstruct the updated triangular polynomial cell from the returned score, strictly preserving width-loss dependency rules.
6. **Iterate (Section 10):** Execute a descending induction scheme across $T = O_k(p)$ density increment rounds. Starting at initial threshold $a_0 = \alpha/2$, the threshold increases by a factor of $(1+\eta)$ each round, terminating in at most $T = O_k(\log(1/\alpha))$ steps when the target density exceeds 1.

---

## 6. Summary of Key Analytic Tools and Technical Engines

### Analytic Infrastructure and Technical Tools

| Analytic Tool / Theorem | Core Function & Mechanism in the Proof |
| :--- | :--- |
| **Theorem A.7 (Leng–Sah–Sawhney Inverse Theorem)** | Converts large Gowers uniformity norms $U^{r+1}$ into strong local correlation with nilsequences $F(g(n)\Gamma)$ on filtered nilmanifolds, providing quasipolynomial quantitative bounds. |
| **Theorem C.1 (Shift Comparison Theorem)** | Translates non-negative correlation with higher-degree nilsequences into positive progression counts. Lower-degree comparison permits multiplication by a translated non-negative function outside an exceptional set (via Kelley–Meka unbalancing/sifting and Schoen–Sisask radius-sensitive almost-periodicity), while top-degree frequencies are removed via Leng's efficient nilpotency reductions. |
| **Lemma D.1 & Proposition D.2 (Positive Grids & Counting)** | Lifts low-degree polynomial patch correlations to positive integer progression counts over localized grids. |
| **Proposition D.3 & Proposition D.7 (Absolute Starting Rule & Relative Lifting)** | Establishes the dimension-independent fresh rank bound ($d_0 = (2+p)^C$) for density increments on arbitrary box dimensions $n$, separating fresh coordinate rank from ambient space complexity. |
| **Proposition 4.1 (Rank Cuts & Preparation)** | Modifies cell value spaces $W_h$ when formal matrix rank tests fail, reducing dimensions while preserving integer determining values and box certificates. |
| **Lemma 5.1 & Lemma 5.2 (Cube Comparison & Relative Densification)** | Adapts Conlon–Fox–Zhao densification to affine cubes. Eliminates dependency on current chart mass $m_j^{-1}$, ensuring detection bounds remain independent of $Q_j$. |
| **Lemma 6.1 (Selected Affine Planes & Bad Flags)** | Builds affine sections modulo $M$ over finite fields to detect and mask bad residue flags, preserving selected solution counts $w_{\varpi, a}(t)$ and exact translation invariance. |
| **Proposition 7.4 (Scalar Comparison under $\mathbb{K}$)** | Establishes total variation and Fourier character bounds comparing path averages against the comparison measure $\mathbb{K}$ on normalized chart units. |

---

## 7. Explicit Theoretical Limits and Boundaries

To ensure complete mathematical transparency, the paper outlines explicit theoretical limits regarding its achievements:

* **No $k=3$ Exponent Improvement:** The paper does **not** improve the numerical exponent $\epsilon_3$ for three-term arithmetic progressions beyond existing three-term bounds established by Kelley–Meka ($\epsilon_3 = 1/12$), Bloom–Sisask ($\epsilon_3 = 1/9$), or Raghavan ($\epsilon_3 = 1/6 - o(1)$).
* **Non-Optimized Exponent for General $k \ge 4$:** The constants $C_k, c_k$ and the stretched-exponential power $\epsilon_k > 0$ for general $k$-term progressions are proven to exist, but their explicit numerical values are **not optimized**.
* **Power Savings Impossibility:** Fixed power savings of the form $r_k(N) \le N^{1-\delta}$ (for fixed $\delta > 0$) are **mathematically impossible** for any $k \ge 3$. This theoretical boundary is established by Behrend's lower bound construction:
  $$r_3(N) \ge N \exp\left( -C \sqrt{\log N} \right)$$
  which decays strictly slower than $N^{1-\delta}$ for every positive $\delta > 0$.

---

## 8. Scope of the Lean Formalization

> **Scope of Machine Verification**
> The interactive theorem prover formalization in **Lean** accompanying this paper strictly covers the machine verification of the **reciprocal-sum statement** (Corollary 1.2) as derived from the quantitative density bound in Theorem 1.1.
>
> The deep underlying analytic increment engine—comprising the triangular polynomial iteration, shift comparison, higher-order nilmanifold inverse theory, and relative lifting infrastructure (Sections 2–10 and Appendices A–I)—is established via standard analytical paper proofs.