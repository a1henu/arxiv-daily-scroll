---
layout: default
title: Out-of-Distribution Generalization for Neural Physics Solvers
---

# Out-of-Distribution Generalization for Neural Physics Solvers
**arXiv**：[2601.19091v1](https://arxiv.org/abs/2601.19091) · [PDF](https://arxiv.org/pdf/2601.19091.pdf)  
**作者**：Zhao Wei, Chin Chun Ooi, Jian Cheng Wong, Abhishek Gupta, Pao-Hsiung Chiu, Yew-Soon Ong  

**一句话要点**：提出NOVA方法以提升神经物理求解器在分布外场景下的泛化能力

**关键词**：神经物理求解器, 分布外泛化, 物理对齐表示, 非线性偏微分方程, 长期动力学模拟, 生成设计优化

## 3 点简述
- 核心问题：神经物理求解器在训练分布外泛化差，限制新设计和长期预测探索
- 方法要点：通过从稀疏场景学习物理对齐表示，实现参数、几何和初始条件分布偏移下的准确求解
- 实验或效果：在热传导、扩散反应和流体流动等非线性问题中，分布外误差比基线低1-2个数量级

## 摘要（原文）

> Neural physics solvers are increasingly used in scientific discovery, given their potential for rapid in silico insights into physical, materials, or biological systems and their long-time evolution. However, poor generalization beyond their training support limits exploration of novel designs and long-time horizon predictions. We introduce NOVA, a route to generalizable neural physics solvers that can provide rapid, accurate solutions to scenarios even under distributional shifts in partial differential equation parameters, geometries and initial conditions. By learning physics-aligned representations from an initial sparse set of scenarios, NOVA consistently achieves 1-2 orders of magnitude lower out-of-distribution errors than data-driven baselines across complex, nonlinear problems including heat transfer, diffusion-reaction and fluid flow. We further showcase NOVA's dual impact on stabilizing long-time dynamical rollouts and improving generative design through application to the simulation of nonlinear Turing systems and fluidic chip optimization. Unlike neural physics solvers that are constrained to retrieval and/or emulation within an a priori space, NOVA enables reliable extrapolation beyond known regimes, a key capability given the need for exploration of novel hypothesis spaces in scientific discovery

