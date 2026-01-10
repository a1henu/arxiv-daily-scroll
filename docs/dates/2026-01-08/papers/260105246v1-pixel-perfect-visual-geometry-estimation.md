---
layout: default
title: Pixel-Perfect Visual Geometry Estimation
---

# Pixel-Perfect Visual Geometry Estimation
**arXiv**：[2601.05246v1](https://arxiv.org/abs/2601.05246) · [PDF](https://arxiv.org/pdf/2601.05246.pdf)  
**作者**：Gangwei Xu, Haotong Lin, Hongcheng Luo, Haiyang Sun, Bing Wang, Guang Chen, Sida Peng, Hangjun Ye, Xin Yang  

**一句话要点**：提出像素级视觉几何模型，通过像素空间生成建模预测高质量无飞点云，用于机器人和增强现实。

**关键词**：像素空间扩散, 单目深度估计, 视频深度估计, 生成建模, 点云优化, 语义提示

## 3 点简述
- 现有几何基础模型存在飞点和细节丢失问题，影响点云质量。
- 引入像素完美深度模型，基于像素空间扩散变换器，结合语义提示和级联架构提升效率与精度。
- 扩展至视频模型，通过语义一致扩散变换器和参考引导令牌传播保持时间一致性，性能领先。

## 摘要（原文）

> Recovering clean and accurate geometry from images is essential for robotics and augmented reality. However, existing geometry foundation models still suffer severely from flying pixels and the loss of fine details. In this paper, we present pixel-perfect visual geometry models that can predict high-quality, flying-pixel-free point clouds by leveraging generative modeling in the pixel space. We first introduce Pixel-Perfect Depth (PPD), a monocular depth foundation model built upon pixel-space diffusion transformers (DiT). To address the high computational complexity associated with pixel-space diffusion, we propose two key designs: 1) Semantics-Prompted DiT, which incorporates semantic representations from vision foundation models to prompt the diffusion process, preserving global semantics while enhancing fine-grained visual details; and 2) Cascade DiT architecture that progressively increases the number of image tokens, improving both efficiency and accuracy. To further extend PPD to video (PPVD), we introduce a new Semantics-Consistent DiT, which extracts temporally consistent semantics from a multi-view geometry foundation model. We then perform reference-guided token propagation within the DiT to maintain temporal coherence with minimal computational and memory overhead. Our models achieve the best performance among all generative monocular and video depth estimation models and produce significantly cleaner point clouds than all other models.

