---
layout: default
title: SRU-Pix2Pix: A Fusion-Driven Generator Network for Medical Image Translation with Few-Shot Learning
---

# SRU-Pix2Pix: A Fusion-Driven Generator Network for Medical Image Translation with Few-Shot Learning
**arXiv**：[2601.04785v1](https://arxiv.org/abs/2601.04785) · [PDF](https://arxiv.org/pdf/2601.04785.pdf)  
**作者**：Xihe Qiu, Yang Dai, Xiaoyu Tan, Sijia Li, Fenghao Sun, Lu Gan, Liang Liu  

**一句话要点**：提出SRU-Pix2Pix，融合SEResNet与U-Net++以提升少样本医学图像翻译的质量与结构保真度。

**关键词**：医学图像翻译, 少样本学习, Pix2Pix, SEResNet, U-Net++, MRI

## 3 点简述
- 核心问题：MRI图像获取时间长、成本高、分辨率受限，需高效图像翻译方法。
- 方法要点：集成SEResNet增强特征表示，U-Net++改进多尺度融合，简化PatchGAN稳定训练。
- 实验或效果：在少于500张图像的少样本条件下，多任务中实现高结构保真度和图像质量，泛化能力强。

## 摘要（原文）

> Magnetic Resonance Imaging (MRI) provides detailed tissue information, but its clinical application is limited by long acquisition time, high cost, and restricted resolution. Image translation has recently gained attention as a strategy to address these limitations. Although Pix2Pix has been widely applied in medical image translation, its potential has not been fully explored. In this study, we propose an enhanced Pix2Pix framework that integrates Squeeze-and-Excitation Residual Networks (SEResNet) and U-Net++ to improve image generation quality and structural fidelity. SEResNet strengthens critical feature representation through channel attention, while U-Net++ enhances multi-scale feature fusion. A simplified PatchGAN discriminator further stabilizes training and refines local anatomical realism. Experimental results demonstrate that under few-shot conditions with fewer than 500 images, the proposed method achieves consistent structural fidelity and superior image quality across multiple intra-modality MRI translation tasks, showing strong generalization ability. These results suggest an effective extension of Pix2Pix for medical image translation.

