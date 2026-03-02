Linear part:

z=wTx+b

Sigmoid:

p=σ(z)=1/(1+e^−z)

Loss:

L=−[ylog(p)+(1−y)log(1−p)]

Each iteration:

Forward

Z = Xw + b

P = sigmoid(Z)

Compute loss

Backward

dW = (1/n) Xᵀ (P − Y)

dB = (1/n) sum(P − Y)

Update

w = w − lr * dW

b = b − lr * dB

Repeat.