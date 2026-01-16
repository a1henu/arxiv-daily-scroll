---
layout: default
title: SatMap: Revisiting Satellite Maps as Prior for Online HD Map Construction
---

# SatMap: Revisiting Satellite Maps as Prior for Online HD Map Construction
**arXiv**：[2601.10512v1](https://arxiv.org/abs/2601.10512) · [PDF](https://arxiv.org/pdf/2601.10512.pdf)  
**作者**：Kanak Mazumder, Fabian B. Flohr  

**一句话要点**：提出SatMap方法，通过融合卫星地图与多视角相机观测，在线构建高精地图以解决自动驾驶中的深度模糊和遮挡问题。

**关键词**：高精地图构建, 卫星地图先验, 多视角融合, 自动驾驶感知, 矢量化预测, 鸟瞰视角

## 3 点简述
- 核心问题：在线高精地图构建中，仅依赖车载相机存在深度感知有限和遮挡导致的精度下降问题。
- 方法要点：利用鸟瞰视角的卫星地图作为全局先验，结合多视角相机观测，直接预测矢量化高精地图。
- 实验或效果：在nuScenes数据集上，相比仅相机基线提升34.8% mAP，相比相机-LiDAR融合基线提升8.5% mAP，并在长距离和恶劣天气条件下验证优势。

## 摘要（原文）

> Online high-definition (HD) map construction is an essential part of a safe and robust end-to-end autonomous driving (AD) pipeline. Onboard camera-based approaches suffer from limited depth perception and degraded accuracy due to occlusion. In this work, we propose SatMap, an online vectorized HD map estimation method that integrates satellite maps with multi-view camera observations and directly predicts a vectorized HD map for downstream prediction and planning modules. Our method leverages lane-level semantics and texture from satellite imagery captured from a Bird's Eye View (BEV) perspective as a global prior, effectively mitigating depth ambiguity and occlusion. In our experiments on the nuScenes dataset, SatMap achieves 34.8% mAP performance improvement over the camera-only baseline and 8.5% mAP improvement over the camera-LiDAR fusion baseline. Moreover, we evaluate our model in long-range and adverse weather conditions to demonstrate the advantages of using a satellite prior map. Source code will be available at https://iv.ee.hm.edu/satmap/.

