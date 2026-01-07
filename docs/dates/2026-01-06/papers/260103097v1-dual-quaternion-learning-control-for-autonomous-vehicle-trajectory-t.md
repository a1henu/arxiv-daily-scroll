---
layout: default
title: Dual-quaternion learning control for autonomous vehicle trajectory tracking with safety guarantees
---

# Dual-quaternion learning control for autonomous vehicle trajectory tracking with safety guarantees
**arXiv**：[2601.03097v1](https://arxiv.org/abs/2601.03097) · [PDF](https://arxiv.org/pdf/2601.03097.pdf)  
**作者**：Omayra Yago Nieto, Alexandre Anahory Simoes, Juan I. Giribet, Leonardo Colombo  

**一句话要点**：提出基于对偶四元数学习的轨迹跟踪控制器，用于自主车辆在SE(3)运动中的安全保证控制。

**关键词**：轨迹跟踪控制, 对偶四元数, 高斯过程回归, SE(3)运动, 自主机器人, 稳定性分析

## 3 点简述
- 核心问题：自主机器人平台在SE(3)运动中的轨迹跟踪，受未知状态依赖扰动和建模不完美影响。
- 方法要点：结合高斯过程回归与几何反馈律，在线学习补偿扰动，保持刚体运动代数结构。
- 实验或效果：仿真显示在磁力计扰动等局部干扰下实现准确平滑跟踪，提供概率稳定性保证。

## 摘要（原文）

> We propose a learning-based trajectory tracking controller for autonomous robotic platforms whose motion can be described kinematically on $\mathrm{SE}(3)$. The controller is formulated in the dual quaternion framework and operates at the velocity level, assuming direct command of angular and linear velocities, as is standard in many aerial vehicles and omnidirectional mobile robots. Gaussian Process (GP) regression is integrated into a geometric feedback law to learn and compensate online for unknown, state-dependent disturbances and modeling imperfections affecting both attitude and position, while preserving the algebraic structure and coupling properties inherent to rigid-body motion.
>   The proposed approach does not rely on explicit parametric models of the unknown effects, making it well-suited for robotic systems subject to sensor-induced disturbances, unmodeled actuation couplings, and environmental uncertainties. A Lyapunov-based analysis establishes probabilistic ultimate boundedness of the pose tracking error under bounded GP uncertainty, providing formal stability guarantees for the learning-based controller.
>   Simulation results demonstrate accurate and smooth trajectory tracking in the presence of realistic, localized disturbances, including correlated rotational and translational effects arising from magnetometer perturbations. These results illustrate the potential of combining geometric modeling and probabilistic learning to achieve robust, data-efficient pose control for autonomous robotic systems.

