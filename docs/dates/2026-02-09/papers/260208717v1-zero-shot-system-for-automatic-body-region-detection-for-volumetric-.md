---
layout: default
title: Zero-shot System for Automatic Body Region Detection for Volumetric CT and MR Images
---

# Zero-shot System for Automatic Body Region Detection for Volumetric CT and MR Images
**arXiv**：[2602.08717v1](https://arxiv.org/abs/2602.08717) · [PDF](https://arxiv.org/pdf/2602.08717.pdf)  
**作者**：Farnaz Khun Jush, Grit Werner, Mark Klemens, Matthias Lenga  

**一句话要点**：提出零样本方法，利用预训练基础模型自动检测CT和MR图像中的身体区域。

**关键词**：零样本学习, 身体区域检测, 医学影像分析, CT和MR图像, 预训练模型

## 3 点简述
- 核心问题：现有方法依赖不可靠的DICOM元数据，监督学习在真实场景中适用性受限。
- 方法要点：评估三种免训练流程，包括基于分割的规则系统、MLLM引导和分割感知MLLM。
- 实验或效果：在887个CT和MR扫描上测试，基于分割的规则方法性能最佳，加权F1分数达0.947（CT）和0.914（MR）。

## 摘要（原文）

> Reliable identification of anatomical body regions is a prerequisite for many automated medical imaging workflows, yet existing solutions remain heavily dependent on unreliable DICOM metadata. Current solutions mainly use supervised learning, which limits their applicability in many real-world scenarios. In this work, we investigate whether body region detection in volumetric CT and MR images can be achieved in a fully zero-shot manner by using knowledge embedded in large pre-trained foundation models. We propose and systematically evaluate three training-free pipelines: (1) a segmentation-driven rule-based system leveraging pre-trained multi-organ segmentation models, (2) a Multimodal Large Language Model (MLLM) guided by radiologist-defined rules, and (3) a segmentation-aware MLLM that combines visual input with explicit anatomical evidence. All methods are evaluated on 887 heterogeneous CT and MR scans with manually verified anatomical region labels. The segmentation-driven rule-based approach achieves the strongest and most consistent performance, with weighted F1-scores of 0.947 (CT) and 0.914 (MR), demonstrating robustness across modalities and atypical scan coverage. The MLLM performs competitively in visually distinctive regions, while the segmentation-aware MLLM reveals fundamental limitations.

