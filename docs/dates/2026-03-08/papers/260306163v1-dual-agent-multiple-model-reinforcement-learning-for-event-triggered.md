---
layout: default
title: Dual-Agent Multiple-Model Reinforcement Learning for Event-Triggered Human-Robot Co-Adaptation in Decoupled Task Spaces
---

# Dual-Agent Multiple-Model Reinforcement Learning for Event-Triggered Human-Robot Co-Adaptation in Decoupled Task Spaces
**arXiv**：[2603.06163v1](https://arxiv.org/abs/2603.06163) · [PDF](https://arxiv.org/pdf/2603.06163.pdf)  
**作者**：Yaqi Li, Zhengqi Han, Huifang Liu, Steven W. Su  

**一句话要点**：提出双代理多模型强化学习，用于解耦任务空间中事件触发的人机协同适应控制。

**关键词**：人机协同控制, 事件触发控制, 强化学习, 解耦任务空间, 康复机器人, 轨迹优化

## 3 点简述
- 核心问题：传统固定频率控制在复杂到达任务中因逆运动学执行时间变化导致轨迹振荡。
- 方法要点：采用事件驱动策略，仅在末端执行器进入目标点准入球时触发控制动作，结合DAMMRL框架优化人机协同。
- 实验或效果：在半虚拟设置中验证，有效抑制路径点抖动，平衡空间精度与时间效率，提升物体获取任务成功率。

## 摘要（原文）

> This paper presents a shared-control rehabilitation policy for a custom 6-degree-of-freedom (6-DoF) upper-limb robot that decomposes complex reaching tasks into decoupled spatial axes. The patient governs the primary reaching direction using binary commands, while the robot autonomously manages orthogonal corrective motions. Because traditional fixed-frequency control often induces trajectory oscillations due to variable inverse-kinematics execution times, an event-driven progression strategy is proposed. This architecture triggers subsequent control actions only when the end-effector enters an admission sphere centred on the immediate target waypoint, and was validated in a semi-virtual setup linking a physical pressure sensor to a MuJoCo simulation. To optimise human--robot co-adaptation safely and efficiently, this study introduces Dual Agent Multiple Model Reinforcement Learning (DAMMRL). This framework discretises decision characteristics: the human agent selects the admission sphere radius to reflect their inherent speed--accuracy trade-off, while the robot agent dynamically adjusts its 3D Cartesian step magnitudes to complement the user's cognitive state. Trained in simulation and deployed across mixed environments, this event-triggered DAMMRL approach effectively suppresses waypoint chatter, balances spatial precision with temporal efficiency, and significantly improves success rates in object acquisition tasks.

