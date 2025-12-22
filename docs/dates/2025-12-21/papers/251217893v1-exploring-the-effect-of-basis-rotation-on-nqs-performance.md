---
layout: default
title: Exploring the Effect of Basis Rotation on NQS Performance
---

# Exploring the Effect of Basis Rotation on NQS Performance
**arXiv**：[2512.17893v1](https://arxiv.org/abs/2512.17893) · [PDF](https://arxiv.org/pdf/2512.17893.pdf)  
**作者**：Sven Benjamin Kožić, Vinko Zlatić, Fabio Franchini, Salvatore Marco Giampaolo  

**一句话要点**：提出基于可解旋转伊辛模型的框架，揭示浅层神经量子态优化中的信息几何障碍

**关键词**：神经量子态, 基旋转, 损失景观, 量子自然梯度, 伊辛模型, 信息几何

## 3 点简述
- 核心问题：神经量子态性能受基选择影响，但机制不明，需理解优化障碍。
- 方法要点：使用可解一维伊辛模型，通过局部基旋转分析损失景观中目标波函数位置变化。
- 实验或效果：计算量子费舍信息等，发现浅层架构易陷入鞍点区域，导致系数分布错误。

## 摘要（原文）

> Neural Quantum States (NQS) use neural networks to represent wavefunctions of quantum many-body systems, but their performance depends on the choice of basis, yet the underlying mechanism remains poorly understood. We use a fully solvable one-dimensional Ising model to show that local basis rotations leave the loss landscape unchanged while relocating the exact wavefunction in parameter space, effectively increasing its geometric distance from typical initializations. By sweeping a rotation angle, we compute quantum Fisher information and Fubini-Study distances to quantify how the rotated wavefunction moves within the loss landscape. Shallow architectures (with focus on Restricted Boltzmann Machines (RBMs)) trained with quantum natural gradient are more likely to fall into saddle-point regions depending on the rotation angle: they achieve low energy error but fail to reproduce correct coefficient distributions. In the ferromagnetic case, near-degenerate eigenstates create high-curvature barriers that trap optimization at intermediate fidelities. We introduce a framework based on an analytically solvable rotated Ising model to investigate how relocating the target wavefunction within a fixed loss landscape exposes information-geometric barriers,such as saddle points and high-curvature regions,that hinder shallow NQS optimization, underscoring the need for landscape-aware model design in variational training.

