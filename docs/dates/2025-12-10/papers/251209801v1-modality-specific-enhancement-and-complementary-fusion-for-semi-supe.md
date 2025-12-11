---
layout: default
title: Modality-Specific Enhancement and Complementary Fusion for Semi-Supervised Multi-Modal Brain Tumor Segmentation
---

# Modality-Specific Enhancement and Complementary Fusion for Semi-Supervised Multi-Modal Brain Tumor Segmentation
**arXiv**：[2512.09801v1](https://arxiv.org/abs/2512.09801) · [PDF](https://arxiv.org/pdf/2512.09801.pdf)  
**作者**：Tien-Dat Chung, Ba-Thinh Lam, Thanh-Huy Nguyen, Thien Nguyen, Nguyen Lan Vi Vu, Hoang-Loc Cao, Phat Kim Huynh, Min Xu  

**一句话要点**：提出模态特定增强与互补融合框架以解决半监督多模态脑肿瘤分割中的跨模态差异问题

**关键词**：半监督学习, 多模态医学图像分割, 脑肿瘤分割, 跨模态融合, 注意力机制, 一致性正则化

## 3 点简述
- 核心问题：现有半监督多模态方法因语义差异和错位难以利用模态间互补信息
- 方法要点：引入模态特定增强模块和可学习互补信息融合模块，优化混合目标函数
- 实验或效果：在BraTS 2019数据集上优于基线，提升Dice和Sensitivity分数

## 摘要（原文）

> Semi-supervised learning (SSL) has become a promising direction for medical image segmentation, enabling models to learn from limited labeled data alongside abundant unlabeled samples. However, existing SSL approaches for multi-modal medical imaging often struggle to exploit the complementary information between modalities due to semantic discrepancies and misalignment across MRI sequences. To address this, we propose a novel semi-supervised multi-modal framework that explicitly enhances modality-specific representations and facilitates adaptive cross-modal information fusion. Specifically, we introduce a Modality-specific Enhancing Module (MEM) to strengthen semantic cues unique to each modality via channel-wise attention, and a learnable Complementary Information Fusion (CIF) module to adaptively exchange complementary knowledge between modalities. The overall framework is optimized using a hybrid objective combining supervised segmentation loss and cross-modal consistency regularization on unlabeled data. Extensive experiments on the BraTS 2019 (HGG subset) demonstrate that our method consistently outperforms strong semi-supervised and multi-modal baselines under 1\%, 5\%, and 10\% labeled data settings, achieving significant improvements in both Dice and Sensitivity scores. Ablation studies further confirm the complementary effects of our proposed MEM and CIF in bridging cross-modality discrepancies and improving segmentation robustness under scarce supervision.

