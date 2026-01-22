---
layout: default
title: CAG-Avatar: Cross-Attention Guided Gaussian Avatars for High-Fidelity Head Reconstruction
---

# CAG-Avatar: Cross-Attention Guided Gaussian Avatars for High-Fidelity Head Reconstruction
**arXiv**：[2601.14844v1](https://arxiv.org/abs/2601.14844) · [PDF](https://arxiv.org/pdf/2601.14844.pdf)  
**作者**：Zhe Chang, Haodong Jin, Yan Song, Hui Yu  

**一句话要点**：提出条件自适应高斯化身以解决3D头部重建中全局驱动导致的模糊失真问题

**关键词**：3D高斯溅射, 头部重建, 条件自适应驱动, 交叉注意力, 实时渲染

## 3 点简述
- 核心问题：现有3D高斯溅射动画技术采用全局统一驱动，无法区分面部不同区域的动态，导致模糊和失真。
- 方法要点：基于交叉注意力构建条件自适应融合模块，使每个高斯基元根据其规范位置自适应提取驱动信号。
- 实验或效果：显著提升重建保真度，尤其在牙齿等挑战区域，同时保持实时渲染性能。

## 摘要（原文）

> Creating high-fidelity, real-time drivable 3D head avatars is a core challenge in digital animation. While 3D Gaussian Splashing (3D-GS) offers unprecedented rendering speed and quality, current animation techniques often rely on a "one-size-fits-all" global tuning approach, where all Gaussian primitives are uniformly driven by a single expression code. This simplistic approach fails to unravel the distinct dynamics of different facial regions, such as deformable skin versus rigid teeth, leading to significant blurring and distortion artifacts. We introduce Conditionally-Adaptive Gaussian Avatars (CAG-Avatar), a framework that resolves this key limitation. At its core is a Conditionally Adaptive Fusion Module built on cross-attention. This mechanism empowers each 3D Gaussian to act as a query, adaptively extracting relevant driving signals from the global expression code based on its canonical position. This "tailor-made" conditioning strategy drastically enhances the modeling of fine-grained, localized dynamics. Our experiments confirm a significant improvement in reconstruction fidelity, particularly for challenging regions such as teeth, while preserving real-time rendering performance.

