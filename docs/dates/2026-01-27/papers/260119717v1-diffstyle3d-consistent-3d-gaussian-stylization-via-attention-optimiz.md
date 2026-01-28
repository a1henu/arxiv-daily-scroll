---
layout: default
title: DiffStyle3D: Consistent 3D Gaussian Stylization via Attention Optimization
---

# DiffStyle3D: Consistent 3D Gaussian Stylization via Attention Optimization
**arXiv**：[2601.19717v1](https://arxiv.org/abs/2601.19717) · [PDF](https://arxiv.org/pdf/2601.19717.pdf)  
**作者**：Yitong Yang, Xuexin Liu, Yinglin Wang, Jing Wang, Hao Dou, Changshuo Wang, Shuting He  

**一句话要点**：提出DiffStyle3D以解决3D高斯风格化中的多视角一致性问题

**关键词**：3D风格迁移, 高斯风格化, 注意力优化, 多视角一致性, 扩散模型

## 3 点简述
- 现有方法难以建模多视角一致性，扩散方法训练不稳定
- 通过注意力优化在潜在空间直接对齐风格特征，保持内容特征
- 实验显示DiffStyle3D在风格化质量和视觉真实感上优于先进方法

## 摘要（原文）

> 3D style transfer enables the creation of visually expressive 3D content, enriching the visual appearance of 3D scenes and objects. However, existing VGG- and CLIP-based methods struggle to model multi-view consistency within the model itself, while diffusion-based approaches can capture such consistency but rely on denoising directions, leading to unstable training. To address these limitations, we propose DiffStyle3D, a novel diffusion-based paradigm for 3DGS style transfer that directly optimizes in the latent space. Specifically, we introduce an Attention-Aware Loss that performs style transfer by aligning style features in the self-attention space, while preserving original content through content feature alignment. Inspired by the geometric invariance of 3D stylization, we propose a Geometry-Guided Multi-View Consistency method that integrates geometric information into self-attention to enable cross-view correspondence modeling. Based on geometric information, we additionally construct a geometry-aware mask to prevent redundant optimization in overlapping regions across views, which further improves multi-view consistency. Extensive experiments show that DiffStyle3D outperforms state-of-the-art methods, achieving higher stylization quality and visual realism.

