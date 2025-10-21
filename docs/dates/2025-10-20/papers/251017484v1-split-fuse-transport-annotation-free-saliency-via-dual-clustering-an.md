---
layout: default
title: Split-Fuse-Transport: Annotation-Free Saliency via Dual Clustering and Optimal Transport Alignment
---

# Split-Fuse-Transport: Annotation-Free Saliency via Dual Clustering and Optimal Transport Alignment
**arXiv**：[2510.17484v1](https://arxiv.org/abs/2510.17484) · [PDF](https://arxiv.org/pdf/2510.17484.pdf)  
**作者**：Muhammad Umer Ramzan, Ali Zia, Abdelwahed Khamis, Noman Ali, Usman Ali, Wei Xiang  

**一句话要点**：提出POTNet方法，通过双聚类和最优传输实现无标注显著目标检测

**关键词**：显著目标检测, 无监督学习, 最优传输, 双聚类, 伪掩码生成, 计算机视觉

## 3 点简述
- 核心问题：显著目标检测需可靠伪掩码，但现有方法在原型质量和全局一致性上不足
- 方法要点：采用熵引导双聚类，高熵像素谱聚类、低熵像素k均值，并用最优传输对齐
- 实验或效果：在五个基准上，F-measure优于无监督方法26%、弱监督方法36%

## 摘要（原文）

> Salient object detection (SOD) aims to segment visually prominent regions in
> images and serves as a foundational task for various computer vision
> applications. We posit that SOD can now reach near-supervised accuracy without
> a single pixel-level label, but only when reliable pseudo-masks are available.
> We revisit the prototype-based line of work and make two key observations.
> First, boundary pixels and interior pixels obey markedly different geometry;
> second, the global consistency enforced by optimal transport (OT) is
> underutilized if prototype quality is weak. To address this, we introduce
> POTNet, an adaptation of Prototypical Optimal Transport that replaces POT's
> single k-means step with an entropy-guided dual-clustering head: high-entropy
> pixels are organized by spectral clustering, low-entropy pixels by k-means, and
> the two prototype sets are subsequently aligned by OT. This
> split-fuse-transport design yields sharper, part-aware pseudo-masks in a single
> forward pass, without handcrafted priors. Those masks supervise a standard
> MaskFormer-style encoder-decoder, giving rise to AutoSOD, an end-to-end
> unsupervised SOD pipeline that eliminates SelfMask's offline voting yet
> improves both accuracy and training efficiency. Extensive experiments on five
> benchmarks show that AutoSOD outperforms unsupervised methods by up to 26% and
> weakly supervised methods by up to 36% in F-measure, further narrowing the gap
> to fully supervised models.

