---
layout: default
title: Joint Optimization of Neural Autoregressors via Scoring rules
---

# Joint Optimization of Neural Autoregressors via Scoring rules
**arXiv**：[2601.05683v1](https://arxiv.org/abs/2601.05683) · [PDF](https://arxiv.org/pdf/2601.05683.pdf)  
**作者**：Jonas Landsgesell  

**一句话要点**：提出基于评分规则的神经自回归器联合优化，以解决多变量非参数分布回归中的维度灾难问题。

**关键词**：非参数分布回归, 神经自回归器, 评分规则, 多变量建模, 维度灾难

## 3 点简述
- 核心问题：非参数分布回归在多变量设置下，网格方法面临指数级复杂度增长和过拟合挑战。
- 方法要点：通过评分规则联合优化神经自回归器，避免显式高维网格，降低参数数量。
- 实验或效果：未知，但旨在提升低数据场景下的可扩展性和性能。

## 摘要（原文）

> Non-parametric distributional regression has achieved significant milestones in recent years. Among these, the Tabular Prior-Data Fitted Network (TabPFN) has demonstrated state-of-the-art performance on various benchmarks. However, a challenge remains in extending these grid-based approaches to a truly multivariate setting. In a naive non-parametric discretization with $N$ bins per dimension, the complexity of an explicit joint grid scales exponentially and the paramer count of the neural networks rise sharply. This scaling is particularly detrimental in low-data regimes, as the final projection layer would require many parameters, leading to severe overfitting and intractability.

