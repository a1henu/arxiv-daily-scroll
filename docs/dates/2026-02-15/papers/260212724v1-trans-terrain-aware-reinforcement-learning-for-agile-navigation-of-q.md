---
layout: default
title: TRANS: Terrain-aware Reinforcement Learning for Agile Navigation of Quadruped Robots under Social Interactions
---

# TRANS: Terrain-aware Reinforcement Learning for Agile Navigation of Quadruped Robots under Social Interactions
**arXiv**：[2602.12724v1](https://arxiv.org/abs/2602.12724) · [PDF](https://arxiv.org/pdf/2602.12724.pdf)  
**作者**：Wei Zhu, Irfan Tito Kurniawan, Ye Zhao, Mistuhiro Hayashibe  

**一句话要点**：提出TRANS框架以解决四足机器人在非结构化地形和社交交互环境中的敏捷导航问题

**关键词**：四足机器人导航, 深度强化学习, 地形感知, 社交交互, 仿真到现实迁移

## 3 点简述
- 核心问题：传统四足导航方法分离运动规划与运动控制，忽略全身约束和地形感知，且多数假设静态环境，不适用于人群环境。
- 方法要点：采用两阶段训练框架，包含三个深度强化学习管道，分别处理地形感知运动、社交导航及其集成，无需显式地形观测。
- 实验或效果：通过基准测试验证有效性，硬件实验显示其具备仿真到现实迁移潜力。

## 摘要（原文）

> This study introduces TRANS: Terrain-aware Reinforcement learning for Agile Navigation under Social interactions, a deep reinforcement learning (DRL) framework for quadrupedal social navigation over unstructured terrains. Conventional quadrupedal navigation typically separates motion planning from locomotion control, neglecting whole-body constraints and terrain awareness. On the other hand, end-to-end methods are more integrated but require high-frequency sensing, which is often noisy and computationally costly. In addition, most existing approaches assume static environments, limiting their use in human-populated settings. To address these limitations, we propose a two-stage training framework with three DRL pipelines. (1) TRANS-Loco employs an asymmetric actor-critic (AC) model for quadrupedal locomotion, enabling traversal of uneven terrains without explicit terrain or contact observations. (2) TRANS-Nav applies a symmetric AC framework for social navigation, directly mapping transformed LiDAR data to ego-agent actions under differential-drive kinematics. (3) A unified pipeline, TRANS, integrates TRANS-Loco and TRANS-Nav, supporting terrain-aware quadrupedal navigation in uneven and socially interactive environments. Comprehensive benchmarks against locomotion and social navigation baselines demonstrate the effectiveness of TRANS. Hardware experiments further confirm its potential for sim-to-real transfer.

