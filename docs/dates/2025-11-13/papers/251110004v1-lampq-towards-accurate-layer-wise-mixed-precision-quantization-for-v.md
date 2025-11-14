---
layout: default
title: LampQ: Towards Accurate Layer-wise Mixed Precision Quantization for Vision Transformers
---

# LampQ: Towards Accurate Layer-wise Mixed Precision Quantization for Vision Transformers
**arXiv**：[2511.10004v1](https://arxiv.org/abs/2511.10004) · [PDF](https://arxiv.org/pdf/2511.10004.pdf)  
**作者**：Minjun Kim, Jaeri Lee, Jongjin Kim, Jeongin Yun, Yongmo Kwon, U Kang  

**一句话要点**：提出LampQ方法以解决Vision Transformer层间量化精度问题

**关键词**：Vision Transformer量化, 混合精度量化, 层间量化, Fisher度量, 整数线性规划

## 3 点简述
- 核心问题：现有ViT量化方法采用统一精度，忽略组件敏感性差异。
- 方法要点：使用层间混合精度量化，结合类型感知Fisher度量和整数线性规划。
- 实验效果：在图像分类等任务中实现最先进的量化性能。

## 摘要（原文）

> How can we accurately quantize a pre-trained Vision Transformer model? Quantization algorithms compress Vision Transformers (ViTs) into low-bit formats, reducing memory and computation demands with minimal accuracy degradation. However, existing methods rely on uniform precision, ignoring the diverse sensitivity of ViT components to quantization. Metric-based Mixed Precision Quantization (MPQ) is a promising alternative, but previous MPQ methods for ViTs suffer from three major limitations: 1) coarse granularity, 2) mismatch in metric scale across component types, and 3) quantization-unaware bit allocation. In this paper, we propose LampQ (Layer-wise Mixed Precision Quantization for Vision Transformers), an accurate metric-based MPQ method for ViTs to overcome these limitations. LampQ performs layer-wise quantization to achieve both fine-grained control and efficient acceleration, incorporating a type-aware Fisher-based metric to measure sensitivity. Then, LampQ assigns bit-widths optimally through integer linear programming and further updates them iteratively. Extensive experiments show that LampQ provides the state-of-the-art performance in quantizing ViTs pre-trained on various tasks such as image classification, object detection, and zero-shot quantization.

