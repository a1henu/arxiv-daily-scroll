---
layout: default
title: C3G: Learning Compact 3D Representations with 2K Gaussians
---

# C3G: Learning Compact 3D Representations with 2K Gaussians
**arXiv**：[2512.04021v1](https://arxiv.org/abs/2512.04021) · [PDF](https://arxiv.org/pdf/2512.04021.pdf)  
**作者**：Honggyu An, Jaewoo Jung, Mungyeom Kim, Sunghwan Hong, Chaehyun Kim, Kazumi Fukuda, Minkyeong Jeon, Jisang Han, Takuya Narihira, Hyuna Ko, Junsu Kim, Yuki Mitsufuji, Seungryong Kim  

**一句话要点**：提出C3G框架以解决无姿态稀疏视图下3D重建与理解中高斯冗余和特征聚合问题

**关键词**：3D高斯溅射, 紧凑表示, 多视图特征聚合, 无姿态重建, 开放词汇分割, 视图不变特征

## 3 点简述
- 核心问题：现有方法生成过多冗余3D高斯，导致内存开销大和多视图特征聚合不佳，影响新视图合成和场景理解性能。
- 方法要点：引入可学习令牌通过自注意力聚合多视图特征，指导在关键空间位置生成紧凑3D高斯，并利用注意力模式高效提升特征。
- 实验或效果：在无姿态新视图合成、3D开放词汇分割和视图不变特征聚合实验中，C3G在内存效率和特征保真度上优于现有方法。

## 摘要（原文）

> Reconstructing and understanding 3D scenes from unposed sparse views in a feed-forward manner remains as a challenging task in 3D computer vision. Recent approaches use per-pixel 3D Gaussian Splatting for reconstruction, followed by a 2D-to-3D feature lifting stage for scene understanding. However, they generate excessive redundant Gaussians, causing high memory overhead and sub-optimal multi-view feature aggregation, leading to degraded novel view synthesis and scene understanding performance. We propose C3G, a novel feed-forward framework that estimates compact 3D Gaussians only at essential spatial locations, minimizing redundancy while enabling effective feature lifting. We introduce learnable tokens that aggregate multi-view features through self-attention to guide Gaussian generation, ensuring each Gaussian integrates relevant visual features across views. We then exploit the learned attention patterns for Gaussian decoding to efficiently lift features. Extensive experiments on pose-free novel view synthesis, 3D open-vocabulary segmentation, and view-invariant feature aggregation demonstrate our approach's effectiveness. Results show that a compact yet geometrically meaningful representation is sufficient for high-quality scene reconstruction and understanding, achieving superior memory efficiency and feature fidelity compared to existing methods.

