---
layout: default
title: Sim2Swim: Zero-Shot Velocity Control for Agile AUV Maneuvering in 3 Minutes
---

# Sim2Swim: Zero-Shot Velocity Control for Agile AUV Maneuvering in 3 Minutes
**arXiv**：[2512.08656v1](https://arxiv.org/abs/2512.08656) · [PDF](https://arxiv.org/pdf/2512.08656.pdf)  
**作者**：Lauritz Rismark Fosso, Herman Biørn Amundsen, Marios Xanthidis, Sveinung Johan Ohrem  

**一句话要点**：提出Sim2Swim零样本深度强化学习速度控制器，实现水下机器人敏捷6自由度操控

**关键词**：水下机器人控制, 深度强化学习, 零样本学习, 敏捷操控, 域随机化, 仿真到现实

## 3 点简述
- 水下机器人因复杂流体动力学和参数不确定性，敏捷操控面临挑战
- 方法基于深度强化学习，利用域随机化和并行训练，无需调参即可部署
- 实验在池中验证，展示了对多种配置的鲁棒控制和高度敏捷运动

## 摘要（原文）

> Holonomic autonomous underwater vehicles (AUVs) have the hardware ability for agile maneuvering in both translational and rotational degrees of freedom (DOFs). However, due to challenges inherent to underwater vehicles, such as complex hydrostatics and hydrodynamics, parametric uncertainties, and frequent changes in dynamics due to payload changes, control is challenging. Performance typically relies on carefully tuned controllers targeting unique platform configurations, and a need for re-tuning for deployment under varying payloads and hydrodynamic conditions. As a consequence, agile maneuvering with simultaneous tracking of time-varying references in both translational and rotational DOFs is rarely utilized in practice. To the best of our knowledge, this paper presents the first general zero-shot sim2real deep reinforcement learning-based (DRL) velocity controller enabling path following and agile 6DOF maneuvering with a training duration of just 3 minutes. Sim2Swim, the proposed approach, inspired by state-of-the-art DRL-based position control, leverages domain randomization and massively parallelized training to converge to field-deployable control policies for AUVs of variable characteristics without post-processing or tuning. Sim2Swim is extensively validated in pool trials for a variety of configurations, showcasing robust control for highly agile motions.

