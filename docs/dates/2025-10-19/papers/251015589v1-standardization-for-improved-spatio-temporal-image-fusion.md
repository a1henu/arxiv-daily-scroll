---
layout: default
title: Standardization for improved Spatio-Temporal Image Fusion
---

# Standardization for improved Spatio-Temporal Image Fusion
**arXiv**：[2510.15589v1](https://arxiv.org/abs/2510.15589) · [PDF](https://arxiv.org/pdf/2510.15589.pdf)  
**作者**：Harkaitz Goyena, Peter M. Atkinson, Unai Pérez-Goya, M. Dolores Ugarte  

**一句话要点**：提出两种标准化方法以提升时空图像融合精度

**关键词**：时空图像融合, 图像标准化, 上采样方法, 锐化技术, USTFIP方法

## 3 点简述
- 核心问题：不同传感器图像分辨率不匹配限制时空图像融合应用。
- 方法要点：比较传统上采样与基于异常的锐化方法ABSIS。
- 实验效果：ABSIS显著提升USTFIP方法光谱和空间精度。

## 摘要（原文）

> Spatio-Temporal Image Fusion (STIF) methods usually require sets of images
> with matching spatial and spectral resolutions captured by different sensors.
> To facilitate the application of STIF methods, we propose and compare two
> different standardization approaches. The first method is based on traditional
> upscaling of the fine-resolution images. The second method is a sharpening
> approach called Anomaly Based Satellite Image Standardization (ABSIS) that
> blends the overall features found in the fine-resolution image series with the
> distinctive attributes of a specific coarse-resolution image to produce images
> that more closely resemble the outcome of aggregating the fine-resolution
> images. Both methods produce a significant increase in accuracy of the Unpaired
> Spatio Temporal Fusion of Image Patches (USTFIP) STIF method, with the
> sharpening approach increasing the spectral and spatial accuracies of the fused
> images by up to 49.46\% and 78.40\%, respectively.

