---
layout: default
title: Learning Robust Control Policies for Inverted Pose on Miniature Blimp Robots
---

# Learning Robust Control Policies for Inverted Pose on Miniature Blimp Robots
**arXiv**：[2602.23972v1](https://arxiv.org/abs/2602.23972) · [PDF](https://arxiv.org/pdf/2602.23972.pdf)  
**作者**：Yuanlin Yang, Lin Hong, Fumin Zhang  

**一句话要点**：提出基于仿真与强化学习的框架，以解决微型飞艇机器人倒立姿态的鲁棒控制问题。

**关键词**：微型飞艇机器人, 倒立姿态控制, 强化学习, 仿真到现实迁移, 鲁棒控制策略

## 3 点简述
- 核心问题：微型飞艇机器人因复杂欠驱动动力学，倒立姿态控制困难。
- 方法要点：构建高保真仿真环境，结合域随机化和改进TD3算法训练鲁棒策略。
- 实验或效果：仿真中成功率高于能量整形控制器，实际部署通过映射层实现倒立姿态。

## 摘要（原文）

> The ability to achieve and maintain inverted poses is essential for unlocking the full agility of miniature blimp robots (MBRs). However, developing reliable control methods for MBRs remains challenging due to their complex and underactuated dynamics. To address this challenge, we propose a novel framework that enables robust control policy learning for inverted pose on MBRs. The proposed framework operates through three core stages: First, a high-fidelity three-dimensional (3D) simulation environment was constructed, which was calibrated against real-world MBR motion data to ensure accurate replication of inverted-state dynamics. Second, a robust policy for MBR inverted control was trained within the simulation environment via a domain randomization strategy and a modified Twin Delayed Deep Deterministic Policy Gradient (TD3) algorithm. Third, a mapping layer was designed to bridge the sim-to-real gap for the learned policy deployment. Comprehensive evaluations in the simulation environment demonstrate that the learned policy achieves a higher success rate compared to the energy-shaping controller. Furthermore, experimental results confirm that the learned policy with a mapping layer enables an MBR to achieve and maintain a fully upside-down pose in real-world settings.

