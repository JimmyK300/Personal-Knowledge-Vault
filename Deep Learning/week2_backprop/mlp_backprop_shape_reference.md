# 1-Hidden-Layer MLP Backprop Shape Reference

Use one convention and keep it fixed.

This note uses NumPy-friendly row-batch form.

## Setup

- Batch size: B
- Input dimension: D
- Hidden dimension: H
- Output dimension: 1

## Shapes

- X: (B, D)
- Y: (B, 1)
- W1: (D, H)
- b1: (1, H)
- Z1: (B, H)
- A1: (B, H)
- W2: (H, 1)
- b2: (1, 1)
- Z2: (B, 1)
- P: (B, 1)

## Forward Pass

```python
Z1 = X @ W1 + b1
A1 = np.maximum(0, Z1)
Z2 = A1 @ W2 + b2
P = 1 / (1 + np.exp(-Z2))
```

## Loss

For binary cross-entropy:

```python
loss = -(1 / B) * np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))
```

Clip `P` if needed before `log`.

## Backward Pass

For sigmoid + binary cross-entropy, the output gradient simplifies to:

```python
dZ2 = P - Y
```

Then:

```python
dW2 = (A1.T @ dZ2) / B
db2 = np.sum(dZ2, axis=0, keepdims=True) / B

dA1 = dZ2 @ W2.T
dZ1 = dA1 * (Z1 > 0)

dW1 = (X.T @ dZ1) / B
db1 = np.sum(dZ1, axis=0, keepdims=True) / B
```

## Why The Transposes Appear

- `dW2` must have the same shape as `W2`, which is `(H, 1)`.
- `A1` is `(B, H)` and `dZ2` is `(B, 1)`.
- To combine batch contributions and get `(H, 1)`, use `A1.T @ dZ2`.
- `dA1` must have shape `(B, H)` because it is the gradient flowing back into the hidden activations.
- `dZ2` is `(B, 1)` and `W2.T` is `(1, H)`, so `dZ2 @ W2.T` gives `(B, H)`.
- `dW1` must match `W1`, which is `(D, H)`, so use `X.T @ dZ1`.

Rule: the weight gradient always has the same shape as the weight it updates.

## Mental Model

- Forward: data moves left to right.
- Backward: gradient moves right to left.
- Transpose appears when you need to line up dimensions so the gradient matches the parameter shape.
- Bias gradient is a sum across the batch because the same bias is shared by every sample.

## Common Confusion Traps

- Do not switch between row-batch and column-vector notation in the same derivation.
- If forward is `X @ W1`, then `W1` is `(D, H)`, not `(H, D)`.
- `dZ2 = P - Y` is for sigmoid + binary cross-entropy. Do not re-derive a more complicated form unless you need to.
- `db1` and `db2` come from summing over samples, not from another matrix multiply.

## Quick Check

If these shapes are true, the derivation is probably consistent:

- `X @ W1 -> (B, H)`
- `A1 @ W2 -> (B, 1)`
- `A1.T @ dZ2 -> (H, 1)`
- `X.T @ dZ1 -> (D, H)`

If one line breaks shape consistency, stop there and fix that line before continuing.
