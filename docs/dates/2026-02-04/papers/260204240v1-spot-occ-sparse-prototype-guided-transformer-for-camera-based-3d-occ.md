---
layout: default
title: SPOT-Occ: Sparse Prototype-guided Transformer for Camera-based 3D Occupancy Prediction
---

# SPOT-Occ: Sparse Prototype-guided Transformer for Camera-based 3D Occupancy Prediction
**arXiv**：[2602.04240v1](https://arxiv.org/abs/2602.04240) · [PDF](https://arxiv.org/pdf/2602.04240.pdf)  
**作者**：Suzeyu Chen, Leheng Li, Ying-Cong Chen  

**一句话要点**：提出SPOT-Occ稀疏原型引导Transformer，以高效解决相机3D占用预测中的稀疏特征聚合问题。

**关键词**：3D占用预测, 稀疏Transformer, 原型引导, 相机感知, 自动驾驶, 特征聚合

## 3 点简述
- 核心问题：稀疏3D表示导致解码器需高效聚合非均匀分布体素特征，避免计算密集注意力瓶颈。
- 方法要点：采用原型引导稀疏Transformer解码器，通过自适应原型选择和去噪范式实现稳定特征聚合。
- 实验或效果：模型在速度和精度上均显著超越先前方法，适用于自动驾驶实时部署。

## 摘要（原文）

> Achieving highly accurate and real-time 3D occupancy prediction from cameras is a critical requirement for the safe and practical deployment of autonomous vehicles. While this shift to sparse 3D representations solves the encoding bottleneck, it creates a new challenge for the decoder: how to efficiently aggregate information from a sparse, non-uniformly distributed set of voxel features without resorting to computationally prohibitive dense attention.
>   In this paper, we propose a novel Prototype-based Sparse Transformer Decoder that replaces this costly interaction with an efficient, two-stage process of guided feature selection and focused aggregation. Our core idea is to make the decoder's attention prototype-guided. We achieve this through a sparse prototype selection mechanism, where each query adaptively identifies a compact set of the most salient voxel features, termed prototypes, for focused feature aggregation.
>   To ensure this dynamic selection is stable and effective, we introduce a complementary denoising paradigm. This approach leverages ground-truth masks to provide explicit guidance, guaranteeing a consistent query-prototype association across decoder layers. Our model, dubbed SPOT-Occ, outperforms previous methods with a significant margin in speed while also improving accuracy. Source code is released at https://github.com/chensuzeyu/SpotOcc.

