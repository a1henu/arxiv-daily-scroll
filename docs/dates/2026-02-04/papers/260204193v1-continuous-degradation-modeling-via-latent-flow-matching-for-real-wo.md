---
layout: default
title: Continuous Degradation Modeling via Latent Flow Matching for Real-World Super-Resolution
---

# Continuous Degradation Modeling via Latent Flow Matching for Real-World Super-Resolution
**arXiv**：[2602.04193v1](https://arxiv.org/abs/2602.04193) · [PDF](https://arxiv.org/pdf/2602.04193.pdf)  
**作者**：Hyeonjae Kim, Dongjin Kim, Eugene Jin, Tae Hyun Kim  

**一句话要点**：提出基于潜在流匹配的连续退化建模框架，以生成真实世界超分辨率训练数据

**关键词**：真实世界超分辨率, 连续退化建模, 潜在流匹配, 数据合成, 图像增强

## 3 点简述
- 核心问题：现有超分辨率方法在真实图像上表现不佳，因退化复杂且数据对有限
- 方法要点：利用潜在退化空间和流匹配，从单张高分辨率图像合成真实低分辨率图像
- 实验或效果：合成图像准确模拟真实退化，提升超分辨率模型性能

## 摘要（原文）

> While deep learning-based super-resolution (SR) methods have shown impressive outcomes with synthetic degradation scenarios such as bicubic downsampling, they frequently struggle to perform well on real-world images that feature complex, nonlinear degradations like noise, blur, and compression artifacts. Recent efforts to address this issue have involved the painstaking compilation of real low-resolution (LR) and high-resolution (HR) image pairs, usually limited to several specific downscaling factors. To address these challenges, our work introduces a novel framework capable of synthesizing authentic LR images from a single HR image by leveraging the latent degradation space with flow matching. Our approach generates LR images with realistic artifacts at unseen degradation levels, which facilitates the creation of large-scale, real-world SR training datasets. Comprehensive quantitative and qualitative assessments verify that our synthetic LR images accurately replicate real-world degradations. Furthermore, both traditional and arbitrary-scale SR models trained using our datasets consistently yield much better HR outcomes.

