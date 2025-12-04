---
layout: default
title: Optimal Transportation and Alignment Between Gaussian Measures
---

# Optimal Transportation and Alignment Between Gaussian Measures
**arXiv**：[2512.03579v1](https://arxiv.org/abs/2512.03579) · [PDF](https://arxiv.org/pdf/2512.03579.pdf)  
**作者**：Sanjit Dandapanthula, Aleksandr Podkopaev, Shiva Prasad Kasiviswanathan, Aaditya Ramdas, Ziv Goldfeld  

**一句话要点**：提出高斯分布下最优传输与内积Gromov-Wasserstein对齐的闭式解，以提升异构数据集比较与聚合效率。

**关键词**：最优传输, Gromov-Wasserstein对齐, 高斯分布, 知识蒸馏, 异构聚类, 闭式解

## 3 点简述
- 核心问题：高斯分布下最优传输与Gromov-Wasserstein对齐计算成本高，现有闭式解不完整。
- 方法要点：为未中心化高斯提供闭式表达式，扩展至中心化高斯的对齐与重心计算，并处理多边际最优传输。
- 实验或效果：应用于知识蒸馏和异构聚类，在合成与真实数据集上验证实用性。

## 摘要（原文）

> Optimal transport (OT) and Gromov-Wasserstein (GW) alignment provide interpretable geometric frameworks for comparing, transforming, and aggregating heterogeneous datasets -- tasks ubiquitous in data science and machine learning. Because these frameworks are computationally expensive, large-scale applications often rely on closed-form solutions for Gaussian distributions under quadratic cost. This work provides a comprehensive treatment of Gaussian, quadratic cost OT and inner product GW (IGW) alignment, closing several gaps in the literature to broaden applicability. First, we treat the open problem of IGW alignment between uncentered Gaussians on separable Hilbert spaces by giving a closed-form expression up to a quadratic optimization over unitary operators, for which we derive tight analytic upper and lower bounds. If at least one Gaussian measure is centered, the solution reduces to a fully closed-form expression, which we further extend to an analytic solution for the IGW barycenter between centered Gaussians. We also present a reduction of Gaussian multimarginal OT with pairwise quadratic costs to a tractable optimization problem and provide an efficient algorithm to solve it using a rank-deficiency constraint. To demonstrate utility, we apply our results to knowledge distillation and heterogeneous clustering on synthetic and real-world datasets.

