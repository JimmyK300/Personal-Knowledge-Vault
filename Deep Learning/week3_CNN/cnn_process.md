# CNN Checkpoint

## Core Takeaways

From this CNN exercise, the important things learned are:

1. Convolution mechanics
   - kernels
   - filters
   - feature maps
   - spatial locality

2. Representation hierarchy

```text
pixels
-> edges
-> strokes
-> digit parts
-> class
```

3. Training dynamics
   - backpropagation
   - cross-entropy
   - optimizer behavior

4. Model inspection
   - filter visualization
   - feature maps
   - internal representations

## Convolution Process

A 2D kernel is the basic spatial pattern detector.

A filter is a stack of kernels across the input channels, with shape:

```text
(channels, kernel_height, kernel_width)
```

For one convolution layer:

1. Add padding `P` around the input if needed.
2. Slide the filter across the input with stride `S`.
3. At each location:
   - take the local patch
   - do element-wise multiplication with the filter across all channels
   - sum everything into one scalar
   - add the bias
4. Repeat for every spatial location and every filter.

The output shape is:

```text
(num_filters,
 floor((H_in - K + 2P) / S) + 1,
 floor((W_in - K + 2P) / S) + 1)
```

## What Matters Next

The next useful step is to move beyond implementing CNNs and study the broader deep learning system.

### 1. Optimization

Understand why training works:

- SGD vs Adam
- momentum
- learning rate schedules
- curvature and Hessian intuition

### 2. Generalization

Understand why large models can still generalize:

- bias-variance
- overparameterization
- double descent
- implicit regularization of SGD

### 3. Representation Learning

Understand what deep networks actually learn:

- manifolds
- latent space
- feature reuse
- hierarchical representations

### 4. Modern Vision Architectures

CNNs are foundational, but modern vision systems also rely on:

- ResNet
- Vision Transformer (ViT)
- ConvNeXt

ResNet is a strong next topic because it explains how deeper networks train effectively.

## Self-Check

You should be able to answer these clearly:

1. Why does convolution improve sample efficiency?
2. Why do deeper layers learn more abstract features?
3. Why does SGD find good minima in large parameter spaces?
4. Why can overparameterization help generalization?
