---
layout: default
title: A Generalized Voronoi Graph based Coverage Control Approach for Non-Convex Environment
---

# A Generalized Voronoi Graph based Coverage Control Approach for Non-Convex Environment
**arXiv**：[2603.09596v1](https://arxiv.org/abs/2603.09596) · [PDF](https://arxiv.org/pdf/2603.09596.pdf)  
**作者**：Zuyi Guo, Ronghao Zheng, Meiqin Liu, Senlin Zhang  

**一句话要点**：提出基于广义Voronoi图的多机器人覆盖控制方法，以解决非凸环境中的高效覆盖问题。

**关键词**：多机器人系统, 覆盖控制, 广义Voronoi图, 负载均衡, 非凸环境, 协作控制

## 3 点简述
- 核心问题：多机器人系统在含多个障碍的非凸区域中实现高效覆盖的挑战。
- 方法要点：基于广义Voronoi图分区，采用加权负载均衡算法优化机器人分配，并设计新控制器进行协作覆盖。
- 实验或效果：通过仿真评估性能，并证明了方法的收敛性。

## 摘要（原文）

> To address the challenge of efficient coverage by multi-robot systems in non-convex regions with multiple obstacles, this paper proposes a coverage control method based on the Generalized Voronoi Graph (GVG), which has two phases: Load-Balancing Algorithm phase and Collaborative Coverage phase. In Load-Balancing Algorithm phase, the non-convex region is partitioned into multiple sub-regions based on GVG. Besides, a weighted load-balancing algorithm is developed, which considers the quality differences among sub-regions. By iteratively optimizing the robot allocation ratio, the number of robots in each sub-region is matched with the sub-region quality to achieve load balance. In Collaborative Coverage phase, each robot is controlled by a new controller to effectively coverage the region. The convergence of the method is proved and its performance is evaluated through simulations.

