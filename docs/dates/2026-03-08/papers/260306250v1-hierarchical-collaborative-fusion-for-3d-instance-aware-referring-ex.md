---
layout: default
title: Hierarchical Collaborative Fusion for 3D Instance-aware Referring Expression Segmentation
---

# Hierarchical Collaborative Fusion for 3D Instance-aware Referring Expression Segmentation
**arXiv**：[2603.06250v1](https://arxiv.org/abs/2603.06250) · [PDF](https://arxiv.org/pdf/2603.06250.pdf)  
**作者**：Keshen Zhou, Runnan Chen, Mingming Gong, Tongliang Liu  

**一句话要点**：提出HCF-RES框架，通过分层视觉语义分解与渐进融合解决3D指代表达分割中多模态特征利用不足的问题

**关键词**：3D指代表达分割, 多模态融合, 分层语义分解, 实例感知, 点云处理, 视觉语言对齐

## 3 点简述
- 核心问题：现有3D指代表达分割方法仅依赖稀疏点云，缺乏细粒度视觉语义信息
- 方法要点：利用SAM实例掩码引导CLIP编码，实现像素级与实例级的双粒度特征提取
- 实验效果：在ScanRefer和Multi3DRefer数据集上达到最先进性能

## 摘要（原文）

> Generalised 3D Referring Expression Segmentation (3D-GRES) localizes objects in 3D scenes based on natural language, even when descriptions match multiple or zero targets. Existing methods rely solely on sparse point clouds, lacking rich visual semantics for fine-grained descriptions. We propose HCF-RES, a multi-modal framework with two key innovations. First, Hierarchical Visual Semantic Decomposition leverages SAM instance masks to guide CLIP encoding at dual granularities -- pixel-level and instance-level features -- preserving object boundaries during 2D-to-3D projection. Second, Progressive Multi-level Fusion integrates representations through intra-modal collaboration, cross-modal adaptive weighting between 2D semantic and 3D geometric features, and language-guided refinement. HCF-RES achieves state-of-the-art results on both ScanRefer and Multi3DRefer.

