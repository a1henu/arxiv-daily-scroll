---
layout: default
title: Vec-QMDP: Vectorized POMDP Planning on CPUs for Real-Time Autonomous Driving
---

# Vec-QMDP: Vectorized POMDP Planning on CPUs for Real-Time Autonomous Driving
**arXiv**：[2602.08334v1](https://arxiv.org/abs/2602.08334) · [PDF](https://arxiv.org/pdf/2602.08334.pdf)  
**作者**：Xuanjin Jin, Yanxin Dong, Bin Sun, Huan Xu, Zhihui Hao, XianPeng Lang, Panpan Cai  

**一句话要点**：提出Vec-QMDP，一种CPU原生并行规划器，用于实时自动驾驶中的不确定性规划。

**关键词**：POMDP规划, CPU并行计算, 自动驾驶, 数据导向设计, 向量化算法

## 3 点简述
- 核心问题：自动驾驶等机器人任务需在高维信念空间规划，计算密集，现有CPU-GPU混合求解器因同步延迟和分支发散限制实时性。
- 方法要点：采用数据导向设计重构内存布局，结合分层并行方案，实现CPU上的SIMD向量化树扩展和碰撞检查。
- 实验或效果：在自动驾驶基准测试中，相比串行规划器加速227至1073倍，达到毫秒级延迟和先进规划性能。

## 摘要（原文）

> Planning under uncertainty for real-world robotics tasks, such as autonomous driving, requires reasoning in enormous high-dimensional belief spaces, rendering the problem computationally intensive. While parallelization offers scalability, existing hybrid CPU-GPU solvers face critical bottlenecks due to host-device synchronization latency and branch divergence on SIMT architectures, limiting their utility for real-time planning and hindering real-robot deployment. We present Vec-QMDP, a CPU-native parallel planner that aligns POMDP search with modern CPUs' SIMD architecture, achieving $227\times$--$1073\times$ speedup over state-of-the-art serial planners. Vec-QMDP adopts a Data-Oriented Design (DOD), refactoring scattered, pointer-based data structures into contiguous, cache-efficient memory layouts. We further introduce a hierarchical parallelism scheme: distributing sub-trees across independent CPU cores and SIMD lanes, enabling fully vectorized tree expansion and collision checking. Efficiency is maximized with the help of UCB load balancing across trees and a vectorized STR-tree for coarse-level collision checking. Evaluated on large-scale autonomous driving benchmarks, Vec-QMDP achieves state-of-the-art planning performance with millisecond-level latency, establishing CPUs as a high-performance computing platform for large-scale planning under uncertainty.

