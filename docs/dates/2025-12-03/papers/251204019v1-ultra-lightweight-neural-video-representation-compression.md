---
layout: default
title: Ultra-lightweight Neural Video Representation Compression
---

# Ultra-lightweight Neural Video Representation Compression
**arXiv**：[2512.04019v1](https://arxiv.org/abs/2512.04019) · [PDF](https://arxiv.org/pdf/2512.04019.pdf)  
**作者**：Ho Man Kwan, Tianhao Peng, Ge Gao, Fan Zhang, Mike Nilsson, Andrew Gower, David Bull  

**一句话要点**：提出NVRC-Lite以加速轻量级神经视频表示压缩，结合多尺度特征网格和八叉树上下文模型。

**关键词**：神经视频压缩, 轻量级表示, 多尺度特征网格, 八叉树熵编码, 计算加速

## 3 点简述
- 核心问题：现有基于INR的视频压缩方法计算复杂度高，熵编码速度慢，影响实际应用。
- 方法要点：集成多尺度特征网格提升低复杂度INR性能，采用八叉树上下文模型加速熵编码。
- 实验或效果：在PSNR和MS-SSIM上优于C3，BD-rate节省达21.03%和23.06%，编码和解码速度分别提升8.4倍和2.5倍。

## 摘要（原文）

> Recent works have demonstrated the viability of utilizing over-fitted implicit neural representations (INRs) as alternatives to autoencoder-based models for neural video compression. Among these INR-based video codecs, Neural Video Representation Compression (NVRC) was the first to adopt a fully end-to-end compression framework that compresses INRs, achieving state-of-the-art performance. Moreover, some recently proposed lightweight INRs have shown comparable performance to their baseline codecs with computational complexity lower than 10kMACs/pixel. In this work, we extend NVRC toward lightweight representations, and propose NVRC-Lite, which incorporates two key changes. Firstly, we integrated multi-scale feature grids into our lightweight neural representation, and the use of higher resolution grids significantly improves the performance of INRs at low complexity. Secondly, we address the issue that existing INRs typically leverage autoregressive models for entropy coding: these are effective but impractical due to their slow coding speed. In this work, we propose an octree-based context model for entropy coding high-dimensional feature grids, which accelerates the entropy coding module of the model. Our experimental results demonstrate that NVRC-Lite outperforms C3, one of the best lightweight INR-based video codecs, with up to 21.03% and 23.06% BD-rate savings when measured in PSNR and MS-SSIM, respectively, while achieving 8.4x encoding and 2.5x decoding speedup. The implementation of NVRC-Lite will be made available.

