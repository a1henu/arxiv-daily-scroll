---
layout: default
title: Evaluating the Impact of Data Anonymization on Image Retrieval
---

# Evaluating the Impact of Data Anonymization on Image Retrieval
**arXiv**：[2602.19641v1](https://arxiv.org/abs/2602.19641) · [PDF](https://arxiv.org/pdf/2602.19641.pdf)  
**作者**：Marvin Chen, Manuel Eberhardinger, Johannes Maucher  

**一句话要点**：评估数据匿名化对图像检索的影响，提出评估框架以平衡隐私与性能

**关键词**：数据匿名化, 图像检索, 隐私保护, DINOv2, 评估框架, 检索偏差

## 3 点简述
- 核心问题：匿名化可能降低基于内容的图像检索性能，缺乏系统研究
- 方法要点：基于DINOv2，系统评估三种匿名化方法、四种程度和四种训练策略
- 实验或效果：发现训练于原始数据的模型在匿名化后检索结果最相似，揭示检索偏差

## 摘要（原文）

> With the growing importance of privacy regulations such as the General Data Protection Regulation, anonymizing visual data is becoming increasingly relevant across institutions. However, anonymization can negatively affect the performance of Computer Vision systems that rely on visual features, such as Content-Based Image Retrieval (CBIR). Despite this, the impact of anonymization on CBIR has not been systematically studied. This work addresses this gap, motivated by the DOKIQ project, an artificial intelligence-based system for document verification actively used by the State Criminal Police Office Baden-Württemberg. We propose a simple evaluation framework: retrieval results after anonymization should match those obtained before anonymization as closely as possible. To this end, we systematically assess the impact of anonymization using two public datasets and the internal DOKIQ dataset. Our experiments span three anonymization methods, four anonymization degrees, and four training strategies, all based on the state of the art backbone Self-Distillation with No Labels (DINO)v2. Our results reveal a pronounced retrieval bias in favor of models trained on original data, which produce the most similar retrievals after anonymization. The findings of this paper offer practical insights for developing privacy-compliant CBIR systems while preserving performance.

