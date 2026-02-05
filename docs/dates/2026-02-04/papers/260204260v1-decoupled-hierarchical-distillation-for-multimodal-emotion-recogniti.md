---
layout: default
title: Decoupled Hierarchical Distillation for Multimodal Emotion Recognition
---

# Decoupled Hierarchical Distillation for Multimodal Emotion Recognition
**arXiv**：[2602.04260v1](https://arxiv.org/abs/2602.04260) · [PDF](https://arxiv.org/pdf/2602.04260.pdf)  
**作者**：Yong Li, Yuanzhi Wang, Yi Ding, Shiqing Zhang, Ke Lu, Cuntai Guan  

**一句话要点**：提出解耦分层蒸馏框架以解决多模态情感识别中的异质性与模态贡献不均问题。

**关键词**：多模态情感识别, 特征解耦, 知识蒸馏, 图神经网络, 跨模态对齐

## 3 点简述
- 核心问题：多模态情感识别面临模态异质性和贡献差异的挑战。
- 方法要点：通过自回归机制解耦模态特征，采用图蒸馏单元和跨模态字典匹配进行分层知识蒸馏。
- 实验或效果：在CMU-MOSI/MOSEI数据集上性能优于现有方法，可视化显示特征分布有意义。

## 摘要（原文）

> Human multimodal emotion recognition (MER) seeks to infer human emotions by integrating information from language, visual, and acoustic modalities. Although existing MER approaches have achieved promising results, they still struggle with inherent multimodal heterogeneities and varying contributions from different modalities. To address these challenges, we propose a novel framework, Decoupled Hierarchical Multimodal Distillation (DHMD). DHMD decouples each modality's features into modality-irrelevant (homogeneous) and modality-exclusive (heterogeneous) components using a self-regression mechanism. The framework employs a two-stage knowledge distillation (KD) strategy: (1) coarse-grained KD via a Graph Distillation Unit (GD-Unit) in each decoupled feature space, where a dynamic graph facilitates adaptive distillation among modalities, and (2) fine-grained KD through a cross-modal dictionary matching mechanism, which aligns semantic granularities across modalities to produce more discriminative MER representations. This hierarchical distillation approach enables flexible knowledge transfer and effectively improves cross-modal feature alignment. Experimental results demonstrate that DHMD consistently outperforms state-of-the-art MER methods, achieving 1.3\%/2.4\% (ACC$_7$), 1.3\%/1.9\% (ACC$_2$) and 1.9\%/1.8\% (F1) relative improvement on CMU-MOSI/CMU-MOSEI dataset, respectively. Meanwhile, visualization results reveal that both the graph edges and dictionary activations in DHMD exhibit meaningful distribution patterns across modality-irrelevant/-exclusive feature spaces.

