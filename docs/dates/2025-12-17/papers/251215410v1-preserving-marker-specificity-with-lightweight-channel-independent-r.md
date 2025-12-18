---
layout: default
title: Preserving Marker Specificity with Lightweight Channel-Independent Representation Learning
---

# Preserving Marker Specificity with Lightweight Channel-Independent Representation Learning
**arXiv**：[2512.15410v1](https://arxiv.org/abs/2512.15410) · [PDF](https://arxiv.org/pdf/2512.15410.pdf)  
**作者**：Simon Gutwein, Arthur Longuefosse, Jun Seita, Sabine Taschner-Mandl, Roxane Licandro  

**一句话要点**：提出轻量级通道独立模型CIM-S，以提升多路组织成像数据的自监督表示学习效果。

**关键词**：多路组织成像, 自监督学习, 通道独立架构, 轻量模型, 表示学习, 罕见细胞识别

## 3 点简述
- 核心问题：早期通道融合模型在多路数据中难以保留标记特异性信息，尤其在罕见细胞识别上表现不佳。
- 方法要点：采用通道独立架构结合浅层设计，通过对比预训练学习标记特异性表示。
- 实验或效果：在霍奇金淋巴瘤数据集上，CIM-S以5.5K参数超越深度早期融合CNN，表示学习效果更强且稳定。

## 摘要（原文）

> Multiplexed tissue imaging measures dozens of protein markers per cell, yet most deep learning models still apply early channel fusion, assuming shared structure across markers. We investigate whether preserving marker independence, combined with deliberately shallow architectures, provides a more suitable inductive bias for self-supervised representation learning in multiplex data than increasing model scale. Using a Hodgkin lymphoma CODEX dataset with 145,000 cells and 49 markers, we compare standard early-fusion CNNs with channel-separated architectures, including a marker-aware baseline and our novel shallow Channel-Independent Model (CIM-S) with 5.5K parameters. After contrastive pretraining and linear evaluation, early-fusion models show limited ability to retain marker-specific information and struggle particularly with rare-cell discrimination. Channel-independent architectures, and CIM-S in particular, achieve substantially stronger representations despite their compact size. These findings are consistent across multiple self-supervised frameworks, remain stable across augmentation settings, and are reproducible across both the 49-marker and reduced 18-marker settings. These results show that lightweight, channel-independent architectures can match or surpass deep early-fusion CNNs and foundation models for multiplex representation learning. Code is available at https://github.com/SimonBon/CIM-S.

