# Catalan's Constant is Irrational: A Sectioned Explainer and Technical Breakdown

---

## 1. Introduction to the Problem & Fundamental Definitions

Catalan's constant, universally denoted by $G$, is a foundational real number arising at the intersection of analytic number theory, complex analysis, and hyperbolic geometry. It is defined by the alternating infinite series:

$$G = \sum_{j=0}^{\infty} \frac{(-1)^j}{(2j+1)^2} = 1 - \frac{1}{9} + \frac{1}{25} - \frac{1}{49} + \dots \approx 0.915965594177...$$

In the classification of special values of $L$-functions, $G$ corresponds to the Dirichlet beta function $\beta(s)$ evaluated at $s = 2$:

$$\beta(s) = \sum_{j=0}^{\infty} \frac{(-1)^j}{(2j+1)^s} \quad (\mathrm{Re}(s) > 0) \implies G = \beta(2)$$

Equivalently, $G = L(2, \chi_{-4})$, where $\chi_{-4}$ is the unique primitive odd quadratic character modulo 4, defined by $\chi_{-4}(n) = 1$ if $n \equiv 1 \pmod 4$, $\chi_{-4}(n) = -1$ if $n \equiv 3 \pmod 4$, and $\chi_{-4}(n) = 0$ for even $n$.

> ### **Core Definitions**
> * **Rational Numbers ($\mathbb{Q}$):** The field of numbers expressible as a quotient of two integers $a/b$ with $b \neq 0$.
> * **Irrational Numbers ($\mathbb{R} \setminus \mathbb{Q}$):** Real numbers that cannot be represented as a ratio of integers; their decimal expansions are non-terminating and non-repeating.
> * **Dirichlet Beta Function ($\beta(s)$):** The analytic function defined for $\mathrm{Re}(s) > 0$ by $\sum_{j=0}^{\infty} (-1)^j (2j+1)^{-s}$.
> * **Arithmetic Nature of Beta Values:**
>   * **Odd Beta Values ($\beta(2k+1)$):** Rational multiples of $\pi^{2k+1}$. For instance, $\beta(1) = \frac{\pi}{4}$ (Leibniz formula) and $\beta(3) = \frac{\pi^3}{32}$.
>   * **Even Beta Values ($\beta(2k)$):** Transcendental or irrational properties for individual even integers $s \ge 2$ historically resisted proof because these values do not reduce to elementary algebraic powers of $\pi$.

### Arithmetic Distinction Between Odd and Even Beta Values
The fundamental arithmetic difference between odd and even Dirichlet beta values lies in their algebraic connection to $\pi$. Odd beta values $\beta(2k+1)$ are directly computable via Euler-type evaluation formulas involving Euler numbers $E_k$:

$$\beta(2k+1) = \frac{(-1)^k E_{2k} \pi^{2k+1}}{2^{2k+2} (2k)!}$$

Because $\pi$ is transcendental (Lindemann, 1882), every odd beta value $\beta(2k+1)$ is immediately transcendental, and therefore irrational. 

In contrast, even beta values $\beta(2k)$, starting with $\beta(2) = G$, possess no such evaluation in terms of $\pi^n$. Their qualitative arithmetic nature—whether rational or irrational—remained an open conjecture for over a century.

### Logarithmic and Geometric Integral Representations
Catalan's constant possesses several classical integral representations. A primary representation connects $G$ to double moments and logarithmic integrals:

$$K_0^- = M(0,0) = \int_{0}^{\pi/2} \log \left( \frac{1 + \sin \theta}{1 - \sin \theta} \right) d\theta = -4 \int_{0}^{\pi/4} \log(\tan v) \, dv = 4G$$

To verify $K_0^- = 4G$, substitute $x = \tan v$ into the integral $-4 \int_0^{\pi/4} \log(\tan v) \, dv$:

$$-4 \int_{0}^{1} \frac{\log x}{1 + x^2} \, dx = -4 \int_{0}^{1} \log x \left( \sum_{j=0}^{\infty} (-1)^j x^{2j} \right) dx$$

Integrating term-by-term using $\int_0^1 x^{2j} \log x \, dx = -\frac{1}{(2j+1)^2}$ yields:

$$-4 \sum_{j=0}^{\infty} (-1)^j \left( -\frac{1}{(2j+1)^2} \right) = 4 \sum_{j=0}^{\infty} \frac{(-1)^j}{(2j+1)^2} = 4G$$

---

## 2. Mechanics of Irrationality Proofs & The Denominator-Clearing Obstruction

