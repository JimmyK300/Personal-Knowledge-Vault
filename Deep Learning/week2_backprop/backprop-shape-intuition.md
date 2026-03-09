# Backprop Shape Intuition

## 1. Linear Layer Forward

Forward equation:

```text
Z = A_prev W + b
```

Shapes:

```text
A_prev : (batch x in_features)
W      : (in_features x out_features)
b      : (out_features)

Z      : (batch x out_features)
```

Matrix multiplication rule:

```text
(a x b)(b x c) -> (a x c)
```

## 2. Gradient Shape Rule

Rule:

> The gradient of a variable always has the same shape as the variable.

Examples:

```text
Z  -> dZ : (batch x out_features)
W  -> dW : (in_features x out_features)
A  -> dA : (batch x features)
```

## 3. Linear Layer Backprop

Core formulas:

```text
dW = A_prev^T dZ
db = sum(dZ over batch)
dA_prev = dZ W^T
```

Shape logic:

```text
dW      : (in_features x out_features)
db      : (out_features)
dA_prev : (batch x in_features)
```

## 4. Why The Transpose Appears

Forward:

```text
Z = A_prev W
```

Shapes:

```text
(batch x in_features)(in_features x out_features)
```

To compute `dW`, we need:

```text
(in_features x out_features)
```

So we multiply:

```text
A_prev^T : (in_features x batch)
dZ       : (batch x out_features)
```

Result:

```text
(in_features x out_features)
```

## 5. Bias Gradient Rule

```text
db = sum(dZ over batch)
```

Reason:

Each example in the batch contributes to the same bias parameter, so the gradients are summed across the batch.

This removes the batch dimension.

## 6. Backprop Flow Through Layers

Flow:

```text
dZ_l
 |
+-> dW_l
+-> db_l
 |
+-> dA_{l-1}
```

Universal formulas:

```text
dW_l = A_{l-1}^T dZ_l
db_l = sum(dZ_l over batch)
dA_{l-1} = dZ_l W_l^T
```

## 7. Mental Shortcut

Rule:

```text
Parameter gradients do not depend on batch size.
```

Why:

The batch dimension sits in the middle:

```text
(in_features x batch)(batch x out_features)
```

and cancels out in the multiplication.