---
layout: default
title: Implicit Hypothesis Testing and Divergence Preservation in Neural Network Representations
---

# Implicit Hypothesis Testing and Divergence Preservation in Neural Network Representations
**arXiv**：[2601.20477v1](https://arxiv.org/abs/2601.20477) · [PDF](https://arxiv.org/pdf/2601.20477.pdf)  
**作者**：Kadircan Aksoy, Peter Jung, Protim Bhattacharjee  

**一句话要点**：提出基于二元假设检验的神经网络表示分析框架，以解释监督训练动态与泛化性能。

**关键词**：神经网络表示, 假设检验, KL散度, 监督训练, 泛化性能, 正则化策略

## 3 点简述
- 核心问题：研究神经网络分类器在监督训练中的表示动态与泛化机制。
- 方法要点：将分类建模为类条件分布间的二元假设检验，分析KL散度单调改进与Neyman-Pearson最优决策规则的对齐。
- 实验或效果：实证显示泛化良好的网络沿训练轨迹逐渐优化错误率指数，并讨论对训练或正则化策略的启示。

## 摘要（原文）

> We study the supervised training dynamics of neural classifiers through the lens of binary hypothesis testing. We model classification as a set of binary tests between class-conditional distributions of representations and empirically show that, along training trajectories, well-generalizing networks increasingly align with Neyman-Pearson optimal decision rules via monotonic improvements in KL divergence that relate to error rate exponents. We finally discuss how this yields an explanation and possible training or regularization strategies for different classes of neural networks.

