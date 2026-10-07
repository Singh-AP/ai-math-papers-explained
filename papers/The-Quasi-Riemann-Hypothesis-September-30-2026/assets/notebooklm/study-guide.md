# Study Guide: The Riemann Hypothesis and Analytic Number Theory

This study guide provides a comprehensive, fact-dense overview of the Riemann hypothesis, the mathematical structure of the Riemann zeta function, its theoretical consequences, historical computational milestones, and modern breakthroughs. It is designed for advanced study, review, and self-assessment.

---

## 1. Executive Summary & Core Concepts

### 1.1 The Riemann Hypothesis
Proposed by Bernhard Riemann in his seminal 1859 paper *"On the Number of Primes Less Than a Given Magnitude"*, the **Riemann hypothesis** is a central conjecture in pure mathematics and number theory. 

* **The Statement:** All non-trivial zeros of the Riemann zeta function $\zeta(s)$ have a real part equal to $\frac{1}{2}$.
* **The Critical Line:** The complex numbers of the form $s = \frac{1}{2} + it$, where $t$ is a real number and $i = \sqrt{-1}$.
* **Significance:** It is listed as part of **Hilbert's eighth problem** in David Hilbert's 1900 list of 23 unsolved problems and is one of the seven **Millennium Prize Problems** established by the Clay Mathematics Institute, which offers a US$ 1 million reward for a valid proof.

### 1.2 Zeros of the Zeta Function
The zeros of $\zeta(s)$ are divided into two distinct categories:
1. **Trivial Zeros:** Located at the negative even integers ($s = -2, -4, -6, \dots$). These arise directly from the sine factor in Riemann's functional equation.
2. **Non-Trivial Zeros:** Complex numbers $s = \sigma + it$ located strictly inside the **critical strip** ($0 < \operatorname{Re}(s) < 1$). The Riemann hypothesis asserts that all non-trivial zeros lie precisely on the central line $\operatorname{Re}(s) = \frac{1}{2}$.

---

## 2. Mathematical Foundations & Functional Properties

### 2.1 Infinite Series and Euler Product
For complex numbers $s$ with real part $\operatorname{Re}(s) > 1$, the Riemann zeta function is defined as the absolutely convergent infinite series:

$$\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s} = \frac{1}{1^s} + \frac{1}{2^s} + \frac{1}{3^s} + \dots$$

In the 1730s, Leonhard Euler evaluated this series for real values of $s$ in connection with the Basel problem and established the fundamental identity known as the **Euler product**:

$$\zeta(s) = \prod_{p \text{ prime}} \frac{1}{1 - p^{-s}} = \frac{1}{1 - 2^{-s}} \cdot \frac{1}{1 - 3^{-s}} \cdot \frac{1}{1 - 5^{-s}} \cdots$$

This product extends over all prime numbers $p$, providing the foundational bridge between continuous complex analysis and discrete number theory.

### 2.2 Analytic Continuation
Because the initial series and Euler product converge only when $\operatorname{Re}(s) > 1$, analytic continuation is required to extend $\zeta(s)$ to the entire complex plane. By the identity theorem, any meromorphic continuation yields a unique result.

#### Extension to $\operatorname{Re}(s) > 0$
The zeta function relates to the **Dirichlet eta function** $\eta(s)$ by:

$$\left(1 - \frac{2}{2^s}\right)\zeta(s) = \eta(s) = \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n^s} = \frac{1}{1^s} - \frac{1}{2^s} + \frac{1}{3^s} - \dots$$

The alternating series for $\eta(s)$ converges for all $s$ with $\operatorname{Re}(s) > 0$. Thus, $\zeta(s)$ can be redefined as $\frac{\eta(s)}{1 - 2/2^s}$, extending its domain to $\operatorname{Re}(s) > 0$, except for a single **simple pole at $s = 1$** (and removable singularities where $1 - 2/2^s = 0$, handled via limits).

