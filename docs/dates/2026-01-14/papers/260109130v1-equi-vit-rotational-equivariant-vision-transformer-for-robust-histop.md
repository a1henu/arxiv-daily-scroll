---
layout: default
title: Equi-ViT: Rotational Equivariant Vision Transformer for Robust Histopathology Analysis
---

# Equi-ViT: Rotational Equivariant Vision Transformer for Robust Histopathology Analysis
**arXiv**：[2601.09130v1](https://arxiv.org/abs/2601.09130) · [PDF](https://arxiv.org/pdf/2601.09130.pdf)  
**作者**：Fuyao Chen, Yuexi Du, Elèonore V. Lieffrig, Nicha C. Dvornek, John A. Onofrey  

**一句话要点**：提出Equi-ViT以解决组织病理学分析中ViT对旋转和反射变换的非等变性限制。

**关键词**：等变性视觉Transformer, 组织病理学分析, 旋转等变性, 补丁嵌入, 鲁棒性增强, 数字病理学

## 3 点简述
- 标准ViT在组织病理学图像中缺乏对旋转和反射的等变性，影响鲁棒性。
- 在ViT的补丁嵌入阶段集成等变卷积核，实现旋转等变表示学习。
- 在结直肠癌数据集上展示增强的数据效率和跨图像方向的稳定分类性能。

## 摘要（原文）

> Vision Transformers (ViTs) have gained rapid adoption in computational pathology for their ability to model long-range dependencies through self-attention, addressing the limitations of convolutional neural networks that excel at local pattern capture but struggle with global contextual reasoning. Recent pathology-specific foundation models have further advanced performance by leveraging large-scale pretraining. However, standard ViTs remain inherently non-equivariant to transformations such as rotations and reflections, which are ubiquitous variations in histopathology imaging. To address this limitation, we propose Equi-ViT, which integrates an equivariant convolution kernel into the patch embedding stage of a ViT architecture, imparting built-in rotational equivariance to learned representations. Equi-ViT achieves superior rotation-consistent patch embeddings and stable classification performance across image orientations. Our results on a public colorectal cancer dataset demonstrate that incorporating equivariant patch embedding enhances data efficiency and robustness, suggesting that equivariant transformers could potentially serve as more generalizable backbones for the application of ViT in histopathology, such as digital pathology foundation models.

