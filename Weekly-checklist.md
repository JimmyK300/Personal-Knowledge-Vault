# Week 1 — Linear Algebra + Optimization Foundations

Goal: Understand what the network is _computing_ and how parameters move.

---

## 1. Vectors & Geometry (Day 1)

You must understand:

- Vector as point vs direction
    
- Dot product  
    [  
    x \cdot w = \sum_i x_i w_i  
    ]
    
- Norms (L1, L2)
    
- Angle & cosine similarity
    

Why it matters:  
A neuron is just:  
[  
z = w \cdot x + b  
]

Deliverable:

- Compute dot product manually
    
- Visualize 2D linear classifier decision boundary
    

---

## 2. Matrix Multiplication & Shapes (Day 2)

Topics:

- Matrix multiplication rules
    
- Shape reasoning
    
- Batch dimension intuition
    
- Transpose
    

You must be able to answer instantly:

If:

- X ∈ ℝ^(batch × features)
    
- W ∈ ℝ^(features × hidden)
    

Then:  
Output ∈ ℝ^(batch × hidden)

If you cannot reason shapes fast, debugging CNN later becomes painful.

Deliverable:

- Implement matrix multiplication manually (small case)
    
- Write shape reasoning examples
    

---

## 3. Eigenvalues & Why They Matter (Day 3)

You don’t need full spectral theory.

You must understand:

- Definition:  
    [  
    Av = \lambda v  
    ]
    
- Intuition: scaling directions
    
- Why large eigenvalues cause instability in optimization
    

Connection:  
Learning rate must relate to curvature.

Deliverable:

- Compute eigenvalues of 2×2 matrix
    
- Explain in 1 page:  
    “Why curvature affects gradient descent stability”
    

---

## 4. Derivatives & Gradients (Day 4)

Topics:

- Derivative of:
    
    - x²
        
    - sigmoid
        
    - softmax (basic idea)
        
- Partial derivatives
    
- Gradient vector
    

Understand:  
Gradient = direction of steepest ascent.

Deliverable:

- Derive gradient of MSE for linear regression
    
- Verify with finite differences (numerically)
    

---

## 5. Gradient Descent (Day 5–6)

Topics:

- Update rule:  
    [  
    \theta \leftarrow \theta - \eta \nabla L(\theta)  
    ]
    
- Learning rate effect
    
- Convex vs non-convex
    
- Loss surface intuition
    

Critical:  
Explain why too large η causes divergence.

Deliverable:

- Implement gradient descent for linear regression
    
- Plot:
    
    - Convergence for small η
        
    - Divergence for large η
        

---

# Week 2 — Probability + Backpropagation

Goal: Understand generalization and error behavior.

---

## 1. Random Variables & Expectation (Day 1)

Topics:

- Discrete vs continuous
    
- Expectation:  
    [  
    \mathbb{E}[X]  
    ]
    
- Variance:  
    [  
    Var(X)  
    ]
    

Why:  
Test accuracy is a random variable.

Deliverable:

- Simulate random variable in code
    
- Show empirical mean converges
    

---

## 2. Bias–Variance Decomposition (Day 2)

Understand:

Error = Bias² + Variance + Noise

Conceptually, not full formal proof.

Explain:

- High bias → underfitting
    
- High variance → overfitting
    

Deliverable:  
1-page explanation using your own words.

---

## 3. Cross-Entropy & Logistic Regression (Day 3)

Topics:

- Sigmoid function
    
- Log-loss
    
- Why cross-entropy works better than MSE for classification
    

Derive gradient of logistic regression.

Deliverable:

- Implement logistic regression from scratch
    
- Compare with MSE classification
    

---

## 4. Chain Rule & Backpropagation (Day 4–5)

Core concept:

If:  
[  
L = f(g(h(x)))  
]

Then:  
[  
\frac{dL}{dx} = \frac{dL}{df} \cdot \frac{df}{dg} \cdot \frac{dg}{dh} \cdot \frac{dh}{dx}  
]

You must derive backprop for:

1 hidden layer network:

- Forward pass
    
- Compute loss
    
- Backward pass manually
    

Deliverable:

- Write full gradient expressions
    
- Implement 1 hidden layer MLP from scratch (NumPy)
    

No PyTorch yet.

---

## 5. Capacity & Overparameterization (Conceptual)

Understand:

- Parameters count vs data size
    
- Why bigger model fits noise
    
- Double descent (conceptually)
    

Write:  
Short memo:  
“Why deeper networks can memorize small datasets.”

---

# What You Should Be Able To Do After 2 Weeks

After 2 weeks, I will be able to derive and implement a 1-hidden-layer neural network without using deep learning libraries.