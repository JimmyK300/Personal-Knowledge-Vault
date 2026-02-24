# 60-Day Deep Learning Foundation Plan

(6–8 hrs/day, structured)

---

# PHASE 1 (Days 1–20)

### Optimization + Logistic → Geometry First

## Primary Text

* Convex Optimization (selected sections only)
* Deep Learning (Ch. 4–6 carefully)

## Objectives

1. Understand convexity geometrically.
2. Derive logistic regression fully.
3. Understand conditioning.
4. Visualize gradient descent dynamics.

## Daily Structure

**Deep (4 hrs):**

* Matrix calculus
* Gradient derivations
* Convex sets & functions
* Hessian intuition

**Light (2 hrs):**

* Implement experiments
* Plot surfaces
* Compare optimizers

## Deliverables

* Logistic regression from scratch (vectorized)
* 3D loss surface visualizer
* Conditioning experiment
* SGD vs Momentum vs Adam comparison

If you cannot explain why conditioning affects convergence, don’t move on.

---

# PHASE 2 (Days 21–40)

### Backprop + Representation Learning

## Primary Text

* Deep Learning (Ch. 6–8 deeply)
* Matrix Calculus for Deep Learning

## Objectives

1. Derive full backprop manually.
2. Understand vanishing/exploding gradients.
3. Study initialization schemes.
4. Study regularization (L2, dropout).

## Experiments

* 2-layer MLP on MNIST (no autograd first)
* Initialization comparison
* Gradient norm tracking across layers
* Batch size vs noise experiment

Deliverable:
Write a 5–8 page technical report explaining gradient flow behavior in your network.

---

# PHASE 3 (Days 41–60)

### Transformers & Scaling Foundations

## Primary Text

* Attention Is All You Need
* Scaling Laws for Neural Language Models

Supplement:

* The Principles of Deep Learning Theory (selected theory intuition)

## Objectives

1. Implement minimal transformer block.
2. Understand attention as weighted projection.
3. Study scaling law implications.
4. Study parameter vs data tradeoff.

## Experiments

* Tiny transformer on toy sequence task
* Measure scaling vs performance
* Compare depth vs width tradeoff

Deliverable:
Write your own explanation of why transformers scale well.

---

# Weekly Structure (Non-Negotiable)

* 5 days heavy build
* 1 day consolidation + rewrite notes
* 1 day light reading + reflection

Sleep properly. Insight requires consolidation.

---

# How We Use AI Properly

You:

1. Derive first.
2. Implement.
3. Get stuck.
4. Bring me:

   * Your derivation
   * Your reasoning
   * Your failure mode

I critique.
Not replace thinking.

---

# What This 60 Days Produces

If executed seriously:

* You will think in gradients.
* You will visualize curvature.
* You will understand why scaling works.
* You will stop being intimidated by papers.

You won’t be “frontier,”
but you’ll have research-grade foundation.
