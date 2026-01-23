---
layout: default
title: EVolSplat4D: Efficient Volume-based Gaussian Splatting for 4D Urban Scene Synthesis
---

# EVolSplat4D: Efficient Volume-based Gaussian Splatting for 4D Urban Scene Synthesis
**arXiv**：[2601.15951v1](https://arxiv.org/abs/2601.15951) · [PDF](https://arxiv.org/pdf/2601.15951.pdf)  
**作者**：Sheng Miao, Sijin Li, Pan Wang, Dongfeng Bai, Bingbing Liu, Yue Wang, Andreas Geiger, Yiyi Liao  

**一句话要点**：提出EVolSplat4D框架，通过多分支高斯预测高效合成4D城市场景

**关键词**：4D场景合成, 高斯溅射, 前馈框架, 城市场景重建, 多视图预测, 动态对象处理

## 3 点简述
- 核心问题：现有方法在静态与动态城市场景新视角合成中难以平衡重建时间与质量，前馈方法常因逐像素高斯表示导致3D不一致性。
- 方法要点：采用三分支统一体素与像素高斯预测，包括静态区域体素几何预测、动态对象中心化空间处理及远场景逐像素分支，确保4D重建一致性。
- 实验效果：在KITTI-360等数据集上验证，EVolSplat4D在准确性和一致性上优于逐场景优化和前馈基线方法。

## 摘要（原文）

> Novel view synthesis (NVS) of static and dynamic urban scenes is essential for autonomous driving simulation, yet existing methods often struggle to balance reconstruction time with quality. While state-of-the-art neural radiance fields and 3D Gaussian Splatting approaches achieve photorealism, they often rely on time-consuming per-scene optimization. Conversely, emerging feed-forward methods frequently adopt per-pixel Gaussian representations, which lead to 3D inconsistencies when aggregating multi-view predictions in complex, dynamic environments. We propose EvolSplat4D, a feed-forward framework that moves beyond existing per-pixel paradigms by unifying volume-based and pixel-based Gaussian prediction across three specialized branches. For close-range static regions, we predict consistent geometry of 3D Gaussians over multiple frames directly from a 3D feature volume, complemented by a semantically-enhanced image-based rendering module for predicting their appearance. For dynamic actors, we utilize object-centric canonical spaces and a motion-adjusted rendering module to aggregate temporal features, ensuring stable 4D reconstruction despite noisy motion priors. Far-Field scenery is handled by an efficient per-pixel Gaussian branch to ensure full-scene coverage. Experimental results on the KITTI-360, KITTI, Waymo, and PandaSet datasets show that EvolSplat4D reconstructs both static and dynamic environments with superior accuracy and consistency, outperforming both per-scene optimization and state-of-the-art feed-forward baselines.

