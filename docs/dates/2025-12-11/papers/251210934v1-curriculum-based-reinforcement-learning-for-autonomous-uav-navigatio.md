---
layout: default
title: Curriculum-Based Reinforcement Learning for Autonomous UAV Navigation in Unknown Curved Tubular Conduit
---

# Curriculum-Based Reinforcement Learning for Autonomous UAV Navigation in Unknown Curved Tubular Conduit
**arXiv**：[2512.10934v1](https://arxiv.org/abs/2512.10934) · [PDF](https://arxiv.org/pdf/2512.10934.pdf)  
**作者**：Zamirddine Mari, Jérôme Pasquet, Julien Seinturier  

**一句话要点**：提出基于课程学习的强化学习方法，用于无人机在未知弯曲管道中的自主导航。

**关键词**：无人机导航, 强化学习, 课程学习, 管道环境, LiDAR感知, 自主系统

## 3 点简述
- 核心问题：无人机在狭窄管道中导航面临几何约束、壁面接近和感知限制的挑战。
- 方法要点：使用强化学习，结合LiDAR局部观测和视觉中心检测，通过课程学习逐步训练。
- 实验或效果：PPO策略在未知几何下优于确定性基线，验证了行为在高保真环境中的可迁移性。

## 摘要（原文）

> Autonomous drone navigation in confined tubular environments remains a major challenge due to the constraining geometry of the conduits, the proximity of the walls, and the perceptual limitations inherent to such scenarios. We propose a reinforcement learning approach enabling a drone to navigate unknown three-dimensional tubes without any prior knowledge of their geometry, relying solely on local observations from LiDAR and a conditional visual detection of the tube center. In contrast, the Pure Pursuit algorithm, used as a deterministic baseline, benefits from explicit access to the centerline, creating an information asymmetry designed to assess the ability of RL to compensate for the absence of a geometric model. The agent is trained through a progressive Curriculum Learning strategy that gradually exposes it to increasingly curved geometries, where the tube center frequently disappears from the visual field. A turning-negotiation mechanism, based on the combination of direct visibility, directional memory, and LiDAR symmetry cues, proves essential for ensuring stable navigation under such partial observability conditions. Experiments show that the PPO policy acquires robust and generalizable behavior, consistently outperforming the deterministic controller despite its limited access to geometric information. Validation in a high-fidelity 3D environment further confirms the transferability of the learned behavior to a continuous physical dynamics.
>   The proposed approach thus provides a complete framework for autonomous navigation in unknown tubular environments and opens perspectives for industrial, underground, or medical applications where progressing through narrow and weakly perceptive conduits represents a central challenge.

