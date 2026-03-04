---
layout: default
title: Convex and Non-convex Federated Learning with Stale Stochastic Gradients: Diminishing Step Size is All You Need
---

# Convex and Non-convex Federated Learning with Stale Stochastic Gradients: Diminishing Step Size is All You Need
**arXiv**：[2603.02639v1](https://arxiv.org/abs/2603.02639) · [PDF](https://arxiv.org/pdf/2603.02639.pdf)  
**作者**：Xinran Zheng, Tara Javidi, Behrouz Touri  

**一句话要点**：提出分布式随机优化框架，证明递减步长在延迟梯度下足以匹配自适应方案性能。

**关键词**：分布式优化, 延迟梯度, 随机梯度下降, 递减步长, 非凸优化, 强凸优化

## 3 点简述
- 研究分布式随机优化中延迟梯度模型下的收敛问题。
- 证明预选递减步长可替代延迟自适应步长，恢复最优收敛率。
- 分析覆盖非凸和强凸目标，理论验证递减步长的有效性。

## 摘要（原文）

> We propose a general framework for distributed stochastic optimization under delayed gradient models. In this setting, $n$ local agents leverage their own data and computation to assist a central server in minimizing a global objective composed of agents' local cost functions. Each agent is allowed to transmit stochastic-potentially biased and delayed-estimates of its local gradient. While a prior work has advocated delay-adaptive step sizes for stochastic gradient descent (SGD) in the presence of delays, we demonstrate that a pre-chosen diminishing step size is sufficient and matches the performance of the adaptive scheme. Moreover, our analysis establishes that diminishing step sizes recover the optimal SGD rates for nonconvex and strongly convex objectives.

