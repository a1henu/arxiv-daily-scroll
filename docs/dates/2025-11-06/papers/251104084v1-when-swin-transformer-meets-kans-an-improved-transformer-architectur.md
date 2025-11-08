---
layout: default
title: When Swin Transformer Meets KANs: An Improved Transformer Architecture for Medical Image Segmentation
---

# When Swin Transformer Meets KANs: An Improved Transformer Architecture for Medical Image Segmentation
**arXiv**：[2511.04084v1](https://arxiv.org/abs/2511.04084) · [PDF](https://arxiv.org/pdf/2511.04084.pdf)  
**作者**：Nishchal Sapkota, Haoyan Shi, Yejia Zhang, Xianshi Ma, Bofang Zheng, Danny Z. Chen  

**一句话要点**：提出UKAST架构，集成KANs于Swin Transformer，提升医学图像分割的数据效率与性能。

**关键词**：医学图像分割, Swin Transformer, Kolmogorov-Arnold网络, 数据效率, 全局上下文建模

## 3 点简述
- 医学图像分割面临复杂结构和标注数据稀缺的挑战。
- 在Swin Transformer编码器中引入基于有理函数的KANs，优化计算效率。
- 在多个2D/3D基准测试中实现SOTA，数据稀缺下表现优异。

## 摘要（原文）

> Medical image segmentation is critical for accurate diagnostics and treatment
> planning, but remains challenging due to complex anatomical structures and
> limited annotated training data. CNN-based segmentation methods excel at local
> feature extraction, but struggle with modeling long-range dependencies.
> Transformers, on the other hand, capture global context more effectively, but
> are inherently data-hungry and computationally expensive. In this work, we
> introduce UKAST, a U-Net like architecture that integrates rational-function
> based Kolmogorov-Arnold Networks (KANs) into Swin Transformer encoders. By
> leveraging rational base functions and Group Rational KANs (GR-KANs) from the
> Kolmogorov-Arnold Transformer (KAT), our architecture addresses the
> inefficiencies of vanilla spline-based KANs, yielding a more expressive and
> data-efficient framework with reduced FLOPs and only a very small increase in
> parameter count compared to SwinUNETR. UKAST achieves state-of-the-art
> performance on four diverse 2D and 3D medical image segmentation benchmarks,
> consistently surpassing both CNN- and Transformer-based baselines. Notably, it
> attains superior accuracy in data-scarce settings, alleviating the data-hungry
> limitations of standard Vision Transformers. These results show the potential
> of KAN-enhanced Transformers to advance data-efficient medical image
> segmentation. Code is available at: https://github.com/nsapkota417/UKAST

