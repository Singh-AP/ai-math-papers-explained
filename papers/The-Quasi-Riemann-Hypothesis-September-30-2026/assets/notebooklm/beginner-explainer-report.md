# Understanding the Quasi-Riemann Hypothesis: A Beginner's Guide to the $\text{Re}(s) > 7/8$ Zero-Free Half-Plane

### 1. The One-Sentence Version

> In a September 30, 2026 research breakthrough, OpenAI established the Quasi-Riemann Hypothesis by proving that all finite-order Hecke $L$-functions over the imaginary quadratic field $\mathbb{Q}(\sqrt{-3})$, all Dirichlet $L$-functions, and the Riemann zeta function possess no zeros in the complex half-plane $\text{Re}(s) > 7/8$ (with the simple pole at $s = 1$ naturally permitted for principal characters).

---

### 2. The Problem: Zeros, Zero-Free Half-Planes, and the Quasi-Riemann Hypothesis

#### 2.1 What are Zeta and Dirichlet $L$-Functions?
The **Riemann zeta function**, denoted by $\zeta(s)$, is an infinite series defined for complex numbers $s = \sigma + it$ in the half-plane of absolute convergence $\text{Re}(s) = \sigma > 1$:

$$\zeta(s) = \sum_{n=1}^\infty \frac{1}{n^s} = \frac{1}{1^s} + \frac{1}{2^s} + \frac{1}{3^s} + \cdots$$

First evaluated for real integers by Leonhard Euler in the 1730s, the function provides the fundamental bridge between continuous analysis and discrete number theory through the **Euler product**, which equates the sum over all natural numbers to an infinite product over all prime numbers $p$:

$$\zeta(s) = \prod_{p \text{ prime}} \frac{1}{1 - p^{-s}} = \frac{1}{1 - 2^{-s}} \cdot \frac{1}{1 - 3^{-s}} \cdot \frac{1}{1 - 5^{-s}} \cdots$$

**Dirichlet $L$-functions**, denoted $L(s, \chi)$, generalize the Riemann zeta function by weighting each term with a periodic arithmetic character $\chi(n)$:

$$L(s, \chi) = \sum_{n=1}^\infty \frac{\chi(n)}{n^s}$$

Through **analytic continuation**, these functions are extended beyond $\text{Re}(s) > 1$ to meromorphic functions defined across the entire complex plane. Crucially, $s = 1$ is a simple pole *only* for the Riemann zeta function $\zeta(s)$ and for $L$-functions attached to principal Dirichlet or Hecke characters; for all non-principal characters, $L(s, \chi)$ is an entire function with no pole at $s = 1$. 

During continuation, two classes of zeros (points where the function evaluates to zero) emerge:
*   **Trivial Zeros:** Zeros arising predictably from the gamma/sine factors in the functional equation, located at negative even integers ($s = -2, -4, -6, \dots$) for $\zeta(s)$.
*   **Nontrivial Zeros:** Zeros located in the interior region of the complex plane whose precise distribution dictates the fine distribution of prime numbers.

#### 2.2 The Critical Strip and Zero-Free Regions
The open vertical strip $0 < \text{Re}(s) < 1$ is known as the **critical strip**, and its central vertical symmetry axis $\text{Re}(s) = 1/2$ is called the **critical line**. Functional equations show that all nontrivial zeros of $\zeta(s)$ and related $L$-functions must lie inside this critical strip, positioned symmetrically around $\text{Re}(s) = 1/2$.

Geometrically, a **zero-free region** denotes a domain in the complex plane where the function is mathematically proven never to vanish. 

#### 2.3 Defining the Quasi-Riemann Hypothesis (QRH)
*   **The Riemann Hypothesis (RH):** Conjectures that *all* nontrivial zeros lie exactly on the critical line $\text{Re}(s) = 1/2$.
*   **The Quasi-Riemann Hypothesis (QRH):** A foundational assertion stating that there exists some fixed threshold $\theta < 1$ such that $\zeta(s)$ (and its generalizations) has no zeros in the uniform vertical half-plane $\text{Re}(s) > \theta$.

Understanding the geometric contrast between classical zero-free regions and a zero-free half-plane is vital:
Classical zero-free regions are *asymptotically narrowing curves* of the form $1 - \sigma \ge C / \log |t|$. Because the width $C / \log |t|$ shrinks to zero as the imaginary height $|t| \to \infty$, classical theorems allow nontrivial zeros to creep arbitrarily close to the boundary line $\text{Re}(s) = 1$ at high imaginary coordinates. 

