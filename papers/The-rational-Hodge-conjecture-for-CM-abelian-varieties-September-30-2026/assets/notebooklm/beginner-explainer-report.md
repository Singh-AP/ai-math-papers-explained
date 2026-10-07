# Technical Explainer: The Rational Hodge Conjecture for CM Abelian Varieties (OpenAI Preprint, 30 September 2026)

---

### 1. Fundamentals of the Rational Hodge Conjecture

In classical complex algebraic geometry, a smooth projective variety $X$ defined over $\mathbb{C}$ possesses Betti cohomology groups with rational coefficients, denoted $H^{2p}(X, \mathbb{Q})$. Complexifying these coefficients yields the complex cohomology vector space $H^{2p}(X, \mathbb{C}) = H^{2p}(X, \mathbb{Q}) \otimes_{\mathbb{Q}} \mathbb{C}$. According to classical Hodge theory, this complexified cohomology group admits a canonical direct-sum decomposition known as the **Hodge decomposition**:

$$H^{2p}(X, \mathbb{C}) = \bigoplus_{a+b=2p} H^{a,b}(X)$$

where $H^{a,b}(X)$ represents the subspace of cohomology classes of degree $2p$ represented by differential forms containing $a$ holomorphic and $b$ antiholomorphic components. Under complex conjugation, these subspaces satisfy $\overline{H^{a,b}(X)} = H^{b,a}(X)$.

The primary objects of interest in the Hodge conjecture are those rational classes that purely reside in the middle bidegree $(p,p)$.

#### Definition: Rational Hodge Classes
A **rational Hodge class** of codimension $p$ (or degree $2p$) on $X$ is a rational cohomology class whose image in $H^{2p}(X, \mathbb{C})$ lies entirely within the $(p,p)$ component of the Hodge decomposition. The space of rational Hodge classes is defined as the intersection:

$$Hdg^{2p}(X) = H^{2p}(X, \mathbb{Q}) \cap H^{p,p}(X, \mathbb{C})$$

Algebraic subvarieties of $X$ naturally give rise to rational Hodge classes. Let $CH^p(X)$ denote the Chow group of codimension-$p$ algebraic cycles modulo rational equivalence. Tensoring with $\mathbb{Q}$ yields $CH^p(X)_{\mathbb{Q}} = CH^p(X) \otimes_{\mathbb{Z}} \mathbb{Q}$. The **Betti cycle-class map** is a canonical linear homomorphism:

$$cl_B: CH^p(X)_{\mathbb{Q}} \longrightarrow H^{2p}(X, \mathbb{Q}) \cap H^{p,p}(X, \mathbb{C})$$

Because algebraic cycles are geometric subvarieties of $X$, their fundamental integration classes are guaranteed to be of rational type $(p,p)$.

> **The Rational Hodge Conjecture**
> Let $X$ be a smooth projective complex variety. For every integer $p \ge 0$, the Betti cycle-class map
> $$cl_B: CH^p(X)_{\mathbb{Q}} \longrightarrow H^{2p}(X, \mathbb{Q}) \cap H^{p,p}(X, \mathbb{C})$$
> is surjective. That is, every rational Hodge class of type $(p,p)$ on $X$ is a rational linear combination of algebraic cycle classes.

---

### 2. Complex Multiplication (CM) and Special Cohomology Classes

When $X = A$ is a complex abelian variety of dimension $g$, its full cohomology ring is given by the exterior algebra of its degree-one cohomology: $H^*(A, \mathbb{Q}) = \Lambda^* H^1(A, \mathbb{Q})$.

#### CM Abelian Varieties
A complex abelian variety $A$ is said to be of **CM type** (or simply **CM**) if its rational endomorphism algebra $\text{End}(A) \otimes_{\mathbb{Z}} \mathbb{Q}$ contains a commutative semisimple $\mathbb{Q}$-algebra of dimension $2 \dim A$. By convention, zero-dimensional abelian varieties (points) are included. Finite products and arbitrary tensor powers of CM abelian varieties remain CM.

