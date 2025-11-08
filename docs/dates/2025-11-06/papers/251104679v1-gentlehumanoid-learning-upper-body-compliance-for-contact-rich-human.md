---
layout: default
title: GentleHumanoid: Learning Upper-body Compliance for Contact-rich Human and Object Interaction
---

# GentleHumanoid: Learning Upper-body Compliance for Contact-rich Human and Object Interaction
**arXiv**：[2511.04679v1](https://arxiv.org/abs/2511.04679) · [PDF](https://arxiv.org/pdf/2511.04679.pdf)  
**作者**：Qingzhou Lu, Yao Feng, Baiyu Shi, Michael Piseno, Zhenan Bao, C. Karen Liu  

**一句话要点**：提出GentleHumanoid框架，通过集成阻抗控制实现上半身柔顺，以支持人机安全交互。

**关键词**：人形机器人, 阻抗控制, 强化学习, 物理交互, 柔顺控制, 运动跟踪

## 3 点简述
- 问题：人形机器人交互中，现有强化学习策略强调刚性跟踪，抑制外力，缺乏柔顺性。
- 方法：统一弹簧模型模拟阻力和引导接触，确保肩、肘、腕运动一致，并调整力阈值保障安全。
- 效果：在仿真和Unitree G1机器人上测试，减少峰值接触力，任务成功且交互更平滑自然。

## 摘要（原文）

> Humanoid robots are expected to operate in human-centered environments where
> safe and natural physical interaction is essential. However, most recent
> reinforcement learning (RL) policies emphasize rigid tracking and suppress
> external forces. Existing impedance-augmented approaches are typically
> restricted to base or end-effector control and focus on resisting extreme
> forces rather than enabling compliance. We introduce GentleHumanoid, a
> framework that integrates impedance control into a whole-body motion tracking
> policy to achieve upper-body compliance. At its core is a unified spring-based
> formulation that models both resistive contacts (restoring forces when pressing
> against surfaces) and guiding contacts (pushes or pulls sampled from human
> motion data). This formulation ensures kinematically consistent forces across
> the shoulder, elbow, and wrist, while exposing the policy to diverse
> interaction scenarios. Safety is further supported through task-adjustable
> force thresholds. We evaluate our approach in both simulation and on the
> Unitree G1 humanoid across tasks requiring different levels of compliance,
> including gentle hugging, sit-to-stand assistance, and safe object
> manipulation. Compared to baselines, our policy consistently reduces peak
> contact forces while maintaining task success, resulting in smoother and more
> natural interactions. These results highlight a step toward humanoid robots
> that can safely and effectively collaborate with humans and handle objects in
> real-world environments.

