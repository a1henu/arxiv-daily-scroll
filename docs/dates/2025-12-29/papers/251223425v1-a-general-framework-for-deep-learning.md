---
layout: default
title: A general framework for deep learning
---

# A general framework for deep learning
**arXiv**：[2512.23425v1](https://arxiv.org/abs/2512.23425) · [PDF](https://arxiv.org/pdf/2512.23425.pdf)  
**作者**：William Kengne, Modou Wade  

**一句话要点**：提出非惩罚和稀疏惩罚深度神经网络估计器，用于非参数回归和分类的广义深度学习框架。

**关键词**：深度学习框架, 非参数估计, 混合过程, 风险界分析, 极小极大最优

## 3 点简述
- 核心问题：在满足广义Bernstein型不等式的数据设置中，包括独立和多种混合观测，进行深度学习。
- 方法要点：提出NPDNN和SPDNN估计器，建立Hölder光滑函数类上的期望超额风险界。
- 实验或效果：在独立和混合过程示例中，推导风险上界，证明估计器在经典设置中达到极小极大最优（除对数因子）。

## 摘要（原文）

> This paper develops a general approach for deep learning for a setting that includes nonparametric regression and classification. We perform a framework from data that fulfills a generalized Bernstein-type inequality, including independent, $φ$-mixing, strongly mixing and $\mathcal{C}$-mixing observations. Two estimators are proposed: a non-penalized deep neural network estimator (NPDNN) and a sparse-penalized deep neural network estimator (SPDNN). For each of these estimators, bounds of the expected excess risk on the class of Hölder smooth functions and composition Hölder functions are established. Applications to independent data, as well as to $φ$-mixing, strongly mixing, $\mathcal{C}$-mixing processes are considered. For each of these examples, the upper bounds of the expected excess risk of the proposed NPDNN and SPDNN predictors are derived. It is shown that both the NPDNN and SPDNN estimators are minimax optimal (up to a logarithmic factor) in many classical settings.