A classic 1-dimensional example of a CM abelian variety is an elliptic curve $E = \mathbb{C}/\Lambda$ admitting complex multiplication by an order in an imaginary quadratic field $K = \mathbb{Q}(\sqrt{-d})$, such as the Gaussian integers $\mathbb{Z}[i]$ acting on $\mathbb{C}/\mathbb{Z}[i]$. In this 1-dimensional setting, the algebra $\text{End}(E) \otimes_{\mathbb{Z}} \mathbb{Q} \cong K$ has dimension $2 = 2 \dim E$.

#### Embedding Lines and Sign Functions
Let $E \subset \overline{\mathbb{Q}}$ be a Galois CM field containing the CM fields acting on $H^1(A, \mathbb{Q})$, with Galois group $G_E = \text{Gal}(E/\mathbb{Q})$ and complex conjugation denoted by $c \in G_E$. An **odd sign function** is a map $v: G_E \to \{1, -1\}$ satisfying $v(c\tau) = -v(\tau)$ for all $\tau \in G_E$.

An odd sign function $v$ determines a weight-one polarizable rational Hodge structure $U(v)$ on the rational vector space $E$. Extending coefficients to $\mathbb{C}$ decomposes $U(v)_{\mathbb{C}}$ into a direct sum of 1-dimensional **embedding lines** $U(v)_\lambda$ for $\lambda \in G_E$, upon which $a \in E$ acts via scalar multiplication by $\lambda(a)$. The line $U(v)_\lambda$ is assigned:
*   Hodge type $(1,0)$ if $v(\lambda) = 1$;
*   Hodge type $(0,1)$ if $v(\lambda) = -1$.