### Quantitative Criterion for Irrationality
The classical quantitative criterion for proving that a real number $x$ is irrational relies on constructing sequence approximations by rational numbers. If $x \in \mathbb{Q}$, say $x = a/b$ with $a, b \in \mathbb{Z}$ and $b > 0$, then for any integers $A, B$ such that $Ax - B \neq 0$:

$$|Ax - B| = \left| A \frac{a}{b} - B \right| = \frac{|Aa - Bb|}{b} \ge \frac{1}{b} > 0$$

Thus, if one constructs a sequence of non-zero integer linear forms $I_m = A_m x - B_m$ (where $A_m, B_m \in \mathbb{Z}$) that satisfies $\lim_{m \to \infty} I_m = 0$, the hypothesis $x \in \mathbb{Q}$ produces a contradiction, proving $x \notin \mathbb{Q}$.

In practice, analytic approximations initially yield rational quotients $p_m / q_m \to x$ where $q_m \in \mathbb{N}$ are non-integer linear form denominators. To build pure integer forms $A_m x - B_m$, one must multiply by a denominator factor $D_m = \mathrm{lcm}(1, 2, \dots, N_m)$ to clear fractions. The central operational challenge is ensuring that the **analytical decay** of the error $|x - p_m/q_m|$ is sufficiently rapid to overcome the **arithmetic growth** of $D_m$.

### Classical Successes
* **Fourier's Proof for $e$:** Taylor series truncations of $e = \sum_{k=0}^m \frac{1}{k!} + R_m$ yield errors bounded by $\frac{1}{(m+1)!}$. Multiplying by $m!$ clears all denominators while leaving a tail of size $\frac{1}{m+1} \to 0$.
* **Apéry (1978) & Beukers (1979) for $\zeta(2)$ and $\zeta(3)$:** Apéry constructed explicit linear recurrences, which Beukers reinterpreted via double and triple integrals such as:

  $$I_m = \int_0^1 \int_0^1 \frac{x^m (1-x)^m y^m (1-y)^m}{(1 - xy)^{m+1}} \, dx \, dy = A_m \zeta(2) - B_m$$

  The analytical decay rate $(\sqrt{2}-1)^4 \approx 0.0294$ easily outpaces the prime-power growth rate $e^{2} \approx 7.389$ of $D_m^2 = \mathrm{lcm}(1, \dots, m)^2$, driving $D_m^2 I_m \to 0$.

### The Denominator-Clearing Obstruction for Catalan's Constant
For Catalan's constant, explicit approximation pipelines generated rapidly converging rational sequences $p_m / q_m \to G$. However, individual linear forms consistently failed to establish irrationality.

As detailed by Wadim Zudilin regarding Apéry-like difference equations, continued fractions, and double integrals for $G$, the cleared denominators $D_m$ grow at a rate $e^{c m}$ that strictly dominates the analytical decay rate $e^{-r m}$ ($c > r$). When individual forms $q_m G - p_m$ are multiplied by $D_m$ to clear rational coefficients, the arithmetic growth completely destroys the analytical decay, leaving integer forms whose magnitudes explode rather than vanish.

### Overcoming the Obstruction: Individual Forms vs. Determinant Matrices
The key breakthrough of the determinant strategy is replacing single linear forms $A_m G - B_m$ with high-dimensional determinantal linear forms $\Delta_N$ of size $n = 48N$. 

For an individual linear form, clearing denominators imposes a brute-force growth penalty proportional to $D_m \approx e^{m}$. In contrast, taking an $n \times n$ determinant $\Delta_N$ causes massive, systematic arithmetic cancellations across prime factors *within the matrix structure itself*. Local $p$-adic digit reductions and column eliminations reduce the local prime valuations of $\Delta_N$ on the scale of $n^2 = (48N)^2$. This matrix-level arithmetic economy allows the analytical decay of the multidimensional integral representation to outpace the denominator growth.

