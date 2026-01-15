---
layout: default
title: COMPOSE: Hypergraph Cover Optimization for Multi-view 3D Human Pose Estimation
---

# COMPOSE: Hypergraph Cover Optimization for Multi-view 3D Human Pose Estimation
**arXiv**：[2601.09698v1](https://arxiv.org/abs/2601.09698) · [PDF](https://arxiv.org/pdf/2601.09698.pdf)  
**作者**：Tony Danjun Wang, Tolga Birdal, Nassir Navab, Lennart Bastian  

**一句话要点**：提出COMPOSE框架，通过超图划分解决多视角3D人体姿态估计中的对应匹配问题。

**关键词**：多视角3D人体姿态估计, 超图划分, 对应匹配, 几何剪枝, 整数线性规划

## 3 点简述
- 核心问题：多视角3D姿态估计中，现有方法依赖成对关联，全局一致性约束脆弱，易受虚假关联误差传播影响。
- 方法要点：将多视角姿态对应匹配建模为超图划分问题，引入高效几何剪枝策略，降低整数线性规划搜索空间复杂度。
- 实验或效果：相比优化方法平均精度提升达23%，优于自监督端到端学习方法达11%。

## 摘要（原文）

> 3D pose estimation from sparse multi-views is a critical task for numerous applications, including action recognition, sports analysis, and human-robot interaction. Optimization-based methods typically follow a two-stage pipeline, first detecting 2D keypoints in each view and then associating these detections across views to triangulate the 3D pose. Existing methods rely on mere pairwise associations to model this correspondence problem, treating global consistency between views (i.e., cycle consistency) as a soft constraint. Yet, reconciling these constraints for multiple views becomes brittle when spurious associations propagate errors. We thus propose COMPOSE, a novel framework that formulates multi-view pose correspondence matching as a hypergraph partitioning problem rather than through pairwise association. While the complexity of the resulting integer linear program grows exponentially in theory, we introduce an efficient geometric pruning strategy to substantially reduce the search space. COMPOSE achieves improvements of up to 23% in average precision over previous optimization-based methods and up to 11% over self-supervised end-to-end learned methods, offering a promising solution to a widely studied problem.

