---
layout: default
title: EVolSplat4D: Efficient Volume-based Gaussian Splatting for 4D Urban Scene Synthesis
---

# EVolSplat4D: Efficient Volume-based Gaussian Splatting for 4D Urban Scene Synthesis
**arXiv**：[2601.15951v1](https://arxiv.org/abs/2601.15951) · [PDF](https://arxiv.org/pdf/2601.15951.pdf)  
**作者**：Sheng Miao, Sijin Li, Pan Wang, Dongfeng Bai, Bingbing Liu, Yue Wang, Andreas Geiger, Yiyi Liao  

**一句话要点**：提出EVolSplat4D框架，通过体积与像素高斯预测统一，高效合成4D城市场景新视图。

**关键词**：4D场景合成, 高斯溅射, 前馈重建, 城市场景, 新视图合成, 体积预测

## 3 点简述
- 核心问题：现有方法在城市场景新视图合成中难以平衡重建时间与质量，前馈方法常因逐像素高斯表示导致3D不一致。
- 方法要点：采用三分支统一体积与像素高斯预测，近景静态区域基于3D特征体积预测几何，动态对象使用对象中心规范空间，远景用逐像素分支覆盖。
- 实验或效果：在KITTI-360等数据集上，EVolSplat4D在静态和动态环境重建中优于逐场景优化和前馈基线，实现更高精度和一致性。

## 摘要（原文）

> Novel view synthesis (NVS) of static and dynamic urban scenes is essential for autonomous driving simulation, yet existing methods often struggle to balance reconstruction time with quality. While state-of-the-art neural radiance fields and 3D Gaussian Splatting approaches achieve photorealism, they often rely on time-consuming per-scene optimization. Conversely, emerging feed-forward methods frequently adopt per-pixel Gaussian representations, which lead to 3D inconsistencies when aggregating multi-view predictions in complex, dynamic environments. We propose EvolSplat4D, a feed-forward framework that moves beyond existing per-pixel paradigms by unifying volume-based and pixel-based Gaussian prediction across three specialized branches. For close-range static regions, we predict consistent geometry of 3D Gaussians over multiple frames directly from a 3D feature volume, complemented by a semantically-enhanced image-based rendering module for predicting their appearance. For dynamic actors, we utilize object-centric canonical spaces and a motion-adjusted rendering module to aggregate temporal features, ensuring stable 4D reconstruction despite noisy motion priors. Far-Field scenery is handled by an efficient per-pixel Gaussian branch to ensure full-scene coverage. Experimental results on the KITTI-360, KITTI, Waymo, and PandaSet datasets show that EvolSplat4D reconstructs both static and dynamic environments with superior accuracy and consistency, outperforming both per-scene optimization and state-of-the-art feed-forward baselines.

