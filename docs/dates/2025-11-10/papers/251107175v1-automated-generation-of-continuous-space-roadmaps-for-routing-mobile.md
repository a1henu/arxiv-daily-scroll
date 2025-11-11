---
layout: default
title: Automated Generation of Continuous-Space Roadmaps for Routing Mobile Robot Fleets
---

# Automated Generation of Continuous-Space Roadmaps for Routing Mobile Robot Fleets
**arXiv**：[2511.07175v1](https://arxiv.org/abs/2511.07175) · [PDF](https://arxiv.org/pdf/2511.07175.pdf)  
**作者**：Marvin Rüdt, Constantin Enke, Kai Furmans  

**一句话要点**：提出自动化连续空间路线图生成方法，以优化移动机器人车队在内部物流中的路由效率。

**关键词**：移动机器人路由, 连续空间路线图, 内部物流优化, 路径规划, 车队协调

## 3 点简述
- 核心问题：现有路线图方法在几何精度或实际约束方面存在不足，影响移动机器人车队的路由效率和系统吞吐量。
- 方法要点：结合自由空间离散化、运输需求驱动的K最短路径优化和路径平滑，生成连续空间路线图并强制最小距离约束。
- 实验或效果：在多个内部物流用例中，该方法优于网格和随机采样基线，实现低复杂度、高冗余和近最优路径长度。

## 摘要（原文）

> Efficient routing of mobile robot fleets is crucial in intralogistics, where
> delays and deadlocks can substantially reduce system throughput. Roadmap
> design, specifying feasible transport routes, directly affects fleet
> coordination and computational performance. Existing approaches are either
> grid-based, compromising geometric precision, or continuous-space approaches
> that disregard practical constraints. This paper presents an automated roadmap
> generation approach that bridges this gap by operating in continuous-space,
> integrating station-to-station transport demand and enforcing minimum distance
> constraints for nodes and edges. By combining free space discretization,
> transport demand-driven $K$-shortest-path optimization, and path smoothing, the
> approach produces roadmaps tailored to intralogistics applications. Evaluation
> across multiple intralogistics use cases demonstrates that the proposed
> approach consistently outperforms established baselines (4-connected grid,
> 8-connected grid, and random sampling), achieving lower structural complexity,
> higher redundancy, and near-optimal path lengths, enabling efficient and robust
> routing of mobile robot fleets.

