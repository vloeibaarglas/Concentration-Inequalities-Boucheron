# Addendum: Errata in the Textbook

*Companion to "Boucheron, Lugosi & Massart, Concentration Inequalities — Exercises with Solutions, All Chapters."*

Errors in the printed text of Stéphane Boucheron, Gábor Lugosi and Pascal Massart, *Concentration Inequalities: A Nonasymptotic Theory of Independence* (Oxford University Press, First Edition 2013; ISBN 978-0-19-953525-5), found while working the exercises: false statements, wrong constants and ranges, missing hypotheses, and hints that do not lead where they claim. Each entry names the defect, says whether it is in the statement or in the hint, and gives the correction; the full counterexample or proof is in the solution to that exercise. 60 entries across 13 of the 14 chapters with exercises.

## Chapter 2 — Basic Inequalities

**2.5 — false as stated (statement: the minimum misses $q=0$).** With the minimum over positive integers $q$ only, $Y\equiv 2t$ gives moment side $\min_{q\ge1}2^q=2$ but Chernoff side $\inf_{\lambda>0}e^{\lambda t}=1$. Include $q=0$, i.e. compare with $\min\bigl(1,\inf_{q\ge1}\mathbb{E}[Y^q]t^{-q}\bigr)$; equivalently, the printed inequality holds whenever the Chernoff bound is below $1$.

