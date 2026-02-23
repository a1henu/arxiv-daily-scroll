---
layout: default
title: JPmHC Dynamical Isometry via Orthogonal Hyper-Connections
---

# JPmHC Dynamical Isometry via Orthogonal Hyper-Connections
**arXiv**：[2602.18308v1](https://arxiv.org/abs/2602.18308) · [PDF](https://arxiv.org/pdf/2602.18308.pdf)  
**作者**：Biswa Sengupta, Jinhua Wang, Leo Brunswic  

**一句话要点**：提出JPmHC框架以解决超连接中训练不稳定和内存开销问题

**关键词**：超连接, 梯度条件控制, 算子范数流形, 隐式微分, 正交混合器, 深度学习稳定性

## 3 点简述
- 超连接扩展残差连接但破坏恒等映射，导致训练不稳定和内存开销增加
- JPmHC使用可训练线性混合器替代恒等跳跃，通过算子范数有界流形约束梯度条件
- 在ARC-AGI上实验显示JPmHC实现更快收敛、更高精度和更低计算成本

## 摘要（原文）

> Recent advances in deep learning, exemplified by Hyper-Connections (HC), have expanded the residual connection paradigm by introducing wider residual streams and diverse connectivity patterns. While these innovations yield significant performance gains, they compromise the identity mapping property of residual connections, leading to training instability, limited scalability, and increased memory overhead. To address these challenges, we propose JPmHC (Jacobian-spectrum Preserving manifold-constrained Hyper-Connections), a framework that replaces identity skips with a trainable linear mixer acting on n parallel streams while explicitly controlling gradient conditioning. By constraining the mixer M on operator-norm-bounded manifolds (e.g., bistochastic, Stiefel, Grassmann), JPmHC prevents gradient pathologies and enhances stability. JPmHC introduces three key contributions: (i) a free-probability analysis that predicts Jacobian spectra for structured skips, providing actionable design rules for mixer selection; (ii) memory-efficient implicit differentiation for fixed-point projections, reducing activation memory and synchronization overhead; and (iii) a Stiefel-constrained mixer via Cayley transforms, ensuring orthogonality without post-hoc normalization. Empirical evaluations on ARC-AGI demonstrate that JPmHC achieves faster convergence, higher accuracy, and lower computational cost compared to bistochastic baselines. As a flexible and scalable extension of HC, JPmHC advances spectrum-aware, stable, and efficient deep learning, offering insights into topological architecture design and foundational model evolution.

