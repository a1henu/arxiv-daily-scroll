---
layout: default
title: Breaking Symmetry-Induced Degeneracy in Multi-Agent Ergodic Coverage via Stochastic Spectral Control
---

# Breaking Symmetry-Induced Degeneracy in Multi-Agent Ergodic Coverage via Stochastic Spectral Control
**arXiv**：[2512.23158v1](https://arxiv.org/abs/2512.23158) · [PDF](https://arxiv.org/pdf/2512.23158.pdf)  
**作者**：Kooktae Lee, Julian Martinez  

**一句话要点**：提出随机谱控制以解决多智能体遍历覆盖中的对称诱导退化问题

**关键词**：多智能体系统, 遍历覆盖, 谱控制, 随机扰动, 对称退化, 轨迹有界性

## 3 点简述
- 核心问题：经典谱多尺度覆盖在对称点附近梯度抵消，导致智能体停滞或沿对称轴运动
- 方法要点：引入随机扰动与收缩项，确保几乎必然逃离零梯度流形并保持轨迹均方有界
- 实验或效果：仿真显示随机谱多尺度覆盖有效缓解瞬态停滞和轴约束运动，所有轨迹保持有界

## 摘要（原文）

> Multi-agent ergodic coverage via Spectral Multiscale Coverage (SMC) provides a principled framework for driving a team of agents so that their collective time-averaged trajectories match a prescribed spatial distribution. While classical SMC has demonstrated empirical success, it can suffer from gradient cancellation, particularly when agents are initialized near symmetry points of the target distribution, leading to undesirable behaviors such as stalling or motion constrained along symmetry axes. In this work, we rigorously characterize the initial conditions and symmetry-induced invariant manifolds that give rise to such directional degeneracy in first-order agent dynamics. To address this, we introduce a stochastic perturbation combined with a contraction term and prove that the resulting dynamics ensure almost-sure escape from zero-gradient manifolds while maintaining mean-square boundedness of agent trajectories. Simulations on symmetric multi-modal reference distributions demonstrate that the proposed stochastic SMC effectively mitigates transient stalling and axis-constrained motion, while ensuring that all agent trajectories remain bounded within the domain.

