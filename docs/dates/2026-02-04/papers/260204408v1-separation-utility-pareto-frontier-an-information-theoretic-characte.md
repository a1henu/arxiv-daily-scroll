---
layout: default
title: Separation-Utility Pareto Frontier: An Information-Theoretic Characterization
---

# Separation-Utility Pareto Frontier: An Information-Theoretic Characterization
**arXiv**：[2602.04408v1](https://arxiv.org/abs/2602.04408) · [PDF](https://arxiv.org/pdf/2602.04408.pdf)  
**作者**：Shizhou Xu  

**一句话要点**：提出基于信息论的分离-效用帕累托前沿表征与条件互信息正则化方法，以在深度学习中实现公平性分离准则。

**关键词**：公平机器学习, 信息论, 帕累托前沿, 条件互信息, 深度学习正则化, 分离准则

## 3 点简述
- 研究预测效用与分离公平性之间的帕累托前沿，分离要求预测在给定真实结果下独立于敏感属性。
- 通过信息论证明前沿特性，开发基于条件互信息的正则化器，兼容梯度优化模型。
- 在COMPAS等数据集上实验，显著减少分离违规，同时匹配或超越基线方法的效用。

## 摘要（原文）

> We study the Pareto frontier (optimal trade-off) between utility and separation, a fairness criterion requiring predictive independence from sensitive attributes conditional on the true outcome. Through an information-theoretic lens, we prove a characterization of the utility-separation Pareto frontier, establish its concavity, and thereby prove the increasing marginal cost of separation in terms of utility. In addition, we characterize the conditions under which this trade-off becomes strict, providing a guide for trade-off selection in practice. Based on the theoretical characterization, we develop an empirical regularizer based on conditional mutual information (CMI) between predictions and sensitive attributes given the true outcome. The CMI regularizer is compatible with any deep model trained via gradient-based optimization and serves as a scalar monitor of residual separation violations, offering tractable guarantees during training. Finally, numerical experiments support our theoretical findings: across COMPAS, UCI Adult, UCI Bank, and CelebA, the proposed method substantially reduces separation violations while matching or exceeding the utility of established baseline methods. This study thus offers a provable, stable, and flexible approach to enforcing separation in deep learning.