#### Extension to $\operatorname{Re}(s) \le 0$ (The Functional Equation)
In the critical strip $0 < \operatorname{Re}(s) < 1$, $\zeta(s)$ satisfies Riemann's functional equation:

$$\zeta(s) = 2^s \pi^{s-1} \sin\left(\frac{\pi s}{2}\right) \Gamma(1-s) \zeta(1-s)$$

where $\Gamma$ is the Euler gamma function. This equation allows $\zeta(s)$ to be defined for all nonzero complex numbers. 
* When $s$ is a negative even integer, $\sin\left(\frac{\pi s}{2}\right) = 0$, giving rise to the **trivial zeros**.
* At $s = 0$, taking limits yields $\zeta(0) = -\frac{1}{2}$.
* The functional equation demonstrates that $\zeta(s)$ has no zeros with negative real part other than the trivial zeros, confirming that all non-trivial zeros must reside within the **critical strip** $0 < \operatorname{Re}(s) < 1$.

---

## 3. Origin in Prime Number Theory

In his 1859 paper, Bernhard Riemann derived an explicit formula for $\pi(x)$, the number of primes less than or equal to $x$. He framed this in terms of the prime-power counting function $\Pi(x)$:

$$\Pi(x) = \pi(x) + \frac{1}{2}\pi(x^{1/2}) + \frac{1}{3}\pi(x^{1/3}) + \frac{1}{4}\pi(x^{1/4}) + \dots$$

Using the Möbius inversion formula with the Möbius function $\mu(n)$, $\pi(x)$ can be recovered:

$$\pi(x) = \sum_{n=1}^{\infty} \frac{\mu(n)}{n} \Pi(x^{1/n})$$

Riemann showed that $\Pi_0(x)$ (the average of the left and right limits of $\Pi(x)$ at discontinuities) is given by the **explicit formula**:

$$\Pi_0(x) = \operatorname{li}(x) - \sum_{\rho} \operatorname{li}(x^\rho) - \log 2 + \int_{x}^{\infty} \frac{dt}{t(t^2-1)\log t}$$

* $\operatorname{li}(x) = \int_{0}^{x} \frac{dt}{\log t}$ is the offset-free logarithmic integral function.
* The sum $\sum_{\rho} \operatorname{li}(x^\rho)$ runs over all non-trivial zeros $\rho$ of the zeta function, ordered by the absolute value of their imaginary parts.
* **Core Insight:** The non-trivial zeros $\rho$ directly act as "frequencies" that dictate the exact wave-like **oscillations of prime numbers** around their expected distribution $\operatorname{li}(x)$.

---

## 4. Equivalent Formulations and Consequences

The truth of the Riemann hypothesis implies precise control over error terms across various branches of number theory and analysis.

