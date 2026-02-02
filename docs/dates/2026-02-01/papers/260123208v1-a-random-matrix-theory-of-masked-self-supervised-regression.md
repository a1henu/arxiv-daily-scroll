---
layout: default
title: A Random Matrix Theory of Masked Self-Supervised Regression
---

# A Random Matrix Theory of Masked Self-Supervised Regression
**arXiv**：[2601.23208v1](https://arxiv.org/abs/2601.23208) · [PDF](https://arxiv.org/pdf/2601.23208.pdf)  
**作者**：Arie Wortsman Zurich, Federica Gerace, Bruno Loureiro, Yue M. Lu  

**一句话要点**：提出随机矩阵理论分析掩码自监督回归，揭示其在高维比例机制下的泛化误差与谱结构。

**关键词**：随机矩阵理论, 掩码自监督学习, 高维分析, 泛化误差, 谱结构, 尖峰协方差模型

## 3 点简述
- 核心问题：掩码自监督学习产生矩阵值预测器，其坐标间条件依赖关系带来分析挑战。
- 方法要点：在样本数与维度成比例的高维机制下，推导泛化误差显式表达式并表征预测器谱结构。
- 实验或效果：在尖峰协方差模型中，预测器经历BBP型相变，显示掩码SSL优于PCA的结构化机制。

## 摘要（原文）

> In the era of transformer models, masked self-supervised learning (SSL) has become a foundational training paradigm. A defining feature of masked SSL is that training aggregates predictions across many masking patterns, giving rise to a joint, matrix-valued predictor rather than a single vector-valued estimator. This object encodes how coordinates condition on one another and poses new analytical challenges. We develop a precise high-dimensional analysis of masked modeling objectives in the proportional regime where the number of samples scales with the ambient dimension. Our results provide explicit expressions for the generalization error and characterize the spectral structure of the learned predictor, revealing how masked modeling extracts structure from data. For spiked covariance models, we show that the joint predictor undergoes a Baik--Ben Arous--Péché (BBP)-type phase transition, identifying when masked SSL begins to recover latent signals. Finally, we identify structured regimes in which masked self-supervised learning provably outperforms PCA, highlighting potential advantages of SSL objectives over classical unsupervised methods

