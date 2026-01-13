---
layout: default
title: Convergence Rate Analysis of the AdamW-Style Shampoo: Unifying One-sided and Two-Sided Preconditioning
---

# Convergence Rate Analysis of the AdamW-Style Shampoo: Unifying One-sided and Two-Sided Preconditioning
**arXiv**：[2601.07326v1](https://arxiv.org/abs/2601.07326) · [PDF](https://arxiv.org/pdf/2601.07326.pdf)  
**作者**：Huan Li, Yiming Dong, Zhouchen Lin  

**一句话要点**：分析AdamW风格Shampoo优化器的收敛率，统一单侧与双侧预条件方法。

**关键词**：优化算法, 收敛率分析, 预条件方法, AdamW, Shampoo, 核范数

## 3 点简述
- 研究AdamW风格Shampoo优化器，基于经典Shampoo在算法竞赛中表现优异。
- 理论分析统一单侧和双侧预条件，建立基于核范数的收敛率上界。
- 收敛率与SGD最优收敛率类比，支持在理想情况下类似性能。

## 摘要（原文）

> This paper studies the AdamW-style Shampoo optimizer, an effective implementation of classical Shampoo that notably won the external tuning track of the AlgoPerf neural network training algorithm competition. Our analysis unifies one-sided and two-sided preconditioning and establishes the convergence rate $\frac{1}{K}\sum_{k=1}^K E\left[\\|\nabla f(X_k)\\|_*\right]\leq O(\frac{\sqrt{m+n}C}{K^{1/4}})$ measured by nuclear norm, where $K$ represents the iteration number, $(m,n)$ denotes the size of matrix parameters, and $C$ matches the constant in the optimal convergence rate of SGD. Theoretically, we have $\\|\nabla f(X)\\|_F\leq \\|\nabla f(X)\\|_*\leq \sqrt{m+n}\\|\nabla f(X)\\|_F$, supporting that our convergence rate can be considered to be analogous to the optimal $\frac{1}{K}\sum_{k=1}^KE\left[\\|\nabla f(X_k)\\|_F\right]\leq O(\frac{C}{K^{1/4}})$ convergence rate of SGD in the ideal case of $\\|\nabla f(X)\\|_*= Θ(\sqrt{m+n})\\|\nabla f(X)\\|_F$.

