---
layout: default
title: Data-driven control of hydraulic impact hammers under strict operational and control constraints
---

# Data-driven control of hydraulic impact hammers under strict operational and control constraints
**arXiv**：[2601.07813v1](https://arxiv.org/abs/2601.07813) · [PDF](https://arxiv.org/pdf/2601.07813.pdf)  
**作者**：Francisco Leiva, Claudio Canales, Michelle Valenzuela, Javier Ruiz-del-Solar  

**一句话要点**：提出数据驱动方法控制液压冲击锤，在严格约束下实现末端执行器目标位姿定位。

**关键词**：数据驱动控制, 液压冲击锤, 系统识别, 强化学习, 模型预测控制, Sim2Real迁移

## 3 点简述
- 核心问题：控制液压冲击锤在有限传感和离散控制接口约束下达到目标位姿。
- 方法要点：通过监督学习从遥操作数据中识别系统动态模型，结合强化学习和模型预测控制进行策略合成。
- 实验或效果：在真实世界中，最佳策略实现位置误差低于12厘米、俯仰角误差低于0.08弧度，仅需约68分钟训练数据。

## 摘要（原文）

> This paper presents a data-driven methodology for the control of static hydraulic impact hammers, also known as rock breakers, which are commonly used in the mining industry. The task addressed in this work is that of controlling the rock-breaker so its end-effector reaches arbitrary target poses, which is required in normal operation to place the hammer on top of rocks that need to be fractured. The proposed approach considers several constraints, such as unobserved state variables due to limited sensing and the strict requirement of using a discrete control interface at the joint level. First, the proposed methodology addresses the problem of system identification to obtain an approximate dynamic model of the hydraulic arm. This is done via supervised learning, using only teleoperation data. The learned dynamic model is then exploited to obtain a controller capable of reaching target end-effector poses. For policy synthesis, both reinforcement learning (RL) and model predictive control (MPC) algorithms are utilized and contrasted. As a case study, we consider the automation of a Bobcat E10 mini-excavator arm with a hydraulic impact hammer attached as end-effector. Using this machine, both the system identification and policy synthesis stages are studied in simulation and in the real world. The best RL-based policy consistently reaches target end-effector poses with position errors below 12 cm and pitch angle errors below 0.08 rad in the real world. Considering that the impact hammer has a 4 cm diameter chisel, this level of precision is sufficient for breaking rocks. Notably, this is accomplished by relying only on approximately 68 min of teleoperation data to train and 8 min to evaluate the dynamic model, and without performing any adjustments for a successful policy Sim2Real transfer. A demonstration of policy execution in the real world can be found in https://youtu.be/e-7tDhZ4ZgA.

