---
layout: default
title: Mastering Diverse, Unknown, and Cluttered Tracks for Robust Vision-Based Drone Racing
---

# Mastering Diverse, Unknown, and Cluttered Tracks for Robust Vision-Based Drone Racing
**arXiv**：[2512.09571v1](https://arxiv.org/abs/2512.09571) · [PDF](https://arxiv.org/pdf/2512.09571.pdf)  
**作者**：Feng Yu, Yu Hu, Yang Su, Yang Deng, Linzuo Zhang, Danping Zou  

**一句话要点**：提出两阶段学习框架以解决无人机在未知杂乱环境中视觉竞速的泛化问题

**关键词**：无人机竞速, 强化学习, 视觉导航, 泛化能力, 避障控制

## 3 点简述
- 核心问题：强化学习方法在固定无障赛道泛化不足，需平衡速度与避障，且深度图中门与障碍物感知模糊
- 方法要点：采用软碰撞训练和硬碰撞精炼两阶段，结合自适应噪声课程和非对称架构，增强视觉输入依赖
- 实验或效果：通过仿真和真实实验验证，在计算受限四旋翼上实现敏捷飞行，对门位置误差鲁棒

## 摘要（原文）

> Most reinforcement learning(RL)-based methods for drone racing target fixed, obstacle-free tracks, leaving the generalization to unknown, cluttered environments largely unaddressed. This challenge stems from the need to balance racing speed and collision avoidance, limited feasible space causing policy exploration trapped in local optima during training, and perceptual ambiguity between gates and obstacles in depth maps-especially when gate positions are only coarsely specified. To overcome these issues, we propose a two-phase learning framework: an initial soft-collision training phase that preserves policy exploration for high-speed flight, followed by a hard-collision refinement phase that enforces robust obstacle avoidance. An adaptive, noise-augmented curriculum with an asymmetric actor-critic architecture gradually shifts the policy's reliance from privileged gate-state information to depth-based visual input. We further impose Lipschitz constraints and integrate a track-primitive generator to enhance motion stability and cross-environment generalization. We evaluate our framework through extensive simulation and ablation studies, and validate it in real-world experiments on a computationally constrained quadrotor. The system achieves agile flight while remaining robust to gate-position errors, developing a generalizable drone racing framework with the capability to operate in diverse, partially unknown and cluttered environments. https://yufengsjtu.github.io/MasterRacing.github.io/

