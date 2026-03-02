import numpy as np

# CONSTS and decisions
# single sample training, XOR sample classification (all 4 XOR example)
FEATURE = 2 # feature
OUTPUT = 1 # output
BATCH = 1 # samples
INPUT_SHAPE = (FEATURE, BATCH)
OUTPUT_SHAPE = (OUTPUT, BATCH)
HIDDEN_DIM = 4
EPOCHS = 10000
LEARNING_RATE = 0.1


class XOR_DATASET:
  @staticmethod
  def xor_inp():
    return np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

  @staticmethod
  def xor_out():
    return np.array([[0], [1], [1], [0]])


# Main traing process
def relu(z):
  return np.maximum(0, z)
  
def sigmoid(z):
  return 1/(1+np.exp(-z))

def calc_loss(y, p):
  # −[ylog(p)+(1−y)log(1−p)]
  # *remember to divide using 1/n
  p = np.clip(p, 1e-15, 1 - 1e-15)
  return -(y*np.log(p)+(1-y)*np.log(1-p))

def d_relu(z):
  return(z > 0).astype(int)

def forward_pass(X, W1, b1, W2, b2):
  z1 = X @ W1 + b1
  a1 = relu(z1)
  z2 = a1 @ W2 + b2
  p = sigmoid(z2)
  
  return p

def train_step(X, y, W1, b1, W2, b2, lr):
  # 1. Forward
  z1 = X @ W1 + b1
  a1 = relu(z1)
  z2 = a1 @ W2 + b2
  p = sigmoid(z2)
  
  # 2. Calculate loss
  loss = calc_loss(y, p).mean()
  
  # 3. Backprop
  N = X.shape[0]
  d2 = p - y
  dW2 = (a1.T @ d2) / N
  d1 = d2 @ W2.T * d_relu(z1)
  dW1 = (X.T @ d1) / N
  db1 = np.sum(d1, axis=0, keepdims=True) / N
  db2 = np.sum(d2, axis=0, keepdims=True) / N
  
  # 4. Update
  W1 -= lr*dW1
  b1 -= lr*db1
  W2 -= lr *dW2
  b2 -= lr*db2
  
  return W1, b1, W2, b2, loss


# Init
rng = np.random.default_rng()
# Generate [0, 1), multiply by 0.1 to get [0, 0.1), then add 0.1 to get [0.1, 0.2)
W1 = rng.normal(0, 0.5, (FEATURE, HIDDEN_DIM))   
W2 = rng.normal(0, 0.5, (HIDDEN_DIM, OUTPUT))   

b1 = np.zeros((1, HIDDEN_DIM)) 
b2 = np.zeros((1, OUTPUT))     

X = XOR_DATASET.xor_inp()
y = XOR_DATASET.xor_out()

# tot_loss = []

# Training
for i in range(EPOCHS):
  epoch_loss = 0
  W1, b1, W2, b2, loss = train_step(X, y, W1, b1, W2, b2, LEARNING_RATE)
  # tot_loss.append(loss/len(X))
  epoch_loss += loss
  if i % 1000 == 0:
    print("LOSS AT STEP", i, ":", epoch_loss)


# Evaluate
print("\nEvaluation:")
for j, x_sample in enumerate(X):
  y_sample = y[j]
  
  p = forward_pass(x_sample, W1, b1, W2, b2)
  pred = (p > 0.5).astype(int)
  
  print("Input:", x_sample,
    "Target:", int(y_sample),
    "Prob:", float(p),
    "Pred:", int(pred))