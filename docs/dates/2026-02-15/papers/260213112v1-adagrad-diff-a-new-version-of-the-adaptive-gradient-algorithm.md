---
layout: default
title: AdaGrad-Diff: A New Version of the Adaptive Gradient Algorithm
---

# AdaGrad-Diff: A New Version of the Adaptive Gradient Algorithm
**arXiv**：[2602.13112v1](https://arxiv.org/abs/2602.13112) · [PDF](https://arxiv.org/pdf/2602.13112.pdf)  
**作者**：Matia Bojovic, Saverio Salzo, Massimiliano Pontil  

**一句话要点**：提出AdaGrad-Diff以解决AdaGrad在梯度变化小时不必要减小步长的问题

**关键词**：自适应梯度算法, 步长调整, 梯度差, 优化方法, 鲁棒性

## 3 点简述
- 核心问题：传统梯度方法对步长敏感，AdaGrad虽自适应但可能过度减小步长
- 方法要点：基于梯度差平方和驱动自适应，梯度变化小时保持步长，变化大时自动阻尼
- 实验或效果：数值实验显示在多个实际场景中比AdaGrad更鲁棒

## 摘要（原文）

> Vanilla gradient methods are often highly sensitive to the choice of stepsize, which typically requires manual tuning. Adaptive methods alleviate this issue and have therefore become widely used. Among them, AdaGrad has been particularly influential. In this paper, we propose an AdaGrad-style adaptive method in which the adaptation is driven by the cumulative squared norms of successive gradient differences rather than gradient norms themselves. The key idea is that when gradients vary little across iterations, the stepsize is not unnecessarily reduced, while significant gradient fluctuations, reflecting curvature or instability, lead to automatic stepsize damping. Numerical experiments demonstrate that the proposed method is more robust than AdaGrad in several practically relevant settings.

