---
layout: default
title: Transformer Is Inherently a Causal Learner
---

# Transformer Is Inherently a Causal Learner
**arXiv**：[2601.05647v1](https://arxiv.org/abs/2601.05647) · [PDF](https://arxiv.org/pdf/2601.05647.pdf)  
**作者**：Xinyue Wang, Stephen Wang, Biwei Huang  

**一句话要点**：揭示自回归训练Transformer能自然学习时间延迟因果结构，无需显式因果目标。

**关键词**：Transformer, 因果发现, 自回归训练, 梯度分析, 时间序列预测, 可解释性

## 3 点简述
- 核心问题：Transformer在自回归训练中如何编码因果结构，以提升因果发现性能。
- 方法要点：通过梯度敏感性分析，从Transformer输出中提取因果图，无需额外约束。
- 实验或效果：在非线性、长依赖等挑战下，超越现有方法，随数据异质性增强而提升。

## 摘要（原文）

> We reveal that transformers trained in an autoregressive manner naturally encode time-delayed causal structures in their learned representations. When predicting future values in multivariate time series, the gradient sensitivities of transformer outputs with respect to past inputs directly recover the underlying causal graph, without any explicit causal objectives or structural constraints. We prove this connection theoretically under standard identifiability conditions and develop a practical extraction method using aggregated gradient attributions. On challenging cases such as nonlinear dynamics, long-term dependencies, and non-stationary systems, this approach greatly surpasses the performance of state-of-the-art discovery algorithms, especially as data heterogeneity increases, exhibiting scaling potential where causal accuracy improves with data volume and heterogeneity, a property traditional methods lack. This unifying view lays the groundwork for a future paradigm where causal discovery operates through the lens of foundation models, and foundation models gain interpretability and enhancement through the lens of causality.

