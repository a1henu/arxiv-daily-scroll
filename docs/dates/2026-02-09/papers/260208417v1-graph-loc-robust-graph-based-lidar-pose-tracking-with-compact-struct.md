---
layout: default
title: Graph-Loc: Robust Graph-Based LiDAR Pose Tracking with Compact Structural Map Priors under Low Observability and Occlusion
---

# Graph-Loc: Robust Graph-Based LiDAR Pose Tracking with Compact Structural Map Priors under Low Observability and Occlusion
**arXiv**：[2602.08417v1](https://arxiv.org/abs/2602.08417) · [PDF](https://arxiv.org/pdf/2602.08417.pdf)  
**作者**：Wentao Zhao, Yihe Niu, Zikun Chen, Rui Li, Yanbo Wang, Tianchen Deng, Jingchuan Wang  

**一句话要点**：提出Graph-Loc，基于图结构先验的鲁棒激光雷达位姿跟踪方法，应对低可观测性和遮挡场景。

**关键词**：激光雷达定位, 图结构先验, 不平衡最优传输, 低可观测性, 遮挡鲁棒性, 紧凑地图

## 3 点简述
- 核心问题：激光雷达位姿跟踪在部分观测、重复结构和严重遮挡下需紧凑地图先验以实现长期自主操作。
- 方法要点：使用轻量级点线图表示先验，通过不平衡最优传输和局部图上下文正则化进行扫描到地图关联，增强鲁棒性。
- 实验效果：在公开基准、压力测试和实际部署中，KB级先验下实现准确稳定跟踪，包括几何退化和持续遮挡场景。

## 摘要（原文）

> Map-based LiDAR pose tracking is essential for long-term autonomous operation, where onboard map priors need be compact for scalable storage and fast retrieval, while online observations are often partial, repetitive, and heavily occluded. We propose Graph-Loc, a graph-based localization framework that tracks the platform pose against compact structural map priors represented as a lightweight point-line graph. Such priors can be constructed from heterogeneous sources commonly available in practice, including polygon outlines vectorized from occupancy/grid maps and CAD/model/floor-plan layouts. For each incoming LiDAR scan, Graph-Loc extracts sparse point and line primitives to form an observation graph, retrieves a pose-conditioned visible subgraph via LiDAR ray simulation, and performs scan-to-map association through unbalanced optimal transport with a local graph-context regularizer. The unbalanced formulation relaxes mass conservation, improving robustness to missing, spurious, and fragmented structures under occlusion. To enhance stability in low-observability segments, we estimate information anisotropy from the refinement normal matrix and defer updates along weakly constrained directions until sufficient constraints reappear. Experiments on public benchmarks, controlled stress tests, and real-world deployments demonstrate accurate and stable tracking with KB-level priors from heterogeneous map sources, including under geometrically degenerate and sustained occlusion and in the presence of gradual scene changes.

