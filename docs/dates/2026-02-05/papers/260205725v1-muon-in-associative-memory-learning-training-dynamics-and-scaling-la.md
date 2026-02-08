---
layout: default
title: Muon in Associative Memory Learning: Training Dynamics and Scaling Laws
---

# Muon in Associative Memory Learning: Training Dynamics and Scaling Laws
**arXiv**：[2602.05725v1](https://arxiv.org/abs/2602.05725) · [PDF](https://arxiv.org/pdf/2602.05725.pdf)  
**作者**：Binghui Li, Kaifei Wang, Han Zhong, Pinyan Lu, Liwei Wang  

**一句话要点**：在关联记忆模型中分析Muon优化器的训练动态与缩放定律，证明其优于梯度下降。

**关键词**：优化算法, 训练动态, 缩放定律, 关联记忆模型, 矩阵梯度符号

## 3 点简述
- 研究Muon优化器在带软最大检索的线性关联记忆模型中的理论动态与缩放行为。
- Muon通过矩阵梯度符号更新参数，缓解频率学习不平衡，实现指数级加速和更均匀的收敛。
- 实验在合成长尾分类和LLaMA风格预训练中验证理论，并解释Muon为隐式矩阵预处理器。

## 摘要（原文）

> Muon updates matrix parameters via the matrix sign of the gradient and has shown strong empirical gains, yet its dynamics and scaling behavior remain unclear in theory. We study Muon in a linear associative memory model with softmax retrieval and a hierarchical frequency spectrum over query-answer pairs, with and without label noise. In this setting, we show that Gradient Descent (GD) learns frequency components at highly imbalanced rates, leading to slow convergence bottlenecked by low-frequency components. In contrast, the Muon optimizer mitigates this imbalance, leading to faster and more uniform progress. Specifically, in the noiseless case, Muon achieves an exponential speedup over GD; in the noisy case with a power-decay frequency spectrum, we derive Muon's optimization scaling law and demonstrate its superior scaling efficiency over GD. Furthermore, we show that Muon can be interpreted as an implicit matrix preconditioner arising from adaptive task alignment and block-symmetric gradient structure. In contrast, the preconditioner with coordinate-wise sign operator could match Muon under oracle access to unknown task representations, which is infeasible for SignGD in practice. Experiments on synthetic long-tail classification and LLaMA-style pre-training corroborate the theory.

