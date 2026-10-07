# Expository Report: Hilbert's Tenth Problem Over the Rational Numbers (OpenAI, 24 Sep 2026)

---

### 1. The Problem: Diophantine Equations over the Rational Numbers

A **Diophantine equation** is a polynomial equation with integer coefficients for which solutions are sought in a specified number system, such as the integers ($\mathbb{Z}$) or the rational numbers ($\mathbb{Q}$). Named after the 3rd-century Alexandrian mathematician Diophantus, these equations represent one of the oldest and most fundamental domains of number theory.

The solvability of a Diophantine equation depends entirely on the domain from which candidate solutions are drawn:
*   **Linear Example:** Consider the equation $2x = 1$.
    *   *Integer Domain ($\mathbb{Z}$):* There is no integer $x \in \mathbb{Z}$ satisfying $2x = 1$, because $1/2$ is not a whole number.
    *   *Rational Domain ($\mathbb{Q}$):* There exists a valid rational solution, namely $x = 1/2 \in \mathbb{Q}$.
*   **Quadratic Example:** Consider the equation $x^2 + y^2 = 3$.
    *   *Rational and Integer Domains:* This equation has no rational solutions (and therefore no integer solutions). To see why, express any candidate rational numbers with a common denominator as $x = a/c$ and $y = b/c$, yielding $a^2 + b^2 = 3c^2$. Modular arithmetic modulo 4 shows that the sum of two integer squares $a^2 + b^2 \pmod 4$ can only equal $0, 1,$ or $2$, whereas $3c^2 \pmod 4$ equals $0$ or $3$. Thus, no rational solution can exist.

An **algorithm** is an effective, deterministic, finite step-by-step procedure that takes an equation as input and yields a definitive "YES" or "NO" decision in finite time regarding whether a solution exists.

A **naive search algorithm** systematically enumerates candidate numbers in the target domain and evaluates the polynomial:
*   If a solution exists, a naive search will eventually encounter it in finite time, terminating with a verified **"YES"**.
*   If no solution exists, a naive search will execute indefinitely without producing a **"NO"** answer, because at any finite computation step one cannot distinguish between an equation with no solutions and one whose smallest solution has not yet been checked.

---

### 2. Background: From Integers ($\mathbb{Z}$) to Rational Numbers ($\mathbb{Q}$)

In 1900, David Hilbert presented his famous Tenth Problem at the International Congress of Mathematicians, asking for a general decision algorithm to determine the solvability of any arbitrary Diophantine equation over the integers $\mathbb{Z}$.

*   **Resolution over the Integers ($\mathbb{Z}$):** The integer case was solved through the DPRM Theorem (completed by Martin Davis, Hilary Putnam, Julia Robinson in 1961, and Yuri Matiyasevich in 1970). The DPRM Theorem proved that every recursively enumerable set is Diophantine. Because computationally undecidable recursively enumerable sets exist (such as the set of halting Turing machines), Hilbert's Tenth Problem over $\mathbb{Z}$ is **undecidable**: no general algorithm can decide integer Diophantine solvability.
*   **The Problem over the Rational Numbers ($\mathbb{Q}$):** Proving undecidability over the rational numbers $\mathbb{Q}$ remains an open problem in mathematics and is substantially harder than over $\mathbb{Z}$:
    *   *Transfer via Diophantine Definitions:* If one could construct a purely existential **Diophantine definition** of $\mathbb{Z}$ inside $\mathbb{Q}$—that is, a polynomial condition over $\mathbb{Q}$ whose rational solutions isolate precisely the subset of integers $\mathbb{Z} \subset \mathbb{Q}$—the undecidability over $\mathbb{Z}$ would immediately transfer to $\mathbb{Q}$.
    *   *Existential vs. Universal Quantifiers:* Known subring definitions of $\mathbb{Z}$ inside $\mathbb{Q}$ (such as those established by Julia Robinson, Bjorn Poonen, and Jochen Koenigsmann) require universal quantifiers ("for all" $\forall$) or mixed quantifiers. A genuine Diophantine definition permits exclusively existential quantifiers ("there exists" $\exists$).
    *   *Mazur's Conjecture:* Barry Mazur conjectured that the topological closure of the rational points $V(\mathbb{Q})$ on any algebraic variety $V$ over $\mathbb{Q}$ has at most finitely many connected components in the real topology. Because the set of integers $\mathbb{Z} \subset \mathbb{Q}$ is an infinite, discrete set of points, Mazur's Conjecture implies that $\mathbb{Z}$ cannot be defined existentially inside $\mathbb{Q}$, ruling out the standard mechanism for transferring undecidability from $\mathbb{Z}$ to $\mathbb{Q}$.

