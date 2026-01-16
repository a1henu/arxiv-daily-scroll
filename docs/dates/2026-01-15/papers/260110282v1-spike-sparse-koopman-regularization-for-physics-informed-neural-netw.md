---
layout: default
title: SPIKE: Sparse Koopman Regularization for Physics-Informed Neural Networks
---

# SPIKE: Sparse Koopman Regularization for Physics-Informed Neural Networks
**arXiv**：[2601.10282v1](https://arxiv.org/abs/2601.10282) · [PDF](https://arxiv.org/pdf/2601.10282.pdf)  
**作者**：Jose Marie Antonio Minoza  

**一句话要点**：提出SPIKE框架，通过稀疏Koopman正则化增强PINNs，以解决物理信息神经网络在时空外推中的泛化问题。

**关键词**：物理信息神经网络, Koopman算子, 稀疏正则化, 微分方程求解, 泛化能力, 连续时间模型

## 3 点简述
- PINNs在训练域内易过拟合，导致时空外推时泛化能力差。
- SPIKE利用连续时间Koopman算子学习稀疏动态表示，通过L1正则化强制线性动力学。
- 实验涵盖多种PDE和ODE，显示在时间外推、空间泛化和长期预测精度上一致提升。

## 摘要（原文）

> Physics-Informed Neural Networks (PINNs) provide a mesh-free approach for solving differential equations by embedding physical constraints into neural network training. However, PINNs tend to overfit within the training domain, leading to poor generalization when extrapolating beyond trained spatiotemporal regions. This work presents SPIKE (Sparse Physics-Informed Koopman-Enhanced), a framework that regularizes PINNs with continuous-time Koopman operators to learn parsimonious dynamics representations. By enforcing linear dynamics $dz/dt = Az$ in a learned observable space, both PIKE (without explicit sparsity) and SPIKE (with L1 regularization on $A$) learn sparse generator matrices, embodying the parsimony principle that complex dynamics admit low-dimensional structure. Experiments across parabolic, hyperbolic, dispersive, and stiff PDEs, including fluid dynamics (Navier-Stokes) and chaotic ODEs (Lorenz), demonstrate consistent improvements in temporal extrapolation, spatial generalization, and long-term prediction accuracy. The continuous-time formulation with matrix exponential integration provides unconditional stability for stiff systems while avoiding diagonal dominance issues inherent in discrete-time Koopman operators.

