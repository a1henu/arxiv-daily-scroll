---
layout: default
title: Can Embedding Similarity Predict Cross-Lingual Transfer? A Systematic Study on African Languages
---

# Can Embedding Similarity Predict Cross-Lingual Transfer? A Systematic Study on African Languages
**arXiv**：[2601.03168v1](https://arxiv.org/abs/2601.03168) · [PDF](https://arxiv.org/pdf/2601.03168.pdf)  
**作者**：Tewodros Kederalah Idris, Prasenjit Mitra, Roald Eiselen  

**一句话要点**：评估嵌入相似性指标以指导非洲低资源语言的跨语言迁移源语言选择

**关键词**：跨语言迁移, 嵌入相似性, 低资源语言, 非洲语言, 源语言选择, 模型特定分析

## 3 点简述
- 核心问题：缺乏可靠方法选择跨语言迁移的源语言，影响非洲低资源语言NLP系统构建。
- 方法要点：系统评估五种嵌入相似性指标，涵盖816个迁移实验、三个任务、三个模型和12种语言。
- 实验或效果：余弦间隙和检索指标（P@1、CSLS）能可靠预测迁移成功，而CKA预测能力弱；需模型特定分析以避免辛普森悖论。

## 摘要（原文）

> Cross-lingual transfer is essential for building NLP systems for low-resource African languages, but practitioners lack reliable methods for selecting source languages. We systematically evaluate five embedding similarity metrics across 816 transfer experiments spanning three NLP tasks, three African-centric multilingual models, and 12 languages from four language families. We find that cosine gap and retrieval-based metrics (P@1, CSLS) reliably predict transfer success ($ρ= 0.4-0.6$), while CKA shows negligible predictive power ($ρ\approx 0.1$). Critically, correlation signs reverse when pooling across models (Simpson's Paradox), so practitioners must validate per-model. Embedding metrics achieve comparable predictive power to URIEL linguistic typology. Our results provide concrete guidance for source language selection and highlight the importance of model-specific analysis.

