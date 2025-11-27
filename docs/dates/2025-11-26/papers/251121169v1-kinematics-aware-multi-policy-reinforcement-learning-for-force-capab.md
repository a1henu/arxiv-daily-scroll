---
layout: default
title: Kinematics-Aware Multi-Policy Reinforcement Learning for Force-Capable Humanoid Loco-Manipulation
---

# Kinematics-Aware Multi-Policy Reinforcement Learning for Force-Capable Humanoid Loco-Manipulation
**arXiv**：[2511.21169v1](https://arxiv.org/abs/2511.21169) · [PDF](https://arxiv.org/pdf/2511.21169.pdf)  
**作者**：Kaiyan Xiao, Zihan Xu, Cheng Zhe, Chengju Liu, Qijun Chen  

**一句话要点**：提出基于强化学习的解耦三阶段框架，以解决人形机器人在高负载工业场景中的灵巧与主动力交互问题。

**关键词**：人形机器人, 强化学习, 运动学先验, 力交互, 课程学习, 解耦策略

## 3 点简述
- 核心问题：现有方法在灵巧操作上不足，难以满足高负载工业对灵巧性和主动力交互的复合需求。
- 方法要点：采用解耦三阶段训练，包括上体策略、下体策略和增量命令策略，嵌入运动学先验加速收敛。
- 实验或效果：上体策略通过启发式奖励函数快速收敛，下体策略基于力课程学习主动调控环境力。

## 摘要（原文）

> Humanoid robots, with their human-like morphology, hold great potential for industrial applications. However, existing loco-manipulation methods primarily focus on dexterous manipulation, falling short of the combined requirements for dexterity and proactive force interaction in high-load industrial scenarios. To bridge this gap, we propose a reinforcement learning-based framework with a decoupled three-stage training pipeline, consisting of an upper-body policy, a lower-body policy, and a delta-command policy. To accelerate upper-body training, a heuristic reward function is designed. By implicitly embedding forward kinematics priors, it enables the policy to converge faster and achieve superior performance. For the lower body, a force-based curriculum learning strategy is developed, enabling the robot to actively exert and regulate interaction forces with the environment.

