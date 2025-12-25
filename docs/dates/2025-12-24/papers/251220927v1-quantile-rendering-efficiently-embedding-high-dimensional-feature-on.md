---
layout: default
title: Quantile Rendering: Efficiently Embedding High-dimensional Feature on 3D Gaussian Splatting
---

# Quantile Rendering: Efficiently Embedding High-dimensional Feature on 3D Gaussian Splatting
**arXiv**：[2512.20927v1](https://arxiv.org/abs/2512.20927) · [PDF](https://arxiv.org/pdf/2512.20927.pdf)  
**作者**：Yoonwoo Jeong, Cheng Sun, Frank Wang, Minsu Cho, Jaesung Choe  

**一句话要点**：提出Quantile Rendering以高效渲染3D高斯泼溅中的高维特征，解决开放词汇查询的实时性挑战。

**关键词**：3D高斯泼溅, 高维特征渲染, 开放词汇分割, 实时渲染, 稀疏采样, 神经渲染

## 3 点简述
- 核心问题：现有方法在3D高斯泼溅中渲染高维特征时效率低且信息损失，影响开放词汇分割质量。
- 方法要点：引入Quantile Rendering，稀疏采样主导影响的高斯，结合GS-Net网络预测特征，提升渲染效率。
- 实验或效果：在ScanNet和LeRF上优于现有方法，512维特征图渲染速度提升约43.7倍，支持实时应用。

## 摘要（原文）

> Recent advancements in computer vision have successfully extended Open-vocabulary segmentation (OVS) to the 3D domain by leveraging 3D Gaussian Splatting (3D-GS). Despite this progress, efficiently rendering the high-dimensional features required for open-vocabulary queries poses a significant challenge. Existing methods employ codebooks or feature compression, causing information loss, thereby degrading segmentation quality. To address this limitation, we introduce Quantile Rendering (Q-Render), a novel rendering strategy for 3D Gaussians that efficiently handles high-dimensional features while maintaining high fidelity. Unlike conventional volume rendering, which densely samples all 3D Gaussians intersecting each ray, Q-Render sparsely samples only those with dominant influence along the ray. By integrating Q-Render into a generalizable 3D neural network, we also propose Gaussian Splatting Network (GS-Net), which predicts Gaussian features in a generalizable manner. Extensive experiments on ScanNet and LeRF demonstrate that our framework outperforms state-of-the-art methods, while enabling real-time rendering with an approximate ~43.7x speedup on 512-D feature maps. Code will be made publicly available.

