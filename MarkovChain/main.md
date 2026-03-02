# Markov Chains — Spectral Structure Notes

## 1. Transition Matrix

Let

$$
P =
\begin{pmatrix}
0.99 & 0.01 \\
0.01 & 0.99
\end{pmatrix}
$$

This is a stochastic matrix since:

$$
\sum_j P_{ij} = 1
$$

---

## 2. Stationary Distribution

A stationary distribution satisfies:

$$
\pi P = \pi
$$

For this symmetric chain:

$$
\pi = (0.5, 0.5)
$$

---

## 3. Spectral Decomposition

If the eigenvalues are:

$$
\lambda_1 = 1, \quad \lambda_2 = 0.98
$$

Then any initial distribution can be written as:

$$
v = \pi + c_2 v_2
$$

After $k$ steps:

$$
P^k v = \pi + c_2 \lambda_2^k v_2
$$

Since:

$$
|\lambda_2| < 1
$$

we get convergence:

$$
P^k v \to \pi
$$

---

## 4. Periodic Example

Consider:

$$
P =
\begin{pmatrix}
0 & 1 \\
1 & 0
\end{pmatrix}
$$

Eigenvalues:

$$
1, \quad -1
$$

Here:

$$
|\lambda_2| = 1
$$

So:

$$
P^k v = c_1 v_1 + c_2 (-1)^k v_2
$$

The second term does not decay.

No convergence.

---

## 5. Period 3 Structure

If the chain has period $d = 3$, then eigenvalues on the unit circle are:

$$
e^{2\pi i k / 3}, \quad k=0,1,2
$$

Explicitly:

$$
1
$$

$$
-\frac{1}{2} + i\frac{\sqrt{3}}{2}
$$

$$
-\frac{1}{2} - i\frac{\sqrt{3}}{2}
$$

These are spaced $120^\circ$ apart on the unit circle.

---

## 6. Spectral Gap

The spectral gap is:

$$
\text{gap} = 1 - |\lambda_2|
$$

- Large gap → fast mixing  
- Small gap → slow mixing  
- Zero gap → no convergence  

---

End of test document.