---
layout: default
title: Skullptor: High Fidelity 3D Head Reconstruction in Seconds with Multi-View Normal Prediction
---

# Skullptor: High Fidelity 3D Head Reconstruction in Seconds with Multi-View Normal Prediction
**arXiv**：[2602.21100v1](https://arxiv.org/abs/2602.21100) · [PDF](https://arxiv.org/pdf/2602.21100.pdf)  
**作者**：Noé Artru, Rukhshanda Hussain, Emeline Got, Alexandre Messier, David B. Lindell, Abdallah Dib  

**一句话要点**：提出Skullptor方法，通过多视角法线预测与逆渲染优化，实现高保真3D头部重建，减少相机需求与计算成本。

**关键词**：3D头部重建, 多视角法线预测, 逆渲染优化, 高保真几何, 跨视图注意力, 计算效率

## 3 点简述
- 核心问题：现有方法在单图像重建缺乏细节与多视图重建计算昂贵间存在权衡。
- 方法要点：结合单目基础模型与跨视图注意力，预测几何一致法线，并用于逆渲染优化恢复高频细节。
- 实验或效果：在减少相机需求下，达到与密集视图摄影测量相当的高保真重建，优于现有方法。

## 摘要（原文）

> Reconstructing high-fidelity 3D head geometry from images is critical for a wide range of applications, yet existing methods face fundamental limitations. Traditional photogrammetry achieves exceptional detail but requires extensive camera arrays (25-200+ views), substantial computation, and manual cleanup in challenging areas like facial hair. Recent alternatives present a fundamental trade-off: foundation models enable efficient single-image reconstruction but lack fine geometric detail, while optimization-based methods achieve higher fidelity but require dense views and expensive computation. We bridge this gap with a hybrid approach that combines the strengths of both paradigms. Our method introduces a multi-view surface normal prediction model that extends monocular foundation models with cross-view attention to produce geometrically consistent normals in a feed-forward pass. We then leverage these predictions as strong geometric priors within an inverse rendering optimization framework to recover high-frequency surface details. Our approach outperforms state-of-the-art single-image and multi-view methods, achieving high-fidelity reconstruction on par with dense-view photogrammetry while reducing camera requirements and computational cost. The code and model will be released.

