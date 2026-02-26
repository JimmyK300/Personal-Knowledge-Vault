input layer1 activation hidden_layer output

forward pass
compute loss
compute gradient and backprop
update
repeat

we will do mini batch this time

samples:
s = 30

batch
n = 5

feature: 
d = 10
matrix size:
x: (n * d)
w1: (d * d)
w2: (n * 1)

layer:
z1 = x @ w1 + b1
z2 = z1T @ w2 + b2

loss
def mse(y, p): return np.exp((np.subtract(y, p)), 2)

actiavtion
def ReLU(y):
  if y > 0: return y
  else: return 0

dmse -> dhl -> dRe -> dl1
lossArr = []
lr = 0.001
X = [] # 2d array with 30 subarrays, each 10 features
z1, z2 = [], [] # 2d array with corresponding row and columns (defined above)

for epoch in range(1000):
  for i in range(s//n):
    for y in X[5*i:5*i+5]:
      # compute l1
      z1 = y @ w1 + b1
      
      # activation function ( i think needs some sort of remember if j is zero?)
      for i in z1:
        for j in i:
          j = ReLU(j)
      
      # compute l2
      z2 = z1.T @ w2 + b2
      
      #compute loss
      lossArr.append(mse(z2, y))

      # derive back prop hidden layer
      dw2 = 2(y-p)*z1.T + b2*z2
      //getting a little confused