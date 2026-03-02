Input dimension: 3
Hidden layer: 8 units
Output: 1 unit (binary classification)
Activation: ReLU (hidden), Sigmoid (output)
Loss: Binary cross-entropy
suppose not batch -> input (X1) = 3x1 (feature * sample)
W1 = (sample * hidden) 8x3
b1 = 8x1
z1 = 8x1
a1 = 8x1
W2 = (output * hidden) 1x8
z2 = 1x1
b2 = 1x1
yh = 1x1

def ReLU(z):
  return np.maximum(0, z)

def sigmoid(z):
  return 1/(1+np.exp(-z))
  // remember that this is a matrix, so find function in python that does it matrix wise (i think numpy.array with keepdims=true)
THIS IS WRITEN IN COLUMN FORM, BECAREFUL
z1 = W1 @ X1 + b1
a1 = ReLU(z1)
z2 = W2 @ a1 + b2
yh = sigmoid(z2)

∂L​/∂z2 = y'-y = d2
​∂L​/∂W2​ = d2 @ a1.T
​∂L​/∂a1 = ReLU'(z1) -> returns 1 if > 0; else return 0
​∂L​/∂z1 = W2.T @ d2 . ReLU'(z1) (element wise)
​∂L​/∂W1 = a2.T @ d2