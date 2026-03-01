---
layout: default
title: SCOPE: Skeleton Graph-Based Computation-Efficient Framework for Autonomous UAV Exploration
---

# SCOPE: Skeleton Graph-Based Computation-Efficient Framework for Autonomous UAV Exploration
**arXiv**：[2602.22707v1](https://arxiv.org/abs/2602.22707) · [PDF](https://arxiv.org/pdf/2602.22707.pdf)  
**作者**：Kai Li, Shengtao Zheng, Linkun Xiu, Yuze Sheng, Xiao-Ping Zhang, Dongyue Huang, Xinlei Chen  

**一句话要点**：提出SCOPE框架以解决无人机自主探索中计算延迟和轨迹振荡问题

**关键词**：无人机自主探索, 骨架图构建, 分层规划, 计算效率优化, 隐式未知区域分析

## 3 点简述
- 核心问题：现有方法依赖全局优化，导致高计算延迟和轨迹振荡，尤其在资源受限设备上。
- 方法要点：通过增量构建骨架图和隐式未知区域分析，采用分层按需规划策略，包括近端规划器和区域序列规划器。
- 实验或效果：仿真评估显示，SCOPE在保持探索性能的同时，平均降低86.9%计算成本；真实实验验证了其鲁棒性和低延迟。

## 摘要（原文）

> Autonomous exploration in unknown environments is key for mobile robots, helping them perceive, map, and make decisions in complex areas. However, current methods often rely on frequent global optimization, suffering from high computational latency and trajectory oscillation, especially on resource-constrained edge devices. To address these limitations, we propose SCOPE, a novel framework that incrementally constructs a real-time skeletal graph and introduces Implicit Unknown Region Analysis for efficient spatial reasoning. The planning layer adopts a hierarchical on-demand strategy: the Proximal Planner generates smooth, high-frequency local trajectories, while the Region-Sequence Planner is activated only when necessary to optimize global visitation order. Comparative evaluations in simulation demonstrate that SCOPE achieves competitive exploration performance comparable to state-of-the-art global planners, while reducing computational cost by an average of 86.9%. Real-world experiments further validate the system's robustness and low latency in practical scenarios.

