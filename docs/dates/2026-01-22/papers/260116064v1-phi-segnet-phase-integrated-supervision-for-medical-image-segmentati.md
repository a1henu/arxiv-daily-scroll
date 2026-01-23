---
layout: default
title: Phi-SegNet: Phase-Integrated Supervision for Medical Image Segmentation
---

# Phi-SegNet: Phase-Integrated Supervision for Medical Image Segmentation
**arXiv**：[2601.16064v1](https://arxiv.org/abs/2601.16064) · [PDF](https://arxiv.org/pdf/2601.16064.pdf)  
**作者**：Shams Nafisa Ali, Taufiq Hasan  

**一句话要点**：提出Phi-SegNet，通过相位集成监督解决医学图像分割的泛化挑战。

**关键词**：医学图像分割, 频域表示, 相位感知监督, CNN架构, 跨模态泛化

## 3 点简述
- 核心问题：现有分割方法主要编码空间信息，忽视频域表示，导致跨模态泛化受限。
- 方法要点：结合BFMF模块和RFA块，在架构和优化层面集成相位感知信息，使用相位感知损失对齐特征。
- 实验或效果：在五个公共数据集上实现SOTA性能，IoU和F1-score平均相对提升，并展示跨数据集泛化能力。

## 摘要（原文）

> Deep learning has substantially advanced medical image segmentation, yet achieving robust generalization across diverse imaging modalities and anatomical structures remains a major challenge. A key contributor to this limitation lies in how existing architectures, ranging from CNNs to Transformers and their hybrids, primarily encode spatial information while overlooking frequency-domain representations that capture rich structural and textural cues. Although few recent studies have begun exploring spectral information at the feature level, supervision-level integration of frequency cues-crucial for fine-grained object localization-remains largely untapped. To this end, we propose Phi-SegNet, a CNN-based architecture that incorporates phase-aware information at both architectural and optimization levels. The network integrates Bi-Feature Mask Former (BFMF) modules that blend neighboring encoder features to reduce semantic gaps, and Reverse Fourier Attention (RFA) blocks that refine decoder outputs using phase-regularized features. A dedicated phase-aware loss aligns these features with structural priors, forming a closed feedback loop that emphasizes boundary precision. Evaluated on five public datasets spanning X-ray, US, histopathology, MRI, and colonoscopy, Phi-SegNet consistently achieved state-of-the-art performance, with an average relative improvement of 1.54+/-1.26% in IoU and 0.98+/-0.71% in F1-score over the next best-performing model. In cross-dataset generalization scenarios involving unseen datasets from the known domain, Phi-SegNet also exhibits robust and superior performance, highlighting its adaptability and modality-agnostic design. These findings demonstrate the potential of leveraging spectral priors in both feature representation and supervision, paving the way for generalized segmentation frameworks that excel in fine-grained object localization.

