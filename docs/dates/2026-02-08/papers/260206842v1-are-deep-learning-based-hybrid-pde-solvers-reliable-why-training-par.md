---
layout: default
title: Are Deep Learning Based Hybrid PDE Solvers Reliable? Why Training Paradigms and Update Strategies Matter
---

# Are Deep Learning Based Hybrid PDE Solvers Reliable? Why Training Paradigms and Update Strategies Matter
**arXiv**：[2602.06842v1](https://arxiv.org/abs/2602.06842) · [PDF](https://arxiv.org/pdf/2602.06842.pdf)  
**作者**：Yuhan Wu, Jan Willem van Beek, Victorita Dolean, Alexander Heinlein  

**一句话要点**：提出物理感知安德森加速以解决深度学习混合PDE求解器可靠性问题

**关键词**：深度学习混合PDE求解器, 训练范式, 更新策略, 物理感知安德森加速, 虚假固定点, 可靠性

## 3 点简述
- 深度学习混合迭代方法易停滞于虚假固定点，导致物理残差大
- 训练范式与更新策略对性能敏感，需对齐求解器动力学与物理
- 物理感知安德森加速最小化物理残差，恢复可靠收敛于更少迭代

## 摘要（原文）

> Deep learning-based hybrid iterative methods (DL-HIMs) integrate classical numerical solvers with neural operators, utilizing their complementary spectral biases to accelerate convergence. Despite this promise, many DL-HIMs stagnate at false fixed points where neural updates vanish while the physical residual remains large, raising questions about reliability in scientific computing. In this paper, we provide evidence that performance is highly sensitive to training paradigms and update strategies, even when the neural architecture is fixed. Through a detailed study of a DeepONet-based hybrid iterative numerical transferable solver (HINTS) and an FFT-based Fourier neural solver (FNS), we show that significant physical residuals can persist when training objectives are not aligned with solver dynamics and problem physics. We further examine Anderson acceleration (AA) and demonstrate that its classical form is ill-suited for nonlinear neural operators. To overcome this, we introduce physics-aware Anderson acceleration (PA-AA), which minimizes the physical residual rather than the fixed-point update. Numerical experiments confirm that PA-AA restores reliable convergence in substantially fewer iterations. These findings provide a concrete answer to ongoing controversies surrounding AI-based PDE solvers: reliability hinges not only on architectures but on physically informed training and iteration design.

