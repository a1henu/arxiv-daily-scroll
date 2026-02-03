---
layout: default
title: Unsupervised Physics-Informed Operator Learning through Multi-Stage Curriculum Training
---

# Unsupervised Physics-Informed Operator Learning through Multi-Stage Curriculum Training
**arXiv**：[2602.02264v1](https://arxiv.org/abs/2602.02264) · [PDF](https://arxiv.org/pdf/2602.02264.pdf)  
**作者**：Paolo Marcandelli, Natansh Mathur, Stefano Markidis, Martina Siena, Stefano Mariani  

**一句话要点**：提出多阶段课程训练策略与PhIS-FNO，以解决物理信息算子学习中的收敛不稳定问题。

**关键词**：物理信息算子学习, 多阶段课程训练, 傅里叶神经算子, 无监督学习, 偏微分方程求解

## 3 点简述
- 核心问题：无监督物理信息算子学习存在收敛不稳定和泛化能力有限的问题。
- 方法要点：采用多阶段训练策略，逐步施加边界条件和内部残差，结合优化器重初始化。
- 实验或效果：PhIS-FNO在基准测试中达到与监督学习相当的精度，仅需边界区域标签信息。

## 摘要（原文）

> Solving partial differential equations remains a central challenge in scientific machine learning. Neural operators offer a promising route by learning mappings between function spaces and enabling resolution-independent inference, yet they typically require supervised data. Physics-informed neural networks address this limitation through unsupervised training with physical constraints but often suffer from unstable convergence and limited generalization capability. To overcome these issues, we introduce a multi-stage physics-informed training strategy that achieves convergence by progressively enforcing boundary conditions in the loss landscape and subsequently incorporating interior residuals. At each stage the optimizer is re-initialized, acting as a continuation mechanism that restores stability and prevents gradient stagnation. We further propose the Physics-Informed Spline Fourier Neural Operator (PhIS-FNO), combining Fourier layers with Hermite spline kernels for smooth residual evaluation. Across canonical benchmarks, PhIS-FNO attains a level of accuracy comparable to that of supervised learning, using labeled information only along a narrow boundary region, establishing staged, spline-based optimization as a robust paradigm for physics-informed operator learning.

