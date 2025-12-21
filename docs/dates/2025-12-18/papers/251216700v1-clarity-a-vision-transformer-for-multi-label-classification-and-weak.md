---
layout: default
title: CLARiTy: A Vision Transformer for Multi-Label Classification and Weakly-Supervised Localization of Chest X-ray Pathologies
---

# CLARiTy: A Vision Transformer for Multi-Label Classification and Weakly-Supervised Localization of Chest X-ray Pathologies
**arXiv**：[2512.16700v1](https://arxiv.org/abs/2512.16700) · [PDF](https://arxiv.org/pdf/2512.16700.pdf)  
**作者**：John M. Statheros, Hairong Wang, Richard Klein  

**一句话要点**：提出CLARiTy视觉Transformer，用于胸部X光多标签分类与弱监督定位，解决标注稀缺问题。

**关键词**：胸部X光分析, 多标签分类, 弱监督定位, 视觉Transformer, 注意力机制, 背景抑制

## 3 点简述
- 核心问题：胸部X光多标签分类与定位任务受限于区域级标注稀缺，需不同粒度标注。
- 方法要点：采用类特定令牌生成注意力图，SegmentCAM模块结合解剖先验进行前景分割与背景抑制。
- 实验或效果：在NIH ChestX-ray14数据集上，分类性能竞争，弱监督定位在8种病理上领先50.7%，小病理如结节提升显著。

## 摘要（原文）

> The interpretation of chest X-rays (CXRs) poses significant challenges, particularly in achieving accurate multi-label pathology classification and spatial localization. These tasks demand different levels of annotation granularity but are frequently constrained by the scarcity of region-level (dense) annotations. We introduce CLARiTy (Class Localizing and Attention Refining Image Transformer), a vision transformer-based model for joint multi-label classification and weakly-supervised localization of thoracic pathologies. CLARiTy employs multiple class-specific tokens to generate discriminative attention maps, and a SegmentCAM module for foreground segmentation and background suppression using explicit anatomical priors. Trained on image-level labels from the NIH ChestX-ray14 dataset, it leverages distillation from a ConvNeXtV2 teacher for efficiency. Evaluated on the official NIH split, the CLARiTy-S-16-512 (a configuration of CLARiTy), achieves competitive classification performance across 14 pathologies, and state-of-the-art weakly-supervised localization performance on 8 pathologies, outperforming prior methods by 50.7%. In particular, pronounced gains occur for small pathologies like nodules and masses. The lower-resolution variant of CLARiTy, CLARiTy-S-16-224, offers high efficiency while decisively surpassing baselines, thereby having the potential for use in low-resource settings. An ablation study confirms contributions of SegmentCAM, DINO pretraining, orthogonal class token loss, and attention pooling. CLARiTy advances beyond CNN-ViT hybrids by harnessing ViT self-attention for global context and class-specific localization, refined through convolutional background suppression for precise, noise-reduced heatmaps.

