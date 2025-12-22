---
layout: default
title: Multi-level distortion-aware deformable network for omnidirectional image super-resolution
---

# Multi-level distortion-aware deformable network for omnidirectional image super-resolution
**arXiv**：[2512.17343v1](https://arxiv.org/abs/2512.17343) · [PDF](https://arxiv.org/pdf/2512.17343.pdf)  
**作者**：Cuixin Yang, Rongkang Dong, Kin-Man Lam, Yuhang Zhang, Guoping Qiu  

**一句话要点**：提出多级失真感知可变形网络以解决全向图像超分辨率中的几何失真问题

**关键词**：全向图像超分辨率, 几何失真处理, 可变形卷积, 多级特征融合, 低秩分解

## 3 点简述
- 核心问题：ERP投影导致全向图像纬度依赖的几何失真，现有方法采样范围有限，难以捕获大范围失真模式。
- 方法要点：设计三支路特征提取器，结合可变形注意力和扩张可变形卷积，扩展采样范围以捕获失真模式，并采用多级特征融合和低秩分解策略。
- 实验或效果：在公开数据集上实验表明，MDDN优于现有方法，验证了其在ODISR中的有效性和优越性。

## 摘要（原文）

> As augmented reality and virtual reality applications gain popularity, image processing for OmniDirectional Images (ODIs) has attracted increasing attention. OmniDirectional Image Super-Resolution (ODISR) is a promising technique for enhancing the visual quality of ODIs. Before performing super-resolution, ODIs are typically projected from a spherical surface onto a plane using EquiRectangular Projection (ERP). This projection introduces latitude-dependent geometric distortion in ERP images: distortion is minimal near the equator but becomes severe toward the poles, where image content is stretched across a wider area. However, existing ODISR methods have limited sampling ranges and feature extraction capabilities, which hinder their ability to capture distorted patterns over large areas. To address this issue, we propose a novel Multi-level Distortion-aware Deformable Network (MDDN) for ODISR, designed to expand the sampling range and receptive field. Specifically, the feature extractor in MDDN comprises three parallel branches: a deformable attention mechanism (serving as the dilation=1 path) and two dilated deformable convolutions with dilation rates of 2 and 3. This architecture expands the sampling range to include more distorted patterns across wider areas, generating dense and comprehensive features that effectively capture geometric distortions in ERP images. The representations extracted from these deformable feature extractors are adaptively fused in a multi-level feature fusion module. Furthermore, to reduce computational cost, a low-rank decomposition strategy is applied to dilated deformable convolutions. Extensive experiments on publicly available datasets demonstrate that MDDN outperforms state-of-the-art methods, underscoring its effectiveness and superiority in ODISR.