Under Galois conjugation $\sigma \in \text{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$ restricting to $g \in G_E$, the embedding lines transform as $\sigma U(v)_\lambda = U(v)_{g\lambda}$.

#### Pohlmann's Balance Criterion
For tensors constructed from embedding lines, algebraicity and Hodge properties are closely linked to conjugate symmetries. **Pohlmann's Balance Criterion** states that a tensor product of embedding lines belongs to the scalar extension of rational Hodge classes if and only if every scalar conjugate of the tensor contains an equal number of holomorphic $(1,0)$ and antiholomorphic $(0,1)$ factors (i.e., its total type sign sums to zero across every Galois conjugate).

#### Weil Classes vs. Divisor-Generated Classes
On an abelian variety, cup products of codimension-one divisor classes yield algebraic Hodge classes in higher codimensions. However, these *divisor-generated classes* do not exhaust $Hdg^{2p}(A)$.

**Weil classes** arise when an imaginary quadratic field $K$ (or a CM field) acts on an abelian variety $A$ of dimension $2n$ such that its two complex embeddings occur with equal multiplicity $n$ in $H^{1,0}(A)$. This structure creates a two-dimensional rational space of determinant classes in $\Lambda_K^{2n} H^1(A, \mathbb{Q})$ residing in $H^{n,n}(A, \mathbb{C})$.

| Property | Divisor-Generated Classes | Weil Classes |
| :--- | :--- | :--- |
| **Definition** | Classes in $H^{2p}(A, \mathbb{Q})$ formed by cup products of $p$ codimension-one divisor classes ($Hdg^2(A)$). | Determinant classes residing in $\Lambda_K^{2n} H^1(A, \mathbb{Q})$ under imaginary quadratic or CM field actions. |
| **Origin** | Standard exterior product algebra on $H^1(A, \mathbb{Q}) = \Lambda^1 H^1(A, \mathbb{Q})$. | Equal multiplicity condition of field embeddings within the holomorphic space $H^{1,0}(A)$. |
| **Generation Properties** | Spanned by products of $Hdg^2(A)$; easy to establish algebraicity via Lefschetz $(1,1)$. | **Not** generally generated by products of divisor classes; non-trivial to algebraize (occurs already on fourfolds). |

---

### 3. Historical Development and Precursor Work

The proof of the Rational Hodge Conjecture for CM abelian varieties synthesizes decades of foundational advances in algebraic geometry, Hodge theory, and arithmetic geometry.

* **1950 — W.V.D. Hodge:** Following Solomon Lefschetz's proof of the $(1,1)$ theorem for codimension-one algebraic cycles, Hodge formulated the broader problem during his ICM address, asking whether higher-degree rational Hodge classes are similarly algebraic.
* **1982 — Pierre Deligne:** Proved that every Hodge class on an abelian variety is *absolute Hodge* (it remains a Hodge class after transport through de Rham cohomology to any conjugate variety). Deligne established that CM abelian varieties play a central role because their Hodge groups are algebraic tori, enabling explicit embedding-line decompositions.
* **1992 — Yves André & Pierre Deligne:** Reduced arbitrary CM Hodge classes to sums of pullbacks of *split Weil classes* on auxiliary CM abelian varieties.
* **2003 — Fumio Hazama:** Introduced the coordinate-arrangement method, demonstrating that the rational balance kernel of CM Hodge matrices is spanned by antipodal pairs and elementary four-label relations, yielding a fundamental reduction to codimension-two algebraicity problems.
* **1999–2026 — J.S. Milne:** Constructed deep arithmetic reduction theorems demonstrating that the Hodge conjecture for CM abelian varieties directly implies both the Tate conjecture for abelian varieties over finite fields and Grothendieck's Hodge standard conjecture.
* **2025 — Eyal Markman:** Proved the algebraicity of Weil classes on polarized abelian sixfolds of Weil type with discriminant $-1$, thereby establishing the Hodge conjecture for all abelian fourfolds.
* **2025–2026 — Ziyang Gao & Emmanuel Ullmo:** Formulated equivalent quadratic indicator relations, using auxiliary CM factors to establish period relations among Hodge-induced periods.
* **2026 — OpenAI Preprint:** Proves the full Rational Hodge Conjecture for all CM abelian varieties in arbitrary dimension and codimension.

---

### 4. Main Theoretical Results: Theorem 1.1 and the Four-Factor Switch

The preprint resolves the main problem by establishing two central theorems and an explicit algebraic reduction strategy.

#### Formal Statement of Main Results

> **Theorem 1.1 (Main Theorem)**  
> Let $A$ be a complex CM abelian variety. For every integer $p \ge 0$, the Betti cycle-class map
> $$cl_B : CH^p(A)_{\mathbb{Q}} \longrightarrow H^{2p}(A, \mathbb{Q}) \cap H^{p,p}(A, \mathbb{C})$$
> is surjective. In particular, the rational Hodge conjecture holds in every codimension on every finite product of complex CM abelian varieties and on every power of such a product.

The elementary combinatorial and geometric engine powering Theorem 1.1 is the **Four-Factor Switch**:

> **Theorem 2.5 (Four-Factor Switch)**  
> Let $E$ be a Galois CM field and let $v_1, v_2, v_3, v_4 : G_E \to \{1, -1\}$ be odd sign functions satisfying $v_1 + v_2 = v_3 + v_4$. Under the Künneth inclusion, the embedding line
> $$U(v_1)_1 \otimes U(v_2)_1 \otimes U(v_3)_c \otimes U(v_4)_c \subset H^4\left( \prod_{i=1}^4 B(v_i), \mathbb{Q} \right)$$
> is algebraic (i.e., lies in the scalar extension of rational algebraic cycle classes).
> 
> *Note:* This tensor line possesses Hodge type $(2,2)$ across every scalar conjugate, since for any $g \in G_E$:
> $$v_1(g) + v_2(g) - v_3(g) - v_4(g) = 0$$

#### Reduction Strategy (Proposition 2.6)
To prove Theorem 1.1 from Theorem 2.5, the paper executes a structured algebraic reduction:

1.  **Matrix Representation:** Decompose $H^1(A, \mathbb{Q})$ into rank-one CM field modules. Represent ordered lists of odd sign functions as matrices with $p$ rows and columns indexed by $G_E / \langle c \rangle$.
2.  **Balanced List Linking:** Represent two lists $x = (x_1, \dots, x_p)$ and $y = (y_1, \dots, y_p)$ having equal sign sums $\sum x_i = \sum y_i$. Construct a finite sequence $x = x^{(0)}, x^{(1)}, \dots, x^{(N)} = y$ linked by elementary two-row swaps satisfying $a + b = a' + b'$ at every coordinate.
3.  **Transition Tensor Assembly:** Theorem 2.5 yields pure algebraic generators for the transition lines $L_{x^{(j)}, x^{(j+1)}}$. Unchanged rows are joined by algebraic two-factor classes $U(v)_1 \otimes U(v)_c \subset H^2(B(v) \times B(v), \mathbb{Q})$.
4.  **Polarization Contractions:** Compose consecutive transition tensors via algebraic correspondences. Let $s = [F : \mathbb{Q}] = \dim B(b_i)$ denote the dimension of the auxiliary factor $B(b_i)$, where $F = E^+$. Given ample divisor classes $\ell_i$ on intermediate factors $B(b_i)$, execute cup-product pushforwards using the power $\ell_i^{s-1}$ of top-degree complementary dimension:
    $$(r_{ae})_* \left( r_{ab}^* t_{ab} \smile r_{be}^* t_{be} \smile \prod_{i=1}^p \ell_i^{s-1} \right) = (-1)^{p(p-1)/2} \left( \prod_{i=1}^p q_i \right) t_{ae}$$
    Hodge–Riemann positivity guarantees that $q_i = \int_{B(b_i)} \beta_i \wedge \gamma_i \wedge \ell_i^{s-1} \in \mathbb{Q}^\times$ is non-zero, contracting intermediate slots without losing algebraicity or nonvanishing (noting that the total degree on the left is $p + p + p(s-1) - ps = p$).
5.  **Diagonal Pullback:** Transfer the resulting algebraic classes back to $A^{2p}$ and pull back along the diagonal $A \to A^{2p}$, completing the proof of Theorem 1.1.

---

### 5. The Geometric Bridge: The Surface Criterion (Proposition 3.1)

To establish the Four-Factor Switch (Theorem 2.5), the paper maps the abstract tensor relation onto a physical geometric object—a smooth algebraic surface.

#### Proposition 3.1 (Surface Criterion)
Let $E$ be a Galois CM field, and $v_1, v_2, v_3, v_4$ be odd sign functions satisfying $v_1 + v_2 = v_3 + v_4$. Set $\lambda = (1,1,c,c)$. Suppose there exists a smooth connected projective complex surface $S$, rational Hodge maps $h_i : U(v_i) \to H^1(S, \mathbb{Q})$, and non-zero vectors $\alpha_i \in U(v_i)_{\lambda_i}$ such that the cup-product period is non-zero:

$$\int_S h_1(\alpha_1) \smile h_2(\alpha_2) \smile h_3(\alpha_3) \smile h_4(\alpha_4) \neq 0$$

Then the four-factor switch line $U(v_1)_1 \otimes U(v_2)_1 \otimes U(v_3)_c \otimes U(v_4)_c$ is algebraic.

#### Morphism Realization and Divisor Kernel Conversion
1.  **Morphism Realization:** By Lemma 2.2, rational Hodge maps $h_i$ into $H^1(S, \mathbb{Q})$ are induced (up to integer multiples $m_i$) by algebraic morphisms $f_i : S \to B(v_i)$ via the Albanese property. The product morphism $f = (f_1, f_2, f_3, f_4) : S \to \prod_{i=1}^4 B(v_i) = A$ defines an algebraic cycle $Z = cl(f_* [S]) \in Z^{2n-4}(A)$ (where $n = \dim A = 4s$).
2.  **Functional Evaluation:** The class $Z$ acts as a linear functional pairing non-trivially with $t_\alpha = \alpha_1 \otimes \alpha_2 \otimes \alpha_3 \otimes \alpha_4$:
    $$\int_A Z \smile t_\alpha = k \in \mathbb{Q}^\times$$
3.  **Divisor Kernel Conversion:** For secondary vectors $\beta_i \in U(v_i)'_{c\lambda_i}$, define pure classes $D_i = \alpha_i \otimes \beta_i \in H^2(B(v_i) \times B(v_i)', \mathbb{Q})$. Every scalar conjugate of $D_i$ has bidegree $(1,1)$. By scalar descent and the Lefschetz $(1,1)$ theorem, $D_i$ is algebraic.
4.  **Target Vector Isolation:** Set $A' = \prod_{i=1}^4 B(v_i)'$, and let $p : A \times A' \to A$ and $p' : A \times A' \to A'$ be the canonical projections onto the first and second product factors. Define $q_i: A \times A' \to B(v_i) \times B(v_i)'$ to be the natural projection maps onto the corresponding $i$-th factor pairs. Convolving $Z$ with the algebraic product kernel $K = \prod_{i=1}^4 q_i^* D_i$ isolates a pure non-zero algebraic vector on the target line $t_\beta = \beta_1 \otimes \beta_2 \otimes \beta_3 \otimes \beta_4$:
    $$p'_* \left( p^* Z \smile K \right) = \left( \int_A Z \smile t_\alpha \right) t_\beta = k \cdot t_\beta$$

