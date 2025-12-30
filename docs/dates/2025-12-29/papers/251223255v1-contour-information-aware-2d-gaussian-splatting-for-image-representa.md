---
layout: default
title: Contour Information Aware 2D Gaussian Splatting for Image Representation
---

# Contour Information Aware 2D Gaussian Splatting for Image Representation
**arXiv**：[2512.23255v1](https://arxiv.org/abs/2512.23255) · [PDF](https://arxiv.org/pdf/2512.23255.pdf)  
**作者**：Masaya Takabe, Hiroshi Watanabe, Sujun Hong, Tomohiro Ikai, Zheming Fan, Ryo Ishimoto, Kakeru Sugimoto, Ruri Imichi  

**一句话要点**：提出轮廓信息感知的2D高斯泼溅框架，以解决图像表示中边界模糊问题。

**关键词**：图像表示, 2D高斯泼溅, 轮廓感知, 对象分割, 压缩表示, 实时渲染

## 3 点简述
- 核心问题：现有2D高斯泼溅方法在高压缩下因缺乏轮廓感知导致边界模糊。
- 方法要点：结合对象分割先验，约束高斯到特定区域，防止跨边界混合。
- 实验或效果：在合成色卡和DAVIS数据集上，边缘重建质量优于现有方法，保持快速渲染和低内存。

## 摘要（原文）

> Image representation is a fundamental task in computer vision. Recently, Gaussian Splatting has emerged as an efficient representation framework, and its extension to 2D image representation enables lightweight, yet expressive modeling of visual content. While recent 2D Gaussian Splatting (2DGS) approaches provide compact storage and real-time decoding, they often produce blurry or indistinct boundaries when the number of Gaussians is small due to the lack of contour awareness. In this work, we propose a Contour Information-Aware 2D Gaussian Splatting framework that incorporates object segmentation priors into Gaussian-based image representation. By constraining each Gaussian to a specific segmentation region during rasterization, our method prevents cross-boundary blending and preserves edge structures under high compression. We also introduce a warm-up scheme to stabilize training and improve convergence. Experiments on synthetic color charts and the DAVIS dataset demonstrate that our approach achieves higher reconstruction quality around object edges compared to existing 2DGS methods. The improvement is particularly evident in scenarios with very few Gaussians, while our method still maintains fast rendering and low memory usage.

