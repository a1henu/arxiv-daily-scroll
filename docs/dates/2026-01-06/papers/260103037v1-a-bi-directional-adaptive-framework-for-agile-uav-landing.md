---
layout: default
title: A Bi-directional Adaptive Framework for Agile UAV Landing
---

# A Bi-directional Adaptive Framework for Agile UAV Landing
**arXiv**：[2601.03037v1](https://arxiv.org/abs/2601.03037) · [PDF](https://arxiv.org/pdf/2601.03037.pdf)  
**作者**：Chunhui Zhao, Xirui Kao, Yilin Lu, Yang Lyu  

**一句话要点**：提出双向自适应框架以解决动态场景下四旋翼无人机敏捷着陆问题

**关键词**：无人机着陆, 动态场景, 协同控制, 系统优化, 轨迹规划, 鲁棒性

## 3 点简述
- 核心问题：传统方法在动态场景中效率低下，依赖顺序跟踪-下降范式。
- 方法要点：将着陆重构为耦合系统优化，移动平台主动倾斜以协同姿态对齐。
- 实验或效果：验证显示框架提升效率、精度和鲁棒性，适用于时间受限任务。

## 摘要（原文）

> Autonomous landing on mobile platforms is crucial for extending quadcopter operational flexibility, yet conventional methods are often too inefficient for highly dynamic scenarios. The core limitation lies in the prevalent ``track-then-descend'' paradigm, which treats the platform as a passive target and forces the quadcopter to perform complex, sequential maneuvers. This paper challenges that paradigm by introducing a bi-directional cooperative landing framework that redefines the roles of the vehicle and the platform. The essential innovation is transforming the problem from a single-agent tracking challenge into a coupled system optimization. Our key insight is that the mobile platform is not merely a target, but an active agent in the landing process. It proactively tilts its surface to create an optimal, stable terminal attitude for the approaching quadcopter. This active cooperation fundamentally breaks the sequential model by parallelizing the alignment and descent phases. Concurrently, the quadcopter's planning pipeline focuses on generating a time-optimal and dynamically feasible trajectory that minimizes energy consumption. This bi-directional coordination allows the system to execute the recovery in an agile manner, characterized by aggressive trajectory tracking and rapid state synchronization within transient windows. The framework's effectiveness, validated in dynamic scenarios, significantly improves the efficiency, precision, and robustness of autonomous quadrotor recovery in complex and time-constrained missions.

