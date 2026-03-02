---
layout: default
title: Histopathology Image Normalization via Latent Manifold Compaction
---

# Histopathology Image Normalization via Latent Manifold Compaction
**arXiv**：[2602.24251v1](https://arxiv.org/abs/2602.24251) · [PDF](https://arxiv.org/pdf/2602.24251.pdf)  
**作者**：Xiaolong Zhang, Jianwei Zhang, Selim Sevim, Emek Demir, Ece Eksi, Xubo Song  

**一句话要点**：提出Latent Manifold Compaction以解决组织病理学图像批次效应问题

**关键词**：组织病理学图像归一化, 批次效应消除, 无监督表示学习, 潜在流形压缩, 跨批次泛化

## 3 点简述
- 核心问题：组织病理学图像因染色协议、扫描仪等技术差异产生批次效应，阻碍模型跨批次泛化。
- 方法要点：通过无监督表示学习框架，压缩染色诱导的潜在流形，学习批次不变嵌入进行图像归一化。
- 实验或效果：在多个公开和内部基准测试中，LMC显著减少批次分离，在跨批次分类和检测任务中优于现有方法。

## 摘要（原文）

> Batch effects arising from technical variations in histopathology staining protocols, scanners, and acquisition pipelines pose a persistent challenge for computational pathology, hindering cross-batch generalization and limiting reliable deployment of models across clinical sites. In this work, we introduce Latent Manifold Compaction (LMC), an unsupervised representation learning framework that performs image harmonization by learning batch-invariant embeddings from a single source dataset through explicit compaction of stain-induced latent manifolds. This allows LMC to generalize to target domain data unseen during training. Evaluated on three challenging public and in-house benchmarks, LMC substantially reduces batch-induced separations across multiple datasets and consistently outperforms state-of-the-art normalization methods in downstream cross-batch classification and detection tasks, enabling superior generalization.