| Method / Context | Outcome / Denominator Obstruction Status |
| :--- | :--- |
| **Fourier ($e$) / Apéry & Beukers ($\zeta(2), \zeta(3)$)** | **Successful:** Analytical decay outpaces denominator growth ($r > c$); integer forms $A_m x - B_m \to 0$. |
| **Zudilin Apéry-Like Recurrences ($G$)** | **Obstructed:** Rational quotients $p_m/q_m \to G$ converge rapidly, but denominators grow too fast ($c > r$); cleared integer forms explode. |
| **Padé & Hypergeometric Constructions ($G$)** | **Obstructed:** Hypergeometric cancellations improve prime bounds (Rivoal, Krattenthaler), but individual linear form costs remain strictly above $1$. |
| **Permutation-Group Exponents (Viola–Marcovecchio, Eskandari)** | **Obstructed:** Bounds like $|G - p_m/q_m| \le q_m^{-0.62}$ yield approximation exponents $< 1$, which cannot force $q_m G - p_m \to 0$. |
| **Determinant Strategy (OpenAI, 2026)** | **Resolved:** Replaces single linear forms with $n \times n$ determinants $\Delta_N$; matrix arithmetic cancellations lower denominator cost to $-2.29084$, enabling analytical decay ($-2.29094$) to force a contradiction. |

---

## 3. Chronological Landscape of Earlier Results

* **Rivoal & Zudilin (2003):** Proved that infinitely many even Dirichlet beta values $\beta(2k)$ are irrational, and established that at least one value in the finite set $\{\beta(2), \beta(4), \beta(6), \dots, \beta(14)\}$ is irrational.
* **Zudilin (2003, 2017, 2019):** Reduced the finite collection containing at least one irrational value down to six values: $\{\beta(2), \beta(4), \dots, \beta(12)\}$. Constructed Apéry-like difference equations, continued fractions, double-integral representations, and established the determinantal Hankel matrix framework for special values.
* **Lai & Zhou (2022):** Further narrowed the set guaranteed to contain an irrational beta value to five values: $\{\beta(2), \beta(4), \beta(6), \beta(8), \beta(10)\}$.
* **Fischler (2020):** Obtained quantitative irrationality and linear independence results for families of Dirichlet $L$-values, confirming irrationality within structural families without isolating the individual value $\beta(2) = G$.
* **Rivoal, Krattenthaler–Rivoal, & Krattenthaler–Zudilin (2006, 2008, 2019):** Connected Padé approximations to hypergeometric series and proved conjectured denominator bounds. Identified dual hypergeometric constructions that explained hidden arithmetic cancellations in approximation summands.
* **Nesterenko (2016):** Developed effective explicit approximations to Catalan's constant using half-integer hypergeometric series and double Euler integrals.
* **Viola–Marcovecchio (2022) & Eskandari (2026):** Viola and Marcovecchio used the Rhin–Viola permutation-group method to derive an explicit approximation exponent of $0.6293...$. Eskandari constructed explicit rational approximations satisfying:

  $$0 < \left| G - \frac{p_m}{q_m} \right| \le q_m^{-0.62}$$

  Because these approximation exponents are strictly below $1$, they do not establish qualitative irrationality.
* **Calegari, Dimitrov & Tang (2005, 2024, 2025):** Calegari proved the irrationality of the $2$-adic analogue $G_2 \in \mathbb{Q}_2$. Calegari, Dimitrov, and Tang proved the $\mathbb{Q}$-linear independence of $1, \pi^2,$ and $L(2, \chi_{-3})$ (conductor 3). Crucially, Calegari, Dimitrov, and Tang observed that for conductor 3, the real identity contains an additional $\pi^2$ term that is absent in the 2-adic setting. (This real $\pi^2$ term for conductor 3 is distinct from the $\zeta(2)$ term cancellation mechanism constructed for conductor 4 in the present proof).
* **Sun (2026):** Announced a preprint claiming qualitative irrationality of Catalan's constant; no result or technique from Sun's preprint is used in the proof analyzed here.

---

## 4. Main Theorem Statement & Geometric Consequences

### Main Theorem
> **Theorem 1.1** (OpenAI, September 24, 2026)  
> *Catalan’s constant $G$ is irrational.*

### Geometric and Topological Consequences
The resolution of Theorem 1.1 solves longstanding conjectures regarding hyperbolic volumes in 3-manifold topology and arithmetic geometry (Section 8 of the source paper):

* **Minimal 2-Cusped Hyperbolic 3-Manifold Volume:** By Agol's Theorem (2010), $4G$ is the precise minimal volume of an orientable complete finite-volume hyperbolic 3-manifold with exactly two cusps (realized uniquely by the Whitehead-link complement and the $(-2,3,8)$-pretzel-link complement). Theorem 1.1 proves that **this minimal 2-cusped volume $4G$, as well as the volumes of both link complements, are irrational**.
* **Volumes of Arithmetic Hyperbolic 3-Orbifolds over $\mathbb{Q}(i)$:** Let $\mathcal{O}$ be a maximal order in a quaternion algebra $B / \mathbb{Q}(i)$ with finite reduced discriminant $D$, and let $\Gamma_1(\mathcal{O}) = \mathcal{O}^1 / \{\pm 1\}$ be its projective norm-one group. The volume formula for the arithmetic 3-orbifold is:

