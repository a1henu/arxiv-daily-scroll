---
layout: default
title: TransLocNet: Cross-Modal Attention for Aerial-Ground Vehicle Localization with Contrastive Learning
---

# TransLocNet: Cross-Modal Attention for Aerial-Ground Vehicle Localization with Contrastive Learning
**arXiv**：[2512.10419v1](https://arxiv.org/abs/2512.10419) · [PDF](https://arxiv.org/pdf/2512.10419.pdf)  
**作者**：Phu Pham, Damon Conover, Aniket Bera  

**一句话要点**：提出TransLocNet，通过跨模态注意力与对比学习解决地面LiDAR与空中图像间的定位难题。

**关键词**：跨模态定位, 注意力机制, 对比学习, LiDAR-图像融合, 空中-地面定位

## 3 点简述
- 核心问题：地面LiDAR与空中图像间存在大视角和模态差异，导致空中-地面定位困难。
- 方法要点：使用跨模态注意力融合LiDAR几何与空中语义，结合对比学习优化共享嵌入空间。
- 实验或效果：在CARLA和KITTI上优于现有方法，定位误差降低达63%，实现亚米、亚度精度。

## 摘要（原文）

> Aerial-ground localization is difficult due to large viewpoint and modality gaps between ground-level LiDAR and overhead imagery. We propose TransLocNet, a cross-modal attention framework that fuses LiDAR geometry with aerial semantic context. LiDAR scans are projected into a bird's-eye-view representation and aligned with aerial features through bidirectional attention, followed by a likelihood map decoder that outputs spatial probability distributions over position and orientation. A contrastive learning module enforces a shared embedding space to improve cross-modal alignment. Experiments on CARLA and KITTI show that TransLocNet outperforms state-of-the-art baselines, reducing localization error by up to 63% and achieving sub-meter, sub-degree accuracy. These results demonstrate that TransLocNet provides robust and generalizable aerial-ground localization in both synthetic and real-world settings.

