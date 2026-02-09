---
layout: default
title: An Integer Linear Programming Approach to Geometrically Consistent Partial-Partial Shape Matching
---

# An Integer Linear Programming Approach to Geometrically Consistent Partial-Partial Shape Matching
**arXiv**：[2602.06590v1](https://arxiv.org/abs/2602.06590) · [PDF](https://arxiv.org/pdf/2602.06590.pdf)  
**作者**：Viktoria Ehm, Paul Roetzer, Florian Bernard, Daniel Cremers  

**一句话要点**：提出整数线性规划方法以解决几何一致的部分-部分三维形状匹配问题

**关键词**：三维形状匹配, 部分-部分匹配, 整数线性规划, 几何一致性, 重叠区域估计

## 3 点简述
- 核心问题：部分-部分三维形状匹配需同时估计重叠区域和计算对应关系，是现实场景中的挑战。
- 方法要点：利用几何一致性作为先验，通过整数线性规划实现鲁棒的重叠区域估计和邻域保持对应。
- 实验或效果：实验显示方法在匹配误差和平滑度上表现优异，且比先前方法更具可扩展性。

## 摘要（原文）

> The task of establishing correspondences between two 3D shapes is a long-standing challenge in computer vision. While numerous studies address full-full and partial-full 3D shape matching, only a limited number of works have explored the partial-partial setting, very likely due to its unique challenges: we must compute accurate correspondences while at the same time find the unknown overlapping region. Nevertheless, partial-partial 3D shape matching reflects the most realistic setting, as in many real-world cases, such as 3D scanning, shapes are only partially observable. In this work, we introduce the first integer linear programming approach specifically designed to address the distinctive challenges of partial-partial shape matching. Our method leverages geometric consistency as a strong prior, enabling both robust estimation of the overlapping region and computation of neighbourhood-preserving correspondences. We empirically demonstrate that our approach achieves high-quality matching results both in terms of matching error and smoothness. Moreover, we show that our method is more scalable than previous formalisms.

