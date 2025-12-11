---
layout: default
title: Log NeRF: Comparing Spaces for Learning Radiance Fields
---

# Log NeRF: Comparing Spaces for Learning Radiance Fields
**arXiv**：[2512.09375v1](https://arxiv.org/abs/2512.09375) · [PDF](https://arxiv.org/pdf/2512.09375.pdf)  
**作者**：Sihe Chen, Luv Verma, Bruce A. Maxwell  

**一句话要点**：提出Log NeRF，通过log RGB空间学习辐射场以提升渲染质量与鲁棒性。

**关键词**：神经辐射场, 颜色空间, 对数变换, 渲染质量, 低光条件, BIDR模型

## 3 点简述
- 核心问题：NeRF在sRGB空间学习辐射场，未考虑颜色空间对表示学习的影响。
- 方法要点：基于BIDR模型，假设log RGB空间能简化光照与反射分离，训练NeRF在不同颜色空间进行比较。
- 实验或效果：log RGB空间在渲染质量、场景鲁棒性和低光条件下表现更优，且适用于不同网络变体。

## 摘要（原文）

> Neural Radiance Fields (NeRF) have achieved remarkable results in novel view synthesis, typically using sRGB images for supervision. However, little attention has been paid to the color space in which the network is learning the radiance field representation. Inspired by the BiIlluminant Dichromatic Reflection (BIDR) model, which suggests that a logarithmic transformation simplifies the separation of illumination and reflectance, we hypothesize that log RGB space enables NeRF to learn a more compact and effective representation of scene appearance. To test this, we captured approximately 30 videos using a GoPro camera, ensuring linear data recovery through inverse encoding. We trained NeRF models under various color space interpretations linear, sRGB, GPLog, and log RGB by converting each network output to a common color space before rendering and loss computation, enforcing representation learning in different color spaces. Quantitative and qualitative evaluations demonstrate that using a log RGB color space consistently improves rendering quality, exhibits greater robustness across scenes, and performs particularly well in low light conditions while using the same bit-depth input images. Further analysis across different network sizes and NeRF variants confirms the generalization and stability of the log space advantage.

