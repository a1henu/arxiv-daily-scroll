---
layout: default
title: On Approximate Computation of Critical Points
---

# On Approximate Computation of Critical Points
**arXiv**：[2601.21917v1](https://arxiv.org/abs/2601.21917) · [PDF](https://arxiv.org/pdf/2601.21917.pdf)  
**作者**：Amir Ali Ahmadi, Georgina Hall  

**一句话要点**：证明非凸函数临界点近似计算在多项式时间内不可行，除非P=NP。

**关键词**：非凸优化, 临界点计算, 计算复杂性, NP难问题, 多项式函数, 近似算法

## 3 点简述
- 核心问题：研究非凸函数临界点的近似计算复杂性，挑战其可处理性的普遍认知。
- 方法要点：通过理论证明，即使对低度多项式，输出梯度范数≤2^n的近似点也是NP难的。
- 实验或效果：在多种结构假设下（如临界点存在唯一、函数有下界）均得出硬度结果。

## 摘要（原文）

> We show that computing even very coarse approximations of critical points is intractable for simple classes of nonconvex functions. More concretely, we prove that if there exists a polynomial-time algorithm that takes as input a polynomial in $n$ variables of constant degree (as low as three) and outputs a point whose gradient has Euclidean norm at most $2^n$ whenever the polynomial has a critical point, then P=NP. The algorithm is permitted to return an arbitrary point when no critical point exists. We also prove hardness results for approximate computation of critical points under additional structural assumptions, including settings in which existence and uniqueness of a critical point are guaranteed, the function is lower bounded, and approximation is measured in terms of distance to a critical point. Overall, our results stand in contrast to the commonly-held belief that, in nonconvex optimization, approximate computation of critical points is a tractable task.

