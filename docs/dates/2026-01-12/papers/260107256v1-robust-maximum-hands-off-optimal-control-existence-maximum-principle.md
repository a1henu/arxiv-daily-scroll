---
layout: default
title: Robust maximum hands-off optimal control: existence, maximum principle, and $L^{0}$-$L^1$ equivalence
---

# Robust maximum hands-off optimal control: existence, maximum principle, and $L^{0}$-$L^1$ equivalence
**arXiv**：[2601.07256v1](https://arxiv.org/abs/2601.07256) · [PDF](https://arxiv.org/pdf/2601.07256.pdf)  
**作者**：Siddhartha Ganguly, Kenji Kashima  

**一句话要点**：提出鲁棒最大无手控制框架，解决参数不确定线性系统的稀疏控制问题。

**关键词**：鲁棒控制, 稀疏控制, L^0-L^1等价, 庞特里亚金极大值原理, 半无限优化

## 3 点简述
- 核心问题：针对参数不确定的约束线性系统，构建非凸非光滑的鲁棒优化问题，最小化L^0目标。
- 方法要点：通过L^1凸替代和鲁棒庞特里亚金极大值原理，证明L^0与L^1最优解等价，并设计半无限优化算法。
- 实验或效果：提供示例验证方法的有效性，未知具体性能指标。

## 摘要（原文）

> This work advances the maximum hands-off sparse control framework by developing a robust counterpart for constrained linear systems with parametric uncertainties. The resulting optimal control problem minimizes an $L^{0}$ objective subject to an uncountable, compact family of constraints, and is therefore a nonconvex, nonsmooth robust optimization problem. To address this, we replace the $L^{0}$ objective with its convex $L^{1}$ surrogate and, using a nonsmooth variant of the robust Pontryagin maximum principle, show that the $L^{0}$ and $L^{1}$ formulations have identical sets of optimal solutions -- we call this the robust hands-off principle. Building on this equivalence, we propose an algorithmic framework -- drawing on numerically viable techniques from the semi-infinite robust optimization literature -- to solve the resulting problems. An illustrative example is provided to demonstrate the effectiveness of the approach.