### 4.1 Prime Distribution and Gap Estimates
* **Error in Prime Number Theorem:** Helge von Koch (1901) proved that RH is equivalent to the tightest bound on prime distribution. Schoenfeld (1976) made this explicit:
  $$|\pi(x) - \operatorname{li}(x)| < \frac{1}{8\pi}\sqrt{x}\log(x) \quad \text{for all } x \ge 2657$$
  $$|\psi(x) - x| < \frac{1}{8\pi}\sqrt{x}\log^2(x) \quad \text{for all } x \ge 73.2 \quad (\text{where } \psi(x) \text{ is Chebyshev's second function})$$
* **Short Interval Primes:** Adrian Dudek (2014) showed RH implies that for $x \ge 2$, there is always a prime $p$ in the interval $x - \frac{4}{\pi}\sqrt{x}\log x < p \le x$.
* **Large Prime Gaps:** Cramér proved that under RH, prime gaps $p_{n+1} - p_n = O(\sqrt{p}\log p)$. (Note: Cramér's conjecture predicts a tighter bound of $O((\log p)^2)$).

### 4.2 Growth of Arithmetic Functions
* **Möbius Function & Mertens Function:** RH is equivalent to the claim that $M(x) = \sum_{n \le x} \mu(n) = O(x^{1/2+\varepsilon})$ for all $\varepsilon > 0$. Soundararajan (2009) refined this bound under RH to $M(x) = O\left(x^{1/2} \exp\left((\log x)^{1/2}(\log \log x)^{14}\right)\right)$. Note that the stronger *Mertens conjecture* ($|M(x)| \le \sqrt{x}$) was disproved by Odlyzko and te Riele in 1985.
* **Robin’s Theorem (1984):** RH is true if and only if the sum-of-divisors function $\sigma(n)$ satisfies:
  $$\sigma(n) < e^\gamma n \log\log n \quad \text{for all } n > 5040$$
  where $\gamma \approx 0.577215$ is the Euler–Mascheroni constant.
* **Lagarias’s Criterion (2002):** RH is equivalent to $\sigma(n) < H_n + \log(H_n)e^{H_n}$ for all $n > 1$, where $H_n$ is the $n$-th harmonic number.
* **Euler’s Totient Function $\phi(n)$:** RH is true if and only if $\frac{n}{\phi(n)} < e^\gamma \log\log n + \frac{e^\gamma(4+\gamma-\log 4\pi)}{\sqrt{\log n}}$ for all $n \ge 120569\#$ (where $120569\#$ is the primorial of the 120,569th prime).
* **Farey Sequences:** Franel and Landau (1924) showed RH is equivalent to specific regularity bounds on the distance between terms of the $n$-th Farey sequence $F_n$ and uniform distribution points $i/m$.

### 4.3 Analytic Equivalences
* **Speiser’s Theorem (1934):** RH is equivalent to the derivative $\zeta'(s)$ having no zeros in the strip $0 < \operatorname{Re}(s) < \frac{1}{2}$.
* **De Bruijn–Newman Constant ($\Lambda$):** Defined such that $H(\lambda, z)$ has only real zeros if and only if $\lambda \ge \Lambda$. RH is equivalent to $\Lambda \le 0$. Rodgers and Tao (2020) proved $\Lambda = 0$ is the lower bound (thus RH is equivalent to $\Lambda = 0$). As of 2020, Platt and Trudgian established the upper bound $\Lambda \le 0.2$.
* **Riesz & Nyman–Beurling Criteria:** Equivalences based on power series asymptotics of $\zeta(2k)$ (Riesz) or the density of functional spaces in $L^2(0,1)$ (Nyman–Beurling–Baez-Duarte).

### 4.4 Generalized Riemann Hypothesis (GRH) & Extensions
* **Dirichlet $L$-series:** Extends RH to $L(s, \chi)$. Implies non-existence of Siegel zeros.
* **Dedekind Zeta Functions:** Extended RH applies to algebraic number fields.
* **Applications of GRH:**
  * Proves completeness of Gauss's list of imaginary quadratic fields with class number 1 (Grönwall 1913; later proved unconditionally by Baker, Stark, and Heegner).
  * Solves Goldbach's ternary conjecture for large odd numbers (Hardy-Littlewood 1923; proved unconditionally by Helfgott 2013).
  * Implies polynomial-time primality testing via the Miller test (Miller 1976; proved unconditionally via AKS in 2002).
  * Implies Artin’s conjecture on primitive roots (Hooley 1967).
  * Confirms Patterson's conjecture on cubic Gauss sums (Dunn & Radziwill 2021).

### 4.5 Excluded Middle Proofs
Some mathematical results are proven by showing they hold *both* when GRH/RH is true and when it is false:
* **Littlewood’s Theorem (1914):** $\pi(x) - \operatorname{li}(x)$ changes sign infinitely many times (disproving the idea that $\pi(x)$ is always less than $\operatorname{li}(x)$).
* **Gauss's Class Number Conjecture:** Proved via sequence of theorems by Hecke (assuming GRH), Deuring (assuming RH false), Mordell, and Heilbronn, before Siegel (1935) obtained an unconditional proof.

---

## 5. Zero Distribution & Critical Line Results

### 5.1 Zero Counting Function $N(T)$
The number of zeros $N(T)$ in the critical strip with imaginary part $0 < \operatorname{Im}(s) \le T$ is given by:

$$N(T) = \frac{T}{2\pi}\log\left(\frac{T}{2\pi e}\right) + \frac{7}{8} + S(T) + O\left(\frac{1}{T}\right)$$

where $S(T) = \frac{1}{\pi} \operatorname{Arg}\zeta\left(\frac{1}{2} + iT\right) = O(\log T)$. Trudgian (2014) proved an explicit bound:

$$\left| N(T) - \frac{T}{2\pi}\log \frac{T}{2\pi e} \right| \le 0.112\log T + 0.278\log\log T + 3.385 + \frac{0.2}{T} \quad (T > e)$$

### 5.2 Zero-Free Regions
* **Hadamard & de la Vallée-Poussin (1896):** Independently proved $\zeta(1 + it) \neq 0$, showing no zeros lie on the line $\operatorname{Re}(s) = 1$. This was the key step to proving the Prime Number Theorem.
* **Mossinghoff, Trudgian, and Yang (Dec 2022):** Established modern explicit zero-free boundaries, including $\sigma \ge 1 - \frac{1}{5.558691\log|t|}$ for $|t| \ge 2$.

### 5.3 Proportion of Zeros on the Critical Line
Progress on determining the proportion $\kappa$ of non-trivial zeros lying *strictly on* $\operatorname{Re}(s) = \frac{1}{2}$:

| Year | Mathematician(s) / System | Proportion on Critical Line ($\kappa$) | Method / Notes |
| :--- | :--- | :--- | :--- |
| 1914 | G. H. Hardy | Infinitely many | First proof of infinitely many real zeros on the line. |
| 1942 | Atle Selberg | Positive proportion ($\kappa > 0$) | Moment method over short intervals. |
| 1974 | Norman Levinson | $\kappa > 1/3$ ($33.3\%$) | Related zeros of $\zeta(s)$ to its derivative $\zeta'(s)$ using mollifiers. |
| 1989 | Brian Conrey | $\kappa > 2/5$ ($40.0\%$) | Refinement of Levinson's mollifier method. |
| 2020 | Pratt, Robles, Zaharescu, Zeindler | $\kappa > 5/12$ ($41.6\%$) | Extended mollifiers with Kloosterman sums. |
| **Aug 2026** | **Claude (Anthropic) + Human Researchers** | **$\kappa > 2/3$ ($66.6\% \to \approx 67.25\%$)** | Abandoned Levinson's method. Used Montgomery's pair-correlation, Gabor test families, Sylvester's law of inertia, and von Neumann trace inequalities. Verified in **Lean 4**. |
| **Sep 2026** | **Youness Lamzouri** | **$\kappa > 2/3$ ($\approx 67.25\%$)** | Simplified Claude's proof, replacing matrix algebra with Hilbert space inequalities (Bessel's inequality & Gram-Schmidt). |

### 5.4 High-Height Zero Free Half-Plane (2026 Breakthrough)
* **OpenAI (September 30, 2026):** Published a formalized proof establishing the **Quasi-Riemann Hypothesis** for a fixed zero-free half-plane:
  $$\operatorname{Re}(s) > \frac{7}{8}$$
  This applies uniformly to the Riemann zeta function, all Dirichlet $L$-functions (excluding principal poles at $s=1$), and finite-order Hecke $L$-functions over $\mathbb{Q}(\sqrt{-3})$. It also formalizes a uniform logarithmic exclusion region for Landau–Siegel zeros ($1-\beta \ge c/\log q$).

---

## 6. Numerical Verification & Computational History

Computationally verifying that zeros lie on the critical line involves evaluating Hardy's $Z$-function $Z(t) = \zeta\left(\frac{1}{2}+it\right)e^{i\theta(t)}$ to locate sign changes, combined with **Turing's method** to ensure no zeros off the line were missed.

### 6.1 Historical Verification Milestones

| Year | Zeros Verified | Author / Method | Key Notes / Discoveries |
| :--- | :--- | :--- | :--- |
| 1859? | 3 | B. Riemann | Used the unpublished Riemann–Siegel formula. |
| 1903 | 15 | J. P. Gram | Euler–Maclaurin formula. Formulated **Gram's Law**. |
| 1914 | 79 | R. J. Backlund | Introduced argument tracking $S(T)$. |
| 1925 | 138 | J. I. Hutchinson | Discovered 1st failure of Gram's law at Gram point $g_{126}$. |
| 1935 | 195 | E. C. Titchmarsh | Used rediscovered Riemann–Siegel formula ($O(T^{3/2+\varepsilon})$ steps). |
| 1936 | 1,041 | Titchmarsh & Comrie | Last manual (by hand) computation. |
| 1953 | 1,104 | Alan Turing | First digital computer evaluation; invented **Turing's method**. |
| 1956 | 25,000 | D. H. Lehmer | Discovered **Lehmer's phenomenon** (extremely close zero pairs). |
| 1968 | 3,500,000 | Rosser, Yohe, Schoenfeld | Formulated **Rosser's rule** for Gram blocks. |
| 1979 | 81,000,001 | R. P. Brent | Large-scale computer verification. |
| 1986 | 1,500,000,001 | van de Lune, te Riele, Winter | Extensive statistical analysis of $Z(t)$. |
| 1987–98 | Heights $10^{12}$–$10^{21}$ | Andrew Odlyzko | Tested spacing against **GUE Random Matrix Theory**. |
| 2004 | $\approx 9 \times 10^{11}$ | S. Wedeniwski | ZetaGrid distributed computing project. |
| 2004 | $10^{13}$ | Gourdon & Demichel | Used Odlyzko–Schönhage algorithm. |
| **2020** | **$1.2363 \times 10^{13}$** | **Platt & Trudgian** | Verified all zeros up to height $T = 3 \times 10^{12}$. |

### 6.2 Gram Points, Gram's Law, and Rosser's Rule
* **Gram Point ($g_n$):** A point on the critical line $\frac{1}{2}+it$ where $\zeta(s)$ is real, defined by $\theta(g_n) = n\pi$.
* **Gram's Law:** The heuristic expectation that $Z(t)$ changes sign exactly once between consecutive Gram points $g_n$ and $g_{n+1}$.
  * *First Failure:* Occurs at $g_{126}$ and the 127th zero.
  * *Failure Frequency:* Trudgian (2011) and Hanga (2020) showed Gram's law fails in a positive proportion of cases (~66% enclose 1 zero, ~17% enclose 0 zeros, ~17% enclose 2 zeros).
* **Rosser's Rule:** States that *Gram blocks* (intervals between good Gram points containing bad Gram points) usually contain the expected total number of zeros.

---

## 7. Theoretical Frameworks & Attempted Proofs

Mathematicians have constructed physical, analytical, and geometric frameworks to address the hypothesis:

1. **Operator Theory & Hilbert–Pólya Conjecture:** Proposes that the non-trivial zeros correspond to eigenvalues of a self-adjoint operator on a Hilbert space.
   * *Berry–Keating Conjecture (1999):* Suggests a classical Hamiltonian $H = xp$ whose quantum counterpart's spectrum aligns with the zeros.
2. **Random Matrix Theory (GUE):** Hugh Montgomery (1973) conjectured that the pair correlation of zeros matches the eigenvalues of random Hermitian matrices in the **Gaussian Unitary Ensemble (GUE)**. Andrew Odlyzko confirmed this with high-precision calculations at height $10^{12}$ and $10^{20}$. Katz and Sarnak extended this to families of $L$-functions governed by classical compact groups.
3. **Noncommutative Geometry:** Alain Connes formulated an approach connecting RH to an analogue of the Selberg trace formula acting on the adèle class space.
4. **Turán's Criterion & Failure:** Pál Turán showed a condition on partial sums of $\sum n^{-s}$ that would imply RH. However, Haselgrove (1958) disproved the underlying assumption, making Turán's result vacuously true.
5. **de Branges’ Approach:** Louis de Branges attempted a proof using Hilbert spaces of entire functions, but Conrey and Li (2000) demonstrated that the required positivity conditions fail.

---

## 8. Short-Answer Practice Questions

### Questions

1. **What is the precise statement of the Riemann hypothesis?**
2. **Define the critical strip and the critical line.**
3. **What are the trivial zeros of the Riemann zeta function, and why do they occur?**
4. **How did Euler express the Riemann zeta function as a product, and for which values of $s$ is this valid?**
5. **What is the simple pole of the Riemann zeta function, and what is its residue/value?**
6. **How does the Möbius function $\mu(n)$ relate to the Riemann hypothesis via the Mertens function $M(x)$?**
7. **What is Robin’s theorem concerning the sum-of-divisors function $\sigma(n)$?**
8. **Explain the significance of the 2026 Anthropic/Claude proof regarding zeros on the critical line.**
9. **What result did OpenAI establish on September 30, 2026, regarding zero-free regions?**
10. **What is Lehmer’s phenomenon?**
11. **Why did Turán’s approach to proving the Riemann hypothesis fail?**
12. **What does the Hilbert–Pólya conjecture propose?**

---

### Solutions & Answer Key

1. **Answer:** The Riemann hypothesis states that all non-trivial zeros of the Riemann zeta function $\zeta(s)$ have a real part equal to $\frac{1}{2}$.
2. **Answer:** The *critical strip* is the region of the complex plane where $0 < \operatorname{Re}(s) < 1$. The *critical line* is the vertical line $\operatorname{Re}(s) = \frac{1}{2}$ running down the middle of the critical strip.
3. **Answer:** The trivial zeros occur at the negative even integers ($s = -2, -4, -6, \dots$). They arise because the term $\sin\left(\frac{\pi s}{2}\right)$ in Riemann's functional equation vanishes at these points.
4. **Answer:** Euler expressed $\zeta(s)$ as the infinite product $\prod_{p \text{ prime}} \frac{1}{1 - p^{-s}}$. This identity is valid for complex $s$ with $\operatorname{Re}(s) > 1$.
5. **Answer:** The Riemann zeta function has a single simple pole at $s = 1$ with residue $1$.
6. **Answer:** The Mertens function is $M(x) = \sum_{n \le x} \mu(n)$. The Riemann hypothesis is logically equivalent to the growth bound $M(x) = O(x^{1/2 + \varepsilon})$ for every $\varepsilon > 0$.
7. **Answer:** Robin's theorem states that the Riemann hypothesis is true if and only if $\sigma(n) < e^\gamma n \log\log n$ holds for all $n > 5040$, where $\gamma$ is the Euler–Mascheroni constant.
8. **Answer:** In August 2026, Claude (Anthropic) and human researchers proved unconditionally that more than $2/3$ ($\approx 67.25\%$) of the non-trivial zeros lie on the critical line. They abandoned Levinson's mollifier method in favor of Montgomery's pair correlation, Gabor systems, Sylvester's law of inertia, and von Neumann's trace inequality, formally verifying the proof in Lean 4.
9. **Answer:** OpenAI formalized a proof of the Quasi-Riemann Hypothesis, establishing a fixed zero-free half-plane of $\operatorname{Re}(s) > \frac{7}{8}$ for the Riemann zeta function, Dirichlet $L$-functions, and finite-order Hecke $L$-functions over $\mathbb{Q}(\sqrt{-3})$.
10. **Answer:** Lehmer’s phenomenon refers to instances where two non-trivial zeros on the critical line are located extremely close together, making it difficult for computational algorithms to detect sign changes in Hardy's $Z$-function between them.
11. **Answer:** Turán showed that if partial sums $\sum_{n=1}^N n^{-s}$ had no zeros for $\operatorname{Re}(s) > 1$, RH would follow. However, Haselgrove and later researchers proved these partial sums *do* have zeros with $\operatorname{Re}(s) > 1$ for large $N$, rendering Turán's condition false/vacuous.
12. **Answer:** It proposes that the non-trivial zeros of $\zeta(s)$ correspond to the eigenvalues of an unknown self-adjoint operator on a Hilbert space, which would naturally guarantee that their real parts equal $\frac{1}{2}$.

---

## 9. Essay Prompts for Deeper Exploration

1. **Analytic Continuation and the Functional Equation:** Trace the mathematical steps required to extend the domain of the Riemann zeta function from its initial domain of convergence ($\operatorname{Re}(s) > 1$) across the entire complex plane. Discuss the roles of the Dirichlet eta function, the gamma function, and the functional equation, explaining how these tools reveal the trivial zeros and isolate the critical strip.

2. **The Explicit Formula and the Distribution of Primes:** Analyze Riemann’s 1859 explicit formula for $\Pi_0(x)$. Detail how the non-trivial zeros $\rho$ function as wave-like correction terms that modulate the density of prime numbers. Discuss how precise bounds on the locations of these zeros translate into optimal error bounds in the Prime Number Theorem.

3. **Equivalent Formulations across Mathematical Disciplines:** Select three distinct equivalences to the Riemann hypothesis—one from arithmetic functions (e.g., Robin's or Lagarias's criteria), one from analytic criteria (e.g., Speiser's theorem or the de Bruijn–Newman constant), and one from probabilistic/combinatorial bounds (e.g., Mertens function growth or Farey sequences). Compare their theoretical foundations and explain why RH acts as a unifying thread across these areas.

4. **The Evolution of Methods for Critical Line Zeros:** Compare the traditional mollification techniques pioneered by Levinson (1974) and refined by Conrey (1989) with the 2026 spectral/linear algebra approach developed by Claude/Anthropic and simplified by Lamzouri. Highlight why the historical method stalled near $41.6\%$ and how reformulating the problem via Montgomery's pair correlation and operator inequalities broke through the $2/3$ threshold.

5. **Random Matrix Theory and Quantum Chaos:** Explain the connection between the zeros of the Riemann zeta function and the eigenvalues of random Hermitian matrices in the Gaussian Unitary Ensemble (GUE). Discuss Montgomery's pair correlation conjecture, Odlyzko's computational findings, and how this physical analogue supports the Hilbert–Pólya vision of a spectral origin for the zeros.

---

## 10. Comprehensive Glossary

* **Analytic Continuation:** A mathematical technique used to extend the domain of a given analytic function beyond its original region of convergence while preserving its unique identity.
* **Automorphic $L$-function:** Global $L$-functions associated with automorphic representations, generalized in the Grand Riemann Hypothesis.
* **Critical Line:** The vertical line $\operatorname{Re}(s) = \frac{1}{2}$ in the complex plane where all non-trivial zeros are conjectured to lie.
* **Critical Strip:** The vertical region $0 < \operatorname{Re}(s) < 1$ in the complex plane containing all non-trivial zeros of the zeta function.
* **De Bruijn–Newman Constant ($\Lambda$):** A real constant defining a parametrized family of functions $H(\lambda, z)$. RH is equivalent to $\Lambda \le 0$; proved in 2020 to equal 0 ($\Lambda = 0$).
* **Dirichlet $L$-function:** A series defined by $L(s, \chi) = \sum \chi(n)n^{-s}$, generalizing the Riemann zeta function using Dirichlet characters $\chi$.
* **Dirichlet Eta Function ($\eta(s)$):** The alternating series $\sum_{n=1}^\infty (-1)^{n+1}n^{-s}$, used to analytically continue $\zeta(s)$ to $\operatorname{Re}(s) > 0$.
* **Euler Product:** An expression representing a Dirichlet series as an infinite product indexed over prime numbers, reflecting the unique factorization of integers.
* **Farey Sequence ($F_n$):** The ordered sequence of completely reduced fractions between 0 and 1 whose denominators do not exceed $n$.
* **Gaussian Unitary Ensemble (GUE):** A statistical ensemble of random $N \times N$ Hermitian matrices whose eigenvalue spacing statistics match those of the non-trivial zeros of $\zeta(s)$.
* **Gram Block:** An interval bounded by two "good" Gram points such that all interior Gram points are "bad".
* **Gram Point ($g_n$):** Points $t$ on the critical line where $\zeta\left(\frac{1}{2}+it\right)$ is guaranteed to be a real number, defined by $\theta(g_n) = n\pi$.
* **Gram’s Law:** The heuristic rule stating that $Z(t)$ typically changes sign once between consecutive Gram points.
* **Hardy’s $Z$-Function:** A real-valued function $Z(t) = \zeta\left(\frac{1}{2}+it\right)e^{i\theta(t)}$ used to locate real zeros of the zeta function on the critical line.
* **Ihara Zeta Function:** A zeta function defined on finite graphs whose zero locations correlate with Ramanujan graph properties.
* **Lean 4:** An interactive theorem prover and programming language used to formally verify complex mathematical proofs, including the 2026 Claude critical line proof.
* **Lehmer’s Phenomenon:** The occurrence of pairs of non-trivial zeros that lie exceptionally close together on the critical line.
* **Mertens Function ($M(x)$):** The summatory function of the Möbius function, $M(x) = \sum_{n \le x} \mu(n)$.
* **Möbius Function ($\mu(n)$):** An arithmetic function equal to 0 if $n$ is squared, $1$ if $n$ has an even number of distinct prime factors, and $-1$ if it has an odd number.
* **Non-Trivial Zeros:** Zeros of $\zeta(s)$ located strictly within the critical strip $0 < \operatorname{Re}(s) < 1$.
* **Prime-Counting Function ($\pi(x)$):** The function giving the exact number of prime numbers less than or equal to $x$.
* **Quasi-Riemann Hypothesis:** The statement that all non-trivial zeros lie in a fixed zero-free half-plane $\operatorname{Re}(s) > \theta$ for some $\theta < 1$ (proved for $\theta = 7/8$ by OpenAI in 2026).
* **Riemann Zeta Function ($\zeta(s)$):** The meromorphic function defined for $\operatorname{Re}(s) > 1$ by $\sum_{n=1}^\infty n^{-s}$ and continued across the complex plane.
* **Robin’s Criterion:** An inequality regarding the sum-of-divisors function $\sigma(n) < e^\gamma n \log\log n$ that holds for all $n > 5040$ if and only if RH is true.
* **Rosser’s Rule:** A refined heuristic stating that Gram blocks bounded by good Gram points contain the expected total number of zeros.
* **Selberg Class:** A class of Dirichlet series satisfying specific axioms (functional equation, Ramanujan hypothesis, Euler product) expected to obey generalized Riemann hypotheses.
* **Selberg Zeta Function:** A zeta function defined on Riemann surfaces whose zeros relate to the eigenvalues of the Laplacian operator.
* **Skewes' Number:** An upper bound for the smallest value $x$ for which $\pi(x) > \operatorname{li}(x)$, demonstrating how slowly analytic expressions settle into asymptotic behavior.
* **Trivial Zeros:** The zeros of $\zeta(s)$ located at negative even integers ($s = -2, -4, -6, \dots$).
* **Turing’s Method:** An algorithmic procedure devised by Alan Turing using Gram blocks to rigorously verify that no zeros on the critical line were missed in computational searches.