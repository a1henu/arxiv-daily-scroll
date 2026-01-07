---
layout: default
title: Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation
---

# Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation
**arXiv**：[2601.02778v1](https://arxiv.org/abs/2601.02778) · [PDF](https://arxiv.org/pdf/2601.02778.pdf)  
**作者**：Haoyu Dong, Zhengmao He, Yang Li, Zhibin Li, Xinyu Yi, Zhe Zhao  

**一句话要点**：提出基于触觉与扭矩的强化学习框架，实现灵巧手零样本仿真到真实部署，用于可控抓取与操作。

**关键词**：灵巧手操作, 仿真到真实迁移, 强化学习, 触觉反馈, 扭矩感知, 零样本部署

## 3 点简述
- 核心问题：灵巧手控制策略难以直接部署到真实硬件，因接触物理复杂和驱动不完美。
- 方法要点：结合密集触觉反馈与关节扭矩感知，通过快速触觉仿真、电流-扭矩校准和驱动动态建模实现仿真到真实迁移。
- 实验或效果：在五指手上直接部署策略，实现可控抓取力跟踪和物体重定向，无需真实机器人微调。

## 摘要（原文）

> Human-like dexterous hands with multiple fingers offer human-level manipulation capabilities, but training control policies that can directly deploy on real hardware remains difficult due to contact-rich physics and imperfect actuation. We close this gap with a practical sim-to-real reinforcement learning (RL) framework that utilizes dense tactile feedback combined with joint torque sensing to explicitly regulate physical interactions. To enable effective sim-to-real transfer, we introduce (i) a computationally fast tactile simulation that computes distances between dense virtual tactile units and the object via parallel forward kinematics, providing high-rate, high-resolution touch signals needed by RL; (ii) a current-to-torque calibration that eliminates the need for torque sensors on dexterous hands by mapping motor current to joint torque; and (iii) actuator dynamics modeling to bridge the actuation gaps with randomization of non-ideal effects such as backlash, torque-speed saturation. Using an asymmetric actor-critic PPO pipeline trained entirely in simulation, our policies deploy directly to a five-finger hand. The resulting policies demonstrated two essential skills: (1) command-based, controllable grasp force tracking, and (2) reorientation of objects in the hand, both of which were robustly executed without fine-tuning on the robot. By combining tactile and torque in the observation space with effective sensing/actuation modeling, our system provides a practical solution to achieve reliable dexterous manipulation. To our knowledge, this is the first demonstration of controllable grasping on a multi-finger dexterous hand trained entirely in simulation and transferred zero-shot on real hardware.