#### Conversion Flow Chart
```
  [ Non-zero Surface Cup Product Period ]
  \int_S h_1(\alpha_1) \smile h_2(\alpha_2) \smile h_3(\alpha_3) \smile h_4(\alpha_4) \neq 0
                         |
                         v  (Albanese Property / Morphism Pushforward f_*)
  [ Algebraic Surface Cycle Z = cl(f_*[S]) ]  \in  Z^{2n-4}(A)
                         |
                         v  (Convolve with Divisor Kernels D_i = \alpha_i \otimes \beta_i)
  [ Algebraic Kernel Matrix K = \prod q_i^* D_i ]  (Algebraic by Lefschetz (1,1))
                         |
                         v  (Integration / Projection p'_*)
  [ Pure Algebraic Target Switch Line Vector t_\beta ] = \beta_1 \otimes \beta_2 \otimes \beta_3 \otimes \beta_4
```

*Corollary 3.2* extends this criterion: it is sufficient that complex differential classes $\eta_i \in H^1(S, \mathbb{C})$ reside in the complex spans $\text{span}_{\mathbb{C}} \{ h(U(v_i)_{\lambda_i}) \}$ and yield a non-zero surface period $\int_S \eta_1 \smile \eta_2 \smile \eta_3 \smile \eta_4 \neq 0$.

