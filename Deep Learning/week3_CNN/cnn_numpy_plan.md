


conv:
X = (batch, in_channels, H_in, W_in) # already inited
X_pad = np.pad(X, ((0,0),(0,0),(P,P),(P,P)), mode="constant")
out_tensor = np.zeros((batch, out_channels, H_out, W_out))

for b in range(batch):
  for out in range(out_channels):
    for i in range(H_out):
      for j in range(W_out):
        for inc in range(in_channels):
          out_tensor[b, out, i, j] +=np.sum(X_pad[b, inc, s * i:s * i+k, s * j:s * j+k] * W[out, inc])

maxpool loop:

for b in range(batch):
  for c in range(channels):
    for i in range(H_out):
      for j in range(W_out):
        out_tensor[b, c, i, j] = np.max(X[b, c, s * i:s * i + k,s * j:s * j + k])

batch norm:

X_hat = (X-mean)/np.sqrt(var+epsilon)
out = gamma * X_hat + beta

relu(X):
return np.maximum(0, X)


flatten:
X.reshape(batch, -1)


linear:
z = X @ W + b


softmax:
m = np.maximum(X)
np.exp(X-m)/np.sum(np.exp(X-m))

cross entropy loss:
np.sum(np.log(1-X)*X)

how to store intermediate values for backprop

class SimpleCNN(batch, ):
  def __init__:
    conv1w
    conv2w

    self.fw1 = np.zeros()
    fw2...

  def conv
  def bn
  def relu
  def flatten
  def mp
  def sfmx
  def linear
  def fwp
  def bckprp
  def update
  def train
  def 






# Essential Requirements

You will need to implement these components:

### 1. Data

Dataset:

* MNIST

Tasks:

* load images `(28×28)`
* normalize
* convert labels → one-hot
* batching

Input tensor format:

```
(batch, channels, height, width)
```

For MNIST:

```
(batch, 1, 28, 28)
```

---

# 2. Layers You Listed

Your list is mostly correct:

**Convolution stack**

```
Conv2D
BatchNorm
ReLU
MaxPool
Conv2D
BatchNorm
ReLU
MaxPool
```

**Classifier**

```
Flatten
Linear
ReLU
Linear
Softmax
```

---

# 3. What You Must Implement Manually

For a true "from scratch" implementation:

### Forward operations

* Conv2D
* MaxPool
* BatchNorm
* ReLU
* Linear
* Softmax

### Backward operations

You must compute gradients for:

* conv weights
* batchnorm parameters
* linear weights
* input tensors

---

# 4. Parameter Storage

You need to store:

```
conv1_W
conv1_b

conv2_W
conv2_b

bn1_gamma
bn1_beta

bn2_gamma
bn2_beta

fc1_W
fc1_b

fc2_W
fc2_b
```

And running stats for batchnorm:

```
running_mean
running_var
```

---

# 5. Training Components

Also required:

* cross-entropy loss
* gradient computation
* SGD update step
* training loop
* evaluation loop

---

# 6. Typical Architecture for MNIST

A simple one:

```
Input      (1,28,28)

Conv1      (8 filters)
ReLU
MaxPool

Conv2      (16 filters)
ReLU
MaxPool

Flatten

FC1        128
ReLU

FC2        10
Softmax
```

---

# Critical Missing Detail (You Didn't Mention)

You must decide **how convolution is implemented**:

Two common choices:

1️⃣ **naive sliding loops**

```
for batch
 for filter
  for height
   for width
```

2️⃣ **im2col + matrix multiplication**

This is **10–100× faster** but more complex.

For learning purposes, you probably want:

```
naive loops
```