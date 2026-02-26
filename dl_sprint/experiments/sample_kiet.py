from mnist import MNIST
import numpy as np
import matplotlib.pyplot as plt
from tqdm import trange

mndata = MNIST('samples')
images, labels = mndata.load_training()

samples = 60000
features = 28*28
classes = 10

epochs = 50
batch = 64
lr = 0.5

X = np.array(images[0:samples])/255.                    # (samples, feature)
y = np.zeros((samples,classes))                         # (samples, classes)
y[np.arange(samples), labels[:samples]] = 1             # this is a numpy thing, not a python thing

w = np.random.random((classes, features))               # (classes, feature)
b = np.random.random((1,classes))                       # (1, classes)

h = X @ w.T + b
h -= np.max(h, axis=1, keepdims=True)

p = np.exp(h)
p /= np.sum(p, axis=1, keepdims=True)
L = -np.mean(np.log(p[np.arange(samples), labels[:samples]] + 1e-9))

L_list = [L]
for epoch in trange(epochs, desc= "Training"):
    idx = np.random.permutation(samples)
    X_shuf = X[idx]                             
    y_shuf = y[idx]                             
    for i in range(0, samples, batch):
        x_b = X_shuf[i: i + batch]                      # (batch, feature)
        y_b = y_shuf[i: i + batch]                      # (batch, classes)

        # normal regression
        h = x_b @ w.T + b                               # remeber broadcasting works from the right
        h_shifted = h - np.max(h, axis=1, keepdims=True)# (batch, classes)

        # soft max to get the expected probability
        p = np.exp(h_shifted)                           # (batch, classes)
        p = p/np.sum(p, axis = 1, keepdims=True)        # np.sum returns a (samples, 1) matrix

        dw = (p - y_b).T @ x_b / batch                  # CxB @ BxF
        db = np.mean(p - y_b, axis = 0, keepdims= True)

        w -= lr*dw
        b -= lr*db

    h = X @ w.T + b
    h -= np.max(h, axis=1, keepdims=True)

    p = np.exp(h)
    p /= np.sum(p, axis=1, keepdims=True)
    L = -np.mean(np.log(p[np.arange(samples), labels[:samples]] + 1e-9))
    L_list.append(L)

with open("weights.txt", "w") as f:
    for i in range(classes):
        for j in range(features):
            print(w[i, j],end=" ", file = f)
        print(file = f)
with open("bias.txt", "w") as f:
    for i in range(classes):
        print(b[0,i], end=" ", file = f)

print(L_list)