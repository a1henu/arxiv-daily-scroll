---
layout: default
title: SENSE-STEP: Learning Sim-to-Real Locomotion for a Sensory-Enabled Soft Quadruped Robot
---

# SENSE-STEP: Learning Sim-to-Real Locomotion for a Sensory-Enabled Soft Quadruped Robot
**arXiv**：[2602.13078v1](https://arxiv.org/abs/2602.13078) · [PDF](https://arxiv.org/pdf/2602.13078.pdf)  
**作者**：Storm de Kam, Ebrahim Shahabi, Cosimo Della Santina  

**一句话要点**：提出SENSE-STEP学习框架，通过仿真到现实训练实现软体四足机器人的闭环运动控制

**关键词**：软体机器人, 仿真到现实学习, 四足运动控制, 触觉反馈, 气动驱动, 闭环控制

## 3 点简述
- 核心问题：软体四足机器人因高维动力学和接触交互建模困难，传统本体感知在闭环运动中受限
- 方法要点：基于学习控制框架，结合本体和触觉反馈，通过分阶段仿真训练优化气动和吸盘控制
- 实验或效果：在真实机器人上验证，闭环策略在平坦和倾斜表面提升速度，触觉和惯性反馈显著稳定运动

## 摘要（原文）

> Robust closed-loop locomotion remains challenging for soft quadruped robots due to high-dimensional dynamics, actuator hysteresis, and difficult-to-model contact interactions, while conventional proprioception provides limited information about ground contact. In this paper, we present a learning-based control framework for a pneumatically actuated soft quadruped equipped with tactile suction-cup feet, and we validate the approach experimentally on physical hardware. The control policy is trained in simulation through a staged learning process that starts from a reference gait and is progressively refined under randomized environmental conditions. The resulting controller maps proprioceptive and tactile feedback to coordinated pneumatic actuation and suction-cup commands, enabling closed-loop locomotion on flat and inclined surfaces. When deployed on the real robot, the closed-loop policy outperforms an open-loop baseline, increasing forward speed by 41% on a flat surface and by 91% on a 5-degree incline. Ablation studies further demonstrate the role of tactile force estimates and inertial feedback in stabilizing locomotion, with performance improvements of up to 56% compared to configurations without sensory feedback.

