---
layout: default
title: Learn to Evolve: Self-supervised Neural JKO Operator for Wasserstein Gradient Flow
---

# Learn to Evolve: Self-supervised Neural JKO Operator for Wasserstein Gradient Flow
**arXiv**：[2601.05583v1](https://arxiv.org/abs/2601.05583) · [PDF](https://arxiv.org/pdf/2601.05583.pdf)  
**作者**：Xue Feng, Li Wang, Deanna Needell, Rongjie Lai  

**一句话要点**：提出自监督学习JKO算子以高效计算Wasserstein梯度流，避免重复求解子问题。

**关键词**：Wasserstein梯度流, JKO算子, 自监督学习, 数据增强, 计算效率

## 3 点简述
- 核心问题：JKO方案计算Wasserstein梯度流时，重复求解子问题导致高计算成本。
- 方法要点：通过Learn-to-Evolve算法联合学习JKO算子和轨迹，实现自监督训练和数据增强。
- 实验或效果：数值实验验证了方法在多种能量和初始条件下的准确性、稳定性和鲁棒性。

## 摘要（原文）

> The Jordan-Kinderlehrer-Otto (JKO) scheme provides a stable variational framework for computing Wasserstein gradient flows, but its practical use is often limited by the high computational cost of repeatedly solving the JKO subproblems. We propose a self-supervised approach for learning a JKO solution operator without requiring numerical solutions of any JKO trajectories. The learned operator maps an input density directly to the minimizer of the corresponding JKO subproblem, and can be iteratively applied to efficiently generate the gradient-flow evolution. A key challenge is that only a number of initial densities are typically available for training. To address this, we introduce a Learn-to-Evolve algorithm that jointly learns the JKO operator and its induced trajectories by alternating between trajectory generation and operator updates. As training progresses, the generated data increasingly approximates true JKO trajectories. Meanwhile, this Learn-to-Evolve strategy serves as a natural form of data augmentation, significantly enhancing the generalization ability of the learned operator. Numerical experiments demonstrate the accuracy, stability, and robustness of the proposed method across various choices of energies and initial conditions.

