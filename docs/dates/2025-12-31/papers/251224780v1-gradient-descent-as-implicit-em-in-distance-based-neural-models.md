---
layout: default
title: Gradient Descent as Implicit EM in Distance-Based Neural Models
---

# Gradient Descent as Implicit EM in Distance-Based Neural Models
**arXiv**：[2512.24780v1](https://arxiv.org/abs/2512.24780) · [PDF](https://arxiv.org/pdf/2512.24780.pdf)  
**作者**：Alan Oursland  

**一句话要点**：揭示基于距离的神经网络目标中梯度下降隐式执行期望最大化

**关键词**：梯度下降, 期望最大化, 神经网络理论, 概率推断, 目标几何

## 3 点简述
- 核心问题：神经网络训练中出现的概率推断行为缺乏直接理论解释
- 方法要点：推导出对数-求和-指数结构目标的梯度等于负后验责任，建立代数恒等式
- 实验或效果：统一无监督混合建模、注意力机制和交叉熵分类的学习机制

## 摘要（原文）

> Neural networks trained with standard objectives exhibit behaviors characteristic of probabilistic inference: soft clustering, prototype specialization, and Bayesian uncertainty tracking. These phenomena appear across architectures -- in attention mechanisms, classification heads, and energy-based models -- yet existing explanations rely on loose analogies to mixture models or post-hoc architectural interpretation. We provide a direct derivation. For any objective with log-sum-exp structure over distances or energies, the gradient with respect to each distance is exactly the negative posterior responsibility of the corresponding component: $\partial L / \partial d_j = -r_j$. This is an algebraic identity, not an approximation. The immediate consequence is that gradient descent on such objectives performs expectation-maximization implicitly -- responsibilities are not auxiliary variables to be computed but gradients to be applied. No explicit inference algorithm is required because inference is embedded in optimization. This result unifies three regimes of learning under a single mechanism: unsupervised mixture modeling, where responsibilities are fully latent; attention, where responsibilities are conditioned on queries; and cross-entropy classification, where supervision clamps responsibilities to targets. The Bayesian structure recently observed in trained transformers is not an emergent property but a necessary consequence of the objective geometry. Optimization and inference are the same process.

