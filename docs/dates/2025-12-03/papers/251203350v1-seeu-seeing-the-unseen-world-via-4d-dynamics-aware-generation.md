---
layout: default
title: SeeU: Seeing the Unseen World via 4D Dynamics-aware Generation
---

# SeeU: Seeing the Unseen World via 4D Dynamics-aware Generation
**arXiv**：[2512.03350v1](https://arxiv.org/abs/2512.03350) · [PDF](https://arxiv.org/pdf/2512.03350.pdf)  
**作者**：Yu Yuan, Tharindu Wickremasinghe, Zeeshan Nadir, Xijun Wang, Yiheng Chi, Stanley H. Chan  

**一句话要点**：提出SeeU方法，通过4D动态感知生成解决2D视觉内容生成中的连续性和物理一致性问题。

**关键词**：4D动态建模, 视觉内容生成, 时空上下文感知, 单目重建, 视频编辑, 物理约束学习

## 3 点简述
- 核心问题：现有视觉生成方法基于2D观测，导致性能受限，难以生成连续和物理一致的未见内容。
- 方法要点：采用2D→4D→2D框架，从稀疏单目帧重建4D世界，学习连续动态，并基于时空上下文生成未见区域。
- 实验或效果：在未见时空生成和视频编辑等任务中展示潜力，实现连续和物理一致的新视觉内容生成。

## 摘要（原文）

> Images and videos are discrete 2D projections of the 4D world (3D space + time). Most visual understanding, prediction, and generation operate directly on 2D observations, leading to suboptimal performance. We propose SeeU, a novel approach that learns the continuous 4D dynamics and generate the unseen visual contents. The principle behind SeeU is a new 2D$\to$4D$\to$2D learning framework. SeeU first reconstructs the 4D world from sparse and monocular 2D frames (2D$\to$4D). It then learns the continuous 4D dynamics on a low-rank representation and physical constraints (discrete 4D$\to$continuous 4D). Finally, SeeU rolls the world forward in time, re-projects it back to 2D at sampled times and viewpoints, and generates unseen regions based on spatial-temporal context awareness (4D$\to$2D). By modeling dynamics in 4D, SeeU achieves continuous and physically-consistent novel visual generation, demonstrating strong potentials in multiple tasks including unseen temporal generation, unseen spatial generation, and video editing.