---

### 6. Analytic Construction: Theta One-Forms and Mixed Periods

Section 4 of the preprint constructs the necessary non-zero period on a compact arithmetic quotient of a complex 2-ball.

To define local signs compatible with Galois field actions, we index local compact-place signs via the re-indexing identity:
$$d(\tau) = v(\tau^{-1}), \quad d(c\tau) = -d(\tau), \quad d(\mu) = 1$$
where $\mu = 1$ denotes the active distinguished embedding.

#### Analytical Step-by-Step Construction

1.  **Ball Quotient Setup:**
    Let $V$ be an $E/F$-Hermitian space of dimension 3 having signature $(2,1)$ at the distinguished embedding $\mu = 1$ and positive-definite signature at all other real places $\tau \neq \mu$ of $F = E^+$. Let $G = SU(V)$. The domain $D = \{ L \subset V_\mu : \dim_{\mathbb{C}} L = 1, h_V|_L < 0 \}$ is the complex 2-ball. 
    
    The quotient bundle is defined as $Q = V_\mu / L$. The tangent bundle of $D$ is $TD = \text{Hom}(L, Q)$, and its cotangent bundle is $\Omega_D^1 = L \otimes Q^*$. The canonical bundle of $D$ is given by $K_D = \det \Omega_D^1 = L^2 \otimes \Lambda^2 Q^*$. Quotients $X = \Gamma \backslash D$ by torsion-free principal congruence level subgroups $\Gamma \subset G(F)$ are compact, smooth Kähler surfaces.

2.  **Theta One-Form Generation:**
    Using completed theta series $\hat{\vartheta}_\phi(Z,z)$ associated with finite Schwartz input functions $\phi$, the first Taylor coefficient tensor $T_{1,\phi}(Z)$ projects onto cotangent fibers $L \otimes Q^*$. This yields holomorphic differential one-forms $\Theta_i(\phi) \in H^0(X, \Omega_X^1)$. Varying $\phi$ spans the cotangent fiber $\Omega_D^1|_x$ at any point $x \in D$ (Proposition 4.5).
    
    For a 2-dimensional multiplicity space $W = W_1 \perp W_2$, the second Taylor tensor $T_{2,\phi}$ is projected via the double-alternating operator:
    $$\text{alt}_2 : \text{Sym}^2(Q^* \otimes W_\mu^*) \longrightarrow \Lambda^2 Q^* \otimes \Lambda^2 W_\mu^*$$
    Including the half-determinant line $( \det F_W )^{1/2} \otimes \Lambda^2 Q^* \otimes \Lambda^2 W_\mu^* \cong K_D \otimes (\text{constant line})$, this double-alternating projection map yields a canonical differential two-form $\Xi_W(\phi; t)$ valued in the canonical bundle $K_D$.

