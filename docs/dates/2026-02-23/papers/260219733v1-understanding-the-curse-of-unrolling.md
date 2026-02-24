---
layout: default
title: Understanding the Curse of Unrolling
---

# Understanding the Curse of Unrolling
**arXiv**：[2602.19733v1](https://arxiv.org/abs/2602.19733) · [PDF](https://arxiv.org/pdf/2602.19733.pdf)  
**作者**：Sheheryar Mehmood, Florian Knoll, Peter Ochs  

**一句话要点**：分析算法展开的诅咒，提出截断与预热策略以优化雅可比计算

**关键词**：算法展开, 雅可比计算, 双层优化, 非渐近分析, 截断策略, 预热初始化

## 3 点简述
- 核心问题：算法展开中雅可比计算早期迭代可能偏离真实值，导致诅咒现象
- 方法要点：非渐近分析揭示诅咒根源，截断早期迭代可缓解并减少内存需求
- 实验或效果：理论支持数值实验，预热策略在双层优化中提供实用解决方案

## 摘要（原文）

> Algorithm unrolling is ubiquitous in machine learning, particularly in hyperparameter optimization and meta-learning, where Jacobians of solution mappings are computed by differentiating through iterative algorithms. Although unrolling is known to yield asymptotically correct Jacobians under suitable conditions, recent work has shown that the derivative iterates may initially diverge from the true Jacobian, a phenomenon known as the curse of unrolling. In this work, we provide a non-asymptotic analysis that explains the origin of this behavior and identifies the algorithmic factors that govern it. We show that truncating early iterations of the derivative computation mitigates the curse while simultaneously reducing memory requirements. Finally, we demonstrate that warm-starting in bilevel optimization naturally induces an implicit form of truncation, providing a practical remedy. Our theoretical findings are supported by numerical experiments on representative examples.

