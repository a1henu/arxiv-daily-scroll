---
layout: default
title: Boundary-Aware Test-Time Adaptation for Zero-Shot Medical Image Segmentation
---

# Boundary-Aware Test-Time Adaptation for Zero-Shot Medical Image Segmentation
**arXiv**：[2512.04520v1](https://arxiv.org/abs/2512.04520) · [PDF](https://arxiv.org/pdf/2512.04520.pdf)  
**作者**：Chenlin Xu, Lei Zhang, Lituan Wang, Xinyu Pu, Pengfei Ma, Guangwu Qian, Zizhou Wang, Yan Wang  

**一句话要点**：提出BA-TTA-SAM框架，通过测试时适应增强SAM在零样本医学图像分割中的性能。

**关键词**：医学图像分割, 零样本学习, 测试时适应, 边界感知, 视觉Transformer, SAM模型

## 3 点简述
- 核心问题：SAM在医学图像分割中因领域偏移导致零样本性能受限，需高效增强。
- 方法要点：集成高斯提示注入和边界感知注意力对齐，无需源域训练数据。
- 实验或效果：在四个数据集上平均DICE分数提升12.4%，优于现有方法。

## 摘要（原文）

> Due to the scarcity of annotated data and the substantial computational costs of model, conventional tuning methods in medical image segmentation face critical challenges. Current approaches to adapting pretrained models, including full-parameter and parameter-efficient fine-tuning, still rely heavily on task-specific training on downstream tasks. Therefore, zero-shot segmentation has gained increasing attention, especially with foundation models such as SAM demonstrating promising generalization capabilities. However, SAM still faces notable limitations on medical datasets due to domain shifts, making efficient zero-shot enhancement an urgent research goal. To address these challenges, we propose BA-TTA-SAM, a task-agnostic test-time adaptation framework that significantly enhances the zero-shot segmentation performance of SAM via test-time adaptation. This framework integrates two key mechanisms: (1) The encoder-level Gaussian prompt injection embeds Gaussian-based prompts directly into the image encoder, providing explicit guidance for initial representation learning. (2) The cross-layer boundary-aware attention alignment exploits the hierarchical feature interactions within the ViT backbone, aligning deep semantic responses with shallow boundary cues. Experiments on four datasets, including ISIC, Kvasir, BUSI, and REFUGE, show an average improvement of 12.4\% in the DICE score compared with SAM's zero-shot segmentation performance. The results demonstrate that our method consistently outperforms state-of-the-art models in medical image segmentation. Our framework significantly enhances the generalization ability of SAM, without requiring any source-domain training data. Extensive experiments on publicly available medical datasets strongly demonstrate the superiority of our framework. Our code is available at https://github.com/Emilychenlin/BA-TTA-SAM.

