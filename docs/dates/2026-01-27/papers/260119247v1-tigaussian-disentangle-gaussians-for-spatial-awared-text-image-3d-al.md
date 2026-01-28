---
layout: default
title: TIGaussian: Disentangle Gaussians for Spatial-Awared Text-Image-3D Alignment
---

# TIGaussian: Disentangle Gaussians for Spatial-Awared Text-Image-3D Alignment
**arXiv**：[2601.19247v1](https://arxiv.org/abs/2601.19247) · [PDF](https://arxiv.org/pdf/2601.19247.pdf)  
**作者**：Jiarun Liu, Qifeng Chen, Yiru Zhao, Minghua Liu, Baorui Ma, Sheng Yang  

**一句话要点**：提出TIGaussian框架，利用3D高斯泼溅特性增强跨模态对齐，以解决文本-图像-3D模态融合中的特征提取与对齐挑战。

**关键词**：3D高斯泼溅, 跨模态对齐, 多模态学习, 特征提取, 文本-图像-3D融合

## 3 点简述
- 核心问题：现有方法在提取3D模态特征和弥合文本、图像与3D之间的模态差距方面存在困难。
- 方法要点：通过多分支3DGS分词器解耦3DGS结构属性，并采用双向跨模态对齐策略，包括多视图特征融合和文本-3D投影模块。
- 实验或效果：在多个数据集上的实验表明，TIGaussian在跨模态检索、零样本分类等任务中达到先进性能。

## 摘要（原文）

> While visual-language models have profoundly linked features between texts and images, the incorporation of 3D modality data, such as point clouds and 3D Gaussians, further enables pretraining for 3D-related tasks, e.g., cross-modal retrieval, zero-shot classification, and scene recognition. As challenges remain in extracting 3D modal features and bridging the gap between different modalities, we propose TIGaussian, a framework that harnesses 3D Gaussian Splatting (3DGS) characteristics to strengthen cross-modality alignment through multi-branch 3DGS tokenizer and modality-specific 3D feature alignment strategies. Specifically, our multi-branch 3DGS tokenizer decouples the intrinsic properties of 3DGS structures into compact latent representations, enabling more generalizable feature extraction. To further bridge the modality gap, we develop a bidirectional cross-modal alignment strategies: a multi-view feature fusion mechanism that leverages diffusion priors to resolve perspective ambiguity in image-3D alignment, while a text-3D projection module adaptively maps 3D features to text embedding space for better text-3D alignment. Extensive experiments on various datasets demonstrate the state-of-the-art performance of TIGaussian in multiple tasks.