**2.15 — wrong range (statement).** The bound $\psi_Y(\lambda)\le\log\bigl(1+v(e^{\lambda}-\lambda-1)\bigr)$ is claimed for all $\lambda\in\mathbb{R}$ but fails for $\lambda<0$: for Rademacher $Y$ ($v=1$) at $\lambda=-1$, $\log\cosh1\approx0.434>\log(1+e^{-1})\approx0.313$. It (and the hint's $\mathrm{Var}(Z)\le ve^{\lambda}$) holds for $\lambda\ge0$, which is all Bennett's inequality needs.

**2.18 — insufficient hypothesis (statement).** "$n\ge e^3$" does not suffice: at $n=e^3$ the inner logarithm $\log(\log(n/e)/e)=\log(2/e)$ is negative and the bound is undefined, and at $n=160$ the bound gives $3.113$ while $\mathbb{E}\max_iX_i=4.503$. The lower bound $W(z)\ge\log z-\log\log z$ needs $z=\log(n/e)/e\ge e$, i.e. $n\ge e^{e^2+1}\approx4399$.

**2.20 — insufficient hypothesis (statement).** In the last display "$\log n>c$" does not suffice: the right side is not real unless $(\log n-c)/(ec)>1$, and the appeal to Exercise 2.18's bound on $W$ needs $(\log n-c)/(ec)\ge e$. The bound holds for $\log n\ge(1+e^2)c$ (the same range error as 2.18).

**2.26 — missing hypothesis (statement).** False when $g$ may be negative: $X$ uniform on $\{1,2\}$, $h\equiv1$, $f=(1,0)$, $g=(-10,-9)$ satisfies $\mathbb{E}[hf]=1/2\le1=\mathbb{E}[h]$, yet $\mathbb{E}[fgh]=-5>-9.5=\mathbb{E}[hg]$. Add $g\ge0$.

**2.27 — missing hypothesis: centering (statement).** Without $\mathbb{E}X_i=0$ no $n$-independent $L$ exists: with $p=1$, $X_i\sim\mathrm{Exp}(1)$, $s_i\equiv1$ and $t=n/2$, $\mathbb{P}\{Z\ge n/2\}\to1$ by the law of large numbers, while $L\exp\bigl(-\tfrac1L\min(n/4,n/2)\bigr)\to0$. Assume the $X_i$ are centered.

**2.28 — wrong range (statement).** For the Gumbel variable ($\mathrm{Var}(X)=\pi^2/6$) the mgf bound is claimed for all $\lambda\ge0$, but for $\lambda>1$ the right side $\mathrm{Var}(X)\lambda^2/(2(1-\lambda))$ is finite and negative ($-\pi^2/3\approx-3.29$ at $\lambda=2$) while $\mathbb{E}e^{\lambda X}=+\infty$, and at $\lambda=1$ it is undefined. The correct range is $0\le\lambda<1$ (the hint's $\max_iX_i$ should also read $\max_iY_i$).

## Chapter 3 — Bounding the Variance

**3.4 — insufficient hypothesis (statement).** A bias $c/n+O(n^{-2})$ gives only $\mathbb{E}\tilde Z-\theta=O(n^{-1})$: with remainder $\rho_n=(-1)^n/n^2$ the bias of the corrected estimate $\tilde Z$ is $(-1)^n(2n-1)/(n(n-1))\asymp1/n$. The $O(n^{-2})$ conclusion needs a two-term expansion $c/n+d/n^2+O(n^{-3})$ (and i.i.d. $X_i$).

**3.16 — false hint.** The claim that $\sum_{i,j}p_{ij}^2(\lambda_i(A)-\lambda_j(B))^2$ is minimized over doubly stochastic $P$ at $P=I$ is false: for $n=2$, $\lambda(A)=(2,0)$, $\lambda(B)=(1,1)$, the uniform $P$ gives $1$ and $P=I$ gives $2$. The intended lemma is linear in $P$, $\sum_{i,j}p_{ij}(\lambda_i(A)-\lambda_j(B))^2\ge\sum_i(\lambda_i(A)-\lambda_i(B))^2$, applied to $P=(q_{ij}^2)$.

**3.18 — wrong rate and constant (statement).** A gap bound $\sqrt{a_{k+1}}-\sqrt{a_k}\le ck$ telescopes only to an $e^{-t^{1/4}}$-type tail, so "which implies" fails; the provable gap bound is a universal constant ($4$). The tail $Ce^{-\sqrt t/C}$ then holds with $C$ depending on $MZ$, not universally: for the self-bounding $Z\sim\mathrm{Bin}(n,1/2)$, $\mathbb{P}\{Z>MZ+\sqrt n\}\to\approx0.023$ ($0.0231$ at $n=10^3$), whereas a universal $C$ would force it to $0$.

**3.20 — missing hypothesis (statement).** The condition $V\le WZ$ does not constrain $W$ on $\{Z=0\}$: with $n=1$, $Z=X_1\sim\mathrm{Bernoulli}(1/2)$, $W=1$ on $\{Z=1\}$ and $W=-100$ on $\{Z=0\}$, the hypothesis holds but $\mathbb{E}W=-49.5<1/4=\mathrm{Var}(\sqrt Z)$. Add $W\ge0$.

## Chapter 4 — Basic Information Inequalities

No errata found.

## Chapter 5 — Logarithmic Sobolev Inequalities

**5.1 — false hint (missing normalization).** The hint says $\lim_{p\uparrow2}\Psi_p(Z)=\mathrm{Ent}(Z^2)/2$, but $\Psi_p(Z)\to\Psi_2(Z)=0$ for every square-integrable $Z$ (for $Z$ uniform on $\{1,3\}$, $\Psi_{1.999}(Z)\approx0.00092$ against $\mathrm{Ent}(Z^2)/2\approx0.920$). The limit holds for the normalized ratio of the hint's monotonicity claim: $\Psi_p(Z)/((1/p)-(1/2))\to2\,\mathrm{Ent}(Z^2)$, equivalently $\Psi_p(Z)/(2-p)\to\mathrm{Ent}(Z^2)/2$.

**5.7 — false hint (sign of the exponent).** Both of the hint's decompositions have $e^{t}$ where $e^{-t}$ belongs; the correct identities are $\alpha_0\pm e^{-t}\alpha_1=v(1\pm e^{-t})/2+w(1\mp e^{-t})/2$ (with $\alpha_0=0$, $\alpha_1=1$, $t=1$: left side $\approx0.368$, printed right side $\approx1.543$). Also $|Z_t|$ should be $\|Z_t\|$ and $\beta_1=(\|v\|-\|w\|)/2$; the statement itself is correct.

**5.9 — missing hypothesis (statement).** The second inequality is false without $\mathbb{E}Y_i=0$: $Y_1\equiv1$, $Y_2\equiv-1$ gives $\sqrt2\le0$. With centered $Y_i$ it holds (symmetrization).

**5.23 — false as stated (statement).** For unitary $W$, $WH$ is in general not Hermitian, so it cannot be GUE: $W=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$, $H=\mathrm{diag}(1,2)$ gives $WH=\left(\begin{smallmatrix}0&2\\1&0\end{smallmatrix}\right)$. The intended statement is invariance under conjugation: $WHW^*$ is GUE.

**5.24 — false as stated (statement).** The constant polynomial $p\equiv1$ has $\{p=1\}=\mathbb{R}^n$. The intended claim is that the zero set of every nonzero polynomial is Lebesgue-null; applied to $p-1$ it gives the printed conclusion whenever $p\not\equiv1$.

**5.28 — misstated target (statement, wording).** The natural map $H\mapsto(D,T(U))$ is a diffeomorphism onto the open subset $\mathcal{D}_n^d\times T(\mathcal{U}_n^{vg})$ of $\mathcal{D}_n^d\times\mathbb{R}^{n(n-1)}$, not onto all of it: for $n=2$, $T(\mathcal{U}_2^{vg})=\mathbb{C}\setminus\{0\}$. The statement should read "diffeomorphism onto an open subset of $\mathcal{D}_n^d\times\mathbb{R}^{n(n-1)}$", which is what the hint (openness of $T(\mathcal{U}_n^{vg})$) shows.

**5.30 — wrong matrix (statement).** The printed $M$ is not the real matrix of $A\mapsto U^*AU$: the first column block lacks a factor $2$, and the off-diagonal blocks carry $2\bar U[j',j]U[k',k]$ where $\bar U[j',j]U[k',k]\pm\bar U[k',j]U[j',k]$ belongs. For $U=2^{-1/2}\left(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\right)$ it gives $C^{1,1}[1,1]=3/4$ and $C^{1,2}[1,1]=-1/2$ instead of $1$ and $0$ ($\det M=1/2$ instead of $1$); the two defects are independent, so fixing the factor $2$ alone still leaves $-1/2$.

**5.31 — wrong value (statement).** For $n=2$, $\int_{\mathbb{R}^2}(x_1-x_2)^2\,\gamma^{\otimes2}(dx)=2$, but $\prod_{j=0}^{1}j!=1$. The integral over $\mathbb{R}^n$ is $n!\prod_{j=0}^{n-1}j!$; the printed value is the integral over the ordered region.

**5.35 — wrong constant (hint).** The printed kernel $K_n(x,x)$ with normalization $1/\sqrt{2\pi n}$ is correct, but its derivative is $-\frac{e^{-x^2/2}}{\sqrt{2\pi n}}h_nh_{n-1}=-\frac{e^{-x^2/2}}{\sqrt{2\pi}\,n}h_nh_n'$; the hint drops the factor $1/\sqrt{2\pi n}$. At $n=2$ the true derivative is $1/(2\sqrt\pi)\approx0.282$ times the printed one.

**5.36 — false as stated (statement).** If all entries $A_{ij}$, $i\le j$, have the same variance, the law of $A$ is not orthogonally invariant and the eigenvalue density is not of the printed form: for $n=1$, $\lambda_1\sim N(0,1)$, but the formula gives an $N(0,1/4)$ shape. It holds for the invariant normalization $A_{ii}\sim N(0,\sigma^2)$, $A_{ij}\sim N(0,\sigma^2/2)$ for $i<j$.

**5.37 — wrong constant (statement).** The factor $1/3$ in the denominator $2+tU(2n)/3$ is false: at $tU(2n)=30$ the printed bound is $e^{-37.5}\approx5.18\times10^{-17}$, while the probability is $1.85\times10^{-16}$, $1.22\times10^{-14}$ and $3.05\times10^{-14}$ at $n=10^{20},10^{75},10^{200}$. The bound holds with denominator $2+tU(2n)$.

## Chapter 6 — The Entropy Method

**6.4 — wrong set (statement).** With the printed $A=\{x\in[0,1]^n:\sum_ix_i\le n/2\}$, $A$ is convex, so $f=d(\cdot,A)$ is convex and the claim fails: on $\{0,1\}^n$, $f(x)=(\sum_ix_i-n/2)_+/\sqrt{\sum_ix_i}$, and $\mathbb{P}\{f>\frac12n^{1/4}\}$ is $0.0060$ at $n=100$ and $1.1\times10^{-13}$ at $n=10^4$, nowhere near $1/4$. The example needs the discrete set $A=\{0,1\}^n\cap\{\sum_ix_i\le n/2\}$, for which the limiting probability is $\mathbb{P}\{N(0,1)>1/2\}\approx0.309>1/4$.

**6.8 — missing hypothesis (statement).** The Harris step needs $f$ nondecreasing in each coordinate, and without it the bound is false: $n=1$, $\mathbb{P}\{X=0\}=0.1$, $A=[1,\infty)$, $f=\mathbf{1}_{\{x<1\}}$, $v=10^{-9}$, $C=1$, $t=0.9-10^{-6}$ give probability $0.1$ against a bound of $0.0174$. Add "$f$ nondecreasing in each variable".

**6.9 — false as stated (statement, fourth inequality).** The first three displays are correct, but $\log\mathbb{E}e^{\lambda(Z-\mathbb{E}Z)}\le\frac{16\lambda^2}{2(1-64B\lambda)}\mathbb{E}[Y^2]$ fails: for $\mathcal{T}=\{c(J-I)\}$, $n=1000$, $c=10^{-9}$, $\lambda=0.6/(cn)$, the left side is $24.77$ and the right side $2.88$, with $64B\lambda\approx3.8\times10^{-5}$. Corrected: $\log\mathbb{E}e^{\lambda(Z-\mathbb{E}Z)}\le\frac{8\lambda^2}{2(1-8\sqrt B\lambda)}\mathbb{E}[Y^2]$ for $0\le\lambda<1/(8\sqrt B)$; the scale is $\sqrt B$, not $B$.

**6.13 — missing hypotheses (statement).** The scaled Fisher information ignores mass across gaps in the support: $\mathbb{P}\{X=0\}=0.9$, $\mathbb{P}\{X=10\}=0.1$ gives $K(X)=1$ but $D(X\,\|\,\mathrm{Poisson}(1))=2.185>1$. The final bound also needs Bernoulli summands: $\mathbb{P}\{X_1=0,1,2\}=0.9,0.01,0.09$ gives $D=0.2103>p_1^2/(1-p_1)=0.0446$. Assume gap-free supports, and $X_i\sim\mathrm{Bernoulli}(p_i)$ for the last claim.

**6.14 — false as stated (statement, lower bound).** With $\sigma^2=p(1-p)$ ($p\in(0,1)$ fixed), $x=\sqrt{2\sigma^2n\log n}$ and $\delta_n=a_n\sqrt{\sigma^2n/\log n}$, the lower half of the claim fails whenever $a_n=o(\log\log n)$ (e.g. $a_n=\log\log\log n$): a sharp binomial tail bound plus the union bound give $\mathbb{P}\{D\ge np+x-\delta_n\}\to0$, which reflects the unavoidable Gumbel $\log\log n$ correction. The upper half holds for every $a_n\to\infty$, and the lower half holds for $a_n\gg\log\log n$ (second-moment method).

**6.15 — missing hypothesis (statement).** $p\ge1/n$ is not enough; $p$ must be bounded away from $1$: at $p=1$, $Z=\binom n3=\mathbb{E}Z$ a.s., so the left side is $0$ and the right side $1$. The planted-clique argument proves the bound for $1/n\le p\le1/(2K)$ with $K=3+\lceil(1+6a)^{1/3}\rceil$ and $c=K^2+1$.

## Chapter 7 — Concentration and Isoperimetry

**7.2 — false as stated (statement).** $\beta(t)\ge\alpha(t/2)$ fails: on the uniform two-point space with $d(0,1)=1$, $\beta(t)=\frac12\mathbf{1}\{t\le1/2\}$ satisfies the hypothesis but $\beta(1)=0<1/2=\alpha(1/2)$. The correct relation is $\alpha(2t)\le\beta(t)$.

**7.17 — missing hypothesis $t\ge0$ (statement).** For $X_i\sim\mathrm{Bernoulli}(0.02)$, $n=10^4$ ($\mu=200$): at $t=-100$, $\mathbb{P}\{S\ge300\}\approx1.62\times10^{-11}>5.18\times10^{-17}$, and at $t=-25$, $3.85\times10^{-29}>3.16\times10^{-29}$. The bound holds for all $t\ge0$.

## Chapter 8 — The Transportation Method

**8.2 — false range of $t$ (statement).** The bound $\mathbb{P}\{Z<\mathbb{E}Z-t\}\le\exp\bigl(-(t-1)^2/(8\sum_i\mathbb{E}X_i^2)\bigr)$ of Example 8.9 is stated for all $t>0$ but can fail for $t<1$: for $n=10$, $X_i\sim\mathrm{Bernoulli}(0.01)$, $Z=\sum_iX_i$, at $t=0.05$ the probability is $0.99^{10}\approx0.9044$ against a bound of $\approx0.3236$. The transportation argument gives the bound for $t\ge1$ (at $t=1$ it is trivial).

**8.4 — false hint (sign).** $|X-Y|=X+Y-2\max(X,Y)$ is false (at $(3,5)$ it gives $-2$); it should read $|X-Y|=2\max(X,Y)-X-Y=X+Y-2\min(X,Y)$. The statement is correct.

## Chapter 9 — Influences and Threshold Phenomena

**9.3 — false hint (inverted ratio).** The last hint display has denominator $1+\log\frac{\|g_i\|_1}{\|g_i\|_2}$, which is negative once the ratio is below $1/e$ (ratio $0.3$: $\approx-0.204$), making the bound negative. It should read $1+\log\frac{\|g_i\|_2}{\|g_i\|_1}$; then $C=9/10$ follows.

## Chapter 10 — Isoperimetry on the Hypercube and Gaussian Spaces

**10.1 — false as stated (statement: infimum over the wrong interval).** The bound uses $\inf_{q\in(1/2,1-\varepsilon)}P_q(\partial_V(A))$, but the window need not lie in that interval, and an infimum goes the wrong way: for $A=\{\text{some }x_i=1\}$, $n=20$, $\varepsilon=1/4$, the width $p_{3/4}-p_{1/2}\approx0.0329$ exceeds the right side $\approx1.1\times10^{-10}$ (inner boundary; $1.8\times10^{-12}$ outer), and even a sup over the printed interval gives only $3.8\times10^{-5}$. Via Corollary 10.10 the bound holds with $\sup_{q\in(p_{1/2},p_{1-\varepsilon})}$ and constant $\pi\log2/e$; whether the printed constant $\log2$ suffices with the $\sup$ is open.

**10.6 — false as stated (statement).** Absolute continuity is not enough ($P$ uniform on $[0,1]$, $A=(-1/2,1/2)$: $P(A_t)=\min(1/2+t,1)$ has a kink at $t=1/2$), and even Gaussian $P$ fails for $n=1$: for $A=(-1,1)\cup(3,5)$, $F'(1^-)\approx0.1620$ but $F'(1^+)\approx0.0540$. The claim holds for $n\ge2$ and $P$ with a continuous density.

**10.11 — false as stated (statement: pointwise limit).** $\|\nabla f_{t,\sigma}\|\to1/t$ fails at some points of $A_t\setminus A$: for $A=B(0,1)\cup B(10e_1,1)$, $t=6$, $x=5e_1$, symmetry forces $\nabla f_{t,\sigma}(x)=0$ for every $\sigma$. The limit holds almost everywhere, which is all the dominated-convergence step needs.

## Chapter 11 — The Variance of Suprema of Empirical Processes

**11.15 — false for $n=1$ (statement).** With $n=1$ the left side is $\sqrt{2/\pi}\,\|v_1\|\approx0.798\,\|v_1\|>0$ while $\sqrt{2\log1}=0$. The printed bound holds for all $n\ge2$, and $\sqrt{2\log(2n)}$ works for all $n\ge1$.

## Chapter 12 — Suprema of Empirical Processes: Exponential Inequalities

**12.1 — wrong exponent (hint).** The hint's second step, with $e^{-2n\varepsilon^2}$, is false: for a single set with $P(A)=1/2$, $n=450$, $\varepsilon=0.1$, the exact probability is $0.00299>2e^{-9}\approx2.47\times10^{-4}$. The argument gives $e^{-n\varepsilon^2/2}$, which is what the main bound uses; the statement is correct.

**12.3 — wrong threshold (hint).** The printed bound $e^{-n\varepsilon^2/2}$ is true, but symmetrizing at threshold $\varepsilon$ as hinted yields only $e^{-n\varepsilon^2/4}$ (the per-trace swap probability can exceed $e^{-n\varepsilon^2/2}$: $11/1024\approx0.0107>e^{-5}$ at $n=10$, $\varepsilon=1$). Symmetrize at threshold $\sqrt2\varepsilon$.

**12.7 — missing factor $1/\lambda$ (hint) and missing range $\lambda\ge0$ (statement).** The hint's shift should be $c_i=\lambda^{-1}\log(M/M_i)$: as printed, $\mathbb{E}e^{\lambda\tilde Z_i}=M^\lambda M_i^{1-\lambda}\ne M$ ($M=2$, $M_i=1.5$, $\lambda=0.5$: $1.732\ne2$). The claim also fails for $\lambda<0$: with $\mathcal{T}=\{1,2\}$, $X_i$ uniform on $\{(1,-\tfrac12),(-\tfrac12,1),(-\tfrac12,-\tfrac12)\}$, $n=2$ and $\lambda=-0.1$, the left side is $-0.03153>-0.04746$; it holds for all $\lambda\ge0$.

**12.13 — false second-moment bound (statement).** The bound on $\mathbb{E}M^2$ ignores the lower tail: $X_i\equiv-100$, $n=2$, $\mu=0$, $v=c=1$ gives $\mathbb{E}M^2=10000$ against $\approx28.16$; it holds for $M_+$ (with $\mu\ge0$). Under the tail-form hypothesis used by the parenthetical and the hint, the mgf bound needs an extra factor $\sum_j1/j^2\le\pi^2/6$ (with $v=\mu=0$, $c=1$, $n=2$, centered truncations of $\mathrm{Exp}(1)$ approach $\log\mathbb{E}e^{\lambda M}=0.0150629>0.0150505$ at $\lambda=0.01$); under the literal mgf hypothesis this is unresolved.

**12.14 — wrong range (statement) and misplaced indicator (hint).** The range $0\le\lambda\le\tau_n/2$ should be $0\le\lambda\le1/(2\tau_n)$: for $\tau_n>\sqrt2$ the printed range contains $\lambda\ge1/\tau_n$, where $1-\lambda\tau_n\le0$ (for standard Gaussian $X_i$ the printed right side is then negative while $\log\mathbb{E}e^{\lambda Z}\ge0$). In the hint the indicator must sit inside the exponential; as written the bound tends to $n\log(1/n)<0$ as $\lambda\to0$.

## Chapter 13 — The Expected Value of Suprema of Empirical Processes

**13.1 — missing base-scale term (statement).** For $S=\{s_0,s_1\}$ with $X_{s_1}-X_{s_0}\sim N(0,v\delta^2)$ ($a=c=0$), $e_n(S)=0$ for $n\ge1$, so the right side is $0$, while $\mathbb{E}[\sup_sX_s-X_{s_0}]=\sqrt v\,\delta/\sqrt{2\pi}\approx0.399\sqrt v\,\delta$. Add a term $\delta(\sqrt v+c)$ (start both sums at $n=0$ with $e_0(S)=\delta$).

**13.6 — wrong constant (statement).** At $|\mathcal{T}|=2$, $\mathbb{E}\max(X_1,X_2)=1/\sqrt\pi\approx0.564<\frac1{\sqrt2}\sqrt{\log2}\approx0.589$. The rate is right: $\mathbb{E}\max_sX_s\ge\frac14\sqrt{\log|\mathcal{T}|}$ for all $|\mathcal{T}|\ge2$.

**13.9 — per-link threshold too small (hint).** For a link of length $3\delta_{j+1}$ the hinted threshold $\delta_{j+1}(3ua+2\sqrt{uvL}+cuL)$ does not give $e^{-uL}$ (Gaussian increment, $uL=9$: $0.0228$ against $e^{-9}\approx1.2\times10^{-4}$). Use $3\delta_{j+1}(a+\sqrt{2uvL}+cuL)$; the statement is true.

**13.10 — no universal $\kappa$ (statement).** $\mathbb{P}\{Z\ge uE\}\le\kappa e^{-u}$ fails: for $\mathcal{T}=\{0,M\}$, $M=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$, $E=1.5257$, $e^u\,\mathbb{P}\{Z\ge uE\}=0.588,1.44,11.3,933,8.8\times10^6$ at $u=5,10,20,40,80$. A factor $K\ge1.31$ in front of $E$ is necessary; $\mathbb{P}\{Z\ge137uE\}\le1.42e^{-u}$ holds.

**13.11 — misplaced $V$ (statement).** The right side turns negative once $V\delta^2>2\kappa$ (all subsets of a $10$-point set, $V=10$, $\delta=1$, $\kappa=2$: $20\log0.4\approx-18.3$, while $H(1,\mathcal{T})\ge\log2$). Remove $V$ from inside the logarithm: $H(\delta,\mathcal{T})\le\frac{\kappa}{\kappa-1}V\log(4e\kappa/\delta^2)$.

**13.12 — wrong constant and false self-bounding claim (statement).** $\mathrm{dens}\le V/2$ is false: thresholds ($V=1$) give a path with density $n/(n+1)$; the correct bound is $\mathrm{dens}\le V(1-1/|\mathrm{tr}(x)|)<V$, asymptotically tight. $Z=\mathrm{dens}$ is not self-bounding: for $S=\{000,001,011,110,111\}$, $Z=0.8$ but the leave-one-out values are $1,1,0.667$, and changing one sample point can lower the density by $1.5$.

**13.15 — missing $n$–$\sigma$ condition (statement) and false first display (hint).** No bound uniform in $n$ holds: intervals $[a,a+\sigma^2)$ with $n=1$ give $\mathbb{E}Z^+\ge1-\sigma^2$, while $\sigma\sqrt{\psi(\sigma/2)}=0.0522$ at $\sigma=10^{-2}$. With $\psi\ge1$ (harmless once $\mathcal{T}$ has two distinct sets), the bound holds when $n\sigma^2\ge\psi(\sigma/2)$, and in general reads $K(\sigma\sqrt{\psi(\sigma/2)}+\psi(\sigma/2)/\sqrt n)$. The hint's first display is false as printed ($n=10^6$, $\sigma=0.1$: $\mathbb{E}Z^+=0.0397$ against $0.00501K$, and the ratio is unbounded as $\sigma\to0$): $\sqrt{\sigma^2+\mathbb{E}Z^+/\sqrt n}$ belongs in the upper limit of the integral.

**13.16 — missing $n$–$\sigma$ condition (statement).** The 13.15 counterexample applies verbatim (indicators are $[0,1]$-valued): with $n=1$, $\mathbb{E}Z^+\ge1-\sigma^2$ against $\sigma\sqrt{\psi(\sigma/2)}=0.0522$ at $\sigma=10^{-2}$. With $\psi\ge1$ as in 13.15, the bound holds under $n\sigma^2\ge\psi(\sigma/2)$; the hint's bound on $\mathbb{E}\delta_n^2$ is neither proved nor refuted.

**13.17 — garbled entropy hypothesis and missing $n$ in the proviso (statement).** With $\psi$ nonincreasing as printed, the hypothesis forces every class to be finite in each $L_2(Q)$; it should read $\psi$ nondecreasing and regularly varying at $\infty$ with index $<2$. Even then the proviso must involve $n$: for $f_a=b\mathbf{1}_{[a,a+p]}$, $\sigma=b^{1/10}$, $p=b^{-9/5}$ (printed proviso holds for $b\ge4.31\times10^7$), $n=1$, $b=10^{12}$, $\mathbb{E}Z\approx10^{12}$ against $\sigma\sqrt{\psi}\approx114.0$, a ratio of about $8.8\times10^9$; the corrected proviso is $\sqrt n\,\sigma\ge b\sqrt{\psi(\kappa\|g\|/\sigma)}$.

**13.27 — not sub-linear in the book's sense (statement).** Under the definition on p. 388 ($\psi(1)\ge1$, continuity), $\psi^*$ can fail both: $X_{1,s}=\pm\varepsilon$ gives $\psi^*(1)=\varepsilon/2<1$, and a countable class of sparse $\pm1$ variables gives $\psi^*(0)=0$ but $\psi^*(r)\ge1$ for every $r>0$ (no-hit probabilities $0.0996,0.00996,0.000996$ at $S=10^4,10^6,10^8$). What holds: $\psi^*$ is nondecreasing, subadditive, $\psi^*(r)/r$ nonincreasing, and $\tilde\psi(r)+r$ is sub-linear, where $\tilde\psi=\psi^*$ except $\tilde\psi(0)=\psi^*(0+)$.

**13.31 — wrong logarithm and missing $\sigma^2$ (statement).** The expectation bound $2\sqrt{2\log d}\,\sigma$ is false for $d=1$ ($X_1=\pm1$, $A_1=1$: $\mathbb{E}Z=1$, right side $0$); it should read $\log(2d)$. The tail must be $e^{-t^2/(8\sigma^2)}$, not $e^{-t^2/8}$ (scaling).

**13.37 — missing proviso (statement).** Read literally for all $n$, the variance bound is false: $m=\lfloor1/\sigma^2\rfloor$ disjoint sets of mass $\sigma^2$ ($V=1$) with $n=1$ give $\mathrm{Var}(Z)\approx0.2325$ while the bound tends to $0$ (ratio $1.04$ to $82.4$ for $\sigma=0.1$ to $0.001$; with $n=\sigma$ the ratio is $0.92$ to $10.3$, growing like $\sigma^{-1/2}$). It is correct if "the notation of Theorem 13.7" imports that theorem's proviso $n\gtrsim V\log(e/\sigma)/\sigma^2$; $n\sigma^2\ge V\log(e/\sigma)$ suffices.

**13.38 — missing $1/n$ and incomplete basis (statement and hint).** $P_n([0,x])=\sum_i\mathbf{1}_{\{X_i\le x\}}$ lacks the factor $1/n$. The hinted identity is false: $\{\sqrt2\sin(2\pi ix)\}$ is not complete in $L^2[0,1]$ and $\int_0^1(F_n(x)-x)\,dx=\frac12-\bar X_n\ne0$ a.s.; with the complete system $\sqrt2\sin(\pi ix)$ the identity holds by Parseval.

**13.39 — missing normalization (statement).** With $P_n([0,x])$ as printed in 13.38 (no $1/n$), for $n\ge2$ the integrand is $(n-x)^2/(x(1-x))$ beyond $\max_iX_i$, not integrable at $1$, so $Z=\infty$ a.s. and $\mathbb{E}Z^2=1$ fails. With $F_n=\frac1n\sum_i\mathbf{1}_{\{X_i\le x\}}$ it holds.

**13.40 — false exact inequality (statement).** $\mathbb{E}Z\le\sqrt{2\log\log n}$ fails: at $n=16$ an exact enumeration gives $\mathbb{E}Z\ge1.44118>1.42813=\sqrt{2\log\log16}$, and the Gumbel limit makes it fail for all large $n$. What holds is $\mathbb{E}Z\le\sqrt{2\log\log n}\,(1+o(1))$.

**13.42 — missing hypothesis (statement).** The fixed point $r_*$ controls $\psi\circ\rho$, not $\rho$: with $n=a=b=1$, $c=0$, $\psi(s)=\min(s,\sqrt s)$, $\rho(r)=100r$, $r_*=10^{2/3}$ but $u^2\approx10200>2(a^2+b^2)r_*^2\approx86.2$. The bound holds if $\psi(t)\ge t$ for all $t\ge0$ (then $a\ge1$ is not needed).

## Chapter 14 — $\Phi$-Entropies

**14.1 — missing hypothesis (in Theorem 14.7).** "$\tilde Z\le\min_iZ_i$" does not give the first inequality: $n=1$, $X_1\in\{0,10\}$ equally likely, $Z=X_1$, $Z_1\equiv\tilde Z\equiv5$, $\eta(z)=e^{-z}$, $\Phi(x)=x\log x$ gives $H_\Phi(\eta(Z))\approx0.346$ against $\frac12\cdot25e^{-5}\approx0.084$. $\tilde Z$ must also lie below $Z$: $\tilde Z\le\min(Z,Z_1,\dots,Z_n)$.

## Chapter 15 — Moment Inequalities

**15.9 — missing hypothesis (statement).** The inequality needs $\mathbb{E}Z\ge0$: $Z\equiv-1$, $\sigma^2=2$, $\theta=t=1$, $\lambda=1/2$ makes the deviation $0$, so the left side is $1$ while the right side is $e^{-1/8}\vee e^{-3/28}\approx0.898$. Add $\mathbb{E}Z\ge0$ (true in Adamczak's setting, $Z\ge0$).

## Unresolved

**13.33 — Bennett at scale 1 for non-identical summands.** The variance hypothesis is fine (Klein–Rio, Corollary 1.1), but whether the printed Bennett-type bound holds with scale factor $1$ when the summands are not identically distributed is open: the book itself notes (Section 12.5) that Bousquet's inequality needs identically distributed summands. The solution proves the variance bound and the i.i.d. exponential bounds and marks this case **Status: incomplete**.

## Reference slips (minor)

Wrong theorem, lemma or section numbers; not counted above.

- **2.18, 2.20** — the hint cites "Theorem 2.4"; should be Theorem 2.5 (the maximal inequality).
- **5.19** — cites "Theorem 5.16" (5.16 is a corollary); should be Theorem 5.18.
- **5.20** — calls its result "the exact Gaussian analog of Theorem 5.16"; no Theorem 5.16 exists (the intended target is presumably the §5.8 hypercube relation behind Corollary 5.17 and Theorem 5.18).
- **5.20, 5.22** — "Section 5.9" for the Hermite polynomials; should be Section 5.10.
- **11.4, 11.6** — cite Theorem 11.4; should be Lemma 11.4.
- **11.7** — the hint cites Lemma 10.1, which gives only $\gamma'$, $\gamma\gamma''=-1$ and the convexity of $(\gamma')^2$; the two-sided bounds needed are Lemma 10.3, which at $x=1/t$ yields both printed bounds exactly.
- **12.13** — cites Theorem 2.6; should be Corollary 2.6.
- **13.5** — cites Theorem 13.2; should be Corollary 13.2.
- **13.9** — cites Theorem 13.1; should be Lemma 13.1.
- **13.13** — cites Theorem 13.6; should be Lemma 13.6.
- **13.18** — cites Theorem 11.4; should be Lemma 11.4.
- **13.43** — cites Lemma 11.5; should be Theorem 11.5.
