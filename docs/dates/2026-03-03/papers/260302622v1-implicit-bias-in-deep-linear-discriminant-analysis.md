---
layout: default
title: Implicit Bias in Deep Linear Discriminant Analysis
---

# Implicit Bias in Deep Linear Discriminant Analysis
**arXiv**：[2603.02622v1](https://arxiv.org/abs/2603.02622) · [PDF](https://arxiv.org/pdf/2603.02622.pdf)  
**作者**：Jiawen Li  

**一句话要点**：分析深度线性判别分析中的隐式偏差，揭示网络架构诱导的乘法权重更新机制。

**关键词**：隐式偏差, 深度线性判别分析, 梯度流分析, 乘法权重更新, 准范数守恒, 度量学习

## 3 点简述
- 研究深度LDA目标函数的隐式正则化，填补度量学习优化几何的理论空白。
- 基于L层对角线性网络，分析梯度流，证明平衡初始化下权重更新呈乘法形式。
- 发现网络自动保持(2/L)准范数守恒，为隐式偏差提供理论解释。

## 摘要（原文）

> While the Implicit Bias(or Implicit Regularization) of standard loss functions has been studied, the optimization geometry induced by discriminative metric-learning objectives remains largely unexplored.To the best of our knowledge, this paper presents an initial theoretical analysis of the implicit regularization induced by the Deep LDA,a scale invariant objective designed to minimize intraclass variance and maximize interclass distance. By analyzing the gradient flow of the loss on a L-layer diagonal linear network, we prove that under balanced initialization, the network architecture transforms standard additive gradient updates into multiplicative weight updates, which demonstrates an automatic conservation of the (2/L) quasi-norm.