In contrast, the 2026 proof of QRH at $\theta = 7/8$ establishes a **fixed, uniform vertical barrier** of width $1/8$ extending infinitely upwards and downwards across all imaginary heights $t$.

| Boundary / Hypothesis | Mathematical Definition | Geometric Location in Complex Plane | Status / Significance |
| :--- | :--- | :--- | :--- |
| **Riemann Hypothesis (RH)** | All nontrivial zeros satisfy $\text{Re}(s) = 1/2$ | Strictly on the 1-dimensional critical line $\text{Re}(s) = 1/2$ | Unproven conjecture ($\theta = 1/2$) |
| **Quasi-Riemann Hypothesis (QRH)** | No nontrivial zeros exist with $\text{Re}(s) > \theta$ for a fixed $\theta < 1$ | Entire vertical half-plane to the right of $\text{Re}(s) = \theta$ | **Proven for $\theta = 7/8$** (OpenAI, 2026) |
| **Classical Zero-Free Region** | $1 - \sigma \ge \frac{C}{\log \|t\|}$ or $\frac{C}{(\log \|t\|)^{2/3}(\log \log \|t\|)^{1/3}}$ | Wedge/curve narrowing asymptotically as height $\|t\| \to \infty$ | Classical proven bounds (Hadamard, de la Vallée Poussin, Korobov–Vinogradov, Mossinghoff et al.) |

---

### 3. History: From Euler and Riemann to Modern Breakthroughs

| Era / Date | Mathematician(s) / Entity | Key Contribution / Breakthrough |
| :--- | :--- | :--- |
| **1730s–1744** | Leonhard Euler | Evaluated $\zeta(s)$ for integer values (Basel Problem) and proved the Euler Product formula connecting infinite series to prime numbers. |
| **1859** | Bernhard Riemann | Developed analytic continuation and functional equations for $\zeta(s)$, formulated the explicit formula linking zeros to prime counting $\pi(x)$, and proposed RH ($\text{Re}(s) = 1/2$). |
| **1896** | Jacques Hadamard & Charles Jean de la Vallée Poussin | Independently proved that no zeros lie on $\text{Re}(s) = 1$, unconditionally establishing the Prime Number Theorem. |
| **1899–1900** | Charles Jean de la Vallée Poussin | Established the first classical zero-free region curve $1 - \sigma \ge C / \log\|t\|$. |
| **1914** | G. H. Hardy | Proved that infinitely many nontrivial zeros lie exactly on the critical line $\text{Re}(s) = 1/2$. |
| **1914–1918** | Harald Bohr, Edmund Landau, Erich Hecke | Developed zero-density estimates and extended $L$-function theory to Hecke characters over algebraic number fields. |
| **1930s–1950s** | Edmund Landau, Carl Ludwig Siegel | Formalized the theory of potential real zeros near $s = 1$ (Landau–Siegel zeros) and their connection to quadratic class numbers. |
| **1974** | Norman Levinson | Developed mollifier techniques to prove that at least $1/3$ ($33.3\%$) of nontrivial zeros lie on the critical line. |
| **1989** | Brian Conrey | Refined mollification bounds to prove at least $2/5$ ($40\%$) of nontrivial zeros lie on the critical line. |
| **2020** | Kyle Pratt, Nicolas Robles, Alexandru Zaharescu, Dirk Zeindler | Extended the critical-line zero proportion to more than $5/12$ ($\approx 41.6\%$). |
| **2022** | Michael J. Mossinghoff, Timothy S. Trudgian, Andrew Yang | Established state-of-the-art explicit zero-free curves, including $\sigma \ge 1 - \frac{1}{55.241(\log \|t\|)^{2/3}(\log \log \|t\|)^{1/3}}$. |
| **August 2026** | Anthropic (Claude AI) & Human Researchers | Unconditionally proved that at least $2/3$ ($66.6\%$) of nontrivial zeros lie on the critical line, optimized via test families to $\frac{3}{2} - \frac{1}{\sqrt{2}}\cot\left(\frac{1}{\sqrt{2}}\right) \approx 67.25\%$, using Gabor systems and rank-trace matrix inequalities. Verified in Lean 4. |
| **September 2026** | Youness Lamzouri | Published a simplified Hilbert space proof of the $> 2/3$ critical-line zero bound using Bessel's inequality and Gram–Schmidt orthogonalization. |
| **September 30, 2026 (Preprint) / October 2026** | OpenAI | Proved a uniform, fixed vertical zero-free half-plane $\text{Re}(s) > 7/8$ for finite-order Hecke $L$-functions over $\mathbb{Q}(\sqrt{-3})$, Dirichlet $L$-functions, and the Riemann zeta function. |

---

