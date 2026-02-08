---
layout: default
title: Generalization of Self-Supervised Vision Transformers for Protein Localization Across Microscopy Domains
---

# Generalization of Self-Supervised Vision Transformers for Protein Localization Across Microscopy Domains
**arXiv**：[2602.05527v1](https://arxiv.org/abs/2602.05527) · [PDF](https://arxiv.org/pdf/2602.05527.pdf)  
**作者**：Ben Isselmann, Dilara Göksu, Andreas Weinmann  

**一句话要点**：评估自监督视觉Transformer在跨显微镜域蛋白质定位中的泛化能力，发现领域相关预训练提升性能。

**关键词**：自监督学习, 视觉Transformer, 蛋白质定位, 跨域迁移, 显微镜图像, DINO预训练

## 3 点简述
- 核心问题：显微镜数据集小，自监督学习跨域泛化能力不明确。
- 方法要点：使用DINO预训练视觉Transformer，在OpenCell数据集上评估跨域迁移。
- 实验或效果：HPA预训练模型性能最佳，表明领域相关自监督表示能有效泛化。

## 摘要（原文）

> Task-specific microscopy datasets are often too small to train deep learning models that learn robust feature representations. Self-supervised learning (SSL) can mitigate this by pretraining on large unlabeled datasets, but it remains unclear how well such representations transfer across microscopy domains with different staining protocols and channel configurations. We investigate the cross-domain transferability of DINO-pretrained Vision Transformers for protein localization on the OpenCell dataset. We generate image embeddings using three DINO backbones pretrained on ImageNet-1k, the Human Protein Atlas (HPA), and OpenCell, and evaluate them by training a supervised classification head on OpenCell labels. All pretrained models transfer well, with the microscopy-specific HPA-pretrained model achieving the best performance (mean macro $F_1$-score = 0.8221 \pm 0.0062), slightly outperforming a DINO model trained directly on OpenCell (0.8057 \pm 0.0090). These results highlight the value of large-scale pretraining and indicate that domain-relevant SSL representations can generalize effectively to related but distinct microscopy datasets, enabling strong downstream performance even when task-specific labeled data are limited.

