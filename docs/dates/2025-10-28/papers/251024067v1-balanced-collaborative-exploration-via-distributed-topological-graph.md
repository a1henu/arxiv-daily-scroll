---
layout: default
title: Balanced Collaborative Exploration via Distributed Topological Graph Voronoi Partition
---

# Balanced Collaborative Exploration via Distributed Topological Graph Voronoi Partition
**arXiv**：[2510.24067v1](https://arxiv.org/abs/2510.24067) · [PDF](https://arxiv.org/pdf/2510.24067.pdf)  
**作者**：Tianyi Ding, Ronghao Zheng, Senlin Zhang, Meiqin Liu  

**一句话要点**：提出分布式拓扑图Voronoi分割方法以解决多机器人在非凸环境中的平衡协作探索问题

**关键词**：多机器人协作探索, 分布式规划, 拓扑图分割, Voronoi算法, 平衡任务分配

## 3 点简述
- 核心问题：多机器人在障碍密集非凸环境中实现动态平衡的探索区域划分与任务分配
- 方法要点：引入分布式加权拓扑图Voronoi算法，确保平衡图空间分割与分布式共识收敛
- 实验或效果：基准测试显示在探索效率、完整性和团队负载平衡方面显著提升

## 摘要（原文）

> This work addresses the collaborative multi-robot autonomous online
> exploration problem, particularly focusing on distributed exploration planning
> for dynamically balanced exploration area partition and task allocation among a
> team of mobile robots operating in obstacle-dense non-convex environments.
>   We present a novel topological map structure that simultaneously
> characterizes both spatial connectivity and global exploration completeness of
> the environment. The topological map is updated incrementally to utilize known
> spatial information for updating reachable spaces, while exploration targets
> are planned in a receding horizon fashion under global coverage guidance.
>   A distributed weighted topological graph Voronoi algorithm is introduced
> implementing balanced graph space partitions of the fused topological maps.
> Theoretical guarantees are provided for distributed consensus convergence and
> equitable graph space partitions with constant bounds.
>   A local planner optimizes the visitation sequence of exploration targets
> within the balanced partitioned graph space to minimize travel distance, while
> generating safe, smooth, and dynamically feasible motion trajectories.
>   Comprehensive benchmarking against state-of-the-art methods demonstrates
> significant improvements in exploration efficiency, completeness, and workload
> balance across the robot team.

