---
layout: default
title: FluxNet: Learning Capacity-Constrained Local Transport Operators for Conservative and Bounded PDE Surrogates
---

# FluxNet: Learning Capacity-Constrained Local Transport Operators for Conservative and Bounded PDE Surrogates
**arXiv**：[2602.01941v1](https://arxiv.org/abs/2602.01941) · [PDF](https://arxiv.org/pdf/2602.01941.pdf)  
**作者**：Zishuo Lan, Junjie Li, Lei Wang, Jincheng Wang  

**一句话要点**：提出FluxNet框架，通过容量约束局部传输算子解决守恒与有界PDE代理模型的长时程稳定性问题

**关键词**：PDE代理模型, 守恒定律, 局部传输算子, 容量约束, 自回归学习, 晶格玻尔兹曼方法

## 3 点简述
- 核心问题：自回归学习时间步进算子时，违反全局守恒和状态边界（如非负质量）导致长时程模拟不稳定
- 方法要点：基于晶格玻尔兹曼风格，模型输出局部传输算子而非下一状态，通过邻域交换保证离散守恒，参数化容量约束集强制边界
- 实验或效果：在浅水方程和交通流等任务中验证，相比基线提升模拟稳定性和物理一致性，支持大时间步长加速相场分解

## 摘要（原文）

> Autoregressive learning of time-stepping operators offers an effective approach to data-driven PDE simulation on grids. For conservation laws, however, long-horizon rollouts are often destabilized when learned updates violate global conservation and, in many applications, additional state bounds such as nonnegative mass and densities or concentrations constrained to [0,1]. Enforcing these coupled constraints via direct next-state regression remains difficult. We introduce a framework for learning conservative transport operators on regular grids, inspired by lattice Boltzmann-style discrete-velocity transport representations. Instead of predicting the next state, the model outputs local transport operators that update cells through neighborhood exchanges, guaranteeing discrete conservation by construction. For bounded quantities, we parameterize transport within a capacity-constrained feasible set, enforcing bounds structurally rather than by post-hoc clipping. We validate FluxNet on 1D convection-diffusion, 2D shallow water equations, 1D traffic flow, and 2D spinodal decomposition. Experiments on shallow-water equations and traffic flow show improved rollout stability and physical consistency over strong baselines. On phase-field spinodal decomposition, the method enables large time-steps with long-range transport, accelerating simulation while preserving microstructure evolution in both pointwise and statistical measures.

