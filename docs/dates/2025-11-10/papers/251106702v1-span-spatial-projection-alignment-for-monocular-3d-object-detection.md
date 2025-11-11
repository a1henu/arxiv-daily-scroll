---
layout: default
title: SPAN: Spatial-Projection Alignment for Monocular 3D Object Detection
---

# SPAN: Spatial-Projection Alignment for Monocular 3D Object Detection
**arXiv**：[2511.06702v1](https://arxiv.org/abs/2511.06702) · [PDF](https://arxiv.org/pdf/2511.06702.pdf)  
**作者**：Yifan Wang, Yian Zhao, Fanqi Pu, Xiaochen Yang, Yang Tang, Xi Chen, Wenming Yang  

**一句话要点**：提出SPAN方法以解决单目3D检测中几何一致性缺失问题

**关键词**：单目3D检测, 几何对齐, 空间约束, 投影对齐, 任务学习策略

## 3 点简述
- 核心问题：现有方法解耦预测忽略几何约束，导致性能不佳
- 方法要点：引入空间点对齐和3D-2D投影对齐，增强几何一致性
- 实验或效果：易于集成现有检测器，显著提升性能

## 摘要（原文）

> Existing monocular 3D detectors typically tame the pronounced nonlinear
> regression of 3D bounding box through decoupled prediction paradigm, which
> employs multiple branches to estimate geometric center, depth, dimensions, and
> rotation angle separately. Although this decoupling strategy simplifies the
> learning process, it inherently ignores the geometric collaborative constraints
> between different attributes, resulting in the lack of geometric consistency
> prior, thereby leading to suboptimal performance. To address this issue, we
> propose novel Spatial-Projection Alignment (SPAN) with two pivotal components:
> (i). Spatial Point Alignment enforces an explicit global spatial constraint
> between the predicted and ground-truth 3D bounding boxes, thereby rectifying
> spatial drift caused by decoupled attribute regression. (ii). 3D-2D Projection
> Alignment ensures that the projected 3D box is aligned tightly within its
> corresponding 2D detection bounding box on the image plane, mitigating
> projection misalignment overlooked in previous works. To ensure training
> stability, we further introduce a Hierarchical Task Learning strategy that
> progressively incorporates spatial-projection alignment as 3D attribute
> predictions refine, preventing early stage error propagation across attributes.
> Extensive experiments demonstrate that the proposed method can be easily
> integrated into any established monocular 3D detector and delivers significant
> performance improvements.

