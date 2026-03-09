---
layout: default
title: Iterative Convex Optimization with Control Barrier Functions for Obstacle Avoidance among Polytopes
---

# Iterative Convex Optimization with Control Barrier Functions for Obstacle Avoidance among Polytopes
**arXiv**：[2603.05916v1](https://arxiv.org/abs/2603.05916) · [PDF](https://arxiv.org/pdf/2603.05916.pdf)  
**作者**：Shuo Liu, Zhe Huang, Calin A. Belta  

**一句话要点**：提出迭代凸MPC-DCBF框架，用于多面体机器人避障，实现快速在线安全控制。

**关键词**：控制屏障函数, 模型预测控制, 多面体避障, 凸优化, 实时控制, 机器人导航

## 3 点简述
- 核心问题：多面体机器人避障中，现有方法或几何失真或非凸计算，限制实时性能。
- 方法要点：基于精确最近点计算构建线性DCBF约束，结合系统动态局部线性化，确保迭代凸优化。
- 实验或效果：数值实验在杂乱迷宫场景中实现无碰撞导航，求解时间达毫秒级。

## 摘要（原文）

> Obstacle avoidance of polytopic obstacles by polytopic robots is a challenging problem in optimization-based control and trajectory planning. Many existing methods rely on smooth geometric approximations, such as hyperspheres or ellipsoids, which allow differentiable distance expressions but distort the true geometry and restrict the feasible set. Other approaches integrate exact polytope distances into nonlinear model predictive control (MPC), resulting in nonconvex programs that limit real-time performance. In this paper, we construct linear discrete-time control barrier function (DCBF) constraints by deriving supporting hyperplanes from exact closest-point computations between convex polytopes. We then propose a novel iterative convex MPC-DCBF framework, where local linearization of system dynamics and robot geometry ensures convexity of the finite-horizon optimization at each iteration. The resulting formulation reduces computational complexity and enables fast online implementation for safety-critical control and trajectory planning of general nonlinear dynamics. The framework extends to multi-robot and three-dimensional environments. Numerical experiments demonstrate collision-free navigation in cluttered maze scenarios with millisecond-level solve times.

