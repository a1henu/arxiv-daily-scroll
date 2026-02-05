---
layout: default
title: SkeletonGaussian: Editable 4D Generation through Gaussian Skeletonization
---

# SkeletonGaussian: Editable 4D Generation through Gaussian Skeletonization
**arXiv**：[2602.04271v1](https://arxiv.org/abs/2602.04271) · [PDF](https://arxiv.org/pdf/2602.04271.pdf)  
**作者**：Lifan Wu, Ruijie Zhu, Yubo Ai, Tianzhu Zhang  

**一句话要点**：提出SkeletonGaussian框架，通过骨架化高斯表示实现可编辑的4D生成

**关键词**：4D生成, 动态3D高斯, 骨架驱动, 可编辑运动, 单目视频输入

## 3 点简述
- 现有4D生成方法依赖隐式变形场，限制了直接控制与编辑能力
- 引入分层关节表示，将运动分解为骨架驱动的刚性运动与基于六面体的非刚性细化
- 实验表明该方法在生成质量上超越现有方法，并支持直观的运动编辑

## 摘要（原文）

> 4D generation has made remarkable progress in synthesizing dynamic 3D objects from input text, images, or videos. However, existing methods often represent motion as an implicit deformation field, which limits direct control and editability. To address this issue, we propose SkeletonGaussian, a novel framework for generating editable dynamic 3D Gaussians from monocular video input. Our approach introduces a hierarchical articulated representation that decomposes motion into sparse rigid motion explicitly driven by a skeleton and fine-grained non-rigid motion. Concretely, we extract a robust skeleton and drive rigid motion via linear blend skinning, followed by a hexplane-based refinement for non-rigid deformations, enhancing interpretability and editability. Experimental results demonstrate that SkeletonGaussian surpasses existing methods in generation quality while enabling intuitive motion editing, establishing a new paradigm for editable 4D generation. Project page: https://wusar.github.io/projects/skeletongaussian/

