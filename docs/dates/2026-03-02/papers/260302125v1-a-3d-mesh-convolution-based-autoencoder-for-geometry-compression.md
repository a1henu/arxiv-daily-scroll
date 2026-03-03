---
layout: default
title: A 3D mesh convolution-based autoencoder for geometry compression
---

# A 3D mesh convolution-based autoencoder for geometry compression
**arXiv**：[2603.02125v1](https://arxiv.org/abs/2603.02125) · [PDF](https://arxiv.org/pdf/2603.02125.pdf)  
**作者**：Germain Bregeon, Marius Preda, Radu Ispas, Titus Zaharia  

**一句话要点**：提出基于3D网格卷积的自编码器，用于无需预处理的几何压缩

**关键词**：3D网格压缩, 卷积自编码器, 几何重建, 潜在空间分类, 不规则网格处理

## 3 点简述
- 核心问题：处理不规则网格数据，无需预处理或流形/水密条件限制
- 方法要点：通过网格面直接学习特征，使用专用池化和反池化保持连接性
- 实验或效果：在多类数据集上，几何重建和潜在空间分类任务优于现有方法

## 摘要（原文）

> In this paper, we introduce a novel 3D mesh convolution-based autoencoder for geometry compression, able to deal with irregular mesh data without requiring neither preprocessing nor manifold/watertightness conditions. The proposed approach extracts meaningful latent representations by learning features directly from the mesh faces, while preserving connectivity through dedicated pooling and unpooling operations. The encoder compresses the input mesh into a compact base mesh space, which ensures that the latent space remains comparable. The decoder reconstructs the original connectivity and restores the compressed geometry to its full resolution. Extensive experiments on multi-class datasets demonstrate that our method outperforms state-of-the-art approaches in both 3D mesh geometry reconstruction and latent space classification tasks. Code available at: github.com/germainGB/MeshConv3D

