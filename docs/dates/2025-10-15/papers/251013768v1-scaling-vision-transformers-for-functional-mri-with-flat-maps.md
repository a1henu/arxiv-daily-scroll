---
layout: default
title: Scaling Vision Transformers for Functional MRI with Flat Maps
---

# Scaling Vision Transformers for Functional MRI with Flat Maps
**arXiv**：[2510.13768v1](https://arxiv.org/abs/2510.13768) · [PDF](https://arxiv.org/pdf/2510.13768.pdf)  
**作者**：Connor Lane, Daniel Z. Kaplan, Tanishq Mathew Abraham, Paul S. Scotti  

**一句话要点**：提出基于扁平图的视觉变换器，用于功能磁共振成像视频分析

**关键词**：功能磁共振成像, 视觉变换器, 扁平图表示, 时空掩码自编码, 脑状态解码, 基础模型

## 3 点简述
- 核心问题：如何将4D fMRI数据表示为适合深度学习模型的输入形式。
- 方法要点：将fMRI数据转换为2D扁平图视频，并采用时空掩码自编码器训练。
- 实验或效果：模型性能随数据集规模提升，支持跨受试者状态解码和个体特征解码。

## 摘要（原文）

> A key question for adapting modern deep learning architectures to functional
> MRI (fMRI) is how to represent the data for model input. To bridge the modality
> gap between fMRI and natural images, we transform the 4D volumetric fMRI data
> into videos of 2D fMRI activity flat maps. We train Vision Transformers on 2.3K
> hours of fMRI flat map videos from the Human Connectome Project using the
> spatiotemporal masked autoencoder (MAE) framework. We observe that masked fMRI
> modeling performance improves with dataset size according to a strict power
> scaling law. Downstream classification benchmarks show that our model learns
> rich representations supporting both fine-grained state decoding across
> subjects, as well as subject-specific trait decoding across changes in brain
> state. This work is part of an ongoing open science project to build foundation
> models for fMRI data. Our code and datasets are available at
> https://github.com/MedARC-AI/fmri-fm.

