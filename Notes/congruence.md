# Congruence

## Definition

$$
a \equiv b \pmod m
$$

means

$$
m \mid (a-b)
$$

Equivalently, there exists an integer $k$ such that

$$
a-b = km
$$

## Addition Rule

If

$$
a \equiv b \pmod m
$$

and

$$
c \equiv d \pmod m
$$

then

$$
a+c \equiv b+d \pmod m
$$

### Proof

From the definition, there exist integers $k$ and $l$ such that

$$
a-b = km, \qquad c-d = lm
$$

Add the two equations:

$$
(a-b) + (c-d) = km + lm = (k+l)m
$$

So

$$
(a+c) - (b+d) = (k+l)m
$$

Hence

$$
m \mid ((a+c) - (b+d))
$$

Therefore,

$$
a+c \equiv b+d \pmod m
$$

## Multiplication Rule

If

$$
a \equiv b \pmod m
$$

and

$$
c \equiv d \pmod m
$$

then

$$
ac \equiv bd \pmod m
$$

### Proof

From the definition, there exist integers $k$ and $l$ such that

$$
a-b = km, \qquad c-d = lm
$$

So

$$
a = b + km, \qquad c = d + lm
$$

Substitute into $ac$:

$$
ac = (b+km)(d+lm)
$$

Expand:

$$
ac = bd + blm + dkm + klm^2
$$

Factor out $m$ from the extra terms:

$$
ac = bd + m(bl + dk + klm)
$$

Thus

$$
ac - bd = m(bl + dk + klm)
$$

Hence

$$
m \mid (ac-bd)
$$

Therefore,

$$
ac \equiv bd \pmod m
$$

## A Divisibility Result Modulo 5

If $n-1$, $n$, and $n+1$ are not divisible by $5$, then

$$
5 \mid (n^2 + 1)
$$

### Proof

Among the five consecutive integers

$$
n-2, \quad n-1, \quad n, \quad n+1, \quad n+2
$$

exactly one is divisible by $5$.

Since $n-1$, $n$, and $n+1$ are not divisible by $5$, it follows that either $n-2$ or $n+2$ is divisible by $5$. Hence

$$
(n-2)(n+2) \equiv 0 \pmod 5
$$

But

$$
(n-2)(n+2) = n^2 - 4
$$

so

$$
n^2 - 4 \equiv 0 \pmod 5
$$

Therefore

$$
n^2 \equiv 4 \pmod 5
$$

and thus

$$
n^2 + 1 \equiv 5 \equiv 0 \pmod 5
$$

Hence

$$
5 \mid (n^2 + 1)
$$
