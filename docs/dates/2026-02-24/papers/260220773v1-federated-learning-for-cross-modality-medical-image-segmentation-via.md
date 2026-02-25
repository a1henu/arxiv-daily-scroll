---
layout: default
title: Federated Learning for Cross-Modality Medical Image Segmentation via Augmentation-Driven Generalization
---

# Federated Learning for Cross-Modality Medical Image Segmentation via Augmentation-Driven Generalization
**arXiv**：[2602.20773v1](https://arxiv.org/abs/2602.20773) · [PDF](https://arxiv.org/pdf/2602.20773.pdf)  
**作者**：Sachin Dudda Nagaraju, Ashkan Moradi, Bendik Skarre Abrahamsen, Mattijs Elschot  

**一句话要点**：提出基于增强驱动的泛化方法，以解决联邦学习中跨模态医学图像分割的挑战。

**关键词**：联邦学习, 跨模态分割, 医学图像增强, 泛化能力, 数据隐私保护

## 3 点简述
- 核心问题：跨模态域偏移导致模型泛化差，且现实场景中客户端仅持有单模态数据。
- 方法要点：系统评估多种增强策略，包括全局强度非线性增强，以模拟跨模态外观变化。
- 实验或效果：全局强度非线性增强在集中式和联邦设置中均表现最佳，显著提升分割精度。

## 摘要（原文）

> Artificial intelligence has emerged as a transformative tool in medical image analysis, yet developing robust and generalizable segmentation models remains difficult due to fragmented, privacy-constrained imaging data siloed across institutions. While federated learning (FL) enables collaborative model training without centralizing data, cross-modality domain shifts pose a critical challenge, particularly when models trained on one modality fail to generalize to another. Many existing solutions require paired multimodal data per patient or rely on complex architectures, both of which are impractical in real clinical settings. In this work, we consider a realistic FL scenario where each client holds single-modality data (CT or MRI), and systematically investigate augmentation strategies for cross-modality generalization. Using abdominal organ segmentation and whole-heart segmentation as representative multi-class and binary segmentation benchmarks, we evaluate convolution-based spatial augmentation, frequency-domain manipulation, domain-specific normalization, and global intensity nonlinear (GIN) augmentation. Our results show that GIN consistently outperforms alternatives in both centralized and federated settings by simulating cross-modality appearance variations while preserving anatomical structure. For the pancreas, Dice score improved from 0.073 to 0.437, a 498% gain. Our federated approach achieves 93-98% of centralized training accuracy, demonstrating strong cross-modality generalization without compromising data privacy, pointing toward feasible federated AI deployment across diverse healthcare systems.