---

### 3. Core Results and Statements

The research paper published by OpenAI on September 24, 2026, advances number theory by establishing a pointwise $2$-converse theorem for elliptic curves over $\mathbb{Q}$ possessing rational $2$-torsion.

#### Theorem 1.1 (The Rational-Two-Torsion 2-Converse)
Let $E/\mathbb{Q}$ be an elliptic curve over the rational numbers with nonzero rational two-torsion ($E(\mathbb{Q})[2] \neq 0$), and suppose its $2^\infty$-Selmer corank $s_2(E) = \text{corank}_{\mathbb{Z}_2} \text{Sel}_{2^\infty}(E/\mathbb{Q})$ satisfies $s_2(E) \in \{0, 1\}$. Then:
$$\text{ord}_{s=1} L(E, s) = \text{rank}_{\mathbb{Z}} E(\mathbb{Q}) = s_2(E), \quad \text{and } \text{Sha}(E/\mathbb{Q}) \text{ is finite.}$$

This result holds unconditionally across all of the following configurations:
1.  Curves with one rational two-torsion line as well as curves with full rational two-torsion.
2.  Complex Multiplication (CM) and non-CM curves alike.
3.  Every rational isogeny configuration.
4.  Arbitrary reduction types at $p = 2$ and at all bad primes.

#### Algorithmic and Structural Significance
While the paper does not construct an existential Diophantine definition of $\mathbb{Z}$ inside $\mathbb{Q}$, Theorem 1.1 establishes structural parity between the algebraic $2^\infty$-Selmer corank $s_2(E)$ and the analytic order of vanishing $\text{ord}_{s=1} L(E,s)$ for rational $2$-torsion curves. By removing all local reduction restrictions at the prime $2$ and accommodating both CM and non-CM curves across all isogeny classes, this result completes the pointwise $2$-converse in the residual two-torsion range.

---

### 4. Search Strategy and Reduction Mechanics

To link continuous/rational testing procedures with discrete vanishing conditions, the paper constructs quadratic twist families parametrized over multi-dimensional Boolean hypercubes $\mathbb{F}_2^b$.

*   **Boolean Hypercube Family Setup:** Let $E/\mathbb{Q}$ be a fixed elliptic curve under test (the "base curve"). The paper constructs families of quadratic twists parametrized by binary vectors $x = (x_1, x_2, \dots, x_b) \in \mathbb{F}_2^b$:
    $$h_x = h_0 \prod_{q \in \mathcal{Q}} (q^*)^{\lambda_q(x)}$$
    where $h_0$ is a fixed base discriminant, $\mathcal{Q}$ is a finite set of auxiliary split prime numbers $q \nmid 2N$, $\lambda_q : \mathbb{F}_2^b \to \mathbb{F}_2$ are linear forms, and $q^* = (-1)^{(q-1)/2} q$.
