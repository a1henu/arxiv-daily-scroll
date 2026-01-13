---
layout: default
title: Multi-environment Invariance Learning with Missing Data
---

# Multi-environment Invariance Learning with Missing Data
**arXiv**：[2601.07247v1](https://arxiv.org/abs/2601.07247) · [PDF](https://arxiv.org/pdf/2601.07247.pdf)  
**作者**：Yiran Jia  

**一句话要点**：提出缺失数据下的多环境不变性学习估计器，以提升因果解释与鲁棒预测

**关键词**：领域泛化, 不变性学习, 缺失数据, 因果推断, 鲁棒预测, 非渐近分析

## 3 点简述
- 核心问题：领域泛化中，环境间缺失结果数据阻碍不变性学习，影响模型利用异质性
- 方法要点：从不变性目标推导缺失数据下的估计器，提供变量选择与误差收敛的非渐近保证
- 实验或效果：通过模拟和UCI Bike Sharing数据集验证，估计器在合理偏差范围内高效且降低预测误差

## 摘要（原文）

> Learning models that can handle distribution shifts is a key challenge in domain generalization. Invariance learning, an approach that focuses on identifying features invariant across environments, improves model generalization by capturing stable relationships, which may represent causal effects when the data distribution is encoded within a structural equation model (SEM) and satisfies modularity conditions. This has led to a growing body of work that builds on invariance learning, leveraging the inherent heterogeneity across environments to develop methods that provide causal explanations while enhancing robust prediction. However, in many practical scenarios, obtaining complete outcome data from each environment is challenging due to the high cost or complexity of data collection. This limitation in available data hinders the development of models that fully leverage environmental heterogeneity, making it crucial to address missing outcomes to improve both causal insights and robust prediction. In this work, we derive an estimator from the invariance objective under missing outcomes. We establish non-asymptotic guarantees on variable selection property and $\ell_2$ error convergence rates, which are influenced by the proportion of missing data and the quality of imputation models across environments. We evaluate the performance of the new estimator through extensive simulations and demonstrate its application using the UCI Bike Sharing dataset to predict the count of bike rentals. The results show that despite relying on a biased imputation model, the estimator is efficient and achieves lower prediction error, provided the bias is within a reasonable range.

