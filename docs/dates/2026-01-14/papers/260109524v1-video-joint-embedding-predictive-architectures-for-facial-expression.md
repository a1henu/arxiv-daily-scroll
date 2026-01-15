---
layout: default
title: Video Joint-Embedding Predictive Architectures for Facial Expression Recognition
---

# Video Joint-Embedding Predictive Architectures for Facial Expression Recognition
**arXiv**：[2601.09524v1](https://arxiv.org/abs/2601.09524) · [PDF](https://arxiv.org/pdf/2601.09524.pdf)  
**作者**：Lennart Eing, Cristina Luna-Jiménez, Silvan Mertes, Elisabeth André  

**一句话要点**：提出视频联合嵌入预测架构用于面部表情识别，实现高效预训练与强泛化能力。

**关键词**：视频联合嵌入预测架构, 面部表情识别, 预训练方法, 嵌入预测, 跨数据集泛化

## 3 点简述
- 核心问题：传统视频预训练依赖像素重建，可能捕获无关背景信息，影响面部表情识别效果。
- 方法要点：采用V-JEPA，通过预测掩码区域嵌入从未掩码区域嵌入学习，避免无关信息干扰。
- 实验或效果：在RAVDESS和CREMA-D数据集上达到SOTA，跨数据集评估显示强泛化能力。

## 摘要（原文）

> This paper introduces a novel application of Video Joint-Embedding Predictive Architectures (V-JEPAs) for Facial Expression Recognition (FER). Departing from conventional pre-training methods for video understanding that rely on pixel-level reconstructions, V-JEPAs learn by predicting embeddings of masked regions from the embeddings of unmasked regions. This enables the trained encoder to not capture irrelevant information about a given video like the color of a region of pixels in the background. Using a pre-trained V-JEPA video encoder, we train shallow classifiers using the RAVDESS and CREMA-D datasets, achieving state-of-the-art performance on RAVDESS and outperforming all other vision-based methods on CREMA-D (+1.48 WAR). Furthermore, cross-dataset evaluations reveal strong generalization capabilities, demonstrating the potential of purely embedding-based pre-training approaches to advance FER. We release our code at https://github.com/lennarteingunia/vjepa-for-fer.

