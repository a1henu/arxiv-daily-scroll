---
layout: default
title: Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling
---

# Upsample Anything: A Simple and Hard to Beat Baseline for Feature Upsampling
**arXiv**：[2511.16301v1](https://arxiv.org/abs/2511.16301) · [PDF](https://arxiv.org/pdf/2511.16301.pdf)  
**作者**：Minseok Seo, Mark Hamilton, Changick Kim  

**一句话要点**：提出Upsample Anything框架，通过测试时优化实现特征上采样，解决像素级应用限制。

**关键词**：特征上采样, 测试时优化, 高斯核学习, 像素级重建, 边缘感知操作

## 3 点简述
- 核心问题：视觉基础模型特征下采样限制像素级任务应用，现有方法依赖重训练或复杂优化。
- 方法要点：使用各向异性高斯核结合空间和范围线索，实现无需训练的轻量级每图像优化。
- 实验或效果：在语义分割和深度估计等任务中达到SOTA，每图像处理约0.419秒。

## 摘要（原文）

> We present \textbf{Upsample Anything}, a lightweight test-time optimization (TTO) framework that restores low-resolution features to high-resolution, pixel-wise outputs without any training. Although Vision Foundation Models demonstrate strong generalization across diverse downstream tasks, their representations are typically downsampled by 14x/16x (e.g., ViT), which limits their direct use in pixel-level applications. Existing feature upsampling approaches depend on dataset-specific retraining or heavy implicit optimization, restricting scalability and generalization. Upsample Anything addresses these issues through a simple per-image optimization that learns an anisotropic Gaussian kernel combining spatial and range cues, effectively bridging Gaussian Splatting and Joint Bilateral Upsampling. The learned kernel acts as a universal, edge-aware operator that transfers seamlessly across architectures and modalities, enabling precise high-resolution reconstruction of features, depth, or probability maps. It runs in only $\approx0.419 \text{s}$ per 224x224 image and achieves state-of-the-art performance on semantic segmentation, depth estimation, and both depth and probability map upsampling.

