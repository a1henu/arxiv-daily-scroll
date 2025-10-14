---
layout: default
title: High-resolution Photo Enhancement in Real-time: A Laplacian Pyramid Network
---

# High-resolution Photo Enhancement in Real-time: A Laplacian Pyramid Network
**arXiv**：[2510.11613v1](https://arxiv.org/abs/2510.11613) · [PDF](https://arxiv.org/pdf/2510.11613.pdf)  
**作者**：Feng Zhang, Haoyou Deng, Zhiqiang Li, Lida Li, Bin Xu, Qingbo Lu, Zisheng Cao, Minchen Wei, Changxin Gao, Nong Sang, Xiang Bai  

**一句话要点**：提出LLF-LUT++网络，实现高分辨率图像实时增强与高性能平衡

**关键词**：图像增强, 拉普拉斯金字塔, 3D LUT, 实时处理, 高分辨率图像, 空间频率变换器

## 3 点简述
- 核心问题：现有方法在增强性能与计算效率间难以兼顾，无法在边缘设备部署
- 方法要点：结合全局3D LUT与局部拉普拉斯滤波，通过拉普拉斯金字塔分解重构
- 实验效果：在HDR+数据集PSNR提升2.64 dB，4K图像处理仅需13 ms

## 摘要（原文）

> Photo enhancement plays a crucial role in augmenting the visual aesthetics of
> a photograph. In recent years, photo enhancement methods have either focused on
> enhancement performance, producing powerful models that cannot be deployed on
> edge devices, or prioritized computational efficiency, resulting in inadequate
> performance for real-world applications. To this end, this paper introduces a
> pyramid network called LLF-LUT++, which integrates global and local operators
> through closed-form Laplacian pyramid decomposition and reconstruction. This
> approach enables fast processing of high-resolution images while also achieving
> excellent performance. Specifically, we utilize an image-adaptive 3D LUT that
> capitalizes on the global tonal characteristics of downsampled images, while
> incorporating two distinct weight fusion strategies to achieve coarse global
> image enhancement. To implement this strategy, we designed a spatial-frequency
> transformer weight predictor that effectively extracts the desired distinct
> weights by leveraging frequency features. Additionally, we apply local
> Laplacian filters to adaptively refine edge details in high-frequency
> components. After meticulously redesigning the network structure and
> transformer model, LLF-LUT++ not only achieves a 2.64 dB improvement in PSNR on
> the HDR+ dataset, but also further reduces runtime, with 4K resolution images
> processed in just 13 ms on a single GPU. Extensive experimental results on two
> benchmark datasets further show that the proposed approach performs favorably
> compared to state-of-the-art methods. The source code will be made publicly
> available at https://github.com/fengzhang427/LLF-LUT.

