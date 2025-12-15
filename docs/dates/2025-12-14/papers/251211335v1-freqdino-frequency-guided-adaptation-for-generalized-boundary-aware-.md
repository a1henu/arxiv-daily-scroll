---
layout: default
title: FreqDINO: Frequency-Guided Adaptation for Generalized Boundary-Aware Ultrasound Image Segmentation
---

# FreqDINO: Frequency-Guided Adaptation for Generalized Boundary-Aware Ultrasound Image Segmentation
**arXiv**：[2512.11335v1](https://arxiv.org/abs/2512.11335) · [PDF](https://arxiv.org/pdf/2512.11335.pdf)  
**作者**：Yixuan Zhang, Qing Xu, Yue Li, Xiangjian He, Qian Zhang, Mainul Haque, Rong Qu, Wenting Duan, Zhen Chen  

**一句话要点**：提出FreqDINO以解决超声图像分割中边界退化问题

**关键词**：超声图像分割, 频率引导, 边界感知, 多尺度特征, DINOv3适应

## 3 点简述
- 核心问题：DINOv3预训练于自然图像，对超声图像边界退化不敏感。
- 方法要点：设计多尺度频率提取对齐策略和频率引导边界细化模块。
- 实验或效果：在实验中超越先进方法，展现优异泛化能力。

## 摘要（原文）

> Ultrasound image segmentation is pivotal for clinical diagnosis, yet challenged by speckle noise and imaging artifacts. Recently, DINOv3 has shown remarkable promise in medical image segmentation with its powerful representation capabilities. However, DINOv3, pre-trained on natural images, lacks sensitivity to ultrasound-specific boundary degradation. To address this limitation, we propose FreqDINO, a frequency-guided segmentation framework that enhances boundary perception and structural consistency. Specifically, we devise a Multi-scale Frequency Extraction and Alignment (MFEA) strategy to separate low-frequency structures and multi-scale high-frequency boundary details, and align them via learnable attention. We also introduce a Frequency-Guided Boundary Refinement (FGBR) module that extracts boundary prototypes from high-frequency components and refines spatial features. Furthermore, we design a Multi-task Boundary-Guided Decoder (MBGD) to ensure spatial coherence between boundary and semantic predictions. Extensive experiments demonstrate that FreqDINO surpasses state-of-the-art methods with superior achieves remarkable generalization capability. The code is at https://github.com/MingLang-FD/FreqDINO.

