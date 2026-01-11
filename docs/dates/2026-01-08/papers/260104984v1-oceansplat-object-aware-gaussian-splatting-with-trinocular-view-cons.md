---
layout: default
title: OceanSplat: Object-aware Gaussian Splatting with Trinocular View Consistency for Underwater Scene Reconstruction
---

# OceanSplat: Object-aware Gaussian Splatting with Trinocular View Consistency for Underwater Scene Reconstruction
**arXiv**：[2601.04984v1](https://arxiv.org/abs/2601.04984) · [PDF](https://arxiv.org/pdf/2601.04984.pdf)  
**作者**：Minseong Kweon, Jinsun Park  

**一句话要点**：提出OceanSplat，通过三目视图一致性和深度正则化解决水下场景重建中的光学退化问题。

**关键词**：水下场景重建, 3D高斯溅射, 视图一致性, 深度正则化, 散射介质处理

## 3 点简述
- 核心问题：水下光学退化导致多视图不一致，影响3D高斯溅射的几何重建准确性。
- 方法要点：引入三目视图一致性约束和合成极线深度先验，结合深度感知透明度调整，分离散射介质与物体几何。
- 实验或效果：在真实和模拟水下场景中，显著优于现有方法，减少漂浮伪影，提升重建和恢复质量。

## 摘要（原文）

> We introduce OceanSplat, a novel 3D Gaussian Splatting-based approach for accurately representing 3D geometry in underwater scenes. To overcome multi-view inconsistencies caused by underwater optical degradation, our method enforces trinocular view consistency by rendering horizontally and vertically translated camera views relative to each input view and aligning them via inverse warping. Furthermore, these translated camera views are used to derive a synthetic epipolar depth prior through triangulation, which serves as a self-supervised depth regularizer. These geometric constraints facilitate the spatial optimization of 3D Gaussians and preserve scene structure in underwater environments. We also propose a depth-aware alpha adjustment that modulates the opacity of 3D Gaussians during early training based on their $z$-component and viewing direction, deterring the formation of medium-induced primitives. With our contributions, 3D Gaussians are disentangled from the scattering medium, enabling robust representation of object geometry and significantly reducing floating artifacts in reconstructed underwater scenes. Experiments on real-world underwater and simulated scenes demonstrate that OceanSplat substantially outperforms existing methods for both scene reconstruction and restoration in scattering media.

