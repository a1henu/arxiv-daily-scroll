---
layout: default
title: Learning Hamiltonian Flow Maps: Mean Flow Consistency for Large-Timestep Molecular Dynamics
---

# Learning Hamiltonian Flow Maps: Mean Flow Consistency for Large-Timestep Molecular Dynamics
**arXiv**：[2601.22123v1](https://arxiv.org/abs/2601.22123) · [PDF](https://arxiv.org/pdf/2601.22123.pdf)  
**作者**：Winfried Ripken, Michael Plainer, Gregor Lied, Thorben Frank, Oliver T. Unke, Stefan Chmiela, Frank Noé, Klaus Robert Müller  

**一句话要点**：提出学习哈密顿流映射框架，通过平均流一致性实现大时间步分子动力学模拟

**关键词**：哈密顿系统, 分子动力学, 机器学习力场, 大时间步积分, 平均流一致性

## 3 点简述
- 核心问题：哈密顿系统长期演化受限于小时间步数值积分稳定性
- 方法要点：引入平均流一致性条件，基于独立相空间样本学习时间平均演化
- 实验或效果：在分子动力学中支持更大积分时间步，训练成本与推理成本相当

## 摘要（原文）

> Simulating the long-time evolution of Hamiltonian systems is limited by the small timesteps required for stable numerical integration. To overcome this constraint, we introduce a framework to learn Hamiltonian Flow Maps by predicting the mean phase-space evolution over a chosen time span $Δt$, enabling stable large-timestep updates far beyond the stability limits of classical integrators. To this end, we impose a Mean Flow consistency condition for time-averaged Hamiltonian dynamics. Unlike prior approaches, this allows training on independent phase-space samples without access to future states, avoiding expensive trajectory generation. Validated across diverse Hamiltonian systems, our method in particular improves upon molecular dynamics simulations using machine-learned force fields (MLFF). Our models maintain comparable training and inference cost, but support significantly larger integration timesteps while trained directly on widely-available trajectory-free MLFF datasets.

