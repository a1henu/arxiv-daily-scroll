---
layout: default
title: DAO-GP Drift Aware Online Non-Linear Regression Gaussian-Process
---

# DAO-GP Drift Aware Online Non-Linear Regression Gaussian-Process
**arXiv**：[2512.08879v1](https://arxiv.org/abs/2512.08879) · [PDF](https://arxiv.org/pdf/2512.08879.pdf)  
**作者**：Mohammad Abu-Shaira, Ajita Rattani, Weishi Shi  

**一句话要点**：提出DAO-GP以解决在线高斯过程回归中的概念漂移和超参数固定问题

**关键词**：在线学习, 高斯过程回归, 概念漂移检测, 非参数模型, 自适应算法

## 3 点简述
- 核心问题：在线高斯过程模型缺乏漂移感知、依赖固定超参数，导致预测精度下降
- 方法要点：引入内置漂移检测与适应机制，动态调整模型行为，实现超参数自由和稀疏化
- 实验或效果：在多种漂移类型和数据特性下表现稳健，性能优于或媲美现有先进模型

## 摘要（原文）

> Real-world datasets often exhibit temporal dynamics characterized by evolving data distributions. Disregarding this phenomenon, commonly referred to as concept drift, can significantly diminish a model's predictive accuracy. Furthermore, the presence of hyperparameters in online models exacerbates this issue. These parameters are typically fixed and cannot be dynamically adjusted by the user in response to the evolving data distribution. Gaussian Process (GP) models offer powerful non-parametric regression capabilities with uncertainty quantification, making them ideal for modeling complex data relationships in an online setting. However, conventional online GP methods face several critical limitations, including a lack of drift-awareness, reliance on fixed hyperparameters, vulnerability to data snooping, absence of a principled decay mechanism, and memory inefficiencies. In response, we propose DAO-GP (Drift-Aware Online Gaussian Process), a novel, fully adaptive, hyperparameter-free, decayed, and sparse non-linear regression model. DAO-GP features a built-in drift detection and adaptation mechanism that dynamically adjusts model behavior based on the severity of drift. Extensive empirical evaluations confirm DAO-GP's robustness across stationary conditions, diverse drift types (abrupt, incremental, gradual), and varied data characteristics. Analyses demonstrate its dynamic adaptation, efficient in-memory and decay-based management, and evolving inducing points. Compared with state-of-the-art parametric and non-parametric models, DAO-GP consistently achieves superior or competitive performance, establishing it as a drift-resilient solution for online non-linear regression.

