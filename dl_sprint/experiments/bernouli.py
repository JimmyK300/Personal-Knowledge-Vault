import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100)

p = 0.3
n = 1000

samples = np.random.binomial(1, p, n)
running_mean = np.cumsum(samples) / np.arange(1, n + 1)

plt.plot(running_mean)
plt.axhline(p)
plt.title("Running Mean (LLN)")
plt.show()

n = 100
trials = 10000

means = np.mean(np.random.binomial(1, p, (trials, n)), axis=1)

print("Empirical mean:", means.mean())
print("Empirical variance:", means.var())
print("Theoretical variance:", p*(1-p)/n)

standardized = (means - p) / np.sqrt(p*(1-p)/n)

plt.hist(standardized, bins=40, density=True)
plt.title("Standardized Sample Means (CLT)")
plt.show()