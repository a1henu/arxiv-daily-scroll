---
layout: default
title: Radiology Report Generation with Layer-Wise Anatomical Attention
---

# Radiology Report Generation with Layer-Wise Anatomical Attention
**arXiv**：[2512.16841v1](https://arxiv.org/abs/2512.16841) · [PDF](https://arxiv.org/pdf/2512.16841.pdf)  
**作者**：Emmanuel D. Muñiz-De-León, Jorge A. Rosales-de-Golferichs, Ana S. Muñoz-Rodríguez, Alejandro I. Trejo-Castro, Eduardo de Avila-Armenta, Antonio Martínez-Torteya  

**一句话要点**：提出基于分层解剖注意力的紧凑架构，从单张胸部X光图像生成放射学报告发现部分。

**关键词**：放射学报告生成, 分层解剖注意力, 胸部X光图像, 紧凑架构, 图像到文本, 临床相关性

## 3 点简述
- 当前SOTA系统依赖大规模多模态训练和临床元数据，资源密集且难以普及。
- 模型结合冻结DINOv3 ViT编码器和GPT-2解码器，通过分层高斯平滑集成肺和心脏分割掩码。
- 在MIMIC-CXR数据集上评估，关键病理学CheXpert Macro-F1提升168%，RadGraph F1提升9.7%。

## 摘要（原文）

> Automatic radiology report generation is a promising application of multimodal deep learning, aiming to reduce reporting workload and improve consistency. However, current state-of-the-art (SOTA) systems - such as Multimodal AI for Radiology Applications (MAIRA-2) and Medical Pathways Language Model-Multimodal (MedPaLM-M) - depend on large-scale multimodal training, clinical metadata, and multiple imaging views, making them resource-intensive and inaccessible for most settings. We introduce a compact image-to-text architecture that generates the Findings section of chest X-ray reports from a single frontal image. The model combines a frozen Self-Distillation with No Labels v3 (DINOv3) Vision Transformer (ViT) encoder with a Generative Pre-trained Transformer 2 (GPT-2) decoder enhanced by layer-wise anatomical attention. This mechanism integrates lung and heart segmentation masks through hierarchical Gaussian smoothing, biasing attention toward clinically relevant regions without adding trainable parameters. Evaluated on the official Medical Information Mart for Intensive Care-Chest X-ray (MIMIC-CXR) dataset using Chest Radiograph Expert (CheXpert) and Radiology Graph (RadGraph) metrics, our approach achieved substantial gains: CheXpert Macro-F1 for five key pathologies increased by 168% (0.083 -> 0.238) and Micro-F1 by 146% (0.137 -> 0.337), while broader performance across 14 observations improved by 86% (0.170 -> 0.316). Structural coherence also improved, with RadGraph F1 rising by 9.7%. Despite its small size and purely image-conditioned design, the model demonstrates that decoder-level anatomical guidance improves spatial grounding and enhances coherence in clinically relevant regions. The source code is publicly available at: https://github.com/devMuniz02/UDEM-CXR-Reporting-Thesis-2025.

