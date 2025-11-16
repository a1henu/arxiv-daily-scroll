---
layout: default
title: LampQ: Towards Accurate Layer-wise Mixed Precision Quantization for Vision Transformers
---

# LampQ: Towards Accurate Layer-wise Mixed Precision Quantization for Vision Transformers
**arXiv**：[2511.10004v1](https://arxiv.org/abs/2511.10004) · [PDF](https://arxiv.org/pdf/2511.10004.pdf)  
**作者**：Minjun Kim, Jaeri Lee, Jongjin Kim, Jeongin Yun, Yongmo Kwon, U Kang  

**一句话要点**：提出LampQ方法以解决Vision Transformer混合精度量化中的粒度粗、度量不匹配和位分配问题

**关键词**：Vision Transformer量化, 混合精度量化, 层级别量化, Fisher信息度量, 整数线性规划, 零样本量化

## 3 点简述
- 现有ViT量化方法采用均匀精度，忽略组件对量化的敏感度差异
- LampQ采用层级量化、类型感知Fisher度量和整数线性规划优化位宽分配
- 实验显示LampQ在图像分类、目标检测等任务中实现先进量化性能

## 摘要（原文）

> How can we accurately quantize a pre-trained Vision Transformer model? Quantization algorithms compress Vision Transformers (ViTs) into low-bit formats, reducing memory and computation demands with minimal accuracy degradation. However, existing methods rely on uniform precision, ignoring the diverse sensitivity of ViT components to quantization. Metric-based Mixed Precision Quantization (MPQ) is a promising alternative, but previous MPQ methods for ViTs suffer from three major limitations: 1) coarse granularity, 2) mismatch in metric scale across component types, and 3) quantization-unaware bit allocation. In this paper, we propose LampQ (Layer-wise Mixed Precision Quantization for Vision Transformers), an accurate metric-based MPQ method for ViTs to overcome these limitations. LampQ performs layer-wise quantization to achieve both fine-grained control and efficient acceleration, incorporating a type-aware Fisher-based metric to measure sensitivity. Then, LampQ assigns bit-widths optimally through integer linear programming and further updates them iteratively. Extensive experiments show that LampQ provides the state-of-the-art performance in quantizing ViTs pre-trained on various tasks such as image classification, object detection, and zero-shot quantization.

