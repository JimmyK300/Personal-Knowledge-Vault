import numpy as np
import matplotlib.pyplot as plt

def loss(y, p):
  return -(1/len(y))*np.sum(y*np.log(p) + (1-y)*np.log(1-p))

def sigmoid(z):
  return 1/(1+np.exp(-z))

lr = 0.01

# Each iteration:

# Forward
# Z = Xᵀw + b
# P = sigmoid(Z)

# Compute loss

# Backward
# dW = (1/n) Xᵀ (P − Y)
# dB = (1/n) sum(P − Y)

# Update
# w = w − lr * dW
# b = b − lr * dB
# Repeat.

# we define a set of input, lets say 30. define a set of outputs, lets say 10
# 
# row*col*col*1 res should be row10*col1

n = 30      # samples
d = 10      # features
X = np.random.randn(n, d)
Y = np.random.randint(0, 2, size=(n, 1))

w = np.random.randn(d, 1)
b = 0.0

L = []

for epoch in range(1000):
  Z =  np.array(X) @ np.array(w) + b

  P = sigmoid(Z)

  P = np.clip(P, 1e-8, 1-1e-8)
  L.append(loss(Y, P))

  dW = 1/n * np.array(X).T @ (P-Y)
  dB = 1/n * np.sum(P - Y)

  w -= lr * dW
  b -= lr * dB

Z = X @ w + b
P = sigmoid(Z)

pred = (P >= 0.5).astype(int)

accuracy = np.mean(pred == Y)

print("Final loss:", L[-1])
print("Accuracy:", accuracy)

plt.plot(L)
plt.yscale('log')
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss")
plt.show()