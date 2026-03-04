---
layout: default
title: Layer-wise QUBO-Based Training of CNN Classifiers for Quantum Annealing
---

# Layer-wise QUBO-Based Training of CNN Classifiers for Quantum Annealing
**arXiv**：[2603.02958v1](https://arxiv.org/abs/2603.02958) · [PDF](https://arxiv.org/pdf/2603.02958.pdf)  
**作者**：Mostafa Atallah, Rebekah Herrman  

**一句话要点**：提出基于QUBO的CNN分类器分层训练方法，通过量子退火避免梯度优化，解决量子图像分类中的梯度消失和扩展性问题。

**关键词**：量子退火, QUBO优化, CNN训练, 图像分类, 梯度避免, 比特精度

## 3 点简述
- 核心问题：量子图像分类中变分量子电路存在梯度消失，量子核方法随数据集规模二次扩展。
- 方法要点：使用QUBO迭代优化CNN分类头，卷积层随机初始化冻结，将多类问题分解为独立QUBO子问题。
- 实验或效果：在多个图像分类基准测试中，高比特精度下性能匹配或超越经典SGD，为量子硬件部署建立基线。

## 摘要（原文）

> Variational quantum circuits for image classification suffer from barren plateaus, while quantum kernel methods scale quadratically with dataset size. We propose an iterative framework based on Quadratic Unconstrained Binary Optimization (QUBO) for training the classifier head of convolutional neural networks (CNNs) via quantum annealing, entirely avoiding gradient-based circuit optimization. Following the Extreme Learning Machine paradigm, convolutional filters are randomly initialized and frozen, and only the fully connected layer is optimized. At each iteration, a convex quadratic surrogate derived from the feature Gram matrix replaces the non-quadratic cross-entropy loss, yielding an iteration-stable curvature proxy. A per-output decomposition splits the $C$-class problem into $C$ independent QUBOs, each with $(d+1)K$ binary variables, where $d$ is the feature dimension and $K$ is the bit precision, so that problem size depends on the image resolution and bit precision, not on the number of training samples. We evaluate the method on six image-classification benchmarks (sklearn digits, MNIST, Fashion-MNIST, CIFAR-10, EMNIST, KMNIST). A precision study shows that accuracy improves monotonically with bit resolution, with 10 bits representing a practical minimum for effective optimization; the 15-bit formulation remains within the qubit and coupler limits of current D-Wave Advantage hardware. The 20-bit formulation matches or exceeds classical stochastic gradient descent on MNIST, Fashion-MNIST, and EMNIST, while remaining competitive on CIFAR-10 and KMNIST. All experiments use simulated annealing, establishing a baseline for direct deployment on quantum annealing hardware.

