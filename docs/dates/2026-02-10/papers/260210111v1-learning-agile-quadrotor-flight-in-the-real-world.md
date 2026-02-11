---
layout: default
title: Learning Agile Quadrotor Flight in the Real World
---

# Learning Agile Quadrotor Flight in the Real World
**arXiv**：[2602.10111v1](https://arxiv.org/abs/2602.10111) · [PDF](https://arxiv.org/pdf/2602.10111.pdf)  
**作者**：Yunfan Ren, Zhiyuan Zhu, Jiaxu Xing, Davide Scaramuzza  

**一句话要点**：提出自适应框架以在真实世界中实现敏捷四旋翼飞行，无需精确系统辨识或离线仿真迁移。

**关键词**：四旋翼飞行控制, 在线自适应学习, 真实世界强化学习, 敏捷机动, 模型残差学习, 实时策略更新

## 3 点简述
- 核心问题：基于学习的控制器依赖仿真训练，易受分布外场景影响，导致保守性能限制敏捷性。
- 方法要点：引入自适应时间缩放探索物理极限，结合在线残差学习和实时锚定短时反向传播进行策略更新。
- 实验或效果：在约100秒飞行时间内，将保守策略峰值速度从1.9 m/s提升至7.3 m/s，实现近执行器饱和极限的敏捷机动。

## 摘要（原文）

> Learning-based controllers have achieved impressive performance in agile quadrotor flight but typically rely on massive training in simulation, necessitating accurate system identification for effective Sim2Real transfer. However, even with precise modeling, fixed policies remain susceptible to out-of-distribution scenarios, ranging from external aerodynamic disturbances to internal hardware degradation. To ensure safety under these evolving uncertainties, such controllers are forced to operate with conservative safety margins, inherently constraining their agility outside of controlled settings. While online adaptation offers a potential remedy, safely exploring physical limits remains a critical bottleneck due to data scarcity and safety risks. To bridge this gap, we propose a self-adaptive framework that eliminates the need for precise system identification or offline Sim2Real transfer. We introduce Adaptive Temporal Scaling (ATS) to actively explore platform physical limits, and employ online residual learning to augment a simple nominal model. {Based on the learned hybrid model, we further propose Real-world Anchored Short-horizon Backpropagation Through Time (RASH-BPTT) to achieve efficient and robust in-flight policy updates. Extensive experiments demonstrate that our quadrotor reliably executes agile maneuvers near actuator saturation limits. The system evolves a conservative base policy with a peak speed of 1.9 m/s to 7.3 m/s within approximately 100 seconds of flight time. These findings underscore that real-world adaptation serves not merely to compensate for modeling errors, but as a practical mechanism for sustained performance improvement in aggressive flight regimes.

