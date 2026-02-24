---
layout: default
title: PaReGTA: An LLM-based EHR Data Encoding Approach to Capture Temporal Information
---

# PaReGTA: An LLM-based EHR Data Encoding Approach to Capture Temporal Information
**arXiv**：[2602.19661v1](https://arxiv.org/abs/2602.19661) · [PDF](https://arxiv.org/pdf/2602.19661.pdf)  
**作者**：Kihyuk Yoon, Lingchao Mao, Catherine Chong, Todd J. Schwedt, Chia-Chun Chiang, Jing Li  

**一句话要点**：提出PaReGTA，一种基于LLM的EHR数据编码框架，以捕获时间信息并提升数据有限队列的性能。

**关键词**：电子健康记录编码, 时间信息捕获, 轻量微调, 混合池化, 可解释性分析

## 3 点简述
- 核心问题：结构化电子健康记录中的时间信息在稀疏表示中常丢失，序列模型成本高且需大量数据。
- 方法要点：将纵向EHR事件转换为带时间提示的文本，通过轻量对比微调学习领域适应嵌入，并混合池化聚合为固定维度表示。
- 实验或效果：在39,088名偏头痛患者数据上，PaReGTA优于稀疏基线，且引入PaReGTA-RSS增强可解释性。

## 摘要（原文）

> Temporal information in structured electronic health records (EHRs) is often lost in sparse one-hot or count-based representations, while sequence models can be costly and data-hungry. We propose PaReGTA, an LLM-based encoding framework that (i) converts longitudinal EHR events into visit-level templated text with explicit temporal cues, (ii) learns domain-adapted visit embeddings via lightweight contrastive fine-tuning of a sentence-embedding model, and (iii) aggregates visit embeddings into a fixed-dimensional patient representation using hybrid temporal pooling that captures both recency and globally informative visits. Because PaReGTA does not require training from scratch but instead utilizes a pre-trained LLM, it can perform well even in data-limited cohorts. Furthermore, PaReGTA is model-agnostic and can benefit from future EHR-specialized sentence-embedding models. For interpretability, we introduce PaReGTA-RSS (Representation Shift Score), which quantifies clinically defined factor importance by recomputing representations after targeted factor removal and projecting representation shifts through a machine learning model. On 39,088 migraine patients from the All of Us Research Program, PaReGTA outperforms sparse baselines for migraine type classification while deep sequential models were unstable in our cohort.