3.  **Weak Approximation and Mixed Period Integration:**
    *   Keep the total space $W$, group $G$, reference coordinates, and total finite input $\phi$ fixed.
    *   The sign relation $d_1 + d_2 = d_3 + d_4$ ensures that the multisets of local compact-place signs $\{d_1(\tau), d_2(\tau)\}$ and $\{d_3(\tau), d_4(\tau)\}$ coincide at every place $\tau \neq \mu$.
    *   By weak approximation in $E$, construct a second rational orthogonal decomposition $W = W_3 \perp W_4$ matching the local sign functions $d_3, d_4$.
    *   The total active positive Lagrangian at $\mu = 1$ (consisting of $L \otimes W_\mu$ and $Q^* \otimes W_\mu^*$) remains unchanged, while compact-place data vary continuously in $t$.
    *   The total two-form varies continuously in the $C^\infty$ topology on $X$. Because the self-pairing $\int_X \xi \wedge \bar{\xi} > 0$ is strictly positive for $\xi = \Xi_W(\phi; t_0)$, the perturbed form $\xi' = \Xi_W(\phi; t')$ satisfies $\int_X \xi \wedge \xi' \neq 0$ (Corollary 4.7).
    *   Factoring the two rational endpoints into wedge products of theta one-forms and passing to a common finite cover $\pi : X' \to X$ yields a non-zero mixed period:
        $$\int_{X'} \pi^* \xi \wedge \pi^* \xi' \neq 0$$
        containing two holomorphic and two antiholomorphic theta one-form factors.

---

### 7. Arithmetic Certification and Slope Analysis

To connect the analytic differential forms on $X'$ to the Surface Criterion, the classes must be certified as originating from the specified rational CM Hodge structures $U(v)$.

#### Moduli Space & Lie Rank Distribution
The ball quotient $X$ is embedded into a fine projective moduli scheme $S$ over a number field $K \subset \mathbb{C}$, parameterizing tuples $(B, \lambda, \iota_E, \eta_N)$ of polarized abelian varieties $B$ of dimension $3s$ ($s = [F : \mathbb{Q}]$) with $E$-action $\iota_E$ and full level structure $\eta_N$. Across complex embeddings, the Lie algebra of $B$ decomposes into Lie rank distributions:
$$r_\mu = 2, \quad r_c = 1, \quad \{r_\tau, r_{c\tau}\} = \{0, 3\} \quad \text{for } \tau \notin \{1, c\}$$
Form the product of the Albanese varieties of the connected components $S_j$ of $S$, denoted $A_S = \prod_j A_j$.

#### Algebraic Hecke Operators and Frobenius Identity
At a completely split good reduction prime $q$, the local $q$-divisible group $G_w$ at the prime $w = p_c$ splits into:
$$G_w = M_0 \oplus E_0$$
where $M_0$ is multiplicative of height 1 (and Lie rank 1) and $E_0$ is étale of height 2 (and Lie rank 0).

Raw spherical Hecke operators $D_1, D_2, D_3$ are constructed as integral algebraic correspondences acting on $A_S$. On the crystalline cohomology $H^1_{\text{cris}}(\tilde{A}_S / \mathbb{Z}_q)[1/q]$ of the special fiber $\tilde{A}_S / \mathbb{F}_q$, counting ordinary isogeny neighbors ($X_0, Y_0, Z_0$) proves that the crystalline Frobenius $\phi = \Phi^*$ satisfies the cubic algebraic polynomial identity (Proposition 5.5):

$$\phi^3 - D_1 \phi^2 + q D_2 \phi - q^3 D_3 = 0$$

#### Weil Bounds, Valuation Formula, and Slope Analysis
The active spherical Hecke parameter of a theta form is proved to be $\{q^{1/2}, q^{-1/2}, e\}$ (Proposition 6.3), where $e = e_0^{-1}$ is an algebraic number with all complex conjugates having absolute value one. Under Galois conjugation $\sigma \in \text{Gal}(\overline{\mathbb{Q}}/\mathbb{Q})$, its $q$-adic valuation satisfies the explicit valuation identity:
$$\nu_\iota(\sigma e) = -\frac{3}{2} v(\sigma | E)$$
On $H^1$, Weil's Riemann-hypothesis bound requires all complex Frobenius eigenvalues to have absolute value $q^{1/2}$. Testing the candidate diagonal Frobenius eigenvalues $(bq^{3/2}, bq^{1/2}, qbe')$ against the Weil bound eliminates $bq^{3/2}$ and $qbe'$, leaving $bq^{1/2}$ as the unique surviving eigenvalue. Its $q$-adic Newton slope is given by:

$$t_\eta = \frac{1}{2} - \frac{1}{3} \nu_\iota(e') \in \{0, 1\}$$

Substituting $\nu_\iota(\sigma e) = -\frac{3}{2} v(\sigma | E)$ directly into the slope formula yields:
$$t_\eta = \frac{1}{2} - \frac{1}{3} \left(-\frac{3}{2} v(\sigma | E)\right) = \frac{1 + v(\sigma | E)}{2} \in \{0, 1\}$$

#### Weak Admissibility & Pure Hodge Types
By $p$-adic Hodge theory (Fontaine, Lemma 6.5), the filtered de Rham module $H^1_{\text{dR}}(A_S / \mathbb{Q}_q)$ is weakly admissible, ensuring equality of Hodge numbers and Newton slopes ($t_H = t_N$). Because the algebraic Hecke idempotents $p_\chi$ commute with Frobenius and preserve the Hodge filtration $F^\bullet$, they convert $q$-adic slopes strictly into pure Hodge types:

> **Slope-to-Hodge Translation Summary**
> *   **Newton Slope $t_\eta = 1 \iff v(\sigma | E) = 1 \implies$ Pure Hodge Type $(1,0)$ (Holomorphic)**
> *   **Newton Slope $t_\eta = 0 \iff v(\sigma | E) = -1 \implies$ Pure Hodge Type $(0,1)$ (Antiholomorphic)**

Evaluating this slope identity across all scalar conjugates establishes that the theta classes reside in the complex linear spans of images of $U(v)_1$ under rational Hodge maps (Theorem 5.1 / Corollary 6.7). Applying Corollary 3.2 completes the Four-Factor Switch proof, thereby proving Theorem 1.1.

---

### 8. Consequences and Companion Applications

The surjectivity of $cl_B$ for CM abelian varieties resolves several major open problems in arithmetic geometry.

*   **Grothendieck's Generalized Hodge Conjecture (Corollary 8.2):**
    For any rational Hodge substructure $W \subset H^k(A, \mathbb{Q})$ on a CM abelian variety such that $W(r)$ is effective, there exists a closed algebraic subset $Z \subset A$ of codimension at least $r$ supporting $W$. This is proved by constructing an effective realization via a surjective rational Hodge map $H^n(B, \mathbb{Q})(-r_0) \to W$ from an auxiliary CM abelian variety $B$ (Lemma 8.1) and algebraizing the corresponding correspondence class via Theorem 1.1.
*   **Tate Conjecture over Finite Fields (Corollary 8.3):**
    Combines Theorem 1.1 with J.S. Milne's reduction theorems to prove that for every abelian variety $A / \mathbb{F}_q$, integer $r \ge 0$, and prime $\ell \neq \text{char}(\mathbb{F}_q)$, the $\ell$-adic cycle-class map is surjective:
    $$CH^r(A) \otimes_{\mathbb{Z}} \mathbb{Q}_\ell \longrightarrow H^{2r}_{\text{ét}}(\bar{A}, \mathbb{Q}_\ell(r))^{G_q}$$
    Furthermore, numerical equivalence and $\ell$-adic homological equivalence coincide for rational cycles on $\bar{A}$.
*   **Grothendieck's Hodge Standard Conjecture (Corollary 8.4):**
    Confirms that for an abelian variety $A$ of dimension $g$ over an algebraically closed field $K$, the rational symmetric intersection pairing:
    $$P_h^r(A) \times P_h^r(A) \longrightarrow \mathbb{Q}, \quad (x,y) \longmapsto (-1)^r \deg(x \cdot y \cdot h^{g-2r})$$
    is strictly positive definite on primitive algebraic classes $P_h^r(A)$ for any rational ample divisor class $h$.
*   **Specialization of Hodge Classes (Remark 8.5):**
    Utilizing CM transport (OpenAI, 23 Sep 2026), rational Hodge classes on good-reduction abelian varieties $A / \mathbb{Q}$ specialize to classes of rational algebraic cycles on the special fiber $A_0 / \mathbb{F}_p$ across all prime-to-$p$ and crystalline realizations.
*   **Companion Papers Context:**
    *   *Products of K3 Surfaces (OpenAI, 4 Oct 2026):* Theorem 1.1 serves as a critical core input to establish the rational Hodge conjecture for all finite products of projective complex K3 surfaces ($S_1 \times \dots \times S_m$). Specifically, the Kuga–Satake construction embeds the weight-two K3 transcendental Hodge structure $T(S)(1)$ into the weight-one Clifford algebra representation $W_S = C^+(T(S), q)$ associated with the Kuga–Satake abelian variety $A_S$. Theorem 1.1 algebraizes the Kuga–Satake correspondence $j_w: T(S)(1) \to \text{End}(W_S)$ on $W_S$, allowing the proof to transport algebraicity across tensor products of K3 surfaces.
    *   *Powers of Abelian Varieties:* Provides the necessary foundational cycle algebraicity to extend tensor invariants across full power architectures.

---

### 9. Scope, Limitations, and Current Status

> **Notice on Scope and Formal Verification:**
> 
> *   **Mathematical Scope Boundary:** The theoretical breakthrough in this preprint strictly applies to **CM abelian varieties** (and their finite products and powers). It does **not** prove the Rational Hodge Conjecture for arbitrary complex abelian varieties lacking complex multiplication, nor does it establish the conjecture for general smooth projective complex varieties.
> *   **Publication Status:** The source context is derived from an **unrefereed technical preprint** published by OpenAI on September 30, 2026.
> *   **Formal Verification Status:** The mathematical proof in the preprint has **not been formalized or machine-verified** inside Lean (such as Lean 4 / Mathlib) or any other interactive theorem prover.

---

### 10. Technical Glossary

| Term | Grounded Definition |
| :--- | :--- |
| **Abelian Variety of CM Type** | A complex abelian variety $A$ whose rational endomorphism algebra $\text{End}(A) \otimes_{\mathbb{Z}} \mathbb{Q}$ contains a commutative semisimple $\mathbb{Q}$-algebra of dimension $2 \dim A$. |
| **Betti Cycle-Class Map ($cl_B$)** | The natural cycle homomorphism $CH^p(X)_{\mathbb{Q}} \to H^{2p}(X, \mathbb{Q}) \cap H^{p,p}(X, \mathbb{C})$ mapping codimension-$p$ rational algebraic cycles to Betti cohomology classes. |
| **Four-Factor Switch (Theorem 2.5)** | An algebraic 1-dimensional tensor line in $H^4(\prod_{i=1}^4 B(v_i), \mathbb{Q})$ defined by sign functions satisfying $v_1 + v_2 = v_3 + v_4$. |
| **Odd Sign Function ($v$)** | A function $v: G_E \to \{1, -1\}$ satisfying $v(c\tau) = -v(\tau)$, which assigns weight-one CM Hodge structures to embedding lines. |
| **Pohlmann's Balance Criterion** | The criterion stating that an embedding-line tensor belongs to the rational Hodge class span iff every Galois conjugate contains equal numbers of holomorphic and antiholomorphic factors. |
| **Rational Hodge Class ($Hdg^{2p}(X)$)** | A rational cohomology class of degree $2p$ lying in the $(p,p)$ bidegree component of the complex Hodge decomposition. |
| **Weak Admissibility** | A foundational concept in $p$-adic Hodge theory (Fontaine) asserting equality of Hodge and Newton numbers ($t_H = t_N$), used to convert Hecke/Frobenius slopes into pure Hodge types. |
| **Weil Class** | A non-divisor generated Hodge class residing in determinant spaces $\Lambda_K^{2n} H^1(A, \mathbb{Q})$ for abelian varieties admitting imaginary quadratic or CM field actions. |