$$\mathrm{vol}(\Gamma_1(\mathcal{O}) \backslash \mathbb{H}^3) = \frac{G}{3} \prod_{\mathfrak{p} \mid D} (N\mathfrak{p} - 1)$$

  where $N\mathfrak{p} = |\mathbb{Z}[i]/\mathfrak{p}|$ is the norm of the prime ideal $\mathfrak{p}$. Any lattice $\Gamma \le \mathrm{PSL}_2(\mathbb{C})$ commensurable with $\Gamma_1(\mathcal{O})$ has volume equal to a positive rational multiple of $\mathrm{vol}(\Gamma_1(\mathcal{O}) \backslash \mathbb{H}^3)$. Consequently, **the volumes of all orientable arithmetic hyperbolic 3-orbifolds defined over $\mathbb{Q}(i)$ are irrational**.
* **Modular Orbifold $\mathrm{PSL}_2(\mathbb{Z}[i]) \backslash \mathbb{H}^3$:** In the split quaternion case $B = \mathrm{M}_2(\mathbb{Q}(i))$ and $\mathcal{O} = \mathrm{M}_2(\mathbb{Z}[i])$, the discriminant product is empty, giving:

$$\mathrm{vol}(\mathrm{PSL}_2(\mathbb{Z}[i]) \backslash \mathbb{H}^3) = \frac{G}{3}$$

  which is now proved to be **irrational**.

---

## 5. Step-by-Step Technical Breakdown of the Proof

The proof proceeds by constructing a sequence of determinantal linear forms $\Delta_N$ of size $n = 48N$. Assuming $G \in \mathbb{Q}$, $\Delta_N$ is rational. The argument establishes two mutually exclusive asymptotic bounds on the normalized logarithm:

$$L_N = \frac{\log |\Delta_N|}{(48N)^2} - \frac{1}{2}\log 2$$

1. **Arithmetic Lower Bound (Propositions 2.2, 3.4, 4.1):** By evaluating $2$-adic and odd-prime valuations and proving nonvanishing along prime scales $N = p$, $\liminf_{p \to \infty} L_p > -2.29084$.
2. **Analytic Upper Bound (Propositions 5.3, 7.1):** By multi-variable energy estimates and rational trial function certificates, $\limsup_{N \to \infty} L_N \le -2.290939875 < -2.2909$.

Because $-2.29084 > -2.2909$, the two bounds are mathematically incompatible, forcing the conclusion $G \notin \mathbb{Q}$.

```
                 [ Assume G in Q ]
                         │
        ┌────────────────┴────────────────┐
        ▼                                 ▼
[ Finite-Place Arithmetic ]     [ Real-Place Analytic ]
[ Valuation & Nonvanishing]     [ Potential Estimates ]
        │                                 │
        ▼                                 ▼
   lim inf L_p > -2.29084          lim sup L_N <= -2.2909
        │                                 │
        └────────────────┬────────────────┘
                         ▼
             -2.29084 > -2.2909  (CONTRADICTION!)
                         │
                         ▼
                 [ G is Irrational ]
```

---

### Step 1: Moment Kernels & $\zeta(2)$ Cancellation (Section 2)
For non-negative integers $i, j$, two basic moment kernels are defined:

$$M(i, j) = \int_{-1}^1 \int_{0}^1 \frac{|t| f(t) \, t^i s^j}{1 - ts} \, ds \, dt, \quad Z(i, j) = \int_{0}^1 \int_{0}^1 \frac{t^i s^j}{1 - ts} \, ds \, dt$$

where $f(t) = \sqrt{1 - t^2}$ on $(-1, 1)$. Expanding $(1 - ts)^{-1} = \sum_{u=0}^\infty t^u s^u$ and integrating termwise yields the exact algebraic decompositions:

$$M(i, j) = M_0(i, j) + 4G c_{(i-j)/2} + \frac{3}{2}\zeta(2) c_{(j-i-1)/2}$$

$$Z(i, j) = Z_0(i, j) + [i = j]\zeta(2)$$

