---
layout: default
title: SARMAE: Masked Autoencoder for SAR Representation Learning
---

# SARMAE: Masked Autoencoder for SAR Representation Learning
**arXiv**：[2512.16635v1](https://arxiv.org/abs/2512.16635) · [PDF](https://arxiv.org/pdf/2512.16635.pdf)  
**作者**：Danxu Liu, Di Wang, Hebaixu Wang, Haoyang Chen, Wentao Jiang, Yilin Cheng, Haonan Guo, Wei Cui, Jing Zhang  

**一句话要点**：提出SARMAE以解决SAR图像数据稀缺和斑点噪声问题，实现自监督表示学习。

**关键词**：合成孔径雷达, 自监督学习, 掩码自编码器, 斑点噪声, 表示学习, 遥感图像

## 3 点简述
- 核心问题：SAR图像数据稀缺和斑点噪声阻碍深度学习语义表示学习。
- 方法要点：构建SAR-1M数据集，设计SARE注入斑点噪声和SARC利用光学先验对齐特征。
- 实验或效果：在分类、检测和分割任务上达到先进性能，代码模型开源。

## 摘要（原文）

> Synthetic Aperture Radar (SAR) imagery plays a critical role in all-weather, day-and-night remote sensing applications. However, existing SAR-oriented deep learning is constrained by data scarcity, while the physically grounded speckle noise in SAR imagery further hampers fine-grained semantic representation learning. To address these challenges, we propose SARMAE, a Noise-Aware Masked Autoencoder for self-supervised SAR representation learning. Specifically, we construct SAR-1M, the first million-scale SAR dataset, with additional paired optical images, to enable large-scale pre-training. Building upon this, we design Speckle-Aware Representation Enhancement (SARE), which injects SAR-specific speckle noise into masked autoencoders to facilitate noise-aware and robust representation learning. Furthermore, we introduce Semantic Anchor Representation Constraint (SARC), which leverages paired optical priors to align SAR features and ensure semantic consistency. Extensive experiments across multiple SAR datasets demonstrate that SARMAE achieves state-of-the-art performance on classification, detection, and segmentation tasks. Code and models will be available at https://github.com/MiliLab/SARMAE.

