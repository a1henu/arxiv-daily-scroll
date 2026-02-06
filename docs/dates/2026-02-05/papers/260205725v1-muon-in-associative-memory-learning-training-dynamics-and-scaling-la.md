---
layout: default
title: Muon in Associative Memory Learning: Training Dynamics and Scaling Laws
---

# Muon in Associative Memory Learning: Training Dynamics and Scaling Laws
**arXiv**：[2602.05725v1](https://arxiv.org/abs/2602.05725) · [PDF](https://arxiv.org/pdf/2602.05725.pdf)  
**作者**：Binghui Li, Kaifei Wang, Han Zhong, Pinyan Lu, Liwei Wang  

**一句话要点**：研究Muon优化器在线性联想记忆模型中的训练动态与缩放定律，揭示其优于梯度下降的收敛速度与均匀性。

**关键词**：优化算法, 训练动态, 缩放定律, 联想记忆模型, 梯度下降对比, 矩阵预处理器

## 3 点简述
- 核心问题：梯度下降在软最大检索的线性联想记忆模型中，学习频率组件不平衡，导致低频率组件收敛缓慢。
- 方法要点：Muon通过矩阵梯度符号更新参数，作为隐式矩阵预处理器，缓解学习不平衡，实现更快的均匀进展。
- 实验或效果：在无噪声和噪声情况下，Muon分别实现指数级加速和更优的缩放效率，并在合成分类和预训练中验证理论。

## 摘要（原文）

> Muon updates matrix parameters via the matrix sign of the gradient and has shown strong empirical gains, yet its dynamics and scaling behavior remain unclear in theory. We study Muon in a linear associative memory model with softmax retrieval and a hierarchical frequency spectrum over query-answer pairs, with and without label noise. In this setting, we show that Gradient Descent (GD) learns frequency components at highly imbalanced rates, leading to slow convergence bottlenecked by low-frequency components. In contrast, the Muon optimizer mitigates this imbalance, leading to faster and more uniform progress. Specifically, in the noiseless case, Muon achieves an exponential speedup over GD; in the noisy case with a power-decay frequency spectrum, we derive Muon's optimization scaling law and demonstrate its superior scaling efficiency over GD. Furthermore, we show that Muon can be interpreted as an implicit matrix preconditioner arising from adaptive task alignment and block-symmetric gradient structure. In contrast, the preconditioner with coordinate-wise sign operator could match Muon under oracle access to unknown task representations, which is infeasible for SignGD in practice. Experiments on synthetic long-tail classification and LLaMA-style pre-training corroborate the theory.

