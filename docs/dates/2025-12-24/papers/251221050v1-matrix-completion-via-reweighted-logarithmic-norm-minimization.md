---
layout: default
title: Matrix Completion Via Reweighted Logarithmic Norm Minimization
---

# Matrix Completion Via Reweighted Logarithmic Norm Minimization
**arXiv**：[2512.21050v1](https://arxiv.org/abs/2512.21050) · [PDF](https://arxiv.org/pdf/2512.21050.pdf)  
**作者**：Zhijie Wang, Liangtian He, Qinghua Zhang, Jifei Miao, Liang-Jian Deng, Jun Liu  

**一句话要点**：提出重加权对数范数最小化方法以改进低秩矩阵补全性能

**关键词**：低秩矩阵补全, 非凸优化, 重加权对数范数, ADMM算法, 图像修复

## 3 点简述
- 低秩矩阵补全中核范数作为秩函数凸代理易导致奇异值过度收缩
- 引入非凸重加权对数范数作为更接近秩函数的替代，并用ADMM高效求解
- 图像修复实验显示在视觉质量和量化指标上优于现有方法

## 摘要（原文）

> Low-rank matrix completion (LRMC) has demonstrated remarkable success in a wide range of applications. To address the NP-hard nature of the rank minimization problem, the nuclear norm is commonly used as a convex and computationally tractable surrogate for the rank function. However, this approach often yields suboptimal solutions due to the excessive shrinkage of singular values. In this letter, we propose a novel reweighted logarithmic norm as a more effective nonconvex surrogate, which provides a closer approximation than many existing alternatives. We efficiently solve the resulting optimization problem by employing the alternating direction method of multipliers (ADMM). Experimental results on image inpainting demonstrate that the proposed method achieves superior performance compared to state-of-the-art LRMC approaches, both in terms of visual quality and quantitative metrics.

