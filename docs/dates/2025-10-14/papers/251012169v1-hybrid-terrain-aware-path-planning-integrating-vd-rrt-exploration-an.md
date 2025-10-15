---
layout: default
title: Hybrid Terrain-Aware Path Planning: Integrating VD--RRT\(^{*}\) Exploration and VD--D\(^{*}\) Lite Repair
---

# Hybrid Terrain-Aware Path Planning: Integrating VD--RRT\(^{*}\) Exploration and VD--D\(^{*}\) Lite Repair
**arXiv**：[2510.12169v1](https://arxiv.org/abs/2510.12169) · [PDF](https://arxiv.org/pdf/2510.12169.pdf)  
**作者**：Akshay Naik, William R. Norris, Dustin Nottage, Ahmet Soylemezoglu  

**一句话要点**：提出混合地形感知路径规划框架，集成VD-RRT*探索与VD-D* Lite修复，用于越野自主车辆实时导航。

**关键词**：路径规划, 地形感知, 自主车辆, 实时导航, 越野环境, 车辆动力学

## 3 点简述
- 核心问题：越野自主车辆需实时规划曲率可行路径，同时处理土壤强度和坡度变化。
- 方法要点：结合Bekker压力-沉降模型与坡度惩罚，构建连续状态-成本度量，支持快速重规划。
- 实验或效果：硬件试验显示在软土和坡度变化中实现实时可靠导航。

## 摘要（原文）

> Autonomous ground vehicles operating off-road must plan curvature-feasible
> paths while accounting for spatially varying soil strength and slope hazards in
> real time. We present a continuous state--cost metric that combines a Bekker
> pressure--sinkage model with elevation-derived slope and attitude penalties.
> The resulting terrain cost field is analytic, bounded, and monotonic in soil
> modulus and slope, ensuring well-posed discretization and stable updates under
> sensor noise. This metric is evaluated on a lattice with exact steering
> primitives: Dubins and Reeds--Shepp motions for differential drive and
> time-parameterized bicycle arcs for Ackermann steering. Global exploration is
> performed using Vehicle-Dynamics RRT\(^{*}\), while local repair is managed by
> Vehicle-Dynamics D\(^{*}\) Lite, enabling millisecond-scale replanning without
> heuristic smoothing. By separating the terrain--vehicle model from the planner,
> the framework provides a reusable basis for deterministic, sampling-based, or
> learning-driven planning in deformable terrain. Hardware trials on an off-road
> platform demonstrate real-time navigation across soft soil and slope
> transitions, supporting reliable autonomy in unstructured environments.

