---
layout: default
title: Safety Reinforced Model Predictive Control (SRMPC): Improving MPC with Reinforcement Learning for Motion Planning in Autonomous Driving
---

# Safety Reinforced Model Predictive Control (SRMPC): Improving MPC with Reinforcement Learning for Motion Planning in Autonomous Driving
**arXiv**：[2512.03774v1](https://arxiv.org/abs/2512.03774) · [PDF](https://arxiv.org/pdf/2512.03774.pdf)  
**作者**：Johannes Fischer, Marlon Steiner, Ömer Sahin Tas, Christoph Stiller  

**一句话要点**：提出安全强化模型预测控制（SRMPC），结合强化学习改进自动驾驶运动规划中的MPC性能。

**关键词**：模型预测控制, 安全强化学习, 自动驾驶运动规划, 约束强化学习, 全局优化

## 3 点简述
- 核心问题：MPC在实时规划中依赖凸近似，可能限制解空间，无法找到全局最优。
- 方法要点：使用安全强化学习（SRL）在MPC中生成安全参考轨迹，结合约束强化学习（CRL）确保安全，学习状态依赖拉格朗日乘子。
- 实验或效果：在高速公路场景中实验，SRMPC在安全性和性能上优于MPC和SRL。

## 摘要（原文）

> Model predictive control (MPC) is widely used for motion planning, particularly in autonomous driving. Real-time capability of the planner requires utilizing convex approximation of optimal control problems (OCPs) for the planner. However, such approximations confine the solution to a subspace, which might not contain the global optimum. To address this, we propose using safe reinforcement learning (SRL) to obtain a new and safe reference trajectory within MPC. By employing a learning-based approach, the MPC can explore solutions beyond the close neighborhood of the previous one, potentially finding global optima. We incorporate constrained reinforcement learning (CRL) to ensure safety in automated driving, using a handcrafted energy function-based safety index as the constraint objective to model safe and unsafe regions. Our approach utilizes a state-dependent Lagrangian multiplier, learned concurrently with the safe policy, to solve the CRL problem. Through experimentation in a highway scenario, we demonstrate the superiority of our approach over both MPC and SRL in terms of safety and performance measures.

