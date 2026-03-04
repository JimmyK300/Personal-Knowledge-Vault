# Markdown + MathJax Stress Test

## Inline Math

Eigenvalue: $\lambda_2^k \to 0$

Spectral gap: $\text{gap} = 1 - |\lambda_2|$

Complex root: $e^{2\pi i k / 3}$

---

## Display Math

$$
P^k v = \pi + \sum_{i=2}^{n} c_i \lambda_i^k v_i
$$

---

## Large Matrix

$$
P =
\begin{pmatrix}
0.99 & 0.01 & 0 & 0 \\
0.01 & 0.98 & 0.01 & 0 \\
0 & 0.02 & 0.95 & 0.03 \\
0 & 0 & 0.04 & 0.96
\end{pmatrix}
$$

---

## Aligned Equations

$$
\begin{aligned}
P^k v
&= \pi + \sum_{i=2}^{n} c_i \lambda_i^k v_i \\
&\to \pi \quad \text{as } k \to \infty
\end{aligned}
$$

---

## Cases

$$
f(x) =
\begin{cases}
x^2 & x \ge 0 \\
-x & x < 0
\end{cases}
$$

---

## Nested Fractions

$$
\frac{1}{1 + \frac{1}{1 + \frac{1}{1+x}}}
$$

---

## Limits

$$
\lim_{k \to \infty} P^k = \mathbf{1} \pi
$$

---

## Determinant

$$
\det(P - \lambda I) = 0
$$

---

## Complex Exponentials

$$
e^{i\theta} = \cos \theta + i \sin \theta
$$

---

## Roots of Unity

$$
\lambda_k = e^{2\pi i k / d}, \quad k=0,\dots,d-1
$$

---

## Bold + Calligraphic

$$
\mathcal{L}(f) = \mathbb{E}_\pi[f(X)]
$$

$$
\mathbf{P}^k \mathbf{v}
$$

---

## Large Operators

$$
\prod_{i=1}^{n} (1 - \lambda_i)
$$

---

## Text Inside Math

$$
\text{If } |\lambda_2| < 1, \text{ then convergence holds.}
$$

---

## Intentional Edge Case

$$
\begin{pmatrix}
1 & 2 \\
3 & 4
$$

$$
\require{physics}
\dv{x} x^2
$$

(This should fail — missing \end{pmatrix})

---
