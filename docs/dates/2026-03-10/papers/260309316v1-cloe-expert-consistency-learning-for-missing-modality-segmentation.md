---
layout: default
title: CLoE: Expert Consistency Learning for Missing Modality Segmentation
---

# CLoE: Expert Consistency Learning for Missing Modality Segmentation
**arXiv**：[2603.09316v1](https://arxiv.org/abs/2603.09316) · [PDF](https://arxiv.org/pdf/2603.09316.pdf)  
**作者**：Xinyu Tong, Meihua Zhou, Bowu Fan, Haitao Li  

**一句话要点**：提出CLoE框架，通过专家一致性学习解决多模态医学图像分割中模态缺失导致的融合不稳定问题。

**关键词**：多模态医学图像分割, 模态缺失, 专家一致性学习, 特征重校准, 鲁棒性增强, 跨数据集泛化

## 3 点简述
- 核心问题：多模态医学图像分割在推理时模态缺失，导致专家预测分歧和融合不稳定，尤其影响小前景结构。
- 方法要点：引入双分支专家一致性学习目标，包括模态专家一致性和区域专家一致性，并通过轻量门控网络映射一致性分数到模态可靠性权重进行特征重校准。
- 实验或效果：在BraTS 2020和MSD Prostate数据集上优于现有方法，提升不完整模态分割性能，并增强跨数据集泛化能力和临床关键结构鲁棒性。

## 摘要（原文）

> Multimodal medical image segmentation often faces missing modalities at inference, which induces disagreement among modality experts and makes fusion unstable, particularly on small foreground structures. We propose Consistency Learning of Experts (CLoE), a consistency-driven framework for missing-modality segmentation that preserves strong performance when all modalities are available. CLoE formulates robustness as decision-level expert consistency control and introduces a dual-branch Expert Consistency Learning objective. Modality Expert Consistency enforces global agreement among expert predictions to reduce case-wise drift under partial inputs, while Region Expert Consistency emphasizes agreement on clinically critical foreground regions to avoid background-dominated regularization. We further map consistency scores to modality reliability weights using a lightweight gating network, enabling reliability-aware feature recalibration before fusion. Extensive experiments on BraTS 2020 and MSD Prostate demonstrate that CLoE outperforms state-of-the-art methods in incomplete multimodal segmentation, while exhibiting strong cross-dataset generalization and improving robustness on clinically critical structures.

