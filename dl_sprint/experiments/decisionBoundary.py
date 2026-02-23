import numpy as np
import matplotlib.pyplot as plt

# Define weights and bias
w = np.array([4, -1])
b = -2

# Generate grid
x1 = np.linspace(-5, 5, 100)
x2 = -(w[0]/w[1]) * x1 - b/w[1]

# Plot decision boundary
plt.plot(x1, x2)
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.axhline(0)
plt.axvline(0)
plt.title("Linear Decision Boundary")
plt.show()
