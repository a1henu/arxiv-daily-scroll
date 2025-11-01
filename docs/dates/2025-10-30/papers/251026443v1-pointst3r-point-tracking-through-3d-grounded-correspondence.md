---
layout: default
title: PointSt3R: Point Tracking through 3D Grounded Correspondence
---

# PointSt3R: Point Tracking through 3D Grounded Correspondence
**arXiv**：[2510.26443v1](https://arxiv.org/abs/2510.26443) · [PDF](https://arxiv.org/pdf/2510.26443.pdf)  
**作者**：Rhodri Guerrier, Adam W. Harley, Dima Damen  

**一句话要点**：提出PointSt3R方法，通过3D基础对应实现点跟踪，提升动态和静态场景性能。

**关键词**：点跟踪, 3D对应, 动态场景, 可见性预测, 模型微调, 合成数据训练

## 3 点简述
- 核心问题：现有3D重建模型在动态点跟踪中表现不足，需适应动态对应和可见性处理。
- 方法要点：结合重建损失、动态对应训练和可见性头，微调MASt3R模型用于点跟踪。
- 实验效果：在多个数据集上实现竞争性或更优的点跟踪结果，如TAP-Vid-DAVIS和EgoPoints。

## 摘要（原文）

> Recent advances in foundational 3D reconstruction models, such as DUSt3R and
> MASt3R, have shown great potential in 2D and 3D correspondence in static
> scenes. In this paper, we propose to adapt them for the task of point tracking
> through 3D grounded correspondence. We first demonstrate that these models are
> competitive point trackers when focusing on static points, present in current
> point tracking benchmarks ($+33.5\%$ on EgoPoints vs. CoTracker2). We propose
> to combine the reconstruction loss with training for dynamic correspondence
> along with a visibility head, and fine-tuning MASt3R for point tracking using a
> relatively small amount of synthetic data. Importantly, we only train and
> evaluate on pairs of frames where one contains the query point, effectively
> removing any temporal context. Using a mix of dynamic and static point
> correspondences, we achieve competitive or superior point tracking results on
> four datasets (e.g. competitive on TAP-Vid-DAVIS 73.8 $\delta_{avg}$ / 85.8\%
> occlusion acc. for PointSt3R compared to 75.7 / 88.3\% for CoTracker2; and
> significantly outperform CoTracker3 on EgoPoints 61.3 vs 54.2 and RGB-S 87.0 vs
> 82.8). We also present results on 3D point tracking along with several
> ablations on training datasets and percentage of dynamic correspondences.

