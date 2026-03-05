---
layout: default
title: NOVA3R: Non-pixel-aligned Visual Transformer for Amodal 3D Reconstruction
---

# NOVA3R: Non-pixel-aligned Visual Transformer for Amodal 3D Reconstruction
**arXiv**：[2603.04179v1](https://arxiv.org/abs/2603.04179) · [PDF](https://arxiv.org/pdf/2603.04179.pdf)  
**作者**：Weirong Chen, Chuanxia Zheng, Ganlin Zhang, Andrea Vedaldi, Daniel Cremers  

**一句话要点**：提出NOVA3R方法，通过非像素对齐视觉Transformer从无位姿图像集进行前馈式3D重建。

**关键词**：非像素对齐3D重建, 视觉Transformer, 场景令牌机制, 扩散解码器, 无位姿图像, 点云重建

## 3 点简述
- 核心问题：解决像素对齐方法在3D重建中几何依赖像素预测、无法恢复不可见点及重叠区域结构重复的问题。
- 方法要点：采用场景令牌机制聚合无位姿图像信息，结合扩散解码器重建完整非像素对齐点云。
- 实验或效果：在场景级和对象级数据集上验证，重建精度和完整性优于现有方法。

## 摘要（原文）

> We present NOVA3R, an effective approach for non-pixel-aligned 3D reconstruction from a set of unposed images in a feed-forward manner. Unlike pixel-aligned methods that tie geometry to per-ray predictions, our formulation learns a global, view-agnostic scene representation that decouples reconstruction from pixel alignment. This addresses two key limitations in pixel-aligned 3D: (1) it recovers both visible and invisible points with a complete scene representation, and (2) it produces physically plausible geometry with fewer duplicated structures in overlapping regions. To achieve this, we introduce a scene-token mechanism that aggregates information across unposed images and a diffusion-based 3D decoder that reconstructs complete, non-pixel-aligned point clouds. Extensive experiments on both scene-level and object-level datasets demonstrate that NOVA3R outperforms state-of-the-art methods in terms of reconstruction accuracy and completeness.

