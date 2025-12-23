---
layout: default
title: Total Curvature Regularization and its_Minimization for Surface and Image Smoothing
---

# Total Curvature Regularization and its_Minimization for Surface and Image Smoothing
**arXiv**：[2512.18968v1](https://arxiv.org/abs/2512.18968) · [PDF](https://arxiv.org/pdf/2512.18968.pdf)  
**作者**：Tianle Lu, Ke Chen, Yuping Duan  

**一句话要点**：提出总法曲率正则化方法，用于表面和图像平滑，以保持锐利边缘和精确各向同性。

**关键词**：曲率正则化, 表面平滑, 图像平滑, 偏微分方程, 优化算法, 边缘保持

## 3 点简述
- 核心问题：传统曲率正则化在平滑时易模糊边缘，难以平衡平滑与细节保留。
- 方法要点：通过惩罚多方向法曲率，构建高阶非线性优化，并转化为PDE系统稳态求解。
- 实验或效果：在表面和图像平滑中验证了方法的效率和鲁棒性，无需复杂参数调优。

## 摘要（原文）

> We introduce a novel formulation for curvature regularization by penalizing normal curvatures from multiple directions. This total normal curvature regularization is capable of producing solutions with sharp edges and precise isotropic properties. To tackle the resulting high-order nonlinear optimization problem, we reformulate it as the task of finding the steady-state solution of a time-dependent partial differential equation (PDE) system. Time discretization is achieved through operator splitting, where each subproblem at the fractional steps either has a closed-form solution or can be efficiently solved using advanced algorithms. Our method circumvents the need for complex parameter tuning and demonstrates robustness to parameter choices. The efficiency and effectiveness of our approach have been rigorously validated in the context of surface and image smoothing problems.

