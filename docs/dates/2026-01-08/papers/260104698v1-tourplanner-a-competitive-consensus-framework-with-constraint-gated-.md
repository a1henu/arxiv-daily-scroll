---
layout: default
title: TourPlanner: A Competitive Consensus Framework with Constraint-Gated Reinforcement Learning for Travel Planning
---

# TourPlanner: A Competitive Consensus Framework with Constraint-Gated Reinforcement Learning for Travel Planning
**arXiv**：[2601.04698v1](https://arxiv.org/abs/2601.04698) · [PDF](https://arxiv.org/pdf/2601.04698.pdf)  
**作者**：Yinuo Wang, Mining Tan, Wenxiang Jiao, Xiaoxi Li, Hao Wang, Xuanyu Zhang, Yuan Lu, Weiming Dong  

**一句话要点**：提出TourPlanner框架，结合多路径推理与约束门控强化学习以解决旅行规划中的候选点筛选、解空间探索和约束优化难题。

**关键词**：旅行规划, 多路径推理, 约束优化, 强化学习, 候选点筛选, 空间感知

## 3 点简述
- 核心问题：旅行规划面临候选点兴趣筛选、单一路径限制解空间探索、硬软约束同时优化等挑战。
- 方法要点：采用PReSO工作流构建空间感知候选集，CCoT多路径推理增强探索，集成sigmoid门控机制于强化学习阶段。
- 实验或效果：在旅行规划基准测试中实现最优性能，显著提升可行性与用户偏好对齐。

## 摘要（原文）

> Travel planning is a sophisticated decision-making process that requires synthesizing multifaceted information to construct itineraries. However, existing travel planning approaches face several challenges: (1) Pruning candidate points of interest (POIs) while maintaining a high recall rate; (2) A single reasoning path restricts the exploration capability within the feasible solution space for travel planning; (3) Simultaneously optimizing hard constraints and soft constraints remains a significant difficulty. To address these challenges, we propose TourPlanner, a comprehensive framework featuring multi-path reasoning and constraint-gated reinforcement learning. Specifically, we first introduce a Personalized Recall and Spatial Optimization (PReSO) workflow to construct spatially-aware candidate POIs' set. Subsequently, we propose Competitive consensus Chain-of-Thought (CCoT), a multi-path reasoning paradigm that improves the ability of exploring the feasible solution space. To further refine the plan, we integrate a sigmoid-based gating mechanism into the reinforcement learning stage, which dynamically prioritizes soft-constraint satisfaction only after hard constraints are met. Experimental results on travel planning benchmarks demonstrate that TourPlanner achieves state-of-the-art performance, significantly surpassing existing methods in both feasibility and user-preference alignment.

