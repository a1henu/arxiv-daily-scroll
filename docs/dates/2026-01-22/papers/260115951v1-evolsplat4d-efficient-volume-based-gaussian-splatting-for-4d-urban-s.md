---
layout: default
title: EVolSplat4D: Efficient Volume-based Gaussian Splatting for 4D Urban Scene Synthesis
---

# EVolSplat4D: Efficient Volume-based Gaussian Splatting for 4D Urban Scene Synthesis
**arXiv**：[2601.15951v1](https://arxiv.org/abs/2601.15951) · [PDF](https://arxiv.org/pdf/2601.15951.pdf)  
**作者**：Sheng Miao, Sijin Li, Pan Wang, Dongfeng Bai, Bingbing Liu, Yue Wang, Andreas Geiger, Yiyi Liao  

**一句话要点**：提出EVolSplat4D框架，通过体积与像素高斯预测统一，高效合成4D城市场景新视图。

**关键词**：4D场景合成, 高斯溅射, 前馈框架, 体积预测, 动态重建, 城市场景

## 3 点简述
- 核心问题：现有方法在静态与动态城市场景新视图合成中，难以平衡重建时间与质量，或存在3D不一致性。
- 方法要点：采用三分支架构，结合体积预测、语义增强渲染和对象中心运动调整，统一处理近景静态、动态和远景区域。
- 实验或效果：在多个数据集上验证，优于逐场景优化和前馈基线，实现高精度和一致性重建。

## 摘要（原文）

> Novel view synthesis (NVS) of static and dynamic urban scenes is essential for autonomous driving simulation, yet existing methods often struggle to balance reconstruction time with quality. While state-of-the-art neural radiance fields and 3D Gaussian Splatting approaches achieve photorealism, they often rely on time-consuming per-scene optimization. Conversely, emerging feed-forward methods frequently adopt per-pixel Gaussian representations, which lead to 3D inconsistencies when aggregating multi-view predictions in complex, dynamic environments. We propose EvolSplat4D, a feed-forward framework that moves beyond existing per-pixel paradigms by unifying volume-based and pixel-based Gaussian prediction across three specialized branches. For close-range static regions, we predict consistent geometry of 3D Gaussians over multiple frames directly from a 3D feature volume, complemented by a semantically-enhanced image-based rendering module for predicting their appearance. For dynamic actors, we utilize object-centric canonical spaces and a motion-adjusted rendering module to aggregate temporal features, ensuring stable 4D reconstruction despite noisy motion priors. Far-Field scenery is handled by an efficient per-pixel Gaussian branch to ensure full-scene coverage. Experimental results on the KITTI-360, KITTI, Waymo, and PandaSet datasets show that EvolSplat4D reconstructs both static and dynamic environments with superior accuracy and consistency, outperforming both per-scene optimization and state-of-the-art feed-forward baselines.

