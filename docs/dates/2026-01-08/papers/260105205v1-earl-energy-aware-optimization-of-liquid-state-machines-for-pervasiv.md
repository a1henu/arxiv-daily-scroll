---
layout: default
title: EARL: Energy-Aware Optimization of Liquid State Machines for Pervasive AI
---

# EARL: Energy-Aware Optimization of Liquid State Machines for Pervasive AI
**arXiv**：[2601.05205v1](https://arxiv.org/abs/2601.05205) · [PDF](https://arxiv.org/pdf/2601.05205.pdf)  
**作者**：Zain Iqbal, Lorenzo Valerio  

**一句话要点**：提出EARL框架，通过能量感知强化学习优化液态状态机，以提升资源受限设备AI应用的效率。

**关键词**：能量感知优化, 液态状态机, 强化学习, 贝叶斯优化, 资源受限AI, 超参数调优

## 3 点简述
- 核心问题：液态状态机在部署中面临超参数敏感性和传统优化方法忽略能量约束的高计算成本挑战。
- 方法要点：结合贝叶斯优化与自适应强化学习策略，联合优化准确性和能耗，并采用代理建模和早期终止机制减少开销。
- 实验或效果：在三个基准数据集上，EARL实现更高准确性、更低能耗和更短优化时间，优于现有超参数调优框架。

## 摘要（原文）

> Pervasive AI increasingly depends on on-device learning systems that deliver low-latency and energy-efficient computation under strict resource constraints. Liquid State Machines (LSMs) offer a promising approach for low-power temporal processing in pervasive and neuromorphic systems, but their deployment remains challenging due to high hyperparameter sensitivity and the computational cost of traditional optimization methods that ignore energy constraints. This work presents EARL, an energy-aware reinforcement learning framework that integrates Bayesian optimization with an adaptive reinforcement learning based selection policy to jointly optimize accuracy and energy consumption. EARL employs surrogate modeling for global exploration, reinforcement learning for dynamic candidate prioritization, and an early termination mechanism to eliminate redundant evaluations, substantially reducing computational overhead. Experiments on three benchmark datasets demonstrate that EARL achieves 6 to 15 percent higher accuracy, 60 to 80 percent lower energy consumption, and up to an order of magnitude reduction in optimization time compared to leading hyperparameter tuning frameworks. These results highlight the effectiveness of energy-aware adaptive search in improving the efficiency and scalability of LSMs for resource-constrained on-device AI applications.

