---
layout: default
title: Quantifying and Inducing Shape Bias in CNNs via Max-Pool Dilation
---

# Quantifying and Inducing Shape Bias in CNNs via Max-Pool Dilation
**arXiv**：[2601.05599v1](https://arxiv.org/abs/2601.05599) · [PDF](https://arxiv.org/pdf/2601.05599.pdf)  
**作者**：Takito Sawada, Akinori Iwata, Masahiro Okuda  

**一句话要点**：提出数据驱动指标和最大池化膨胀方法，以量化并诱导CNN形状偏置，提升形状主导数据集分类性能。

**关键词**：形状偏置量化, 最大池化膨胀, CNN纹理偏置, 数据驱动指标, 低数据分类

## 3 点简述
- CNN存在纹理偏置，在形状主导数据上性能下降，缺乏量化指标识别受益数据集。
- 提出基于SSIM的指标量化数据集形状-纹理平衡，并修改最大池化膨胀以诱导形状偏置。
- 实验表明方法在形状主导数据集上提升分类准确率，尤其在低数据场景下有效。

## 摘要（原文）

> Convolutional Neural Networks (CNNs) are known to exhibit a strong texture bias, favoring local patterns over global shape information--a tendency inherent to their convolutional architecture. While this bias is beneficial for texture-rich natural images, it often degrades performance on shape-dominant data such as illustrations and sketches. Although prior work has proposed shape-biased models to mitigate this issue, these approaches lack a quantitative metric for identifying which datasets would actually benefit from such modifications. To address this gap, we propose a data-driven metric that quantifies the shape-texture balance of a dataset by computing the Structural Similarity Index (SSIM) between each image's luminance channel and its L0-smoothed counterpart. Building on this metric, we further introduce a computationally efficient adaptation method that promotes shape bias by modifying the dilation of max-pooling operations while keeping convolutional weights frozen. Experimental results show that this approach consistently improves classification accuracy on shape-dominant datasets, particularly in low-data regimes where full fine-tuning is impractical, requiring training only the final classification layer.

