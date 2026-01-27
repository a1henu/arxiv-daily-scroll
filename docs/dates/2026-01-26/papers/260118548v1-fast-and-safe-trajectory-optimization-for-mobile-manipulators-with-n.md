---
layout: default
title: Fast and Safe Trajectory Optimization for Mobile Manipulators With Neural Configuration Space Distance Field
---

# Fast and Safe Trajectory Optimization for Mobile Manipulators With Neural Configuration Space Distance Field
**arXiv**：[2601.18548v1](https://arxiv.org/abs/2601.18548) · [PDF](https://arxiv.org/pdf/2601.18548.pdf)  
**作者**：Yulin Li, Zhiyuan Song, Yiming Li, Zhicheng Song, Kai Chen, Chunxin Zheng, Zhihai Bi, Jiahang Cao, Sylvain Calinon, Fan Shi, Jun Ma  

**一句话要点**：提出广义配置空间距离场以解决移动机械臂在无界工作空间中的快速安全轨迹优化问题

**关键词**：移动机械臂, 轨迹优化, 配置空间距离场, 神经场, 顺序凸优化, 碰撞推理

## 3 点简述
- 核心问题：移动机械臂在复杂受限空间中的高维非凸轨迹优化与快速碰撞推理困难
- 方法要点：扩展配置空间距离场至移动机械臂，通过神经场建模连续距离与梯度，支持高效GPU批量查询
- 实验或效果：开发基于广义配置空间距离场的顺序凸优化框架，实现大规模隐式约束的快速求解与场景变化下的重规划

## 摘要（原文）

> Mobile manipulators promise agile, long-horizon behavior by coordinating base and arm motion, yet whole-body trajectory optimization in cluttered, confined spaces remains difficult due to high-dimensional nonconvexity and the need for fast, accurate collision reasoning. Configuration Space Distance Fields (CDF) enable fixed-base manipulators to model collisions directly in configuration space via smooth, implicit distances. This representation holds strong potential to bypass the nonlinear configuration-to-workspace mapping while preserving accurate whole-body geometry and providing optimization-friendly collision costs. Yet, extending this capability to mobile manipulators is hindered by unbounded workspaces and tighter base-arm coupling. We lift this promise to mobile manipulation with Generalized Configuration Space Distance Fields (GCDF), extending CDF to robots with both translational and rotational joints in unbounded workspaces with tighter base-arm coupling. We prove that GCDF preserves Euclidean-like local distance structure and accurately encodes whole-body geometry in configuration space, and develop a data generation and training pipeline that yields continuous neural GCDFs with accurate values and gradients, supporting efficient GPU-batched queries. Building on this representation, we develop a high-performance sequential convex optimization framework centered on GCDF-based collision reasoning. The solver scales to large numbers of implicit constraints through (i) online specification of neural constraints, (ii) sparsity-aware active-set detection with parallel batched evaluation across thousands of constraints, and (iii) incremental constraint management for rapid replanning under scene changes.

