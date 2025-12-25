---
layout: default
title: TGC-Net: A Structure-Aware and Semantically-Aligned Framework for Text-Guided Medical Image Segmentation
---

# TGC-Net: A Structure-Aware and Semantically-Aligned Framework for Text-Guided Medical Image Segmentation
**arXiv**：[2512.21135v1](https://arxiv.org/abs/2512.21135) · [PDF](https://arxiv.org/pdf/2512.21135.pdf)  
**作者**：Gaoren Lin, Huangxuan Zhao, Yuan Xiong, Lefei Zhang, Bo Du, Wentao Zhu  

**一句话要点**：提出TGC-Net框架，通过结构感知与语义对齐解决文本引导医学图像分割中的CLIP应用限制。

**关键词**：文本引导医学图像分割, CLIP应用, 多模态融合, 结构感知编码, 语义对齐, 参数高效适应

## 3 点简述
- 核心问题：CLIP直接应用于医学图像时，存在细粒度结构保留不足、复杂临床描述建模不充分和领域语义错位问题。
- 方法要点：引入语义-结构协同编码器增强多尺度结构，领域增强文本编码器注入医学知识，视觉-语言校准模块优化跨模态对应。
- 实验或效果：在五个数据集上实现最先进性能，参数量显著减少，Dice分数在挑战性基准上提升明显。

## 摘要（原文）

> Text-guided medical segmentation enhances segmentation accuracy by utilizing clinical reports as auxiliary information. However, existing methods typically rely on unaligned image and text encoders, which necessitate complex interaction modules for multimodal fusion. While CLIP provides a pre-aligned multimodal feature space, its direct application to medical imaging is limited by three main issues: insufficient preservation of fine-grained anatomical structures, inadequate modeling of complex clinical descriptions, and domain-specific semantic misalignment. To tackle these challenges, we propose TGC-Net, a CLIP-based framework focusing on parameter-efficient, task-specific adaptations. Specifically, it incorporates a Semantic-Structural Synergy Encoder (SSE) that augments CLIP's ViT with a CNN branch for multi-scale structural refinement, a Domain-Augmented Text Encoder (DATE) that injects large-language-model-derived medical knowledge, and a Vision-Language Calibration Module (VLCM) that refines cross-modal correspondence in a unified feature space. Experiments on five datasets across chest X-ray and thoracic CT modalities demonstrate that TGC-Net achieves state-of-the-art performance with substantially fewer trainable parameters, including notable Dice gains on challenging benchmarks.

