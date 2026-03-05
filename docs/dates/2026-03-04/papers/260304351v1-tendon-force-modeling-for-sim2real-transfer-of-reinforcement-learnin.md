---
layout: default
title: Tendon Force Modeling for Sim2Real Transfer of Reinforcement Learning Policies for Tendon-Driven Robots
---

# Tendon Force Modeling for Sim2Real Transfer of Reinforcement Learning Policies for Tendon-Driven Robots
**arXiv**：[2603.04351v1](https://arxiv.org/abs/2603.04351) · [PDF](https://arxiv.org/pdf/2603.04351.pdf)  
**作者**：Valentin Yuryev, Josie Hughes  

**一句话要点**：提出肌腱力建模方法以缩小肌腱驱动机器人强化学习策略的仿真到现实差距

**关键词**：肌腱驱动机器人, 仿真到现实迁移, 强化学习, 肌腱力建模, 变压器模型, 机器人控制

## 3 点简述
- 肌腱驱动机器人控制复杂，仿真与强化学习结合存在仿真到现实差距问题
- 基于上下文历史和新型测试台数据，开发变压器模型预测肌腱力，误差在最大电机力的3%内
- 集成模型到仿真训练强化学习控制器，仿真到现实差距减少41%，指尖姿态跟踪任务性能提升50%

## 摘要（原文）

> Robots which make use of soft or compliant inter- actions often leverage tendon-driven actuation which enables actuators to be placed more flexibly, and compliance to be maintained. However, controlling complex tendon systems is challenging. Simulation paired with reinforcement learning (RL) could be enable more complex behaviors to be generated. Such methods rely on torque and force-based simulation roll- outs which are limited by the sim-to-real gap, stemming from the actuator and system dynamics, resulting in poor transfer of RL policies onto real robots. To address this, we propose a method to model the tendon forces produced by typical servo motors, focusing specifically on the transfer of RL policies for a tendon driven finger. Our approach extends existing data- driven techniques by leveraging contextual history and a novel data collection test-bench. This test-bench allows us to capture tendon forces undergo contact-rich interactions typical of real- world manipulation. We then utilize our force estimation model in a GPU-accelerated tendon force-driven rigid body simulation to train RL-based controllers. Our transformer-based model is capable of predicting tendon forces within 3% of the maximum motor force and is robot-agnostic. By integrating our learned model into simulation, we reduce the sim-to-real gap for test trajectories by 41%. RL-based controller trained with our model achieves a 50% improvement in fingertip pose tracking tasks on real tendon-driven robotic fingers. This approach is generalizable to different actuators and robot systems, and can enable RL policies to be used widely across tendon systems, advancing capabilities of dexterous manipulators and soft robots.

