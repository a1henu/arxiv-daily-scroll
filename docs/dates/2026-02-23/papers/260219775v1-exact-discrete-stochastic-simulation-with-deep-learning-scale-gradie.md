---
layout: default
title: Exact Discrete Stochastic Simulation with Deep-Learning-Scale Gradient Optimization
---

# Exact Discrete Stochastic Simulation with Deep-Learning-Scale Gradient Optimization
**arXiv**：[2602.19775v1](https://arxiv.org/abs/2602.19775) · [PDF](https://arxiv.org/pdf/2602.19775.pdf)  
**作者**：Jose M. G. Vilar, Leonor Saiz  

**一句话要点**：提出解耦前向模拟与反向微分的精确离散随机模拟方法，实现大规模梯度优化

**关键词**：连续时间马尔可夫链, 精确随机模拟, 梯度优化, Gumbel-Softmax, 系统生物学, GPU并行计算

## 3 点简述
- 核心问题：Gillespie类算法中硬分类事件选择阻碍基于梯度的学习
- 方法要点：硬分类采样生成精确轨迹，通过连续并行Gumbel-Softmax直通代理传播梯度
- 实验或效果：在可逆二聚化模型、基因振荡器、大规模基因调控网络和离子通道门控实验中验证准确性、可扩展性和可靠性

## 摘要（原文）

> Exact stochastic simulation of continuous-time Markov chains (CTMCs) is essential when discreteness and noise drive system behavior, but the hard categorical event selection in Gillespie-type algorithms blocks gradient-based learning. We eliminate this constraint by decoupling forward simulation from backward differentiation, with hard categorical sampling generating exact trajectories and gradients propagating through a continuous massively-parallel Gumbel-Softmax straight-through surrogate. Our approach enables accurate optimization at parameter scales over four orders of magnitude beyond existing simulators. We validate for accuracy, scalability, and reliability on a reversible dimerization model (0.09% error), a genetic oscillator (1.2% error), a 203,796-parameter gene regulatory network achieving 98.4% MNIST accuracy (a prototypical deep-learning multilayer perceptron benchmark), and experimental patch-clamp recordings of ion channel gating (R^2 = 0.987) in the single-channel regime. Our GPU implementation delivers 1.9 billion steps per second, matching the scale of non-differentiable simulators. By making exact stochastic simulation massively parallel and autodiff-compatible, our results enable high-dimensional parameter inference and inverse design across systems biology, chemical kinetics, physics, and related CTMC-governed domains.

