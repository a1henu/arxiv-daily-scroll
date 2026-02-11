---
layout: default
title: Fast Motion Planning for Non-Holonomic Mobile Robots via a Rectangular Corridor Representation of Structured Environments
---

# Fast Motion Planning for Non-Holonomic Mobile Robots via a Rectangular Corridor Representation of Structured Environments
**arXiv**：[2602.09714v1](https://arxiv.org/abs/2602.09714) · [PDF](https://arxiv.org/pdf/2602.09714.pdf)  
**作者**：Alejandro Gonzalez-Garcia, Sebastiaan Wyns, Sonia De Santis, Jan Swevers, Wilm Decré  

**一句话要点**：提出基于矩形走廊表示的非完整移动机器人快速运动规划框架，用于复杂结构化环境。

**关键词**：非完整移动机器人, 运动规划, 结构化环境, 矩形走廊表示, 自由空间分解, 在线规划

## 3 点简述
- 核心问题：传统网格规划器可扩展性差，运动学可行规划器计算负担重。
- 方法要点：通过确定性自由空间分解构建重叠矩形走廊图，减少搜索空间。
- 实验或效果：在线规划生成近时间最优轨迹，经仿真和物理机器人验证，效率高。

## 摘要（原文）

> We present a complete framework for fast motion planning of non-holonomic autonomous mobile robots in highly complex but structured environments. Conventional grid-based planners struggle with scalability, while many kinematically-feasible planners impose a significant computational burden due to their search space complexity. To overcome these limitations, our approach introduces a deterministic free-space decomposition that creates a compact graph of overlapping rectangular corridors. This method enables a significant reduction in the search space, without sacrificing path resolution. The framework then performs online motion planning by finding a sequence of rectangles and generating a near-time-optimal, kinematically-feasible trajectory using an analytical planner. The result is a highly efficient solution for large-scale navigation. We validate our framework through extensive simulations and on a physical robot. The implementation is publicly available as open-source software.