*   **Simultaneous Addressing and Non-Zero Evaluation:** Each binary coordinate $x_i$ dictates whether a set of auxiliary primes divides the twist parameter $h_x$. The vertex $x = 0 \in \mathbb{F}_2^b$ represents the base curve $h_0$ whose arithmetic status is unknown. The algorithm designs prime networks (governed by forests of quadratic residue symbol changes) such that every non-zero vertex $x \neq 0$ simultaneously satisfies known arithmetic bounds (analytic non-vanishing for corank 0, or simple zeros for corank 1).
*   **Coefficient Non-Vanishing Detectors:** Central values $L(E(h_x), 1)$ and derivative values $L'(E(h_x), 1)$ are extracted using modular form coefficient systems:
    *   *Even Coefficients:* Half-integral weight modular forms (via Waldspurger's theorem and Shimura correspondence) act as binary non-vanishing detectors for central values $L(E(h_x), 1)$.
    *   *Odd Coefficients:* Weighted Heegner point sums $P_{h_x}$ act as binary non-vanishing detectors for derivative values $L'(E(h_x), 1)$.
*   **Missing-Vertex Interpolation:** By evaluating coefficient tests across all non-zero addresses $x \in \mathbb{F}_2^b \setminus \{0\}$, uniform integral bounds force the behavior at the missing vertex $x = 0$ via characteristic-two Chevalley–Warning congruence arguments, transferring non-vanishing and rank bounds back to the base curve.

---

### 5. The Hard Direction: Analytical Mechanics and "The Squeeze"

The core analytical architecture of the proof relies on combining cyclotomic and ring-class interpolation over Iwasawa algebras with local Kummer switches to force arithmetic bounding conditions.

*   **Cyclotomic Interpolation and Iwasawa Lattices:**
    *   *Setup:* Uses Kato's zeta classes from modular form lattices and the Ferrero–Washington vanishing theorem to control residual cyclotomic cohomology.
    *   *Structure:* Defines the Iwasawa algebra $\Lambda = \mathbb{Z}_2[[t]]$ and its $2$-adic local completion $\mathcal{O} = \hat{\Lambda}_{(2)}$, with residue field $\kappa = \mathbb{F}_2((t))$.
    *   *Uniform Integrality:* Constructs a group-ring scalar family $u \in \Lambda[1/2][G]$ with a uniform 2-power denominator $2^{C_{\text{int}}} u \in \Lambda[G]$.
*   **Ring-Class Interpolation and Cohomological Euler Systems:**
    *   *Setup:* For an imaginary quadratic field $K = \mathbb{Q}(\sqrt{k})$ split at $2N$, CM points $y_c \in E(H_c)$ on ring-class fields $H_c$ define primitive genus sums:
        $$P_h = \sum_{\sigma \in \text{Gal}(H_{|h|}/K)} \chi_h(\sigma) \sigma(y_{|h|}) \in E(h)(K)$$
    *   *Euler Systems:* Deploys Howard's cohomological Euler systems and Kolyvagin derivative operators $D_\ell$ on global Selmer complexes $C_S$.
*   **Local Switches and Split Derivative Primes:**
    *   *Mechanism:* At an inert/split derivative prime $\ell$, the limiting local Selmer module decomposes into an unramified (finite) plane $F_\ell = \{s=0\}$ and a transverse (singular) plane $S_\ell = \{f=0\}$.
    *   *Isotropic Invariance:* The proof substitutes the local Kummer condition from $F_\ell$ to $S_\ell$. Because $F_\ell$ and $S_\ell$ are mutually self-dual Lagrangian planes under local Tate pairing, this local switch preserves integral determinant valuations:
        $$v_{\mathcal{O}}(u_F) = v_{\mathcal{O}}(u_S)$$
        preventing valuation degradation across repeated prime switches.
*   **The Analytical Squeeze and Index Bounding:**
    *   *Index Relation:* Let $j_h$ be the $2$-adic index valuation of the Heegner sum $P_h$ in $E(h)(K) \otimes \mathbb{Z}_2 / \text{torsion}$. The central determinant specialization establishes the precise formula:
        $$v_2(u_h(0)) = 2j_h - s(h) - s(hk) - 4w(h) + O(1)$$
        where $w(h)$ is the local weight sum and $s(h) = \text{length}_{\mathbb{Z}_2} \text{Sha}(E(h)/\mathbb{Q})[2^\infty]$.
    *   *The Squeeze:* The proof sets up a structural squeeze. A bounded clearing factor $f_x u_x = d_x$ in $\mathcal{O}[G]$ bounds the central valuation $v_2(u_x(0))$ from above across non-zero addresses $x \neq 0$. If the central derivative or $L$-value at $x = 0$ were to vanish, $u_0(0)$ would equal zero. Chevalley–Warning parity congruences on a sufficiently large Boolean hypercube $\mathbb{F}_2^b$ contradict this vanishing, squeezing the missing vertex $x = 0$ into forced rank equality $r(E) = s_2(E)$ and establishing the finiteness of $\text{Sha}(E/\mathbb{Q})$.

---

### 6. Proof of the Index Bound and Coefficient Mechanics

To anchor the arithmetic bounds and normalize coefficient tests uniformly, the paper deploys modular representation theory on quaternion orders alongside stabilization mechanics.

1.  **Ternary Theta Lifts on Definite Quaternion Algebras:**
    *   The framework utilizes definite quaternion algebras $B/\mathbb{Q}$ ramified at an auxiliary prime $\ell$ and $\infty$, with Eichler orders $R \subset B$ of level $N$.
    *   Using Shimura's half-integral weight theory and Waldspurger's relations, central values $L(E(h), 1)$ and derivative values $L'(E(h), 1)$ are identified with Fourier coefficients of weight-$3/2$ modular forms $g = \sum a(n) q^n$.
2.  **Weighted Heegner Point Tests and Reduction Descriptions:**
    *   The proof applies the Jetchev–Kane reduction description of supersingular points on modular curves $X_0(N)$ to evaluate local Schwartz functions $f = \prod f_p$.
    *   At the prime 2 and bad places, specific local Schwartz weights are constructed to satisfy Weil representation transformation laws for the metaplectic group $\text{Mp}_2(\mathbb{A}_{\mathbb{Q}})$, yielding integral Fourier coefficients $a_M(n) \pmod{2^M}$ that directly detect reduction images of Heegner sums $\lambda_M(\text{red}_\ell(L P_D))$.
3.  **Coefficient Stabilization and Minimum Normalized Depth:**
    *   The normalized depth of a Fourier coefficient is defined as $v_2(a(D)) - w(D)$.
    *   The paper proves that across quadratic twist families, the minimal normalized depth stabilizes to a finite integer $\delta$.
    *   Adjoining finite prime networks (built by modifying quadratic residue symbols across auxiliary primes) isolates individual addresses in $\mathbb{F}_2^b$, forcing both the even derivative test and the odd central-value test to equal $1$ simultaneously at all non-zero vertices $x \neq 0$.

---

### 7. The Companion Results: Two-Torsion and Selmer Coranks

The algebraic framework establishes precise exact sequences linking Selmer coranks, Mordell–Weil ranks, and Shafarevich–Tate lengths.

*   **Torsion and Finiteness of $\text{Sha}$:**
    *   For an elliptic curve $A/\mathbb{Q}$, the fundamental $2$-power Kummer exact sequence is:
        $$0 \longrightarrow A(\mathbb{Q}) \otimes \mathbb{Q}_2/\mathbb{Z}_2 \longrightarrow \text{Sel}_{2^\infty}(A/\mathbb{Q}) \longrightarrow \text{Sha}(A/\mathbb{Q})[2^\infty] \longrightarrow 0$$
    *   Taking $\mathbb{Z}_2$-coranks yields the strict algebraic identity:
        $$s_2(A) = r(A) + \text{corank}_{\mathbb{Z}_2} \text{Sha}(A/\mathbb{Q})[2^\infty]$$
        where $r(A) = \text{rank}_{\mathbb{Z}} A(\mathbb{Q})$ and $s_2(A) = \text{corank}_{\mathbb{Z}_2} \text{Sel}_{2^\infty}(A/\mathbb{Q})$.
    *   *Corank vs. Length:* The quantity $s_2(A)$ is an infinite divisible corank. In contrast, $s(h) = \text{length}_{\mathbb{Z}_2} \text{Sha}(E(h)/\mathbb{Q})[2^\infty]$ is a finite integer length, defined whenever $s_2(E(h)) = 0$.
    *   When $s_2(E) \in \{0, 1\}$, establishing $r(E) = \text{ord}_{s=1} L(E,s) = s_2(E)$ forces $\text{corank}_{\mathbb{Z}_2} \text{Sha}(E/\mathbb{Q})[2^\infty] = 0$, which combined with the Gross–Zagier–Kolyvagin theorem proves that the full Shafarevich–Tate group $\text{Sha}(E/\mathbb{Q})$ is finite.
*   **Quadratic Transfer and Cassels–Tate Isogeny Identities:**
    *   For a quadratic extension $K = \mathbb{Q}(\sqrt{k})$, the Selmer corank satisfies the exact quadratic identity:
        $$s_2(E/K) = s_2(E/\mathbb{Q}) + s_2(E(k)/\mathbb{Q})$$
    *   To transfer bounds between quadratic companions, consider the Weil restriction $A_h = \text{Res}_{K/\mathbb{Q}}(E(h)_K)$ and the product curve $B_h = E(h) \times E(hk)$.
    *   The Cassels–Tate isogeny formula provides the exact ratio identity:
        $$\frac{\# \text{Sha}(A_h) \text{Reg}(A_h) \text{Per}(A_h) \prod_p c_p(A_h)}{\# A_h(\mathbb{Q})_{\text{tors}} \# A_h^\vee(\mathbb{Q})_{\text{tors}}} = \frac{\# \text{Sha}(B_h) \text{Reg}(B_h) \text{Per}(B_h) \prod_p c_p(B_h)}{\# B_h(\mathbb{Q})_{\text{tors}} \# B_h^\vee(\mathbb{Q})_{\text{tors}}}$$
    *   Because $A_h$ and $B_h$ are naturally isogenous over $\mathbb{Q}$, local component group factors $c_p$ cancel at all split primes dividing $h$, allowing uniform arithmetic index bounds to transfer between $E(h)$ and $E(hk)$ without accumulating losses proportional to the prime count of $h$.

---

### 8. Scope Boundaries: What the Paper Does NOT Prove

To prevent common misinterpretations, the strict scope boundaries of the paper are delineated below:

1.  **No Existential Diophantine Definition:** The paper does **not** construct an existential Diophantine definition of the integers $\mathbb{Z}$ inside the rational numbers $\mathbb{Q}$.
2.  **Mazur's Conjecture Untouched:** The paper leaves Mazur's Conjecture regarding the topological closure of rational points on algebraic varieties entirely open.
3.  **Pointwise Scope Limits:** The paper does **not** establish a general decision algorithm or Turing reduction for arbitrary Diophantine equations over $\mathbb{Q}$ outside the specified class of elliptic curves with rational two-torsion.
4.  **No Universal Variable Bound:** The paper does **not** establish a universal bound on the number of polynomial variables required to represent undecidable statements over $\mathbb{Q}$.

---

### 9. Current Status of the Work

*   **Publication Format:** The source document is an AI-generated mathematical research preprint published by OpenAI on **September 24, 2026**.
*   **Verification Status:** No formal interactive theorem prover verification (such as in Lean 4 or Coq) accompanies the publication. The paper stands as an unverified mathematical preprint undergoing review by the number-theoretic research community.

---

### 10. Glossary of Technical Terms

| Term | Definition |
| :--- | :--- |
| **Diophantine Equation** | A polynomial equation with integer coefficients whose solutions are sought in specified number systems (such as $\mathbb{Z}$ or $\mathbb{Q}$). |
| **Elliptic Curve** | A smooth, projective algebraic curve of genus one equipped with a specified rational base point, defined over $\mathbb{Q}$ by a cubic equation $y^2 = x^3 + ax + b$. |
| **Rational Two-Torsion ($E(\mathbb{Q})[2]$)** | The subgroup of rational points on an elliptic curve $E$ that have order dividing 2 (points $(x,y)$ where $y=0$, plus the point at infinity). |
| **Selmer Group & $2^\infty$-Selmer Corank ($s_2(E)$)** | An algebraic group measuring global obstructions to local Kummer elements; $s_2(E)$ is its $\mathbb{Z}_2$-corank, bounding $r(E) + \text{corank}_{\mathbb{Z}_2} \text{Sha}[2^\infty]$. |
| **Shafarevich–Tate Group ($\text{Sha}$)** | The group measuring the failure of the Hasse local-global principle for an elliptic curve over a number field; defined as the kernel of global to local obstruction maps. |
| **Iwasawa Algebra ($\Lambda$)** | The formal power series ring $\mathbb{Z}_2[[t]]$, representing the completed group ring of the $2$-adic cyclotomic Galois group $\text{Gal}(\mathbb{Q}_\infty/\mathbb{Q})$. |
| **Kato Zeta Class** | An arithmetic cohomology class constructed in the $K$-theory and modular curves framework by Kazuya Kato, supplying cyclotomic $L$-function interpolation. |
| **Heegner Point Sum ($P_h$)** | A sum of CM points on a modular curve weighted by a quadratic character $\chi_h$, yielding a rational point on a quadratic twist $E(h)$ whose height measures $L'(E(h),1)$. |
| **Selmer Complex ($C_S$)** | A derived cochain complex incorporating global Galois cohomology and local Kummer conditions, whose cohomology groups compute Selmer and Tate-Shafarevich groups. |
| **Cassels–Tate Pairing** | A bilinear, non-degenerate pairing on the Tate–Shafarevich group $\text{Sha}(E/\mathbb{Q})$ that controls its quotient structures and isogeny invariants. |
| **Ternary Theta Lift** | An integral theta correspondence mapping weight-$3/2$ modular forms to definite quaternion orders, connecting central $L$-values with arithmetic Heegner points. |