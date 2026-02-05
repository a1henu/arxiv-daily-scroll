---
layout: default
title: Multi-threaded Recast-Based A* Pathfinding for Scalable Navigation in Dynamic Game Environments
---

# Multi-threaded Recast-Based A* Pathfinding for Scalable Navigation in Dynamic Game Environments
**arXiv**：[2602.04130v1](https://arxiv.org/abs/2602.04130) · [PDF](https://arxiv.org/pdf/2602.04130.pdf)  
**作者**：Tiroshan Madushanka, Sakuna Madushanka  

**一句话要点**：提出多线程框架结合Recast网格生成与密度分析，以提升动态游戏环境中A*路径规划的可扩展性和性能。

**关键词**：路径规划, 多线程优化, 动态环境导航, Recast网格生成, 群体协调

## 3 点简述
- 核心问题：A*算法在动态3D游戏环境中面临计算性能与视觉真实性的权衡挑战。
- 方法要点：通过多线程、Recast网格生成、贝塞尔曲线轨迹平滑和密度分析增强A*算法。
- 实验或效果：在10个递增测试阶段中，系统支持1000个同时代理，保持350+ FPS，实现无碰撞群体导航。

## 摘要（原文）

> While the A* algorithm remains the industry standard for game pathfinding, its integration into dynamic 3D environments faces trade-offs between computational performance and visual realism. This paper proposes a multi-threaded framework that enhances standard A* through Recast-based mesh generation, Bezier-curve trajectory smoothing, and density analysis for crowd coordination. We evaluate our system across ten incremental phases, from 2D mazes to complex multi-level dynamic worlds. Experimental results demonstrate that the framework maintains 350+ FPS with 1000 simultaneous agents and achieves collision-free crowd navigation through density-aware path coordination.

