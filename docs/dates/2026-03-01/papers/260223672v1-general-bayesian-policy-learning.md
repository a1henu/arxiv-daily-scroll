---
layout: default
title: General Bayesian Policy Learning
---

# General Bayesian Policy Learning
**arXiv**：[2602.23672v1](https://arxiv.org/abs/2602.23672) · [PDF](https://arxiv.org/pdf/2602.23672.pdf)  
**作者**：Masahiro Kato  

**一句话要点**：提出通用贝叶斯框架以解决策略学习中的决策规则优化问题

**关键词**：策略学习, 贝叶斯方法, 决策规则, 福利最大化, 平方损失代理, PAC-Bayes理论

## 3 点简述
- 核心问题：决策者需从动作集中选择动作以最大化期望福利，如治疗选择或投资组合选择。
- 方法要点：基于损失贝叶斯更新，使用平方损失代理进行福利最大化，等价于最小化缩放平方误差。
- 实验或效果：引入带tanh压缩输出的神经网络作为实现示例，并提供PAC-Bayes风格的理论保证。

## 摘要（原文）

> This study proposes the General Bayes framework for policy learning. We consider decision problems in which a decision-maker chooses an action from an action set to maximize its expected welfare. Typical examples include treatment choice and portfolio selection. In such problems, the statistical target is a decision rule, and the prediction of each outcome $Y(a)$ is not necessarily of primary interest. We formulate this policy learning problem by loss-based Bayesian updating. Our main technical device is a squared-loss surrogate for welfare maximization. We show that maximizing empirical welfare over a policy class is equivalent to minimizing a scaled squared error in the outcome difference, up to a quadratic regularization controlled by a tuning parameter $ζ>0$. This rewriting yields a General Bayes posterior over decision rules that admits a Gaussian pseudo-likelihood interpretation. We clarify two Bayesian interpretations of the resulting generalized posterior, a working Gaussian view and a decision-theoretic loss-based view. As one implementation example, we introduce neural networks with tanh-squashed outputs. Finally, we provide theoretical guarantees in a PAC-Bayes style.

