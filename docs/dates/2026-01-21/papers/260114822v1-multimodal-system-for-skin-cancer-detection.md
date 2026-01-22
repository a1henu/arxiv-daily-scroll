---
layout: default
title: Multimodal system for skin cancer detection
---

# Multimodal system for skin cancer detection
**arXiv**：[2601.14822v1](https://arxiv.org/abs/2601.14822) · [PDF](https://arxiv.org/pdf/2601.14822.pdf)  
**作者**：Volodymyr Sydorskyi, Igor Krashenyi, Oleksii Yakubenko  

**一句话要点**：提出多模态皮肤癌检测系统，结合常规照片与元数据，提升可及性与准确性。

**关键词**：皮肤癌检测, 多模态学习, 数据不平衡处理, 元数据集成, 临床可及性

## 3 点简述
- 核心问题：传统深度学习依赖专业皮肤镜图像，限制临床广泛应用。
- 方法要点：集成图像与元数据，采用多模态神经网络和两阶段模型，处理数据不平衡。
- 实验或效果：通过消融研究优化架构，实现Partial ROC AUC 0.18068，检索灵敏度0.78371。

## 摘要（原文）

> Melanoma detection is vital for early diagnosis and effective treatment. While deep learning models on dermoscopic images have shown promise, they require specialized equipment, limiting their use in broader clinical settings. This study introduces a multi-modal melanoma detection system using conventional photo images, making it more accessible and versatile. Our system integrates image data with tabular metadata, such as patient demographics and lesion characteristics, to improve detection accuracy. It employs a multi-modal neural network combining image and metadata processing and supports a two-step model for cases with or without metadata. A three-stage pipeline further refines predictions by boosting algorithms and enhancing performance. To address the challenges of a highly imbalanced dataset, specific techniques were implemented to ensure robust training. An ablation study evaluated recent vision architectures, boosting algorithms, and loss functions, achieving a peak Partial ROC AUC of 0.18068 (0.2 maximum) and top-15 retrieval sensitivity of 0.78371. Results demonstrate that integrating photo images with metadata in a structured, multi-stage pipeline yields significant performance improvements. This system advances melanoma detection by providing a scalable, equipment-independent solution suitable for diverse healthcare environments, bridging the gap between specialized and general clinical practices.

