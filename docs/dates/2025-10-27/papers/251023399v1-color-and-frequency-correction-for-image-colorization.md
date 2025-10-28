---
layout: default
title: Color and Frequency Correction for Image Colorization
---

# Color and Frequency Correction for Image Colorization
**arXiv**：[2510.23399v1](https://arxiv.org/abs/2510.23399) · [PDF](https://arxiv.org/pdf/2510.23399.pdf)  
**作者**：Yun Kai Zhuang  

**一句话要点**：提出颜色和频率校正方案以优化DDColor图像着色模型性能

**关键词**：图像着色, 颜色校正, 频率优化, DDColor模型, 性能提升

## 3 点简述
- 核心问题：DDColor模型存在频段限制和输入维度不足导致的色偏问题
- 方法要点：构建两种优化方案并组合，针对频率和颜色进行校正
- 实验或效果：在PSNR和SSIM等指标上实现性能提升

## 摘要（原文）

> The project has carried out the re-optimization of image coloring in
> accordance with the existing Autocolorization direction model DDColor. For the
> experiments on the existing weights of DDColor, we found that it has
> limitations in some frequency bands and the color cast problem caused by
> insufficient input dimension. We construct two optimization schemes and combine
> them, which achieves the performance improvement of indicators such as PSNR and
> SSIM of the images after DDColor.