where $M_0(i, j)$ and $Z_0(i, j)$ are explicit rational arrays, $c_l = 4^{-l} \binom{2l}{l}$ for non-negative integers $l$ (and $c_l = 0$ if $l < 0$ or $l \notin \mathbb{Z}$), and $[i=j]$ is the Iverson bracket.

---

### Step 2: Chebyshev Rows & Proposition 2.1
Polynomial row vectors $P_r(t)$ and $D_r(t)$ of size $n = 48N$ (for $0 \le r < n$) are constructed using normalized Chebyshev polynomials $T_d(x)$ and $U_{d-1}(x)$:

$$P_r(t) = (1-t)^h t^{C-1} T_d(1/t), \quad D_r(t) = \mathrm{sgn}(r-g)(1-t)^h t^{C-1} U_{d-1}(1/t)$$

where $d = |r-g|$. Setting $w = t / (1 + \sqrt{1-t^2}) = t/2 + O(t^3)$, high Taylor contact at $t = 0$ is established:

$$\frac{t P_r(t)}{f(t)} - D_r(t) = O(t^L)$$

For raw column indices $j < L$, defining $F_j(r) = M(P_r, j) - \frac{3}{2} Z(D_r, j)$ contracts the Chebyshev rows against the moment kernels. The Taylor contact $O(t^L)$ causes the coefficient of $\zeta(2)$ to vanish identically for all $j < L$:

$$\frac{3}{2} \left( \sum_{i} [t^i] P_r \cdot c_{(j-i-1)/2} - [t^j] D_r \right) = \frac{3}{2} [t^j] \left( \frac{t P_r(t)}{f(t)} - D_r(t) \right) = 0$$

Thus, **Proposition 2.1** confirms that $F_j(r) \in \mathbb{Q} + \mathbb{Q}G$. Under the hypothesis $G \in \mathbb{Q}$, every entry of the determinant $\Delta_N$ is strictly rational.

---

### Step 3: Determinant $\Delta_N$ Construction
For a positive integer scaling parameter $N$, the matrix dimensions and operational parameters are fixed as:

$$\begin{aligned}
n &= 48N, & a &= 11N, & b &= 7N, & q &= 4N, & g &= 4N, \\
h &= 2N, & L &= 59N, & C &= 63N, & H &= 65N, & A &= 19N
\end{aligned}$$

The determinant $\Delta_N$ of size $n \times n$ is defined by filtering the $n \times (n+q)$ raw moment matrix $F$ (with columns $F_j$ for $b \le j < L$) through an integer binomial filter matrix $T$:

$$\Delta_N = \det_{0 \le r, k < n} \left( M\left(P_r, s^{b+k}(1-s)^q\right) - \frac{3}{2} Z\left(D_r, s^{b+k}(1-s)^q\right) \right) = \det(F T)$$

where $T_{j,k} = (-1)^{j-b-k} \binom{q}{j-b-k}$ for $b \le j < L$ and $0 \le k < n$.

---

### Step 4: The 2-Adic Lower Bound (Proposition 2.2)
By constructing a $2$-adic moment series $M_s(i, j) = \sum_{k=0}^\infty \frac{m_{i+k}}{j+k+1} \in \mathbb{Q}_2$, the discrepancy between $M_s$ and $M_0 + 4G c$ is isolated into two constant $2$-adic elements $e_1, e_2 \in \mathbb{Q}_2$. 

Setting $\delta = \frac{q+g+h}{n} = \frac{10N}{48N} = \frac{5}{24}$, **Proposition 2.2** establishes the lower $2$-adic valuation bound for $\Delta_N$ and all its full minors:

$$v_2(\Delta_N) \ge -\left(\frac{\delta}{2} + \frac{\delta^2}{8}\right)n^2 - O_G(n \log(n+2)) = -\frac{505}{4608}n^2 - O_G(n \log(n+2))$$

---

### Step 5: Odd-Prime Digit Reductions & Elimination (Lemmas 3.1–3.3)
For odd primes $2\sqrt{H} < p \le H$, $p$-adic digit reductions are derived using the polynomial $E(t) = (1-t^2)^{(p-1)/2} = \sum_{d=0}^{p-1} E_d t^d \pmod p$, where $E_d \equiv c_{d/2} \pmod p$ for even $d$.

**Lemma 3.1 (Digit Reductions):** For $0 \le i, j < H$, let $\ell = j \bmod p$, $d = (j - i - 1) \bmod p$, $i' = i + 1 + \frac{d - \ell}{p} - 1$, and $j' = \lfloor j/p \rfloor$. Then $i' \ge -1$, and modulo $p$:

