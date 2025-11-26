---
layout: default
title: A Tale of Two Geometries: Adaptive Optimizers and Non-Euclidean Descent
---

# A Tale of Two Geometries: Adaptive Optimizers and Non-Euclidean Descent
**arXiv**：[2511.20584v1](https://arxiv.org/abs/2511.20584) · [PDF](https://arxiv.org/pdf/2511.20584.pdf)  
**作者**：Shuo Xie, Tianhao Wang, Beining Wu, Zhiyuan Li  

**一句话要点**：扩展自适应光滑性理论以统一自适应优化器与非欧几何下降分析

**关键词**：自适应优化器, 非欧几何下降, 自适应光滑性, 随机优化, 收敛分析

## 3 点简述
- 核心问题：自适应优化器与归一化最速下降在几何分析上存在差异，影响收敛性。
- 方法要点：将自适应光滑性扩展到非凸设置，并引入自适应梯度方差进行随机优化比较。
- 实验或效果：在凸设置下实现自适应优化器加速，提供维度无关的收敛保证。

## 摘要（原文）

> Adaptive optimizers can reduce to normalized steepest descent (NSD) when only adapting to the current gradient, suggesting a close connection between the two algorithmic families. A key distinction between their analyses, however, lies in the geometries, e.g., smoothness notions, they rely on. In the convex setting, adaptive optimizers are governed by a stronger adaptive smoothness condition, while NSD relies on the standard notion of smoothness. We extend the theory of adaptive smoothness to the nonconvex setting and show that it precisely characterizes the convergence of adaptive optimizers. Moreover, we establish that adaptive smoothness enables acceleration of adaptive optimizers with Nesterov momentum in the convex setting, a guarantee unattainable under standard smoothness for certain non-Euclidean geometry. We further develop an analogous comparison for stochastic optimization by introducing adaptive gradient variance, which parallels adaptive smoothness and leads to dimension-free convergence guarantees that cannot be achieved under standard gradient variance for certain non-Euclidean geometry.

