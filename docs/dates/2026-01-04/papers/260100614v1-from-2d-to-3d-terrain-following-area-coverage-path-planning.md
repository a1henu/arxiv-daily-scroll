---
layout: default
title: From 2D to 3D terrain-following area coverage path planning
---

# From 2D to 3D terrain-following area coverage path planning
**arXiv**：[2601.00614v1](https://arxiv.org/abs/2601.00614) · [PDF](https://arxiv.org/pdf/2601.00614.pdf)  
**作者**：Mogens Plessen  

**一句话要点**：提出3D地形跟随区域覆盖路径规划算法，用于农业机械作业。

**关键词**：3D路径规划, 地形跟随, 区域覆盖, 农业机械, 高程数据处理

## 3 点简述
- 核心问题：从2D扩展到3D地形跟随区域覆盖路径规划，处理复杂地形数据。
- 方法要点：生成相邻路径，保持工作宽度间距，同时浮动在特定工作高度以上地形。
- 实验或效果：使用真实农业3D数据验证算法，包括均匀间距高程数据生成和局部搜索。

## 摘要（原文）

> An algorithm for 3D terrain-following area coverage path planning is presented. Multiple adjacent paths are generated that are (i) locally apart from each other by a distance equal to the working width of a machinery, while (ii) simultaneously floating at a projection distance equal to a specific working height above the terrain. The complexities of the algorithm in comparison to its 2D equivalent are highlighted. These include uniformly spaced elevation data generation using an Inverse Distance Weighting-approach and a local search. Area coverage path planning results for real-world 3D data within an agricultural context are presented to validate the algorithm.

