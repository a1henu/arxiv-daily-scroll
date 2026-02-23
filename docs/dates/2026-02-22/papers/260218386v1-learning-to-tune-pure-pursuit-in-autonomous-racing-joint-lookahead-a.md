---
layout: default
title: Learning to Tune Pure Pursuit in Autonomous Racing: Joint Lookahead and Steering-Gain Control with PPO
---

# Learning to Tune Pure Pursuit in Autonomous Racing: Joint Lookahead and Steering-Gain Control with PPO
**arXiv**：[2602.18386v1](https://arxiv.org/abs/2602.18386) · [PDF](https://arxiv.org/pdf/2602.18386.pdf)  
**作者**：Mohamed Elgouhary, Amr S. El-Wakeel  

**一句话要点**：提出基于PPO的强化学习方法，联合在线调整纯追踪算法的前瞻距离和转向增益，以提升自动驾驶赛车路径跟踪性能。

**关键词**：自动驾驶赛车, 纯追踪算法, 强化学习, 参数调优, 路径跟踪, PPO算法

## 3 点简述
- 纯追踪算法在自动驾驶赛车中性能高度依赖前瞻距离和转向增益的参数选择，传统速度调度方法适应性差。
- 使用PPO强化学习策略，基于速度和曲率特征在线联合输出前瞻距离和转向增益，无需针对不同赛道重新调参。
- 在仿真和实车测试中，该方法在圈时、路径跟踪精度和转向平滑度上优于固定参数、自适应调度及仅调整前瞻距离的变体，并超越运动学MPC跟踪器。

## 摘要（原文）

> Pure Pursuit (PP) is widely used in autonomous racing for real-time path tracking due to its efficiency and geometric clarity, yet performance is highly sensitive to how key parameters-lookahead distance and steering gain-are chosen. Standard velocity-based schedules adjust these only approximately and often fail to transfer across tracks and speed profiles. We propose a reinforcement-learning (RL) approach that jointly chooses the lookahead Ld and a steering gain g online using Proximal Policy Optimization (PPO). The policy observes compact state features (speed and curvature taps) and outputs (Ld, g) at each control step. Trained in F1TENTH Gym and deployed in a ROS 2 stack, the policy drives PP directly (with light smoothing) and requires no per-map retuning. Across simulation and real-car tests, the proposed RL-PP controller that jointly selects (Ld, g) consistently outperforms fixed-lookahead PP, velocity-scheduled adaptive PP, and an RL lookahead-only variant, and it also exceeds a kinematic MPC raceline tracker under our evaluated settings in lap time, path-tracking accuracy, and steering smoothness, demonstrating that policy-guided parameter tuning can reliably improve classical geometry-based control.

