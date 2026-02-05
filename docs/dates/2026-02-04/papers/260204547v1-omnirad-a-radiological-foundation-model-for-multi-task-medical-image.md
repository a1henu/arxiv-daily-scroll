---
layout: default
title: OmniRad: A Radiological Foundation Model for Multi-Task Medical Image Analysis
---

# OmniRad: A Radiological Foundation Model for Multi-Task Medical Image Analysis
**arXiv**：[2602.04547v1](https://arxiv.org/abs/2602.04547) · [PDF](https://arxiv.org/pdf/2602.04547.pdf)  
**作者**：Luca Zedda, Andrea Loddo, Cecilia Di Ruberto  

**一句话要点**：提出OmniRad放射学基础模型，通过自监督预训练支持多模态医学图像分析任务。

**关键词**：放射学基础模型, 自监督预训练, 多模态医学图像分析, 表示重用, 跨任务可转移性, 医学图像分类与分割

## 3 点简述
- 核心问题：放射学分析需要预训练视觉表示以支持跨模态的异构下游任务。
- 方法要点：基于放射学原理设计自监督模型，预训练120万医学图像，强调表示重用和跨任务可转移性。
- 实验或效果：在MedMNISTv2分类任务中F1提升达2.05%，在MedSegBench分割任务中Dice分数有改进。

## 摘要（原文）

> Radiological analysis increasingly benefits from pretrained visual representations that can support heterogeneous downstream tasks across imaging modalities. In this work, we introduce OmniRad, a self-supervised radiological foundation model pretrained on 1.2 million medical images, designed with radiology-inspired principles emphasizing representation reuse and cross-task transferability. We evaluate the pretrained encoder under multiple downstream adaptation regimes, including lightweight task-specific adapters with a frozen backbone as well as full end-to-end fine-tuning for classification, allowing us to assess both representation quality and task-specific performance. OmniRad is evaluated on a broad suite of public benchmarks spanning classification and segmentation across multiple modalities. On the MedMNISTv2 collection, OmniRad improves classification F1 by up to 2.05% over competing foundation models. For dense prediction, OmniRad attains mean Dice score improvements across six MedSegBench datasets when using frozen representations. Qualitative analyses and latent-space visualizations suggest improved feature clustering and modality-related separation.

