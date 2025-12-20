---
layout: default
title: GFLAN: Generative Functional Layouts
---

# GFLAN: Generative Functional Layouts
**arXiv**：[2512.16275v1](https://arxiv.org/abs/2512.16275) · [PDF](https://arxiv.org/pdf/2512.16275.pdf)  
**作者**：Mohamed Abouagour, Eleftherios Garyfallidis  

**一句话要点**：提出GFLAN框架，通过拓扑规划与几何实现两阶段分解，解决自动平面图生成中捕获建筑推理的挑战。

**关键词**：自动平面图生成, 拓扑规划, 几何实现, 图神经网络, 卷积网络, 建筑推理

## 3 点简述
- 核心问题：自动平面图生成需处理组合搜索、几何约束和功能需求，现有深度学习方法难以捕获拓扑关系优先等建筑推理。
- 方法要点：采用两阶段框架，阶段A用卷积网络分配房间质心，阶段B用图神经网络回归房间边界。
- 实验或效果：未知，但框架旨在通过显式分解改进平面图合成，处理拓扑规划和几何实现。

## 摘要（原文）

> Automated floor plan generation lies at the intersection of combinatorial search, geometric constraint satisfaction, and functional design requirements -- a confluence that has historically resisted a unified computational treatment. While recent deep learning approaches have improved the state of the art, they often struggle to capture architectural reasoning: the precedence of topological relationships over geometric instantiation, the propagation of functional constraints through adjacency networks, and the emergence of circulation patterns from local connectivity decisions. To address these fundamental challenges, this paper introduces GFLAN, a generative framework that restructures floor plan synthesis through explicit factorization into topological planning and geometric realization. Given a single exterior boundary and a front-door location, our approach departs from direct pixel-to-pixel or wall-tracing generation in favor of a principled two-stage decomposition. Stage A employs a specialized convolutional architecture with dual encoders -- separating invariant spatial context from evolving layout state -- to sequentially allocate room centroids within the building envelope via discrete probability maps over feasible placements. Stage B constructs a heterogeneous graph linking room nodes to boundary vertices, then applies a Transformer-augmented graph neural network (GNN) that jointly regresses room boundaries.