$$p^2 M_0(i, j) \equiv E_d M_0(i', j') \pmod p$$

$$p^2 Z_0(i, j) \equiv \begin{cases} Z_0(\lfloor i/p \rfloor, j') \pmod p, & i \equiv j \pmod p \\ 0 \pmod p, & i \not\equiv j \pmod p \end{cases}$$

with the boundary convention $M_0(-1, j') = k_{j'+1}^+$.

* **Column Pairing (Lemma 3.2):** Columns are grouped into pairs $X_\ell = V_\ell$ and $X_{p+\ell} = U_\ell - V_\ell$ whose linear combinations fall into $p^{-1}\mathbb{Z}_p^n$ rather than $p^{-2}\mathbb{Z}_p^n$.
* **Local Integer Elimination (Lemma 3.3):** For central primes $H/2 < p \le H$, central columns are transformed over $\mathbb{Z}_p$ using vectors $V_\ell$, eliminating $p^{-2}$ and $p^{-1}$ denominator contributions down to an explicit rank bound $R(p)$.

---

### Step 6: Prime Loss Function & Proposition 3.4
Integrating local valuation bounds over all odd prime scales $x = p/N$ yields a continuous prime loss function $d(x)$ on $[0, 65]$:

$$\int_0^{65} d(x) dx = \frac{8609}{2}$$

Combining the prime number theorem integral $\frac{1}{2304} \int_0^{65} d(x) dx = \frac{8609}{4608}$ with the $2$-adic valuation bound from Proposition 2.2 yields **Proposition 3.4**:

$$\begin{aligned}
\liminf_{N \to \infty, \Delta_N \neq 0} L_N &\ge -\frac{8609}{4608} - \left(\frac{1}{2} + \frac{505}{4608}\right)\log 2 \\
&= -\frac{8609}{4608} - \frac{2809}{4608}\log 2 \approx -2.2908095 > -2.29084
\end{aligned}$$

---

### Step 7: Nonvanishing at Prime Scales (Proposition 4.1)
To ensure the existence of non-zero determinants along an unbounded sequence, set $N = p$ for a sufficiently large prime $p$. Using Frobenius endomorphisms $t \mapsto t^p$ and palindromic polynomial bases $\mathbf{a}, \mathbf{b}$, the $48p \times 48p$ matrix $\Delta_p$ reduces modulo $p$ to three fixed $48 \times 48$ rational matrices: $B_0$, $B_0 + B_1$, and $B_0 - B_1$.

The determinant factorizes modulo $p$ as:

$$\det L_p = (\det \mathbf{a})^{48} \det B_0 \cdot \det(B_0 + B_1)^{(p-1)/2} \det(B_0 - B_1)^{(p-1)/2}$$

An exact finite Gaussian elimination certificate modulo 101 establishes that $\det B_0 \neq 0$, $\det(B_0 + B_1) \neq 0$, and $\det(B_0 - B_1) \neq 0$ in $\mathbb{F}_{101}$. 

Because nonvanishing modulo 101 guarantees nonvanishing over $\mathbb{Q}$, $\det L_p \neq 0 \pmod p$ for all sufficiently large primes $p$. Thus, **Proposition 4.1** establishes:

$$v_p(\Delta_p) = -96p \implies \Delta_p \neq 0 \quad \text{for all sufficiently large primes } p$$

---

### Step 8: Real-Place Estimates (Section 5)
Applying Andréief's identity and Cauchy's double alternant to $\Delta_N = \det(FT)$ produces an exact $2n$-fold integral representation:

$$\Delta_N = \frac{1}{(n!)^2} \int_{(-1,1)^n} \int_{(0,1)^n} R_n(x) \frac{V(t) V(s)^2 \prod s_j^b (1-s_j)^q}{\prod_{i,j} (1-t_i s_j) \prod |t_i|^{C-1} (1-t_i)^h} \, ds \, d\mu^n(t)$$

where $V(t) = \prod_{i<j} (t_j - t_i)$, $V(s) = \prod_{i<j} (s_j - s_i)$, and $d\mu(t_i) = \frac{|t_i|}{f(t_i)} dt_i$. The coordinate transformation between $t_i \in (-1, 1)$ and $x_i \in (-1, 1)$ is defined by:

$$x_i = \frac{t_i}{1 + \sqrt{1 - t_i^2}} \iff t_i = \frac{2x_i}{1 + x_i^2}, \quad d\mu(t_i) = \frac{4|x_i|}{(1 + x_i^2)^2} dx_i$$

* **Interpolation Range $\Omega_{2,n}$ (Lemma 5.1 & Proposition 5.2):** When $\sum_{i=1}^n \frac{1-x_i^2}{1+x_i^2} \le D^* = 40N-1$, a holomorphic interpolant $h^*(z)$ with $\|h^*\|_\infty \le 10 e^{12} n$ constructed via a finite-dimensional Hardy-space operator cancels evaluation determinants algebraically, yielding:

  $$|R_n(x)| \le (1 + K_0 n)^n V(1/x) \prod_{i=1}^n |x_i|^g = e^{O(n \log n)} V(1/x) \prod_{i=1}^n |x_i|^g$$

* **Hadamard Range $\Omega_{1,n}$ (Proposition 5.3):** In the complementary domain, Hadamard's inequality bounds $R_n(x)$ by $e^{O(n \log n)} 2^{-\binom{n}{2}} \prod (1+x_i^2)^{(n-1)/2} |x_i|^{g-(n-1)}$.

---

### Step 9: Uniform Energy Bound (Section 6)
To bound the logarithmic interactions in the integrand, the one-variable logarithmic potential functions are introduced:

$$W_\kappa(x) = (\alpha + 2\gamma)\log|x| + 2\eta \log(1-x) - \left(\frac{\kappa}{2} + \alpha + \eta + \gamma\right)\log(1+x^2)$$

$$W_s(s) = \beta \log s + \gamma \log(1-s), \quad D(x) = 2\gamma - \frac{2x^2}{1+x^2}$$

Applying Haagerup's Chebyshev expansion of the logarithmic kernel:

$$\log|u - u'| = -\log 2 - 2 \sum_{k=1}^\infty \frac{T_k(u)T_k(u')}{k}$$

