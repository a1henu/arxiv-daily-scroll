---
layout: default
title: Adaptive sampling using variational autoencoder and reinforcement learning
---

# Adaptive sampling using variational autoencoder and reinforcement learning
**arXiv**：[2512.03525v1](https://arxiv.org/abs/2512.03525) · [PDF](https://arxiv.org/pdf/2512.03525.pdf)  
**作者**：Adil Rasheed, Mikael Aleksander Jansen Shahly, Muhammad Faisal Aftab  

**一句话要点**：提出结合变分自编码器与强化学习的自适应稀疏感知框架，以优化压缩感知中的采样策略。

**关键词**：自适应采样, 变分自编码器, 强化学习, 压缩感知, 稀疏重建

## 3 点简述
- 压缩感知依赖通用基和随机测量，效率与重建质量受限。
- 方法结合变分自编码器先验与强化学习，实现序列化自适应采样。
- 实验显示，该方法在稀疏测量下优于传统压缩感知、最优传感器放置和生成模型方法。

## 摘要（原文）

> Compressed sensing enables sparse sampling but relies on generic bases and random measurements, limiting efficiency and reconstruction quality. Optimal sensor placement uses historcal data to design tailored sampling patterns, yet its fixed, linear bases cannot adapt to nonlinear or sample-specific variations. Generative model-based compressed sensing improves reconstruction using deep generative priors but still employs suboptimal random sampling. We propose an adaptive sparse sensing framework that couples a variational autoencoder prior with reinforcement learning to select measurements sequentially. Experiments show that this approach outperforms CS, OSP, and Generative model-based reconstruction from sparse measurements.

