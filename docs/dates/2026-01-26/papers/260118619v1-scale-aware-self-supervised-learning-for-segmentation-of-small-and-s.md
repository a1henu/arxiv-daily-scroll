---
layout: default
title: Scale-Aware Self-Supervised Learning for Segmentation of Small and Sparse Structures
---

# Scale-Aware Self-Supervised Learning for Segmentation of Small and Sparse Structures
**arXiv**：[2601.18619v1](https://arxiv.org/abs/2601.18619) · [PDF](https://arxiv.org/pdf/2601.18619.pdf)  
**作者**：Jorge Quesada, Ghassan AlRegib  

**一句话要点**：提出尺度感知自监督学习方法，通过小窗口裁剪增强，提升小稀疏结构分割性能。

**关键词**：自监督学习, 尺度感知, 小窗口裁剪, 稀疏结构分割, 科学成像

## 3 点简述
- 自监督学习在分割小稀疏结构时性能下降，现有方法偏向大均匀区域。
- 集成小窗口裁剪到增强流程，在预训练中聚焦细尺度结构。
- 在断层分割和细胞描绘任务中，相比基线提升准确率最高达13%和5%。

## 摘要（原文）

> Self-supervised learning (SSL) has emerged as a powerful strategy for representation learning under limited annotation regimes, yet its effectiveness remains highly sensitive to many factors, especially the nature of the target task. In segmentation, existing pipelines are typically tuned to large, homogeneous regions, but their performance drops when objects are small, sparse, or locally irregular. In this work, we propose a scale-aware SSL adaptation that integrates small-window cropping into the augmentation pipeline, zooming in on fine-scale structures during pretraining. We evaluate this approach across two domains with markedly different data modalities: seismic imaging, where the goal is to segment sparse faults, and neuroimaging, where the task is to delineate small cellular structures. In both settings, our method yields consistent improvements over standard and state-of-the-art baselines under label constraints, improving accuracy by up to 13% for fault segmentation and 5% for cell delineation. In contrast, large-scale features such as seismic facies or tissue regions see little benefit, underscoring that the value of SSL depends critically on the scale of the target objects. Our findings highlight the need to align SSL design with object size and sparsity, offering a general principle for buil ding more effective representation learning pipelines across scientific imaging domains.

