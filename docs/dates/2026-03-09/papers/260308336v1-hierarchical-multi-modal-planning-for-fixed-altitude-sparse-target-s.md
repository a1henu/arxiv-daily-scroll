---
layout: default
title: Hierarchical Multi-Modal Planning for Fixed-Altitude Sparse Target Search and Sampling
---

# Hierarchical Multi-Modal Planning for Fixed-Altitude Sparse Target Search and Sampling
**arXiv**：[2603.08336v1](https://arxiv.org/abs/2603.08336) · [PDF](https://arxiv.org/pdf/2603.08336.pdf)  
**作者**：Lingpeng Chen, Yuchen Zheng, Apple Pui-Yi Chui, Junfeng Wu, Ziyang Hong  

**一句话要点**：提出HIMoS框架以解决固定高度稀疏珊瑚搜索与采样的效率问题

**关键词**：自主水下航行器, 稀疏目标搜索, 分层规划, 多模态传感器, 信念传播, 珊瑚监测

## 3 点简述
- 核心问题：传统全覆盖策略能耗高，自适应采样依赖昂贵垂直机动，监测稀疏海底现象效率低。
- 方法要点：采用双层规划架构，全局规划优化拓扑路线，局部规划利用可微分信念传播生成平衡声学、视觉和采样任务的轨迹。
- 实验或效果：基于真实珊瑚礁调查的高保真仿真验证，相比先进基线方法，展示了更优的任务效率。

## 摘要（原文）

> Efficient monitoring of sparse benthic phenomena, such as coral colonies, presents a great challenge for Autonomous Underwater Vehicles. Traditional exhaustive coverage strategies are energy-inefficient, while recent adaptive sampling approaches rely on costly vertical maneuvers. To address these limitations, we propose HIMoS (Hierarchical Informative Multi-Modal Search), a fixed-altitude framework for sparse coral search-and-sample missions. The system integrates a heterogeneous sensor suite within a two-layer planning architecture. At the strategic level, a Global Planner optimizes topological routes to maximize potential discovery. At the tactical level, a receding-horizon Local Planner leverages differentiable belief propagation to generate kinematically feasible trajectories that balance acoustic substrate exploration, visual coral search, and close-range sampling. Validated in high-fidelity simulations derived from real-world coral reef benthic surveys, our approach demonstrates superior mission efficiency compared to state-of-the-art baselines.

