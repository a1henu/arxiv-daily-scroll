---
layout: default
title: SpaCRD: Multimodal Deep Fusion of Histology and Spatial Transcriptomics for Cancer Region Detection
---

# SpaCRD: Multimodal Deep Fusion of Histology and Spatial Transcriptomics for Cancer Region Detection
**arXiv**：[2603.06186v1](https://arxiv.org/abs/2603.06186) · [PDF](https://arxiv.org/pdf/2603.06186.pdf)  
**作者**：Shuailin Xue, Jun Wan, Lihua Zhang, Wenwen Min  

**一句话要点**：提出SpaCRD以解决跨样本和跨平台/批次的癌症组织区域检测问题

**关键词**：癌症区域检测, 多模态融合, 空间转录组学, 迁移学习, 交叉注意力网络, 组织学图像分析

## 3 点简述
- 核心问题：传统方法依赖组织学图像易产生假阳性，且现有方法难以有效整合组织学与空间转录组数据
- 方法要点：基于迁移学习的深度融合网络，通过类别正则化变分重建引导的双向交叉注意力捕获多视角潜在共表达模式
- 实验或效果：在23个匹配数据集上超越八种先进方法，实现跨平台和批次的可靠检测

## 摘要（原文）

> Accurate detection of cancer tissue regions (CTR) enables deeper analysis of the tumor microenvironment and offers crucial insights into treatment response. Traditional CTR detection methods, which typically rely on the rich cellular morphology in histology images, are susceptible to a high rate of false positives due to morphological similarities across different tissue regions. The groundbreaking advances in spatial transcriptomics (ST) provide detailed cellular phenotypes and spatial localization information, offering new opportunities for more accurate cancer region detection. However, current methods are unable to effectively integrate histology images with ST data, especially in the context of cross-sample and cross-platform/batch settings for accomplishing the CTR detection. To address this challenge, we propose SpaCRD, a transfer learning-based method that deeply integrates histology images and ST data to enable reliable CTR detection across diverse samples, platforms, and batches. Once trained on source data, SpaCRD can be readily generalized to accurately detect cancerous regions across samples from different platforms and batches. The core of SpaCRD is a category-regularized variational reconstruction-guided bidirectional cross-attention fusion network, which enables the model to adaptively capture latent co-expression patterns between histological features and gene expression from multiple perspectives. Extensive benchmark analysis on 23 matched histology-ST datasets spanning various disease types, platforms, and batches demonstrates that SpaCRD consistently outperforms existing eight state-of-the-art methods in CTR detection.

