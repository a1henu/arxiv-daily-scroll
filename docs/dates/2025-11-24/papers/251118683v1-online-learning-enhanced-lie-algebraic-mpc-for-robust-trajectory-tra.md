---
layout: default
title: Online Learning-Enhanced Lie Algebraic MPC for Robust Trajectory Tracking of Autonomous Surface Vehicles
---

# Online Learning-Enhanced Lie Algebraic MPC for Robust Trajectory Tracking of Autonomous Surface Vehicles
**arXiv**：[2511.18683v1](https://arxiv.org/abs/2511.18683) · [PDF](https://arxiv.org/pdf/2511.18683.pdf)  
**作者**：Yinan Dong, Ziyu Xu, Tsimafei Lazouski, Sangli Teng, Maani Ghaffari  

**一句话要点**：提出结合李群MPC与在线学习的控制器，以解决自主水面艇在未知扰动下的轨迹跟踪问题。

**关键词**：自主水面艇, 轨迹跟踪, 李群MPC, 在线学习, 扰动补偿, 鲁棒控制

## 3 点简述
- 核心问题：自主水面艇易受风浪等环境扰动影响，轨迹跟踪在动态海洋条件下困难。
- 方法要点：结合李群上的凸误差状态MPC与在线学习模块，实时补偿未知扰动。
- 实验或效果：在仿真和真实实验中，相比现有方法，在各种扰动场景下实现更高跟踪精度。

## 摘要（原文）

> Autonomous surface vehicles (ASVs) are easily influenced by environmental disturbances such as wind and waves, making accurate trajectory tracking a persistent challenge in dynamic marine conditions. In this paper, we propose an efficient controller for trajectory tracking of marine vehicles under unknown disturbances by combining a convex error-state MPC on the Lie group with an online learning module to compensate for these disturbances in real time. This design enables adaptive and robust control while maintaining computational efficiency. Extensive evaluations in numerical simulations, the Virtual RobotX (VRX) simulator, and real-world field experiments demonstrate that our method achieves superior tracking accuracy under various disturbance scenarios compared with existing approaches.

