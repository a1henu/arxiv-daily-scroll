---
layout: default
title: Information Geometry of Absorbing Markov-Chain and Discriminative Random Walks
---

# Information Geometry of Absorbing Markov-Chain and Discriminative Random Walks
**arXiv**：[2602.08185v1](https://arxiv.org/abs/2602.08185) · [PDF](https://arxiv.org/pdf/2602.08185.pdf)  
**作者**：Masanari Kimura  

**一句话要点**：提出基于信息几何的判别随机游走理论框架，用于半监督节点分类与模型分析。

**关键词**：信息几何, 判别随机游走, 半监督节点分类, 吸收马尔可夫链, Fisher信息, 模型敏感性

## 3 点简述
- 核心问题：判别随机游走理论基础不完整，缺乏几何解释。
- 方法要点：将吸收马尔可夫链的击中时间分布建模为统计流形，推导闭式表达式与Fisher信息。
- 实验或效果：引入敏感度分数，支持主动标签获取、边重加权和解释性应用。

## 摘要（原文）

> Discriminative Random Walks (DRWs) are a simple yet powerful tool for semi-supervised node classification, but their theoretical foundations remain fragmentary. We revisit DRWs through the lens of information geometry, treating the family of class-specific hitting-time laws on an absorbing Markov chain as a statistical manifold. Starting from a log-linear edge-weight model, we derive closed-form expressions for the hitting-time probability mass function, its full moment hierarchy, and the observed Fisher information. The Fisher matrix of each seed node turns out to be rank-one, taking the quotient by its null space yields a low-dimensional, globally flat manifold that captures all identifiable directions of the model. Leveraging the geometry, we introduce a sensitivity score for unlabeled nodes that bounds, and in one-dimensional cases attains, the maximal first-order change in DRW betweenness under unit Fisher perturbations. The score can lead to principled strategies for active label acquisition, edge re-weighting, and explanation.