### 4. Why It Matters: Prime Distributions, Siegel Zeros, and Beyond

Establishing a uniform zero-free half-plane $\text{Re}(s) > 7/8$ represents an epochal advance across analytic number theory:

*   **Primes in Arithmetic Progressions:** Under classical zero-free curves, the error term in the prime counting function $\pi(x) - \text{li}(x)$ is bounded only by sub-polynomial decay rates of the form $O(x \exp(-c\sqrt{\log x}))$. Establishing $\text{Re}(s) > 7/8$ unlocks a true **power-saving error bound** of $O(x^{7/8} \log x)$. This dramatically compresses the allowed fluctuations of prime counts in arithmetic progressions, narrowing the gap toward RH's optimal $O(x^{1/2} \log x)$ bound.
*   **Elimination and Bounding of Landau–Siegel Zeros:** Real zeros near $s = 1$ (Landau–Siegel zeros) distort class numbers and prime distributions. The $7/8$ theorem unconditionally eliminates such exceptional zeros near 1 by providing a uniform logarithmic exclusion region: there exists an absolute constant $c > 0$ such that for every primitive nonprincipal real Dirichlet character of conductor $q \ge 3$, any real zero $\beta$ in $0 < \beta < 1$ satisfies $1 - \beta \ge c / \log q$.
*   **Least Quadratic Nonresidues:** Eliminating zero concentrations in $\text{Re}(s) > 7/8$ tightens character sum estimates (such as Burgess-type bounds), placing strict upper limits on the magnitude of the smallest quadratic nonresidue modulo $p$.
*   **Deterministic Primality & Algorithmic Bounds:** Guaranteeing a zero-free buffer zone eliminates structural bad cases in number-theoretic algorithms, providing unconditional runtime guarantees for deterministic primality tests and class number computations.

---

### 5. The Main Idea of the Proof: Step-by-Step in Plain Language

The paper *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\text{Re}(s) > 7/8$* constructs its proof through a 7-step sequence:

1.  **Proof by Contradiction on the Rightmost Zero:** The proof assumes the existence of a hypothetical zero $\rho_0 = \beta_0 + i \gamma_0$ located inside the forbidden region $\text{Re}(s) > 7/8$.
2.  **The "Continuation from a Common Signal" Principle:** The framework identifies a foundational analytic/spectral signal shared across algebraic extensions. Constraints on this shared signal propagate rigid structural dependencies across character values.
3.  **The Cubic-Theta Character Sum & Dual Representations:** The algebraic backbone of the proof relies on the imaginary quadratic field $\mathbb{Q}(\sqrt{-3})$ (the Eisenstein integers $\mathbb{Z}[\omega]$). Because $\mathbb{Q}(\sqrt{-3})$ possesses 6th roots of unity and rich hexagonal symmetry, it uniquely supports the construction of specialized cubic-theta character sums. These sums admit two distinct, exact dual representations: one via functional reflection equations and the other via multi-dimensional Poisson summation formulas.
4.  **Application of Large Sieve Bounds:** Large sieve inequalities on $\mathbb{Q}(\sqrt{-3})$ are deployed to bound the average behavior of these character sums across families of positive moduli, suppressing unexpected phase alignments or local concentrations.
5.  **The Zero Detector Construction:** The proof constructs an analytic "detector" function that integrates the $L$-function against a positive test kernel. If a zero exists at $\beta_0 > 7/8$, its contribution generates a dominant negative term that overpowers the positive contribution of the rest of the spectrum. This forces an impossible negative value on an expression strictly defined as a positive square norm—producing an explicit positivity/norm violation.
6.  **The Two-Stage Thresholding ($11/12 \to 7/8$):** The analysis proceeds in two distinct stages. Section 3 of the paper first establishes an unweighted baseline threshold at $\text{Re}(s) > 11/12$, which represents the natural barrier imposed by standard large sieve estimates. The paper then introduces optimized sieve weights and theta-sum cancellations to sharpen the threshold to the final bound $\text{Re}(s) > 7/8$.
7.  **Transfer Mechanism:** Once established for finite-order Hecke $L$-functions over $\mathbb{Q}(\sqrt{-3})$, a structural transfer mechanism maps the result directly to all Dirichlet $L$-functions and to the classical Riemann zeta function $\zeta(s)$.

---

### 6. Intellectual Foundations: Standing on the Shoulders of Giants

