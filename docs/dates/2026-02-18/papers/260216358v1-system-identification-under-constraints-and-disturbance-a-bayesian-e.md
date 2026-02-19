---
layout: default
title: System Identification under Constraints and Disturbance: A Bayesian Estimation Approach
---

# System Identification under Constraints and Disturbance: A Bayesian Estimation Approach
**arXiv**：[2602.16358v1](https://arxiv.org/abs/2602.16358) · [PDF](https://arxiv.org/pdf/2602.16358.pdf)  
**作者**：Sergi Martinez, Steve Tonneau, Carlos Mastalli  

**一句话要点**：提出贝叶斯系统辨识框架，用于机器人状态轨迹和物理参数的高精度联合估计。

**关键词**：贝叶斯系统辨识, 机器人状态估计, 物理参数辨识, 约束优化, 能量观测, 模型预测控制

## 3 点简述
- 核心问题：机器人系统辨识中状态轨迹和物理参数估计的精度不足，受约束和扰动影响。
- 方法要点：嵌入物理约束和能量观测，推导参数化等式约束Riccati递归以提升可扩展性。
- 实验或效果：在仿真和硬件实验中，相比基线方法，收敛更快、估计误差更低、接触一致性更好。

## 摘要（原文）

> We introduce a Bayesian system identification (SysID) framework for jointly estimating robot's state trajectories and physical parameters with high accuracy. It embeds physically consistent inverse dynamics, contact and loop-closure constraints, and fully featured joint friction models as hard, stage-wise equality constraints. It relies on energy-based regressors to enhance parameter observability, supports both equality and inequality priors on inertial and actuation parameters, enforces dynamically consistent disturbance projections, and augments proprioceptive measurements with energy observations to disambiguate nonlinear friction effects. To ensure scalability, we derive a parameterized equality-constrained Riccati recursion that preserves the banded structure of the problem, achieving linear complexity in the time horizon, and develop computationally efficient derivatives. Simulation studies on representative robotic systems, together with hardware experiments on a Unitree B1 equipped with a Z1 arm, demonstrate faster convergence, lower inertial and friction estimation errors, and improved contact consistency compared to forward-dynamics and decoupled identification baselines. When deployed within model predictive control frameworks, the resulting models yield measurable improvements in tracking performance during locomotion over challenging environments.

