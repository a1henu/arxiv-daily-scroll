---
layout: default
title: Learning Hamiltonian Flow Maps: Mean Flow Consistency for Large-Timestep Molecular Dynamics
---

# Learning Hamiltonian Flow Maps: Mean Flow Consistency for Large-Timestep Molecular Dynamics
**arXiv**：[2601.22123v1](https://arxiv.org/abs/2601.22123) · [PDF](https://arxiv.org/pdf/2601.22123.pdf)  
**作者**：Winfried Ripken, Michael Plainer, Gregor Lied, Thorben Frank, Oliver T. Unke, Stefan Chmiela, Frank Noé, Klaus Robert Müller  

**一句话要点**：提出基于平均流一致性的哈密顿流图学习框架，以解决分子动力学模拟中因小时间步长限制长期演化的问题。

**关键词**：哈密顿系统模拟, 平均流一致性, 大时间步长积分, 机器学习力场, 分子动力学

## 3 点简述
- 核心问题：哈密顿系统长期演化受限于小时间步长，传统数值积分稳定性差。
- 方法要点：通过平均流一致性条件学习哈密顿流图，预测相空间平均演化，支持大时间步长更新。
- 实验或效果：在多种哈密顿系统验证，尤其提升机器学习力场分子动力学模拟，训练成本相近但时间步长显著增大。

## 摘要（原文）

> Simulating the long-time evolution of Hamiltonian systems is limited by the small timesteps required for stable numerical integration. To overcome this constraint, we introduce a framework to learn Hamiltonian Flow Maps by predicting the mean phase-space evolution over a chosen time span $Δt$, enabling stable large-timestep updates far beyond the stability limits of classical integrators. To this end, we impose a Mean Flow consistency condition for time-averaged Hamiltonian dynamics. Unlike prior approaches, this allows training on independent phase-space samples without access to future states, avoiding expensive trajectory generation. Validated across diverse Hamiltonian systems, our method in particular improves upon molecular dynamics simulations using machine-learned force fields (MLFF). Our models maintain comparable training and inference cost, but support significantly larger integration timesteps while trained directly on widely-available trajectory-free MLFF datasets.

