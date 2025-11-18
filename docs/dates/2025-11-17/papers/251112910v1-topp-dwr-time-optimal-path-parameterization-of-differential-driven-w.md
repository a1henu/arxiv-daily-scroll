---
layout: default
title: TOPP-DWR: Time-Optimal Path Parameterization of Differential-Driven Wheeled Robots Considering Piecewise-Constant Angular Velocity Constraints
---

# TOPP-DWR: Time-Optimal Path Parameterization of Differential-Driven Wheeled Robots Considering Piecewise-Constant Angular Velocity Constraints
**arXiv**：[2511.12910v1](https://arxiv.org/abs/2511.12910) · [PDF](https://arxiv.org/pdf/2511.12910.pdf)  
**作者**：Yong Li, Yujun Huang, Yi Chen, Hui Cheng  

**一句话要点**：提出TOPP-DWR算法，为差动轮式机器人实现时间最优路径参数化，考虑角速度等约束。

**关键词**：时间最优路径参数化, 差动轮式机器人, 角速度约束, 二阶锥规划, 轨迹优化, 自主导航

## 3 点简述
- 核心问题：现有TOPP方法忽略角速度和关节速度约束，导致实际控制性能下降。
- 方法要点：采用非均匀B样条表示轨迹，将约束统一为线性速度约束，并转化为SOCP问题求解。
- 实验或效果：比较实验验证算法优越性，现场导航实验证明其在实际应用中的实用性。

## 摘要（原文）

> Differential-driven wheeled robots (DWR) represent the quintessential type of mobile robots and find extensive appli- cations across the robotic field. Most high-performance control approaches for DWR explicitly utilize the linear and angular velocities of the trajectory as control references. However, existing research on time-optimal path parameterization (TOPP) for mobile robots usually neglects the angular velocity and joint vel- ocity constraints, which can result in degraded control perfor- mance in practical applications. In this article, a systematic and practical TOPP algorithm named TOPP-DWR is proposed for DWR and other mobile robots. First, the non-uniform B-spline is adopted to represent the initial trajectory in the task space. Second, the piecewise-constant angular velocity, as well as joint velocity, linear velocity, and linear acceleration constraints, are incorporated into the TOPP problem. During the construction of the optimization problem, the aforementioned constraints are uniformly represented as linear velocity constraints. To boost the numerical computational efficiency, we introduce a slack variable to reformulate the problem into second-order-cone programming (SOCP). Subsequently, comparative experiments are conducted to validate the superiority of the proposed method. Quantitative performance indexes show that TOPP-DWR achieves TOPP while adhering to all constraints. Finally, field autonomous navigation experiments are carried out to validate the practicability of TOPP-DWR in real-world applications.

