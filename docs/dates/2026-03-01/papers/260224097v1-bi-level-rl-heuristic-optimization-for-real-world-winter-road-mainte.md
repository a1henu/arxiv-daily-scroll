---
layout: default
title: Bi-level RL-Heuristic Optimization for Real-world Winter Road Maintenance
---

# Bi-level RL-Heuristic Optimization for Real-world Winter Road Maintenance
**arXiv**：[2602.24097v1](https://arxiv.org/abs/2602.24097) · [PDF](https://arxiv.org/pdf/2602.24097.pdf)  
**作者**：Yue Xie, Zizhen Xu, William Beazley, Fumiya Iida  

**一句话要点**：提出双层强化学习-启发式优化框架以解决冬季道路维护的大规模路由问题

**关键词**：冬季道路维护, 双层优化, 强化学习, 车辆路径问题, 碳排放优化, 大规模路由

## 3 点简述
- 核心问题：冬季道路维护面临大规模路由挑战，依赖人工决策，效率低下且环境影响大。
- 方法要点：上层用强化学习分区和资源分配，下层用多目标车辆路径问题优化旅行时间和碳排放。
- 实验或效果：在真实路网数据上验证，实现平衡工作负载、降低旅行时间至两小时阈值以下、减少排放和成本。

## 摘要（原文）

> Winter road maintenance is critical for ensuring public safety and reducing environmental impacts, yet existing methods struggle to manage large-scale routing problems effectively and mostly reply on human decision. This study presents a novel, scalable bi-level optimization framework, validated on real operational data on UK strategic road networks (M25, M6, A1), including interconnected local road networks in surrounding areas for vehicle traversing, as part of the highway operator's efforts to solve existing planning challenges. At the upper level, a reinforcement learning (RL) agent strategically partitions the road network into manageable clusters and optimally allocates resources from multiple depots. At the lower level, a multi-objective vehicle routing problem (VRP) is solved within each cluster, minimizing the maximum vehicle travel time and total carbon emissions. Unlike existing approaches, our method handles large-scale, real-world networks efficiently, explicitly incorporating vehicle-specific constraints, depot capacities, and road segment requirements. Results demonstrate significant improvements, including balanced workloads, reduced maximum travel times below the targeted two-hour threshold, lower emissions, and substantial cost savings. This study illustrates how advanced AI-driven bi-level optimization can directly enhance operational decision-making in real-world transportation and logistics.