Regularizing diagonal interactions with damping factors $\tau = 1-\varepsilon$, $\rho(x) = 1-\varepsilon(1-x)$, $\sigma(s) = 1-\varepsilon\sqrt{1-s}$ and introducing trial sequences $p, v$ via $-a^2 \le b^2 - 2ab$ reduces the multi-variable energy integral strictly to one-variable suprema:

$$\begin{aligned}
\limsup_{N \to \infty} L_N \le (-1 + \alpha + \gamma)\log 2 + \kappa \|p\|_*^2 + \frac{1}{2} \|v\|_*^2 &+ \sup_{x \in [-1,1) \setminus \{0\}} \{ W_\kappa(x) + \lambda D(x) - 2\kappa T(p,x) - S(v,x) \} \\
&+ \sup_{s \in (0,1)} \{ W_s(s) + 2 T(v,s) \}
\end{aligned}$$

---

### Step 10: Quantitative Certificate (Section 7 & Proposition 7.1)
Explicit rational trial sequences $p, v$ of degrees up to 10 with exponential tails are specified. Derivative numerators $A_X(x)$ and $A_Y(s)$ are formed, and Descartes' rule of signs bounds the number of real roots within isolated open brackets. 

Evaluating $X_\kappa(x)$ and $Y_\kappa(s)$ across 50 candidate bracket endpoints certifies **Proposition 7.1**:

$$\limsup_{N \to \infty} L_N \le -2.290939875 < -2.2909$$

---

### Step 11: Final Contradiction
Combining the bounds along the unbounded prime sequence $N = p$:

$$-2.29084 < \liminf_{p \to \infty} L_p \le \limsup_{N \to \infty} L_N \le -2.290939875$$

Because $-2.29084 > -2.2909$, these bounds create an absolute numerical incompatibility. The assumption $G \in \mathbb{Q}$ must be false. **Catalan's constant $G$ is irrational.**

---

## 6. Key Contributors & Key Figures Index

