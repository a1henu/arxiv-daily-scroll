---
layout: default
title: DynaRetarget: Dynamically-Feasible Retargeting using Sampling-Based Trajectory Optimization
---

# DynaRetarget: Dynamically-Feasible Retargeting using Sampling-Based Trajectory Optimization
**arXiv**：[2602.06827v1](https://arxiv.org/abs/2602.06827) · [PDF](https://arxiv.org/pdf/2602.06827.pdf)  
**作者**：Victor Dhedin, Ilyass Taouil, Shafeef Omar, Dian Yu, Kun Tao, Angela Dai, Majid Khadiv  

**一句话要点**：提出DynaRetarget，通过采样轨迹优化将人体运动重定向为人形机器人动态可行运动

**关键词**：运动重定向, 轨迹优化, 人形机器人, 动态可行性, 采样优化

## 3 点简述
- 核心问题：人体运动重定向至人形机器人时，常因动力学约束导致运动不可行
- 方法要点：基于采样轨迹优化框架，逐步优化长时程轨迹，确保动态可行性
- 实验效果：在数百演示中成功重定向，优于现有方法，泛化至不同物体属性

## 摘要（原文）

> In this paper, we introduce DynaRetarget, a complete pipeline for retargeting human motions to humanoid control policies. The core component of DynaRetarget is a novel Sampling-Based Trajectory Optimization (SBTO) framework that refines imperfect kinematic trajectories into dynamically feasible motions. SBTO incrementally advances the optimization horizon, enabling optimization over the entire trajectory for long-horizon tasks. We validate DynaRetarget by successfully retargeting hundreds of humanoid-object demonstrations and achieving higher success rates than the state of the art. The framework also generalizes across varying object properties, such as mass, size, and geometry, using the same tracking objective. This ability to robustly retarget diverse demonstrations opens the door to generating large-scale synthetic datasets of humanoid loco-manipulation trajectories, addressing a major bottleneck in real-world data collection.

