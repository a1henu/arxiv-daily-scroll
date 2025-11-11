---
layout: default
title: REOcc: Camera-Radar Fusion with Radar Feature Enrichment for 3D Occupancy Prediction
---

# REOcc: Camera-Radar Fusion with Radar Feature Enrichment for 3D Occupancy Prediction
**arXiv**：[2511.06666v1](https://arxiv.org/abs/2511.06666) · [PDF](https://arxiv.org/pdf/2511.06666.pdf)  
**作者**：Chaehee Song, Sanmin Kim, Hyeonjun Jeong, Juyeb Shin, Joonhee Lim, Dongsuk Kum  

**一句话要点**：提出REOcc相机-雷达融合网络，通过丰富雷达特征解决3D占用预测中的稀疏和噪声问题。

**关键词**：3D占用预测, 相机-雷达融合, 雷达特征增强, 空间密度提升, 噪声缓解

## 3 点简述
- 核心问题：相机单独依赖在挑战性环境中表现不佳，雷达数据稀疏和噪声限制融合效果。
- 方法要点：引入雷达密度器和放大器，集成空间与上下文信息，提升雷达特征密度和质量。
- 实验或效果：在Occ3D-nuScenes基准上显著优于相机基线，尤其在动态物体类中表现突出。

## 摘要（原文）

> Vision-based 3D occupancy prediction has made significant advancements, but
> its reliance on cameras alone struggles in challenging environments. This
> limitation has driven the adoption of sensor fusion, among which camera-radar
> fusion stands out as a promising solution due to their complementary strengths.
> However, the sparsity and noise of the radar data limits its effectiveness,
> leading to suboptimal fusion performance. In this paper, we propose REOcc, a
> novel camera-radar fusion network designed to enrich radar feature
> representations for 3D occupancy prediction. Our approach introduces two main
> components, a Radar Densifier and a Radar Amplifier, which refine radar
> features by integrating spatial and contextual information, effectively
> enhancing spatial density and quality. Extensive experiments on the
> Occ3D-nuScenes benchmark demonstrate that REOcc achieves significant
> performance gains over the camera-only baseline model, particularly in dynamic
> object classes. These results underscore REOcc's capability to mitigate the
> sparsity and noise of the radar data. Consequently, radar complements camera
> data more effectively, unlocking the full potential of camera-radar fusion for
> robust and reliable 3D occupancy prediction.

