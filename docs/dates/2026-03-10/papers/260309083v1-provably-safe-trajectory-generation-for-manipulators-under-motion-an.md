---
layout: default
title: Provably Safe Trajectory Generation for Manipulators Under Motion and Environmental Uncertainties
---

# Provably Safe Trajectory Generation for Manipulators Under Motion and Environmental Uncertainties
**arXiv**：[2603.09083v1](https://arxiv.org/abs/2603.09083) · [PDF](https://arxiv.org/pdf/2603.09083.pdf)  
**作者**：Fei Meng, Zijiang Yang, Xinyu Mao, Haobo Liang, Max Q. -H. Meng  

**一句话要点**：提出风险有界运动规划框架，以解决机械臂在不确定非凸环境中的安全轨迹生成问题。

**关键词**：机械臂运动规划, 风险有界控制, 随机Koopman算子, 平方和规划, 模型预测路径积分控制, 人机协作

## 3 点简述
- 核心问题：机械臂在不确定非凸环境中运动规划缺乏高效且形式化认证的碰撞风险保证。
- 方法要点：集成刚性机械臂深度随机Koopman算子模型预测状态分布，结合可并行物理仿真与平方和规划进行分层验证。
- 实验或效果：在两种典型机械臂上通过仿真和真实实验验证，包括人机协作场景，展示安全高效轨迹生成能力。

## 摘要（原文）

> Robot manipulators operating in uncertain and non-convex environments present significant challenges for safe and optimal motion planning. Existing methods often struggle to provide efficient and formally certified collision risk guarantees, particularly when dealing with complex geometries and non-Gaussian uncertainties. This article proposes a novel risk-bounded motion planning framework to address this unmet need. Our approach integrates a rigid manipulator deep stochastic Koopman operator (RM-DeSKO) model to robustly predict the robot's state distribution under motion uncertainty. We then introduce an efficient, hierarchical verification method that combines parallelizable physics simulations with sum-of-squares (SOS) programming as a filter for fine-grained, formal certification of collision risk. This method is embedded within a Model Predictive Path Integral (MPPI) controller that uniquely utilizes binary collision information from SOS decomposition to improve its policy. The effectiveness of the proposed framework is validated on two typical robot manipulators through extensive simulations and real-world experiments, including a challenging human-robot collaboration scenario, demonstrating sim-to-real transfer of the learned model and its ability to generate safe and efficient trajectories in complex, uncertain settings.

