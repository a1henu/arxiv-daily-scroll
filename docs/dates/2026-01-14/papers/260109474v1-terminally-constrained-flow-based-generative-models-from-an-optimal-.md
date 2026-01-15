---
layout: default
title: Terminally constrained flow-based generative models from an optimal control perspective
---

# Terminally constrained flow-based generative models from an optimal control perspective
**arXiv**：[2601.09474v1](https://arxiv.org/abs/2601.09474) · [PDF](https://arxiv.org/pdf/2601.09474.pdf)  
**作者**：Weiguo Gao, Ming Li, Qianxiao Li  

**一句话要点**：提出TOCFlow方法，通过最优控制解决预训练流模型在终端约束分布采样问题。

**关键词**：流生成模型, 最优控制, 终端约束采样, 几何引导, 哈密顿-雅可比-贝尔曼方程, 高维科学计算

## 3 点简述
- 核心问题：基于预训练流模型采样时，如何满足终端约束分布，如等式、不等式和统计约束。
- 方法要点：将问题建模为最优控制，推导哈密顿-雅可比-贝尔曼方程，设计几何感知的采样时间引导方法TOCFlow，避免矩阵求逆。
- 实验或效果：在Darcy流、约束轨迹规划和湍流生成等任务中，TOCFlow提升约束满足度，保持生成质量。

## 摘要（原文）

> We address the problem of sampling from terminally constrained distributions with pre-trained flow-based generative models through an optimal control formulation. Theoretically, we characterize the value function by a Hamilton-Jacobi-Bellman equation and derive the optimal feedback control as the minimizer of the associated Hamiltonian. We show that as the control penalty increases, the controlled process recovers the reference distribution, while as the penalty vanishes, the terminal law converges to a generalized Wasserstein projection onto the constraint manifold. Algorithmically, we introduce Terminal Optimal Control with Flow-based models (TOCFlow), a geometry-aware sampling-time guidance method for pre-trained flows. Solving the control problem in a terminal co-moving frame that tracks reference trajectories yields a closed-form scalar damping factor along the Riemannian gradient, capturing second-order curvature effects without matrix inversions. TOCFlow therefore matches the geometric consistency of Gauss-Newton updates at the computational cost of standard gradient guidance. We evaluate TOCFlow on three high-dimensional scientific tasks spanning equality, inequality, and global statistical constraints, namely Darcy flow, constrained trajectory planning, and turbulence snapshot generation with Kolmogorov spectral scaling. Across all settings, TOCFlow improves constraint satisfaction over Euclidean guidance and projection baselines while preserving the reference model's generative quality.

