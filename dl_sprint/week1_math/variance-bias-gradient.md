variance: how much something spreads
Variance: Var(X)=E[(X−E[X])^2]

Properties:
Linear scaling: Var(aX+b)=a^2*Var(X)

Covariance: It is still a little confusing to me exactly what it measures
Cov(X,Y)=E[(X−E[X])(Y−E[Y])]
Practical form: Cov(X,Y)=E[XY]−E[X]E[Y]
Key insight: independence ⇒ covariance = 0.

Bias-Variance decomposistion
Start from prediction error: E[(f(x)+ε−f^(x))2]

There are **two uncertainties** inside this expectation:

1. **Data noise** ε
    
2. **Model randomness** (training variation across datasets)
    

If you trained on infinitely many datasets, would f^​(x) always be identical?  
No → therefore f^​(x) is a random variable.

Decompose:

f^(x)=E[f^(x)]+(f^(x)−E[f^(x)])

This splits into:

- **Bias**: E[f^(x)]−f(x)
    
- **Variance**: Var(f^(x))
    
- **Noise**: Var(ε)
    

After expansion, expected error becomes:

Bias^2+Variance+Noise

Your confusion about y vs f′:

- True target: y=f(x)+ε
    
- Model: f^(x)
    

They are linked through expectation over:

- data distribution
    
- dataset sampling
    
- training randomness


# C. Optimization & Learning Rate Dynamics

Gradient for logistic regression:

L=−[ylog⁡(y^)+(1−y)log⁡(1−y^)]

With:

y^=σ(z)
z=wTx+b

Gradient:

dL/dw=(y^−y)x

---

### Learning Rate Hypothesis

> “We should maximize learning rate (0.99999)”

Reality:

- Large LR → faster initial progress
    
- Too large → oscillation
    
- Even larger → divergence
    

Optimal LR is near the stability boundary of Hessian curvature.

You’re intuitively sensing the **spectral radius condition**:

η<2/λmax(H)

So: push high, but within curvature limits.