---
layout: default
title: Decoupled Generative Modeling for Human-Object Interaction Synthesis
---

# Decoupled Generative Modeling for Human-Object Interaction Synthesis
**arXiv**：[2512.19049v1](https://arxiv.org/abs/2512.19049) · [PDF](https://arxiv.org/pdf/2512.19049.pdf)  
**作者**：Hwanhee Jung, Seunggwan Lee, Jeongyoon Yoon, SeungHyeon Kim, Giljoo Nam, Qixing Huang, Sangpil Kim  

**一句话要点**：提出DecHOI以解决人-物交互合成中轨迹规划与动作合成的耦合问题

**关键词**：人-物交互合成, 解耦生成建模, 轨迹规划, 动作合成, 对抗训练, 动态场景规划

## 3 点简述
- 核心问题：现有方法需手动指定中间路径点，且优化目标集中于单一网络，导致运动不同步或穿透错误。
- 方法要点：将路径规划与动作合成解耦，先由轨迹生成器生成轨迹，再由动作生成器合成详细运动，并采用对抗训练提升接触真实性。
- 实验或效果：在FullBodyManipulation和3D-FUTURE基准上，DecHOI在多数定量指标和定性评估中超越先前方法，感知研究也偏好其结果。

## 摘要（原文）

> Synthesizing realistic human-object interaction (HOI) is essential for 3D computer vision and robotics, underpinning animation and embodied control. Existing approaches often require manually specified intermediate waypoints and place all optimization objectives on a single network, which increases complexity, reduces flexibility, and leads to errors such as unsynchronized human and object motion or penetration. To address these issues, we propose Decoupled Generative Modeling for Human-Object Interaction Synthesis (DecHOI), which separates path planning and action synthesis. A trajectory generator first produces human and object trajectories without prescribed waypoints, and an action generator conditions on these paths to synthesize detailed motions. To further improve contact realism, we employ adversarial training with a discriminator that focuses on the dynamics of distal joints. The framework also models a moving counterpart and supports responsive, long-sequence planning in dynamic scenes, while preserving plan consistency. Across two benchmarks, FullBodyManipulation and 3D-FUTURE, DecHOI surpasses prior methods on most quantitative metrics and qualitative evaluations, and perceptual studies likewise prefer our results.

