---
layout: default
title: SmartSplat: Feature-Smart Gaussians for Scalable Compression of Ultra-High-Resolution Images
---

# SmartSplat: Feature-Smart Gaussians for Scalable Compression of Ultra-High-Resolution Images
**arXiv**：[2512.20377v1](https://arxiv.org/abs/2512.20377) · [PDF](https://arxiv.org/pdf/2512.20377.pdf)  
**作者**：Linfei Li, Lin Zhang, Zhong Wang, Ying Shen  

**一句话要点**：提出SmartSplat以解决超高分辨率图像压缩中压缩比与重建保真度的平衡问题

**关键词**：图像压缩, 高斯泼溅, 超高分辨率, 特征感知采样, 可扩展编码, 重建保真度

## 3 点简述
- 核心问题：生成式AI加速超高分辨率内容生产，现有2D高斯模型在压缩比与保真度间难以平衡
- 方法要点：引入梯度-颜色引导变分采样和基于排除的均匀采样，优化高斯基元空间布局与颜色初始化
- 实验或效果：在DIV8K和16K数据集上超越先进方法，支持任意分辨率与压缩比，展现强可扩展性

## 摘要（原文）

> Recent advances in generative AI have accelerated the production of ultra-high-resolution visual content, posing significant challenges for efficient compression and real-time decoding on end-user devices. Inspired by 3D Gaussian Splatting, recent 2D Gaussian image models improve representation efficiency, yet existing methods struggle to balance compression ratio and reconstruction fidelity in ultra-high-resolution scenarios. To address this issue, we propose SmartSplat, a highly adaptive and feature-aware GS-based image compression framework that supports arbitrary image resolutions and compression ratios. SmartSplat leverages image-aware features such as gradients and color variances, introducing a Gradient-Color Guided Variational Sampling strategy together with an Exclusion-based Uniform Sampling scheme to improve the non-overlapping coverage of Gaussian primitives in pixel space. In addition, we propose a Scale-Adaptive Gaussian Color Sampling method to enhance color initialization across scales. Through joint optimization of spatial layout, scale, and color initialization, SmartSplat efficiently captures both local structures and global textures using a limited number of Gaussians, achieving high reconstruction quality under strong compression. Extensive experiments on DIV8K and a newly constructed 16K dataset demonstrate that SmartSplat consistently outperforms state-of-the-art methods at comparable compression ratios and exceeds their compression limits, showing strong scalability and practical applicability. The code is publicly available at https://github.com/lif314/SmartSplat.

