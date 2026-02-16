---
layout: default
title: Discovering Semantic Latent Structures in Psychological Scales: A Response-Free Pathway to Efficient Simplification
---

# Discovering Semantic Latent Structures in Psychological Scales: A Response-Free Pathway to Efficient Simplification
**arXiv**：[2602.12575v1](https://arxiv.org/abs/2602.12575) · [PDF](https://arxiv.org/pdf/2602.12575.pdf)  
**作者**：Bo Wang, Yuxuan Zhang, Yueqin Hu, Hanchao Hou, Kaiping Peng, Shiguang Ni  

**一句话要点**：提出基于主题建模的语义潜在结构发现框架，用于无响应简化心理量表

**关键词**：心理量表简化, 语义潜在结构, 主题建模, 句子嵌入, 密度聚类, 无响应方法

## 3 点简述
- 核心问题：传统心理量表简化依赖响应数据，受样本量和跨文化可比性限制。
- 方法要点：使用上下文句子嵌入和密度聚类发现语义潜在因素，无需预设数量。
- 实验或效果：在DASS等量表上验证，平均减少60.5%项目，保持心理测量学充分性。

## 摘要（原文）

> Psychological scale refinement traditionally relies on response-based methods such as factor analysis, item response theory, and network psychometrics to optimize item composition. Although rigorous, these approaches require large samples and may be constrained by data availability and cross-cultural comparability. Recent advances in natural language processing suggest that the semantic structure of questionnaire items may encode latent construct organization, offering a complementary response-free perspective. We introduce a topic-modeling framework that operationalizes semantic latent structure for scale simplification. Items are encoded using contextual sentence embeddings and grouped via density-based clustering to discover latent semantic factors without predefining their number. Class-based term weighting derives interpretable topic representations that approximate constructs and enable merging of semantically adjacent clusters. Representative items are selected using membership criteria within an integrated reduction pipeline. We benchmarked the framework across DASS, IPIP, and EPOCH, evaluating structural recovery, internal consistency, factor congruence, correlation preservation, and reduction efficiency. The proposed method recovered coherent factor-like groupings aligned with established constructs. Selected items reduced scale length by 60.5% on average while maintaining psychometric adequacy. Simplified scales showed high concordance with original factor structures and preserved inter-factor correlations, indicating that semantic latent organization provides a response-free approximation of measurement structure. Our framework formalizes semantic structure as an inspectable front-end for scale construction and reduction. To facilitate adoption, we provide a visualization-supported tool enabling one-click semantic analysis and structured simplification.

