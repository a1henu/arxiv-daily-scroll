---
layout: default
title: A Fast Semidefinite Convex Relaxation for Optimal Control Problems With Spatio-Temporal Constraints
---

# A Fast Semidefinite Convex Relaxation for Optimal Control Problems With Spatio-Temporal Constraints
**arXiv**：[2601.03055v1](https://arxiv.org/abs/2601.03055) · [PDF](https://arxiv.org/pdf/2601.03055.pdf)  
**作者**：Shiying Dong, Zhipeng Shen, Rudolf Reiter, Hailong Huang, Bingzhao Gao, Hong Chen, Wen-Hua Chen  

**一句话要点**：提出基于时间缩放直接多重打靶和半定凸松弛的方法，以高效求解时空约束下的最优控制问题。

**关键词**：最优控制, 时空约束, 凸松弛, 半定规划, 直接多重打靶, 四旋翼导航

## 3 点简述
- 核心问题：时空约束下最优控制问题因动力学与事件时序耦合导致非凸，求解困难且易次优。
- 方法要点：采用时间缩放直接多重打靶划分预测时域，并开发基于半定规划的快速凸松弛以利用稀疏性。
- 实验或效果：仿真验证了最优性和计算效率，四旋翼飞行器实验展示了在复杂环境中的实际应用性。

## 摘要（原文）

> Solving optimal control problems (OCPs) of autonomous agents operating under spatial and temporal constraints fast and accurately is essential in applications ranging from eco-driving of autonomous vehicles to quadrotor navigation. However, the nonlinear programs approximating the OCPs are inherently nonconvex due to the coupling between the dynamics and the event timing, and therefore, they are challenging to solve. Most approaches address this challenge by predefining waypoint times or just using nonconvex trajectory optimization, which simplifies the problem but often yields suboptimal solutions. To significantly improve the numerical properties, we propose a formulation with a time-scaling direct multiple shooting scheme that partitions the prediction horizon into segments aligned with characteristic time constraints. Moreover, we develop a fast semidefinite-programming-based convex relaxation that exploits the sparsity pattern of the lifted formulation. Comprehensive simulation studies demonstrate the solution optimality and computational efficiency. Furthermore, real-world experiments on a quadrotor waypoint flight task with constrained open time windows validate the practical applicability of the approach in complex environments.

