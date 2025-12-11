---
layout: default
title: Perception-Inspired Color Space Design for Photo White Balance Editing
---

# Perception-Inspired Color Space Design for Photo White Balance Editing
**arXiv**：[2512.09383v1](https://arxiv.org/abs/2512.09383) · [PDF](https://arxiv.org/pdf/2512.09383.pdf)  
**作者**：Yang Cheng, Ziteng Cui, Lin Gu, Shenghan Su, Zenghui Zhang  

**一句话要点**：提出基于感知启发的可学习HSI颜色空间框架，以解决sRGB白平衡编辑在复杂光照下的泛化限制。

**关键词**：白平衡校正, 颜色空间设计, 计算摄影, 可学习模型, Mamba网络, 图像处理

## 3 点简述
- 核心问题：sRGB颜色模型因固定非线性变换和颜色通道纠缠，在白平衡编辑中难以泛化到复杂光照条件。
- 方法要点：设计圆柱形颜色模型分离亮度与色度，引入可学习参数增强解耦，并采用Mamba网络适配该颜色空间。
- 实验或效果：在基准数据集上验证了方法的优越性，展示了感知启发颜色空间设计在计算摄影中的潜力。

## 摘要（原文）

> White balance (WB) is a key step in the image signal processor (ISP) pipeline that mitigates color casts caused by varying illumination and restores the scene's true colors. Currently, sRGB-based WB editing for post-ISP WB correction is widely used to address color constancy failures in the ISP pipeline when the original camera RAW is unavailable. However, additive color models (e.g., sRGB) are inherently limited by fixed nonlinear transformations and entangled color channels, which often impede their generalization to complex lighting conditions.
>   To address these challenges, we propose a novel framework for WB correction that leverages a perception-inspired Learnable HSI (LHSI) color space. Built upon a cylindrical color model that naturally separates luminance from chromatic components, our framework further introduces dedicated parameters to enhance this disentanglement and learnable mapping to adaptively refine the flexibility. Moreover, a new Mamba-based network is introduced, which is tailored to the characteristics of the proposed LHSI color space.
>   Experimental results on benchmark datasets demonstrate the superiority of our method, highlighting the potential of perception-inspired color space design in computational photography. The source code is available at https://github.com/YangCheng58/WB_Color_Space.

