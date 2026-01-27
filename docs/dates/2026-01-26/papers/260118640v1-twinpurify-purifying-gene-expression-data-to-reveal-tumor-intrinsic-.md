---
layout: default
title: TwinPurify: Purifying gene expression data to reveal tumor-intrinsic transcriptional programs via self-supervised learning
---

# TwinPurify: Purifying gene expression data to reveal tumor-intrinsic transcriptional programs via self-supervised learning
**arXiv**：[2601.18640v1](https://arxiv.org/abs/2601.18640) · [PDF](https://arxiv.org/pdf/2601.18640.pdf)  
**作者**：Zhiwei Zheng, Kevin Bryson  

**一句话要点**：提出TwinPurify框架，通过自监督学习净化批量转录组数据以揭示肿瘤内在转录程序

**关键词**：批量转录组净化, 自监督学习, 肿瘤内在信号, 表示学习, 癌症队列分析

## 3 点简述
- 核心问题：批量转录组数据中肿瘤纯度变化掩盖肿瘤内在信号，限制下游发现
- 方法要点：采用Barlow Twins自监督目标，利用队列内相邻正常样本作为背景指导学习连续肿瘤嵌入
- 实验或效果：在多个大型癌症队列中优于传统方法，提升分类、生存模型一致性和通路分析

## 摘要（原文）

> Advances in single-cell and spatial transcriptomic technologies have transformed tumor ecosystem profiling at cellular resolution. However, large scale studies on patient cohorts continue to rely on bulk transcriptomic data, where variation in tumor purity obscures tumor-intrinsic transcriptional signals and constrains downstream discovery. Many deconvolution methods report strong performance on synthetic bulk mixtures but fail to generalize to real patient cohorts because of unmodeled biological and technical variation.
>   Here, we introduce TwinPurify, a representation learning framework that adapts the Barlow Twins self-supervised objective, representing a fundamental departure from the deconvolution paradigm. Rather than resolving the bulk mixture into discrete cell-type fractions, TwinPurify instead learns continuous, high-dimensional tumor embeddings by leveraging adjacent-normal profiles within the same cohort as "background" guidance, enabling the disentanglement of tumor-specific signals without relying on any external reference.
>   Benchmarked against multiple large cancer cohorts across RNA-seq and microarray platforms, TwinPurify outperforms conventional representation learning baselines like auto-encoders in recovering tumor-intrinsic and immune signals. The purified embeddings improve molecular subtype and grade classification, enhance survival model concordance, and uncover biologically meaningful pathway activities compared to raw bulk profiles. By providing a transferable framework for decontaminating bulk transcriptomics, TwinPurify extends the utility of existing clinical datasets for molecular discovery.

