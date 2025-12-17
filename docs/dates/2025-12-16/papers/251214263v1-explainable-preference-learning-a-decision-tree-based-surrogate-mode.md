---
layout: default
title: Explainable Preference Learning: a Decision Tree-based Surrogate Model for Preferential Bayesian Optimization
---

# Explainable Preference Learning: a Decision Tree-based Surrogate Model for Preferential Bayesian Optimization
**arXiv**：[2512.14263v1](https://arxiv.org/abs/2512.14263) · [PDF](https://arxiv.org/pdf/2512.14263.pdf)  
**作者**：Nick Leenders, Thomas Quadt, Boris Cule, Roy Lindelauf, Herman Monsuur, Joost van Oijen, Mark Voskuijl  

**一句话要点**：提出基于决策树的解释性偏好学习模型，以提升偏好贝叶斯优化的可解释性和可扩展性。

**关键词**：偏好学习, 贝叶斯优化, 决策树模型, 可解释性, 分类数据处理, 大规模优化

## 3 点简述
- 当前偏好贝叶斯优化依赖高斯过程，存在解释性差、处理分类数据困难、计算复杂等问题。
- 引入基于决策树的替代模型，能处理分类和连续数据，并适用于大规模数据集。
- 在八个优化函数和真实Sushi数据集上实验，模型在尖峰函数上优于高斯过程，并展示利用历史数据加速优化的初步工作。

## 摘要（原文）

> Current Preferential Bayesian Optimization methods rely on Gaussian Processes (GPs) as surrogate models. These models are hard to interpret, struggle with handling categorical data, and are computationally complex, limiting their real-world usability. In this paper, we introduce an inherently interpretable decision tree-based surrogate model capable of handling both categorical and continuous data, and scalable to large datasets. Extensive numerical experiments on eight increasingly spiky optimization functions show that our model outperforms GP-based alternatives on spiky functions and has only marginally lower performance for non-spiky functions. Moreover, we apply our model to the real-world Sushi dataset and show its ability to learn an individual's sushi preferences. Finally, we show some initial work on using historical preference data to speed up the optimization process for new unseen users.