| Researcher | Primary Contribution / Relevance to Catalan's Constant Proof |
| :--- | :--- |
| **Ian Agol** | Proved that $4G$ is the minimal volume of an orientable complete finite-volume 2-cusped hyperbolic 3-manifold. |
| **Roger Apéry** | Established the irrationality of $\zeta(2)$ and $\zeta(3)$ using explicit difference equations and linear forms. |
| **Frits Beukers** | Reinterpreted Apéry's proofs using multidimensional double and triple integrals. |
| **Frank Calegari** | Proved the irrationality of the $2$-adic Catalan analogue $G_2 \in \mathbb{Q}_2$; co-proved linear independence of Dirichlet $L$-values. |
| **Vesselin Dimitrov** | Co-proved $\mathbb{Q}$-linear independence of $1, \pi^2, L(2, \chi_{-3})$ and analyzed Catalan denominator obstructions. |
| **Payman Eskandari** | Constructed explicit rational approximations to $G$ achieving error exponent $0.62$. |
| **Stéphane Fischler** | Proved quantitative irrationality and linear independence results for families of Dirichlet $L$-functions. |
| **Christian Krattenthaler** | Derived hypergeometric proofs of Padé denominator bounds and identified dual hypergeometric identities. |
| **Li Lai** | Co-reduced the finite set containing an irrational beta value down to 5 values. |
| **Raffaele Marcovecchio** | Co-developed permutation-group approximations to $G$ achieving exponent $0.6293...$. |
| **Yu. V. Nesterenko** | Developed effective approximations to $G$ using half-integer hypergeometric series and double Euler integrals. |
| **Tanguy Rivoal** | Proved that infinitely many even beta values are irrational; connected Padé approximations to hypergeometric series. |
| **Zhi-Wei Sun** | Announced an independent preprint on Catalan's constant (unrelated to the current proof). |
| **Yunqing Tang** | Co-proved linear independence results for $L(2, \chi_{-3})$ and studied holonomy bounds. |
| **Carlo Viola** | Co-developed the Rhin–Viola permutation-group approximations for Catalan's constant. |
| **Wadim Zudilin** | Proved key beta-value family reductions, constructed Apéry-like equations for $G$, and established determinantal Hankel criteria. |

---

## 7. Contextual Scope, Limitations & Verification Status

### Scope & Limitations
* **Qualitative Result Only:** The proof establishes that $G \notin \mathbb{Q}$. It **does not** establish an explicit irrationality measure $\mu(G)$ (which would bound $|\beta - p/q| > q^{-\mu(G)}$ for all rational $p/q$).
* **Provenance:** Research paper *Catalan's constant is irrational* published by OpenAI on September 24, 2026.

### Formal Verification Status
The Lean formalization scope is maintained in the open-source repository `openai/math` under file `math/lean/docs/005.md`.

* **Formal Assertion:** $G = \sum_{j=0}^\infty \frac{(-1)^j}{(2j+1)^2} \notin \mathbb{Q}$.
* **Lean Formalization Setup:** The formal theorem statement and comparator challenge setup are specified in `Catalan.lean` within the Lean 4 environment.

---

## 8. Comprehensive Glossary of Technical Terms

* **Catalan's Constant ($G$):** The real number defined by $G = \sum_{j=0}^\infty (-1)^j (2j+1)^{-2} \approx 0.91596559...$.
* **Dirichlet Beta Function ($\beta(s)$):** The analytic function defined for $\mathrm{Re}(s) > 0$ by $\sum_{j=0}^\infty (-1)^j (2j+1)^{-s}$.
* **Dirichlet $L$-Function ($L(s, \chi)$):** The analytic continuation of $\sum_{n=1}^\infty \chi(n) n^{-s}$; for $\chi_{-4} \pmod 4$, $L(2, \chi_{-4}) = G$.
* **Chebyshev Polynomials ($T_d, U_d$):** Families of orthogonal polynomials defined by $T_d(\cos \theta) = \cos(d\theta)$ (first kind) and $U_{d-1}(\cos \theta) \sin \theta = \sin(d\theta)$ (second kind).
* **2-adic Valuation ($v_2(x)$):** The exponent of the highest power of 2 dividing a rational number $x \in \mathbb{Q}_2$.
* **Andréief's Identity:** The determinant integration formula:
  $$\int_{\Omega^n} \det[\phi_r(t_i)]_{r,i} \det[\psi_k(t_i)]_{k,i} \, d\mu^n(t) = n! \, \det_{r,k} \left( \int_\Omega \phi_r(t) \psi_k(t) \, d\mu(t) \right)$$
* **Cauchy's Double Alternant:** The algebraic determinant identity:
  $$\det_{1 \le i, j \le n} \left[ \frac{1}{1 - t_i s_j} \right] = \frac{V(t) V(s)}{\prod_{i=1}^n \prod_{j=1}^n (1 - t_i s_j)}$$
* **Frobenius Endomorphism:** The prime-characteristic ring endomorphism $x \mapsto x^p$, which acts map-wise on polynomial coefficients and collapses degree scales.
* **Orientable Hyperbolic 3-Manifold / Orbifold:** A 3-dimensional smooth manifold or orbifold equipped with a complete Riemannian metric of constant sectional curvature $-1$.