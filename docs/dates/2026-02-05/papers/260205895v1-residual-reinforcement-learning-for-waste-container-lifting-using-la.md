---
layout: default
title: Residual Reinforcement Learning for Waste-Container Lifting Using Large-Scale Cranes with Underactuated Tools
---

# Residual Reinforcement Learning for Waste-Container Lifting Using Large-Scale Cranes with Underactuated Tools
**arXiv**：[2602.05895v1](https://arxiv.org/abs/2602.05895) · [PDF](https://arxiv.org/pdf/2602.05895.pdf)  
**作者**：Qi Li, Karsten Berns  

**一句话要点**：提出残差强化学习方法，结合名义控制器提升大型起重机在垃圾容器吊装任务中的精度与鲁棒性。

**关键词**：残差强化学习, 起重机控制, 摆动抑制, 仿真实验, 鲁棒性提升

## 3 点简述
- 研究城市环境中垃圾容器吊装任务，涉及几何公差小、摆动抑制难的挑战。
- 方法结合名义笛卡尔控制器与PPO训练的残差策略，补偿未建模动态和参数变化。
- 仿真实验显示，相比单独名义控制器，提高了跟踪精度、减少振荡并提升吊装成功率。

## 摘要（原文）

> This paper studies the container lifting phase of a waste-container recycling task in urban environments, performed by a hydraulic loader crane equipped with an underactuated discharge unit, and proposes a residual reinforcement learning (RRL) approach that combines a nominal Cartesian controller with a learned residual policy. All experiments are conducted in simulation, where the task is characterized by tight geometric tolerances between the discharge-unit hooks and the container rings relative to the overall crane scale, making precise trajectory tracking and swing suppression essential. The nominal controller uses admittance control for trajectory tracking and pendulum-aware swing damping, followed by damped least-squares inverse kinematics with a nullspace posture term to generate joint velocity commands. A PPO-trained residual policy in Isaac Lab compensates for unmodeled dynamics and parameter variations, improving precision and robustness without requiring end-to-end learning from scratch. We further employ randomized episode initialization and domain randomization over payload properties, actuator gains, and passive joint parameters to enhance generalization. Simulation results demonstrate improved tracking accuracy, reduced oscillations, and higher lifting success rates compared to the nominal controller alone.

