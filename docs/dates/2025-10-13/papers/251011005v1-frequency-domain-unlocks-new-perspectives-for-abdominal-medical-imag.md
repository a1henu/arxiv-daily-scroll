---
layout: default
title: Frequency Domain Unlocks New Perspectives for Abdominal Medical Image Segmentation
---

# Frequency Domain Unlocks New Perspectives for Abdominal Medical Image Segmentation
**arXiv**：[2510.11005v1](https://arxiv.org/abs/2510.11005) · [PDF](https://arxiv.org/pdf/2510.11005.pdf)  
**作者**：Kai Han, Siqi Ma, Chengxuan Qian, Jun Chen, Chongwen Lyu, Yuqing Song, Zhe Liu  

**一句话要点**：提出FASS框架以解决腹部医学图像中低对比度肿瘤分割难题

**关键词**：医学图像分割, 频率域分析, 小波变换, 前景感知, 边界约束

## 3 点简述
- 核心问题：基础模型在复杂低对比度背景下难以区分肿瘤与正常组织
- 方法要点：结合前景感知、小波变换频率增强和边缘约束模块
- 实验或效果：多数据集验证，在复杂条件下鲁棒性和细节识别表现优异

## 摘要（原文）

> Accurate segmentation of tumors and adjacent normal tissues in medical images
> is essential for surgical planning and tumor staging. Although foundation
> models generally perform well in segmentation tasks, they often struggle to
> focus on foreground areas in complex, low-contrast backgrounds, where some
> malignant tumors closely resemble normal organs, complicating contextual
> differentiation. To address these challenges, we propose the Foreground-Aware
> Spectrum Segmentation (FASS) framework. First, we introduce a foreground-aware
> module to amplify the distinction between background and the entire volume
> space, allowing the model to concentrate more effectively on target areas.
> Next, a feature-level frequency enhancement module, based on wavelet transform,
> extracts discriminative high-frequency features to enhance boundary recognition
> and detail perception. Eventually, we introduce an edge constraint module to
> preserve geometric continuity in segmentation boundaries. Extensive experiments
> on multiple medical datasets demonstrate superior performance across all
> metrics, validating the effectiveness of our framework, particularly in
> robustness under complex conditions and fine structure recognition. Our
> framework significantly enhances segmentation of low-contrast images, paving
> the way for applications in more diverse and complex medical imaging scenarios.

