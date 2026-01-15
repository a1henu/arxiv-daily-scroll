---
layout: default
title: Pairing-free Group-level Knowledge Distillation for Robust Gastrointestinal Lesion Classification in White-Light Endoscopy
---

# Pairing-free Group-level Knowledge Distillation for Robust Gastrointestinal Lesion Classification in White-Light Endoscopy
**arXiv**：[2601.09209v1](https://arxiv.org/abs/2601.09209) · [PDF](https://arxiv.org/pdf/2601.09209.pdf)  
**作者**：Qiang Hu, Qimei Wang, Yingjie Guo, Qiang Li, Zhiwei Wang  

**一句话要点**：提出无配对组级知识蒸馏框架PaGKD，以增强白光内镜胃肠道病变分类的鲁棒性。

**关键词**：知识蒸馏, 跨模态学习, 内镜图像分类, 无配对数据, 组级表示

## 3 点简述
- 核心问题：现有方法依赖配对NBI-WLI图像，成本高且不实用，限制了临床数据利用。
- 方法要点：PaGKD通过组级原型蒸馏和组级密集蒸馏，实现无配对跨模态学习，确保全局语义一致性和局部结构连贯性。
- 实验或效果：在四个临床数据集上，PaGKD显著优于现有方法，AUC相对提升达3.3%、1.1%、2.8%和3.2%。

## 摘要（原文）

> White-Light Imaging (WLI) is the standard for endoscopic cancer screening, but Narrow-Band Imaging (NBI) offers superior diagnostic details. A key challenge is transferring knowledge from NBI to enhance WLI-only models, yet existing methods are critically hampered by their reliance on paired NBI-WLI images of the same lesion, a costly and often impractical requirement that leaves vast amounts of clinical data untapped. In this paper, we break this paradigm by introducing PaGKD, a novel Pairing-free Group-level Knowledge Distillation framework that that enables effective cross-modal learning using unpaired WLI and NBI data. Instead of forcing alignment between individual, often semantically mismatched image instances, PaGKD operates at the group level to distill more complete and compatible knowledge across modalities. Central to PaGKD are two complementary modules: (1) Group-level Prototype Distillation (GKD-Pro) distills compact group representations by extracting modality-invariant semantic prototypes via shared lesion-aware queries; (2) Group-level Dense Distillation (GKD-Den) performs dense cross-modal alignment by guiding group-aware attention with activation-derived relation maps. Together, these modules enforce global semantic consistency and local structural coherence without requiring image-level correspondence. Extensive experiments on four clinical datasets demonstrate that PaGKD consistently and significantly outperforms state-of-the-art methods, achieving relative AUC improvements of 3.3%, 1.1%, 2.8%, and 3.2%, respectively, establishing a new direction for cross-modal learning from unpaired data.

