---
layout: default
title: Grokking in Linear Models for Logistic Regression
---

# Grokking in Linear Models for Logistic Regression
**arXiv**：[2602.08302v1](https://arxiv.org/abs/2602.08302) · [PDF](https://arxiv.org/pdf/2602.08302.pdf)  
**作者**：Nataraj Das, Atreya Vedantam, Chandrashekar Lakshminarayanan  

**一句话要点**：在线性逻辑回归模型中揭示延迟泛化现象，通过梯度下降隐式偏置分析其动态过程。

**关键词**：延迟泛化, 线性模型, 逻辑回归, 梯度下降隐式偏置, 支持向量, 数据不对称性

## 3 点简述
- 研究线性可分数据下逻辑回归的延迟泛化现象，挑战深度网络必要性的观点。
- 理论分析梯度下降隐式偏置导致三阶段学习过程，解释延迟泛化机制。
- 实验验证数据不对称性对延迟泛化的影响，分析不同测试场景下的泛化行为。

## 摘要（原文）

> Grokking, the phenomenon of delayed generalization, is often attributed to the depth and compositional structure of deep neural networks. We study grokking in one of the simplest possible settings: the learning of a linear model with logistic loss for binary classification on data that are linearly (and max margin) separable about the origin. We investigate three testing regimes: (1) test data drawn from the same distribution as the training data, in which case grokking is not observed; (2) test data concentrated around the margin, in which case grokking is observed; and (3) adversarial test data generated via projected gradient descent (PGD) attacks, in which case grokking is also observed. We theoretically show that the implicit bias of gradient descent induces a three-phase learning process-population-dominated, support-vector-dominated unlearning, and support-vector-dominated generalization-during which delayed generalization can arise. Our analysis further relates the emergence of grokking to asymmetries in the data, both in the number of examples per class and in the distribution of support vectors across classes, and yields a characterization of the grokking time. We experimentally validate our theory by planting different distributions of population points and support vectors, and by analyzing accuracy curves and hyperplane dynamics. Overall, our results demonstrate that grokking does not require depth or representation learning, and can emerge even in linear models through the dynamics of the bias term.

