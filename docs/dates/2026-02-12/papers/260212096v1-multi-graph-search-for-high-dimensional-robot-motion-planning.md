---
layout: default
title: Multi Graph Search for High-Dimensional Robot Motion Planning
---

# Multi Graph Search for High-Dimensional Robot Motion Planning
**arXiv**：[2602.12096v1](https://arxiv.org/abs/2602.12096) · [PDF](https://arxiv.org/pdf/2602.12096.pdf)  
**作者**：Itamar Mishani, Maxim Likhachev  

**一句话要点**：提出多图搜索算法以解决高维机器人运动规划中的效率与质量平衡问题

**关键词**：机器人运动规划, 多图搜索, 高维状态空间, 搜索算法, 有界次优性

## 3 点简述
- 核心问题：高维机器人运动规划算法常导致不可预测运动或高计算资源消耗
- 方法要点：将经典单向和双向搜索推广到多图设置，维护多个隐式图并增量扩展
- 实验或效果：证明算法完备且有界次优，在多种操作任务中实证有效

## 摘要（原文）

> Efficient motion planning for high-dimensional robotic systems, such as manipulators and mobile manipulators, is critical for real-time operation and reliable deployment. Although advances in planning algorithms have enhanced scalability to high-dimensional state spaces, these improvements often come at the cost of generating unpredictable, inconsistent motions or requiring excessive computational resources and memory. In this work, we introduce Multi-Graph Search (MGS), a search-based motion planning algorithm that generalizes classical unidirectional and bidirectional search to a multi-graph setting. MGS maintains and incrementally expands multiple implicit graphs over the state space, focusing exploration on high-potential regions while allowing initially disconnected subgraphs to be merged through feasible transitions as the search progresses. We prove that MGS is complete and bounded-suboptimal, and empirically demonstrate its effectiveness on a range of manipulation and mobile manipulation tasks. Demonstrations, benchmarks and code are available at https://multi-graph-search.github.io/.

