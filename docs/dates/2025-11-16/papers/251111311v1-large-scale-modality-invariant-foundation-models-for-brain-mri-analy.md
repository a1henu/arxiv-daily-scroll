---
layout: default
title: Large-scale modality-invariant foundation models for brain MRI analysis: Application to lesion segmentation
---

# Large-scale modality-invariant foundation models for brain MRI analysis: Application to lesion segmentation
**arXiv**：[2511.11311v1](https://arxiv.org/abs/2511.11311) · [PDF](https://arxiv.org/pdf/2511.11311.pdf)  
**作者**：Petros Koutsouvelis, Matej Gazda, Leroy Volmer, Sina Amirrajab, Kamil Barbierik, Branislav Setlak, Jakub Gazda, Peter Drotar  

**一句话要点**：提出模态不变表示学习以提升脑MRI病变分割的少样本性能

**关键词**：脑MRI分析, 模态不变表示学习, 自监督学习, 病变分割, 大规模预训练

## 3 点简述
- 核心问题：自监督学习框架多针对自然图像，难以捕捉多模态MRI信息
- 方法要点：通过大规模预训练学习模态不变表示，并评估其在病变分割中的应用
- 实验或效果：实验表明，病变分割更依赖保留细粒度模态特定特征

## 摘要（原文）

> The field of computer vision is undergoing a paradigm shift toward large-scale foundation model pre-training via self-supervised learning (SSL). Leveraging large volumes of unlabeled brain MRI data, such models can learn anatomical priors that improve few-shot performance in diverse neuroimaging tasks. However, most SSL frameworks are tailored to natural images, and their adaptation to capture multi-modal MRI information remains underexplored. This work proposes a modality-invariant representation learning setup and evaluates its effectiveness in stroke and epilepsy lesion segmentation, following large-scale pre-training. Experimental results suggest that despite successful cross-modality alignment, lesion segmentation primarily benefits from preserving fine-grained modality-specific features. Model checkpoints and code are made publicly available.

