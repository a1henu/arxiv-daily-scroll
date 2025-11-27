---
layout: default
title: FITRep: Attention-Guided Item Representation via MLLMs
---

# FITRep: Attention-Guided Item Representation via MLLMs
**arXiv**：[2511.21389v1](https://arxiv.org/abs/2511.21389) · [PDF](https://arxiv.org/pdf/2511.21389.pdf)  
**作者**：Guoxiao Zhang, Ao Li, Tan Qu, Qianlong Xie, Xingxing Wang  

**一句话要点**：提出FITRep框架以解决在线平台近重复物品导致的用户体验下降问题

**关键词**：多模态大语言模型, 物品去重, 特征整合理论, 注意力引导, FAISS聚类, UMAP降维

## 3 点简述
- 核心问题：近重复物品视觉和文本相似，现有方法忽略结构关系，导致局部结构崩溃
- 方法要点：基于特征整合理论，使用MLLMs提取层次概念，并通过UMAP和FAISS进行降维聚类
- 实验或效果：在美团广告系统A/B测试中，点击率和千次展示收益分别提升3.60%和4.25%

## 摘要（原文）

> Online platforms usually suffer from user experience degradation due to near-duplicate items with similar visuals and text. While Multimodal Large Language Models (MLLMs) enable multimodal embedding, existing methods treat representations as black boxes, ignoring structural relationships (e.g., primary vs. auxiliary elements), leading to local structural collapse problem. To address this, inspired by Feature Integration Theory (FIT), we propose FITRep, the first attention-guided, white-box item representation framework for fine-grained item deduplication. FITRep consists of: (1) Concept Hierarchical Information Extraction (CHIE), using MLLMs to extract hierarchical semantic concepts; (2) Structure-Preserving Dimensionality Reduction (SPDR), an adaptive UMAP-based method for efficient information compression; and (3) FAISS-Based Clustering (FBC), a FAISS-based clustering that assigns each item a unique cluster id using FAISS. Deployed on Meituan's advertising system, FITRep achieves +3.60% CTR and +4.25% CPM gains in online A/B tests, demonstrating both effectiveness and real-world impact.

