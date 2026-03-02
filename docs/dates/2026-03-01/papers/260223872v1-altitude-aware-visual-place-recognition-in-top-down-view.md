---
layout: default
title: Altitude-Aware Visual Place Recognition in Top-Down View
---

# Altitude-Aware Visual Place Recognition in Top-Down View
**arXiv**：[2602.23872v1](https://arxiv.org/abs/2602.23872) · [PDF](https://arxiv.org/pdf/2602.23872.pdf)  
**作者**：Xingyu Shao, Mengfan He, Chunyu Li, Liangzheng Sun, Ziyang Meng  

**一句话要点**：提出基于地面特征密度分析的视觉位置识别方法，以解决空中平台在显著高度变化下的定位问题。

**关键词**：视觉位置识别, 高度估计, 空中平台定位, 地面特征密度分析, 图像分类

## 3 点简述
- 核心问题：空中视觉位置识别在高度大幅变化时面临挑战，传统方法依赖额外硬件或深度估计精度有限。
- 方法要点：通过分析图像中地面特征密度估计相对高度，并基于高度裁剪生成规范查询图像，用于分类式视觉位置识别。
- 实验或效果：在多样地形和高度条件下，该方法提升了定位准确性和鲁棒性，相比传统方法显著减少误差并提高检索性能。

## 摘要（原文）

> To address the challenge of aerial visual place recognition (VPR) problem under significant altitude variations, this study proposes an altitude-adaptive VPR approach that integrates ground feature density analysis with image classification techniques. The proposed method estimates airborne platforms' relative altitude by analyzing the density of ground features in images, then applies relative altitude-based cropping to generate canonical query images, which are subsequently used in a classification-based VPR strategy for localization. Extensive experiments across diverse terrains and altitude conditions demonstrate that the proposed approach achieves high accuracy and robustness in both altitude estimation and VPR under significant altitude changes. Compared to conventional methods relying on barometric altimeters or Time-of-Flight (ToF) sensors, this solution requires no additional hardware and offers a plug-and-play solution for downstream applications, {making it suitable for small- and medium-sized airborne platforms operating in diverse environments, including rural and urban areas.} Under significant altitude variations, incorporating our relative altitude estimation module into the VPR retrieval pipeline boosts average R@1 and R@5 by 29.85\% and 60.20\%, respectively, compared with applying VPR retrieval alone. Furthermore, compared to traditional {Monocular Metric Depth Estimation (MMDE) methods}, the proposed method reduces the mean error by 202.1 m, yielding average additional improvements of 31.4\% in R@1 and 44\% in R@5. These results demonstrate that our method establishes a robust, vision-only framework for three-dimensional visual place recognition, offering a practical and scalable solution for accurate airborne platforms localization under large altitude variations and limited sensor availability.

