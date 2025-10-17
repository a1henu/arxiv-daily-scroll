---
layout: default
title: Vision Mamba for Permeability Prediction of Porous Media
---

# Vision Mamba for Permeability Prediction of Porous Media
**arXiv**：[2510.14516v1](https://arxiv.org/abs/2510.14516) · [PDF](https://arxiv.org/pdf/2510.14516.pdf)  
**作者**：Ali Kashefi, Tapan Mukerji  

**一句话要点**：提出基于Vision Mamba的神经网络以预测三维多孔介质渗透率

**关键词**：渗透率预测, Vision Mamba, 多孔介质, 图像分类, 计算效率, 神经网络

## 3 点简述
- 核心问题：预测三维多孔介质的渗透率，替代传统ViT和CNN方法。
- 方法要点：使用Vision Mamba作为骨干网络，具有线性计算复杂度和较少参数。
- 实验或效果：比较Vision Mamba与ViT和CNN，展示其在效率和准确性上的优势。

## 摘要（原文）

> Vision Mamba has recently received attention as an alternative to Vision
> Transformers (ViTs) for image classification. The network size of Vision Mamba
> scales linearly with input image resolution, whereas ViTs scale quadratically,
> a feature that improves computational and memory efficiency. Moreover, Vision
> Mamba requires a significantly smaller number of trainable parameters than
> traditional convolutional neural networks (CNNs), and thus, they can be more
> memory efficient. Because of these features, we introduce, for the first time,
> a neural network that uses Vision Mamba as its backbone for predicting the
> permeability of three-dimensional porous media. We compare the performance of
> Vision Mamba with ViT and CNN models across multiple aspects of permeability
> prediction and perform an ablation study to assess the effects of its
> components on accuracy. We demonstrate in practice the aforementioned
> advantages of Vision Mamba over ViTs and CNNs in the permeability prediction of
> three-dimensional porous media. We make the source code publicly available to
> facilitate reproducibility and to enable other researchers to build on and
> extend this work. We believe the proposed framework has the potential to be
> integrated into large vision models in which Vision Mamba is used instead of
> ViTs.

