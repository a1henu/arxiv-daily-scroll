---
layout: default
title: Priority-Aware Multi-Robot Coverage Path Planning
---

# Priority-Aware Multi-Robot Coverage Path Planning
**arXiv**：[2601.00580v1](https://arxiv.org/abs/2601.00580) · [PDF](https://arxiv.org/pdf/2601.00580.pdf)  
**作者**：Kanghoon Lee, Hyeonjun Kim, Jiachen Li, Jinkyoo Park  

**一句话要点**：提出优先级感知多机器人覆盖路径规划框架，以解决区域重要性不均场景下的高效覆盖问题。

**关键词**：多机器人系统, 覆盖路径规划, 优先级感知, 路径优化, 实验验证

## 3 点简述
- 核心问题：传统多机器人覆盖路径规划假设区域重要性均匀，无法处理优先级区域需更快覆盖的场景。
- 方法要点：采用两阶段框架，包括贪婪区域分配与局部搜索、基于生成树的路径规划，以及Steiner树引导的剩余覆盖。
- 实验或效果：在多种场景中显著降低优先级加权延迟，同时保持竞争性的总完成时间，并通过敏感性分析验证可扩展性。

## 摘要（原文）

> Multi-robot systems are widely used for coverage tasks that require efficient coordination across large environments. In Multi-Robot Coverage Path Planning (MCPP), the objective is typically to minimize the makespan by generating non-overlapping paths for full-area coverage. However, most existing methods assume uniform importance across regions, limiting their effectiveness in scenarios where some zones require faster attention. We introduce the Priority-Aware MCPP (PA-MCPP) problem, where a subset of the environment is designated as prioritized zones with associated weights. The goal is to minimize, in lexicographic order, the total priority-weighted latency of zone coverage and the overall makespan. To address this, we propose a scalable two-phase framework combining (1) greedy zone assignment with local search, spanning-tree-based path planning, and (2) Steiner-tree-guided residual coverage. Experiments across diverse scenarios demonstrate that our method significantly reduces priority-weighted latency compared to standard MCPP baselines, while maintaining competitive makespan. Sensitivity analyses further show that the method scales well with the number of robots and that zone coverage behavior can be effectively controlled by adjusting priority weights.

