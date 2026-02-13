---
layout: default
title: Learning to Control: The iUzawa-Net for Nonsmooth Optimal Control of Linear PDEs
---

# Learning to Control: The iUzawa-Net for Nonsmooth Optimal Control of Linear PDEs
**arXiv**：[2602.12273v1](https://arxiv.org/abs/2602.12273) · [PDF](https://arxiv.org/pdf/2602.12273.pdf)  
**作者**：Yongcun Song, Xiaoming Yuan, Hangrui Yue, Tianyou Zeng  

**一句话要点**：提出iUzawa-Net以实时求解线性PDE非光滑最优控制问题

**关键词**：最优控制, 偏微分方程, 神经网络求解器, 非光滑优化, Uzawa方法, 实时计算

## 3 点简述
- 核心问题：线性偏微分方程非光滑最优控制问题求解效率低，难以实时应用。
- 方法要点：基于非精确Uzawa方法展开，用可学习神经网络替代传统预处理器和PDE求解器。
- 实验或效果：验证了非光滑椭圆和抛物最优控制问题中的数值效率，证明渐近ε最优性。

## 摘要（原文）

> We propose an optimization-informed deep neural network approach, named iUzawa-Net, aiming for the first solver that enables real-time solutions for a class of nonsmooth optimal control problems of linear partial differential equations (PDEs). The iUzawa-Net unrolls an inexact Uzawa method for saddle point problems, replacing classical preconditioners and PDE solvers with specifically designed learnable neural networks. We prove universal approximation properties and establish the asymptotic $\varepsilon$-optimality for the iUzawa-Net, and validate its promising numerical efficiency through nonsmooth elliptic and parabolic optimal control problems. Our techniques offer a versatile framework for designing and analyzing various optimization-informed deep learning approaches to optimal control and other PDE-constrained optimization problems. The proposed learning-to-control approach synergizes model-based optimization algorithms and data-driven deep learning techniques, inheriting the merits of both methodologies.

