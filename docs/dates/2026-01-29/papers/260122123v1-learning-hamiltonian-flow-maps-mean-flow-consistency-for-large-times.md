---
layout: default
title: Learning Hamiltonian Flow Maps: Mean Flow Consistency for Large-Timestep Molecular Dynamics
---

# Learning Hamiltonian Flow Maps: Mean Flow Consistency for Large-Timestep Molecular Dynamics
**arXiv**：[2601.22123v1](https://arxiv.org/abs/2601.22123) · [PDF](https://arxiv.org/pdf/2601.22123.pdf)  
**作者**：Winfried Ripken, Michael Plainer, Gregor Lied, Thorben Frank, Oliver T. Unke, Stefan Chmiela, Frank Noé, Klaus Robert Müller  

**一句话要点**：提出基于平均流一致性的哈密顿流图学习框架，以解决分子动力学模拟中因小时间步长限制长期演化的问题。

**关键词**：哈密顿流图学习, 平均流一致性, 大时间步长模拟, 分子动力学, 机器学习力场, 相空间演化

## 3 点简述
- 核心问题：哈密顿系统长期演化受限于数值积分所需的小时间步长，导致计算效率低下。
- 方法要点：通过平均流一致性条件学习哈密顿流图，预测相空间在选定时间跨度内的平均演化，支持超越经典积分器稳定性极限的大时间步长更新。
- 实验或效果：在多种哈密顿系统上验证，尤其提升基于机器学习力场的分子动力学模拟，训练和推理成本相当，但支持显著更大的积分时间步长。

## 摘要（原文）

> Simulating the long-time evolution of Hamiltonian systems is limited by the small timesteps required for stable numerical integration. To overcome this constraint, we introduce a framework to learn Hamiltonian Flow Maps by predicting the mean phase-space evolution over a chosen time span $Δt$, enabling stable large-timestep updates far beyond the stability limits of classical integrators. To this end, we impose a Mean Flow consistency condition for time-averaged Hamiltonian dynamics. Unlike prior approaches, this allows training on independent phase-space samples without access to future states, avoiding expensive trajectory generation. Validated across diverse Hamiltonian systems, our method in particular improves upon molecular dynamics simulations using machine-learned force fields (MLFF). Our models maintain comparable training and inference cost, but support significantly larger integration timesteps while trained directly on widely-available trajectory-free MLFF datasets.

