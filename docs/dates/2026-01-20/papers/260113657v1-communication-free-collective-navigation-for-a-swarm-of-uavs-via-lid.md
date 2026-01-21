---
layout: default
title: Communication-Free Collective Navigation for a Swarm of UAVs via LiDAR-Based Deep Reinforcement Learning
---

# Communication-Free Collective Navigation for a Swarm of UAVs via LiDAR-Based Deep Reinforcement Learning
**arXiv**：[2601.13657v1](https://arxiv.org/abs/2601.13657) · [PDF](https://arxiv.org/pdf/2601.13657.pdf)  
**作者**：Myong-Yol Choi, Hankyoul Ko, Hanse Cho, Changseung Kim, Seunghwan Kim, Jaemin Seo, Hyondong Oh  

**一句话要点**：提出基于LiDAR与深度强化学习的无通信无人机群集体导航控制器，用于复杂障碍环境。

**关键词**：无人机群导航, 深度强化学习, LiDAR感知, 无通信控制, 隐式领导-跟随, 仿真到真实迁移

## 3 点简述
- 核心问题：在无通信环境中实现无人机群集体导航，需处理遮挡与有限视场等感知挑战。
- 方法要点：采用隐式领导-跟随框架，仅领导者有目标信息，跟随者通过LiDAR感知学习群聚与避障策略。
- 实验或效果：通过仿真与五架无人机真实实验验证，在多样室内外环境中成功实现无通信导航。

## 摘要（原文）

> This paper presents a deep reinforcement learning (DRL) based controller for collective navigation of unmanned aerial vehicle (UAV) swarms in communication-denied environments, enabling robust operation in complex, obstacle-rich environments. Inspired by biological swarms where informed individuals guide groups without explicit communication, we employ an implicit leader-follower framework. In this paradigm, only the leader possesses goal information, while follower UAVs learn robust policies using only onboard LiDAR sensing, without requiring any inter-agent communication or leader identification. Our system utilizes LiDAR point clustering and an extended Kalman filter for stable neighbor tracking, providing reliable perception independent of external positioning systems. The core of our approach is a DRL controller, trained in GPU-accelerated Nvidia Isaac Sim, that enables followers to learn complex emergent behaviors - balancing flocking and obstacle avoidance - using only local perception. This allows the swarm to implicitly follow the leader while robustly addressing perceptual challenges such as occlusion and limited field-of-view. The robustness and sim-to-real transfer of our approach are confirmed through extensive simulations and challenging real-world experiments with a swarm of five UAVs, which successfully demonstrated collective navigation across diverse indoor and outdoor environments without any communication or external localization.

