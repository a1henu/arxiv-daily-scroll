---
layout: default
title: On the Equivalence of Regression and Classification
---

# On the Equivalence of Regression and Classification
**arXiv**：[2511.04422v1](https://arxiv.org/abs/2511.04422) · [PDF](https://arxiv.org/pdf/2511.04422.pdf)  
**作者**：Jayadeva, Naman Dwivedi, Hari Krishnan, N. M. Anoop Krishnan  

**一句话要点**：提出回归与分类等价性以改进回归模型训练与评估

**关键词**：回归分类等价, 支持向量回归, 可回归性度量, 线性化映射, 神经网络训练

## 3 点简述
- 核心问题：回归与分类间缺乏形式化等价关系，影响模型理论理解。
- 方法要点：证明回归问题可等价转换为分类任务，并推导新回归公式。
- 实验或效果：引入可回归性度量，无需训练即可评估数据集回归难度。

## 摘要（原文）

> A formal link between regression and classification has been tenuous. Even
> though the margin maximization term $\\|w\\|$ is used in support vector
> regression, it has at best been justified as a regularizer. We show that a
> regression problem with $M$ samples lying on a hyperplane has a one-to-one
> equivalence with a linearly separable classification task with $2M$ samples. We
> show that margin maximization on the equivalent classification task leads to a
> different regression formulation than traditionally used. Using the
> equivalence, we demonstrate a ``regressability'' measure, that can be used to
> estimate the difficulty of regressing a dataset, without needing to first learn
> a model for it. We use the equivalence to train neural networks to learn a
> linearizing map, that transforms input variables into a space where a linear
> regressor is adequate.

