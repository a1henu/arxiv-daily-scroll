---
layout: default
title: Polyp Segmentation Using Wavelet-Based Cross-Band Integration for Enhanced Boundary Representation
---

# Polyp Segmentation Using Wavelet-Based Cross-Band Integration for Enhanced Boundary Representation
**arXiv**：[2603.03682v1](https://arxiv.org/abs/2603.03682) · [PDF](https://arxiv.org/pdf/2603.03682.pdf)  
**作者**：Haesung Oh, Jaesung Lee  

**一句话要点**：提出基于小波域灰度与RGB互补交互的息肉分割模型以增强边界表示

**关键词**：息肉分割, 小波分析, 边界增强, 灰度表示, RGB整合, 医学图像处理

## 3 点简述
- 核心问题：息肉分割中边界定位困难，源于黏膜对比度低、光照不均和颜色相似性。
- 方法要点：通过小波分析发现灰度域边界对比度更高，设计模型整合灰度与RGB表示以提升边界精度。
- 实验或效果：在四个基准数据集上验证，模型在边界精度和鲁棒性方面优于传统方法。

## 摘要（原文）

> Accurate polyp segmentation is essential for early colorectal cancer detection, yet achieving reliable boundary localization remains challenging due to low mucosal contrast, uneven illumination, and color similarity between polyps and surrounding tissue. Conventional methods relying solely on RGB information often struggle to delineate precise boundaries due to weak contrast and ambiguous structures between polyps and surrounding mucosa. To establish a quantitative foundation for this limitation, we analyzed polyp-background contrast in the wavelet domain, revealing that grayscale representations consistently preserve higher boundary contrast than RGB images across all frequency bands. This finding suggests that boundary cues are more distinctly represented in the grayscale domain than in the color domain. Motivated by this finding, we propose a segmentation model that integrates grayscale and RGB representations through complementary frequency-consistent interaction, enhancing boundary precision while preserving structural coherence. Extensive experiments on four benchmark datasets demonstrate that the proposed approach achieves superior boundary precision and robustness compared to conventional models.

