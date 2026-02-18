---
layout: default
title: Spatially-Aware Adaptive Trajectory Optimization with Controller-Guided Feedback for Autonomous Racing
---

# Spatially-Aware Adaptive Trajectory Optimization with Controller-Guided Feedback for Autonomous Racing
**arXiv**：[2602.15642v1](https://arxiv.org/abs/2602.15642) · [PDF](https://arxiv.org/pdf/2602.15642.pdf)  
**作者**：Alexander Wachter, Alexander Willert, Marc-Philip Ecker, Christian Hartl-Nesic  

**一句话要点**：提出闭环框架结合轨迹优化与控制器反馈，以提升自动驾驶赛车性能

**关键词**：自动驾驶赛车, 轨迹优化, 闭环控制, 自适应约束, 空间反馈, CMA-ES

## 3 点简述
- 核心问题：传统方法将跟踪误差视为瞬态扰动，未充分利用局部赛道特性信息。
- 方法要点：采用NURBS轨迹表示、CMA-ES全局优化和基于卡尔曼滤波的空间更新，构建自适应约束图。
- 实验或效果：仿真中圈速减少17.38%，真实硬件上在不同摩擦条件下圈速提升7.60%。

## 摘要（原文）

> We present a closed-loop framework for autonomous raceline optimization that combines NURBS-based trajectory representation, CMA-ES global trajectory optimization, and controller-guided spatial feedback. Instead of treating tracking errors as transient disturbances, our method exploits them as informative signals of local track characteristics via a Kalman-inspired spatial update. This enables the construction of an adaptive, acceleration-based constraint map that iteratively refines trajectories toward near-optimal performance under spatially varying track and vehicle behavior. In simulation, our approach achieves a 17.38% lap time reduction compared to a controller parametrized with maximum static acceleration. On real hardware, tested with different tire compounds ranging from high to low friction, we obtain a 7.60% lap time improvement without explicitly parametrizing friction. This demonstrates robustness to changing grip conditions in real-world scenarios.

