---
layout: default
title: Decoupled MPPI-Based Multi-Arm Motion Planning
---

# Decoupled MPPI-Based Multi-Arm Motion Planning
**arXiv**：[2602.10114v1](https://arxiv.org/abs/2602.10114) · [PDF](https://arxiv.org/pdf/2602.10114.pdf)  
**作者**：Dan Evron, Elias Goldsztejn, Ronen I. Brafman  

**一句话要点**：提出MR-STORM算法以解决多机械臂运动规划中的扩展性问题

**关键词**：多机械臂运动规划, 采样算法, 模型预测控制, 分布式规划, 动态障碍物处理

## 3 点简述
- 核心问题：现有基于采样的多臂联合规划算法扩展性差，难以高效处理动态障碍物
- 方法要点：扩展STORM算法，采用分布式方式让各臂独立规划并共享路径，并引入动态优先级机制
- 实验或效果：在静态和动态障碍物场景下，MR-STORM相比SOTA算法展现出明显实证优势

## 摘要（原文）

> Recent advances in sampling-based motion planning algorithms for high DOF arms leverage GPUs to provide SOTA performance. These algorithms can be used to control multiple arms jointly, but this approach scales poorly. To address this, we extend STORM, a sampling-based model-predictive-control (MPC) motion planning algorithm, to handle multiple robots in a distributed fashion. First, we modify STORM to handle dynamic obstacles. Then, we let each arm compute its own motion plan prefix, which it shares with the other arms, which treat it as a dynamic obstacle. Finally, we add a dynamic priority scheme. The new algorithm, MR-STORM, demonstrates clear empirical advantages over SOTA algorithms when operating with both static and dynamic obstacles.

