import numpy as np

x = 0
def f(x): return x**4-3*x**2
learn_rate = 0.01
step = 100

def numerical_grad(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2*h)
  
def gradient_descent(f, grad, x0, lr, steps):
    x = x0
    history = []
    for _ in range(steps):
        x = x - lr * grad(f, x)
        history.append(x)
    return x, history

x, history = gradient_descent(f, numerical_grad, x, learn_rate, step)
for i in history:
  print(i)

behavior = abs(1-numerical_grad(f, 1)*learn_rate)

if behavior > 1:
  print('explodes')
elif behavior > 0.99:
  print('oscillates')
else:
  print('converges')
print(behavior)
print(x)