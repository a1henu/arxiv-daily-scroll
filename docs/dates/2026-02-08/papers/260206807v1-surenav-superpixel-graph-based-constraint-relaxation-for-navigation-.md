---
layout: default
title: SuReNav: Superpixel Graph-based Constraint Relaxation for Navigation in Over-constrained Environments
---

# SuReNav: Superpixel Graph-based Constraint Relaxation for Navigation in Over-constrained Environments
**arXiv**：[2602.06807v1](https://arxiv.org/abs/2602.06807) · [PDF](https://arxiv.org/pdf/2602.06807.pdf)  
**作者**：Keonyoung Koh, Moonkyeong Jung, Samuel Seungsup Lee, Daehyung Park  

**一句话要点**：提出SuReNav方法，基于超像素图约束松弛解决半静态环境中过约束导航问题。

**关键词**：过约束导航, 超像素图, 约束松弛, 图神经网络, 机器人导航, 半静态环境

## 3 点简述
- 核心问题：半静态环境中过约束规划，需避开硬约束区域并最小化穿越低风险区域。
- 方法要点：使用超像素图生成、图神经网络约束松弛和交替执行框架，模仿人类导航。
- 实验或效果：在2D语义图和3D OpenStreetMap上优于基线，实现最高人类相似度，并在四足机器人上验证。

## 摘要（原文）

> We address the over-constrained planning problem in semi-static environments. The planning objective is to find a best-effort solution that avoids all hard constraint regions while minimally traversing the least risky areas. Conventional methods often rely on pre-defined area costs, limiting generalizations. Further, the spatial continuity of navigation spaces makes it difficult to identify regions that are passable without overestimation. To overcome these challenges, we propose SuReNav, a superpixel graph-based constraint relaxation and navigation method that imitates human-like safe and efficient navigation. Our framework consists of three components: 1) superpixel graph map generation with regional constraints, 2) regional-constraint relaxation using graph neural network trained on human demonstrations for safe and efficient navigation, and 3) interleaving relaxation, planning, and execution for complete navigation. We evaluate our method against state-of-the-art baselines on 2D semantic maps and 3D maps from OpenStreetMap, achieving the highest human-likeness score of complete navigation while maintaining a balanced trade-off between efficiency and safety. We finally demonstrate its scalability and generalization performance in real-world urban navigation with a quadruped robot, Spot.