| Proof Component | Foundational Tool / Concept | Pioneering Mathematicians |
| :--- | :--- | :--- |
| **Eisenstein Symmetry & Base Field** | Hexagonal Lattice Symmetry & 6th Roots of Unity in $\mathbb{Q}(\sqrt{-3})$ | Carl Friedrich Gauss, Gotthold Eisenstein |
| **Cubic-Theta Character Sums** | Character Sums, Theta Series, Cubic Reciprocity | Leonhard Euler, Carl Friedrich Gauss, Carl Gustav Jacob Jacobi |
| **Dual Representations** | Harmonic Analysis & Multi-Dimensional Poisson Summation | Siméon Denis Poisson |
| **Bounding Character Averages** | Sieve Theory & The Large Sieve Inequality | Yuri Linnik, Alfréd Rényi, Enrico Bombieri |
| **Reflection Equations & Continuation** | Functional Equations of $L$-Functions | Bernhard Riemann, Erich Hecke |
| **Field Extension Transfer** | $L$-Functions with Grössencharaktern over Number Fields | Erich Hecke |

---

### 7. Scope, Caveats, and What It Does Not Prove

> **IMPORTANT CAVEATS & SCOPE LIMITATIONS**
>
> *   **Not the Full Riemann Hypothesis:** Proving a zero-free half-plane for $\text{Re}(s) > 7/8$ proves the *Quasi-Riemann Hypothesis* ($\theta = 7/8$). It does **not** prove the full Riemann Hypothesis ($\theta = 1/2$). The critical strip interval $1/2 < \text{Re}(s) \le 7/8$ remains unresolved.
> *   **Principal Poles Excluded:** The zero-free assertion applies strictly to zeros. Principal Dirichlet and Hecke characters (and $\zeta(s)$) exhibit a simple pole at $s = 1$, which is naturally permitted and excluded from zero-free assertions; non-principal character $L$-functions are entire functions.
> *   **AI Authorship Context:** The paper was generated and published by OpenAI on September 30, 2026.
> *   **Formalization Status in Lean 4:** According to the official repository documentation (`math/lean/docs/003.md`):
>     *   **What IS Formalized:** The core theorem establishing $\theta = 7/8$ for the Riemann zeta function, Dirichlet $L$-functions (uniformly over all positive moduli and characters), finite-order Hecke $L$-functions over $\mathbb{Q}(\sqrt{-3})$, and the uniform logarithmic Landau–Siegel zero exclusion ($1 - \beta \ge c / \log q$ for real zeros $0 < \beta < 1$ of primitive nonprincipal real characters modulo $q \ge 3$).
>     *   **What IS NOT Formalized:** Secondary downstream applications discussed in later narrative sections of the paper text are omitted from the Lean codebase.

---

### 8. Glossary of Key Terms

| Term | Plain-Language Definition |
| :--- | :--- |
| **Riemann Zeta Function $\zeta(s)$** | An infinite series $\sum n^{-s}$ connecting complex analysis to prime numbers via the Euler product. |
| **Dirichlet $L$-Function** | A generalized zeta function $L(s, \chi) = \sum \chi(n)n^{-s}$ weighted by a periodic arithmetic character $\chi(n)$. |
| **Critical Strip & Critical Line** | The vertical region $0 < \text{Re}(s) < 1$ containing all nontrivial zeros; the central line is $\text{Re}(s) = 1/2$. |
| **Zero-Free Half-Plane** | A continuous vertical half-plane $\text{Re}(s) > \theta$ in the complex plane where a function is proven to have no zeros. |
| **Quasi-Riemann Hypothesis (QRH)** | The assertion that no nontrivial zeros exist to the right of a fixed boundary line $\text{Re}(s) = \theta$ for some threshold $\theta < 1$. |
| **Hecke $L$-Function over $\mathbb{Q}(\sqrt{-3})$** | An $L$-function constructed over the imaginary quadratic field formed by adjoining $\sqrt{-3}$ to the rational numbers, leveraging Eisenstein integer symmetry. |
| **Siegel Zero (Landau–Siegel Zero)** | A hypothetical real zero $\beta$ of an $L$-function located extremely close to $s = 1$ for a real character. |
| **Lean 4 Theorem Prover** | An interactive proof assistant and formal verification system used to mechanically verify the logical correctness of mathematical definitions and proof steps. |

---

### 9. Sources and References

1. OpenAI (September 30, 2026). *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane $\text{Re}(s) > 7/8$*. Research Preprint (`openai/math/preprints/paper.pdf`).
2. OpenAI Math Repository (2026). *Lean 4 Formalization Documentation: Scope of the Quasi-Riemann Hypothesis Proof* (`math/lean/docs/003.md`). GitHub.
3. Wikipedia Contributors (2026). *Riemann Hypothesis*. Wikipedia, The Free Encyclopedia. Excerpts covering classical history, zero density, critical line bounds, and modern AI-assisted results.